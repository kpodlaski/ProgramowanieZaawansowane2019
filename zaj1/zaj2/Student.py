from zaj2.klasy import Person


class Student(Person):

    def __init__(self, name, sname, pesel, id):
        super().__init__(name,sname,pesel)
        self.id = id

    def __str__(self):
        return super().__str__()+" nr albumu:"+str(self.id)

    def add_debit(self,ammount):
        super().add_debit(ammount/2)

def metodaA(x):
    print(x+2)

def main():
    alicja = Student("Alicja", "Olecka", 99111176543,12341)
    print(alicja)
    alicja.add_debit(1253)
    print(alicja.debit)
    _lambda = lambda x, y : 2*x +y -3
    alicja.add_debit = lambda a: print("deb"+str(a/4))
    alicja.add_debit = metodaA
    print( _lambda(3,7))
    alicja.add_debit(200)
    print(alicja.debit)

if __name__=="__main__":
    main()