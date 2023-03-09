# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:14:03 2023

@author: maidi
"""

import calculadora_indices as calc

print("En esta funcion se va a calcular la cantidad de calorias que una persona quema al realizar alguna actividad fisica...")
peso = float(input("Ingrese el peso de la persona (Kg): "))
altura = float(input("Ingrese la altura de la persona (cm): "))
edad = int(input("Ingrese la edad de la persona (años): "))
valor_genero = float(input("Ingrese el valor genero segun considere ( en caso de ser masculino ingrese 5 y en caso de ser femenino ingrese -161): "))
valor_actividad = float(input("Ingrese el valor de actividad fisica semanal dependiendo ->\n 1.2: Poco o ningun ejercicio\n1.375: ejercicio ligero(1 a 3 dias a la semana)\n1.55: ejercicio moderado(3 a 5 dias a la semana)\n1.725: deportista (6-7 dias a la semana)\n1.9: atleta(entrenamientos mañana y tarde):\n"))
print ("La cantidad de calorias que una persona quema al realizar algun tipo de actividad fisica semanalmente es: ", calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad),"")
      
      
      