import os 

print("Dosya yolunuz: ", os.getcwd())

#Dosya açma ve yazma
# dosyam = open("dosyam.txt", "w")
# dosyam.write("Merhaba Dunya!")
# dosyam.close()
#----------------------------------------------------------------------------------
# #otomatik kapatma
# with open("deneme.txt", "w") as file:
#     file.write("Merhaba Dunya!")
#     file.write("\nHello world")
#     file.writelines(["\nMerhaba Dunya", "\nHello world", "\n5"]) #içinin hep string olması gerekiyor.
#-----------------------------------------------------------------------------------

#Dosya okuma
# with open("deneme.txt", "r") as file:
#     list= file.read()
    
# print(list)
#---------------------------------------------------------------------------------

# #Dosya bulunamadı hatası
# if os.path.isfile(r"C:\Users\asus\OneDrive\Masaüstü\Veri Bilimine Giriş\deneme.txt"):
#     with open("deneme.txt", "r") as file:
#         list= file.read()
#         print(list)
# else:
#     print("Dosya yok!")
#-----------------------------------------------------------------------------------
try:
    with open(r"C:\\Users\\asus\\OneDrive\\Masaüstü\\Veri Bilimine Giriş\\hafta_4\\deneme.txt", "r") as file:
        list= file.readlines()
        print(list)
        print("Dosya bulundu")
except FileNotFoundError:
    print("Dosya bulunamadi!")
    
# except Exception as error:
#     print(error)
#--------------------------------------------------------------------------------
# for idx, satir in enumerate(list):
#     print(idx+1, " ", satir)
    
# os.remove("dosyam.txt")
# try:
#     with open("dosyam.txt", "r") as file:
#         list= file.readlines()
#         print(list)
# except FileNotFoundError:
#     print("Dosya bulunamadi!")

#os.rmdir("")   klasörü siler direk
#-------------------------------------------------------------------------------
