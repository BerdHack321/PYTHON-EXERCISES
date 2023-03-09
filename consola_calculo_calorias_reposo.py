# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:11:55 2023

@author: maidi
"""

import calculadora_indices as calc

print ("En esta funcion se va a calcular la cantidad de calorias que una persona quema estando en reposo...")

peso = float(input("Ingrese el peso de la persona (Kg): "))
altura = float(input("Ingrese la altura de la persona (cm): "))
edad = int(input("Ingrese la edad de la persona (años): "))
valor_genero = int(input("Ingrese el valor genero segun considere (en caso de ser masculino debe ingresar 5 y en caso de ser femenino ingrese -161): "))
print ("La cantidad de calorias que la persona quema estando en reposo es: ", calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero), "cal")

