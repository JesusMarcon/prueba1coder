import random as r

#Creamos el lanzamineto de un dado
numero_ale = r.randint(1,6)

for x in range(1,11):
    print(f"El lanzaminetos {x}:")
    print(f"Lanzamos el dado: {numero_ale}")
# si ponemos "git add ."" es como poner git add archivo 1,2,3 y etc"
# si ponemos "git log" pondra los commit echos y si ponemos "git checkout" regreara a la version anterior