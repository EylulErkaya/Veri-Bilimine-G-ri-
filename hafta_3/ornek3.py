"""2 boyutlu düzlemde noktalar için bir sinif tanimlayin
verilen 2 nokta arasindaki uzakliği bulan metot olsun """
import math
class uzaklik():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def find_distance(self):
        return math.sqrt((self.x1-self.x2)**2) + math.sqrt((self.y1-self.y2)**2)
    
    def __str__(self):
        return "<"+ str(self.x1) + "," + str(self.y1) + ">"
    
mesafe = uzaklik(1, 2, 1, 4)
print(mesafe.find_distance())