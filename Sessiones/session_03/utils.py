def test():
    print("Esto es una funcion")

#test()
#
def test2(a,b):
    print(f'valor de a {a} valor de b {b}')

#test2(12,6)
#
def test3(a,b=10,c="A"):
    print(f'valor de a {a} valor de b {b}')

#test3(18)
#
def test4(nombre):
    return "Hola %s" %nombre

print(test4("Juan"))

def test5(*nombres):
    for nombre in nombres:
        print("Hola %s" %nombre)

#test5("Luis","Pedro","Juan")
#nombres= ["Juan","Pedro","Raul"]


test()
test5("Juan")











