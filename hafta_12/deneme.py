# %%

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

n_samples = 10000
data = pd.DataFrame({
    "KullanimSüresi" : np.random.randint(1, 72, n_samples),
    "AylikÖdeme" : np.random.normal(500, 15, n_samples),
    "ToplamGB" : np.random.normal(100, 30, n_samples),
    "ÇağriMerkezi" : np.random.randint(0, 10, n_samples),
    "Internet" : np.random.choice(["Fiber", "DSL", "Yok"], n_samples),
    "TV" : np.random.choice(["Evet", "Hayir"], n_samples),
    "Telefon" : np.random.choice(["Evet", "Hayir"], n_samples),
    "Kayip" : np.random.choice([0, 1], n_samples, p = [0.8, 0.2])
    
})
data.info()

def preproces_data(df):
    df = pd.get_dummies(df, columns= ["Internet", "TV", "Telefon"], dtype= int )
    scaler = StandardScaler()
    numeric_columns= ["KullanimSüresi", "AylikÖdeme", "ToplamGB", "ÇağriMerkezi"]
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    return df
X = preproces_data(data.drop("Kayip", axis = 1))
y = data["Kayip"]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)
X.head()
#Model oluşturma ve eğitme

model = DecisionTreeClassifier(max_depth= 5)
model.fit(X_train, y_train)  #eğitiyor

#tahminler 
y_pred= model.predict(X_test)
print(classification_report(y_test, y_pred)) #siniflandirma performansini raporluyor.

#confistion
plt.figure()
cm= confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot= True, fmt= "d", cmap= "Blues")
plt.title("Confusion Matrix")
plt.xlabel("Tahmin edilen")
plt.ylabel("Gerçek Değer")
plt.show()

#özellik önemlilik grafiği
plt.figure()
ozellik_onemi= pd.DataFrame({
    "özellik" : X.columns,
    "önemi" : model.feature_importances_
})

ozellik_onemi = ozellik_onemi.sort_values("önemi")
plt.bar(range(len(ozellik_onemi)), ozellik_onemi["önemi"])
plt.xlabel("özellikler")
plt.xticks(range(len(ozellik_onemi)), ozellik_onemi.özellik, rotation= 90)
plt.ylabel("Önem derecesi")
plt.title("Müşteri kaybina etki eden faktörler")
plt.show()