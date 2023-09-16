def f(x): "descuentp del 5"
print("ingrese la cantidad de componentes")
aluminio= input()
conectores= input()
cajas= input()
print("el costo total es de")
costo= int(aluminio)*200+int(conectores)*50+int(cajas)*20
print(costo)
descuento=int(costo)*(5/100)
print("con el descuento queda en")
costofinal=int(costo)-int(descuento)
print(costofinal)
