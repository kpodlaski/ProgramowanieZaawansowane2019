class Person:
    data = "2332"

    def __init__(self, name= "Jane"
                 , sname= "Doe"
                 , pesel= 97012209876):
        self.name = name
        self.surname = sname
        self.pesel = pesel
        self.id = self.name+self.surname
        self.debit = 0.0

    def __str__(self):
        return "{0} {1}".format(self.name,
                                self.surname)

    def add_debit(self,ammount):
        self.debit+=ammount

    def return_ammount(self,ammount):
        self.debit-=ammount

def main():
    print(Person.data)

    janek = Person("Jan", "Sobieski", "02211301234")
    janek.add_debit(153.12)
    print(janek.__str__())
    print(janek.debit)
    olaf = Person("Janina","Iwańska","89120587654")
    olaf.data=34
    Person.data='xx'
    print(janek.data)
    print(olaf.data)

if __name__ == "__main__":
    main()



