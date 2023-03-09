# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:11:25 2023

@author: maidi
"""

import calculadora_indices as calc

print ("En esta funcion se va a calcular el porcentaje de grasa de una persona... ")

peso = float(input("Ingrese el peso de la persona (Kg): "))
altura = float(input("Ingrese la altura de la persona (m): "))
edad = int(input("Ingrese la edad de la persona (años): "))
valor_genero = float(input("Ingrese el valor genero segun considere (en caso de ser masculino debe ingresar 10.8 y en caso de ser femenino ingrese 0): "))
print ("El porcentaje de grasa que tiene la persona es: ", calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero), "%")
