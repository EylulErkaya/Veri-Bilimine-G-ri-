class student:
    def __init__(self, a,b):
        self.full_name= a
        self.age= b
    def get_age(self):
        return self.age
    
ogrenci1= student("Eylul", 21)
print(f"Ogrencinin adi: {ogrenci1.full_name}, ogrencinin yasi: {ogrenci1.get_age()}")

del ogrenci1