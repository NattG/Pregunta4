# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:36:30 2022

@author: Natalia

4. Con el uso de librerías en PYTHON, construya la dependencia de Abuelos, tios, padres, primos e hijos de su familia.
"""

from kanren import run,var,Relation, facts
a = var()
b = var()
padres = Relation()
facts(padres, ("Nicanor","Ivan"),("Nicanor","Gabriela"),("Nicanor","Rocio"),
             ("Celia","Ivan"),("Celia","Gabriela"),("Celia","Rocio"),
             ("Rocio","Natalia"),("Rocio","Manuel"),
             ("Gabriela","Fernanda"),("Gabriela","Antonio"))
#print(padres.facts)

tios = Relation()
facts(tios, ("Ivan","Natalia"),("Ivan","Manuel"),("Ivan","Fernanda"),("Ivan","Antonio"),
            ("Gabriela","Natalia"),("Gabriela","Manuel"),
            ("Rocio","Fernanda"),("Rocio","Antonio"))

abuelos = Relation()
facts(abuelos, ("Nicanor","Natalia"), ("Nicanor","Manuel"), ("Nicanor","Fernanda"), ("Nicanor","Antonio"),
               ("Celia","Natalia"), ("Celia","Manuel"), ("Celia","Fernanda"), ("Celia","Antonio"))

primos= Relation()
facts(primos, ("Natalia","Fernanda"),("Natalia","Antonio"),
              ("Manuel","Fernanda"),("Manuel","Antonio"),
              ("Fernanda","Natalia"),("Fernanda","Manuel"),
              ("Antonio","Natalia"),("Antonio","Manuel"))

print(run(1,a,padres(a,"Natalia")))
print(run(3,b,padres("Celia",b)))
print(run(2,b,primos("Fernanda",b)))