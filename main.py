class car():
    def __init__(self,modul,number,driver):
        self.modul=modul
        self.number=number
        self.driver=driver
    def sozdanie(self):
        print("модель машины " + self.modul)
        print("номер машины " + self.number)
        print("водитель машины " + self.driver)
car1=car("mercedes","123", "max")
car1.sozdanie()
