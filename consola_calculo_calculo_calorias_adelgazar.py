# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:14:31 2023

@author: maidi
"""

import calculadora_indices as calc

print("En esta funcion se va a calcular el rango recomendado de calorias\nque debe consumir una persona en caso que desee adelgazar....")
peso = float(input("Ingrese el peso de la persona (Kg): "))
altura = float(input("Ingrese la altura de la persona (cm): "))
edad = int(input("Ingrese la edad de la persona (años): "))
valor_genero = float(input("Ingrese el valor genero segun considere ( en caso de ser masculino ingrese 5 y en caso de ser femenino ingrese -161): "))
print ( calc.consumo__calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero) )
      
      