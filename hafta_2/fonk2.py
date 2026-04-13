# tekrarla4("aBCD") isimli bir fonk yazınız bu fonk giriş parametresi olaraak girilen metin(string)
#değişkenindeki her karakteri 4 kez tekrarlayarak yazsın.

def tekrarla4(str= "ABCD"):
    sonuc=""
    for x in str:
        print(x*4)
        sonuc+= x*4     
    print(sonuc)
       
print(tekrarla4())