from matrix_operations import mat_mul

zakres = range (0,5)
a = "Olaf"
print (type(a))
for a in zakres:
    print(a)

zakres = ["Alan","Maira",'Tamara',"Thomas",12,143,1.23,]
for a in zakres:
    print(a)
if a > 0:
    print(type(a))
else:
    pass
a= '1'

zakres[4]
print(len(zakres))
#print(3+a);



def f(x=1, y=0):
    return 2*x+y

a = f(30)

a = f()

a = f(y=15,x=213)
print("Alan"+a.__str__())

print("========")
A = [[1,0,1],[1,1,0],[2,0,0]]
B = [[3,4,2],[1,4,3],[0,1,3]]
C = mat_mul(A,B)
print(C)

mm = mat_mul
mm(A,B)
print(type(mm))
a=False #True
a=None
if a :   # czy a istnieje, albo prawda fałsz
    print(a)

_set = {"A","B","C"}
_set.add("B")
print(_set)

car = { 'marka': 'Fiat',
        'typ' : 'Punto',
        'rocznik' :1998
      }
for k in car:
    print (car[k])

def count(a):
    return len(a), a

x, y = count(car)
_tupel = x , y
print(x)
print(_tupel[0])