import numpy as np
from numpy import random
from datetime import datetime

x= [1, 2, 3, 4, 5]
y= [6, 7, 8, 9, 10]
#z= [] 
z= np.add(x,y)

# for i, j in zip(x, y):
#     z.append(i + j)
print(z)

#----------------------------------------------------------------------------------
#100 bin elemanlı iki vektöre nokta çarpımı yapın işlem zamanını ölçün

# x= random.randint(100, size= (100000))
# y= random.randint(100, size= (100000))
# z= 0
# for idx in range(100000):
#     z= z+x[idx]*y[idx]
#---------------------------------------------------------------------------------
#100 bin elemanlı iki vektore nokta carpımı yapın.işlem zamanı ölçün
#aynı işlemi vektörizasyon ile yapın. işlem zamnanını ölçün.karşılaştırın.

x=random.randint(1000,size=(100000))
y=random.randint(1000, size=(100000))

z=0
start_time=datetime.now()
for idx in range(len(x)):
    z=z+x[idx]*y[idx]
    
end_time=datetime.now()
time_difference=(end_time- start_time).total_seconds()*10**3
print("execution time of program is:" ,time_difference, "ms")

start_time=datetime.now()
dot_product=np.dot(x,y)
end_time=datetime.now()
time_difference=(end_time-start_time).total_seconds()*10**3
print("execution time of program is:" ,time_difference,"ms")