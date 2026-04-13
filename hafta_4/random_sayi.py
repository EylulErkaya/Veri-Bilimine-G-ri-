from numpy import random
import numpy as np

# for i in range(100):
#     print(i+1, ". sayi=", random.rand())
    
#--------------------------------------------------------------------------   
x= random.randint(100 , size= (5))
# print("Rastgele sayiniz: ", x)
# print(type(x))

filter= x == 0
new_arr= x[filter]
print(new_arr)

#---------------------------------------------------------------------------
#yeniden düzenlenmiş bir dizi döndürür(ve orijinal diziyi değğiştirmeden bırakır)
arr= np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))
#-------------------------------------------------------------------------------
