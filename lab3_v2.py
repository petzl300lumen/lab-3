class documents:
    def __init__(self, passport, snils, inn):
        self.__passport = passport
        self.__snils = snils
        self.__inn = inn
    
    @property    
    def passport(self):
        return self.__passport 
    
    @passport.setter
    def passport(self, passport):
        self.__passport = passport
    
    @property    
    def snils(self):
        return self.__snils 
    @snils.setter
    def snils(self, snils):
        self.__snils = snils 
    
    @property
    def inn(self):
        return self.__inn
    @inn.setter
    def inn(self, inn):
        self.__inn = inn 

p1 = documents(1234457687,23434456534,1232134556)
print(p1.passport)
print(p1.snils)
print(p1.inn)
print("-----------")
p1.passport = 1619098765
print(p1.passport)
p1.snils = 1919191919
print(p1.snils)
p1.inn = 2891931233
print(p1.inn)
 