# Hata yakalama try: .......... except:
try:
    sayi1= input("ilk sayiyi giriniz:")
    sayi2= input("ikinci sayiyi giriniz:")
    sonuc= int(sayi1) / int(sayi2)
    print("sonuc: ", sonuc)
    
except ValueError:
    print("Yanlis deger! ")
except ZeroDivisionError:
    print("0'a bolme yapamazsiniz!")
    
# except Exception:
#     print("yanlis birseyler var!")

finally:
    print("islem gerceklestirildi")
    
