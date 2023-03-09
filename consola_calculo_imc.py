# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:10:47 2023

@author: maidi
"""

import calculadora_indices as calc

print("En esta funcion se va a calcular el indice de masa corporal de una persona...")

peso = float(input("Ingrese el peso de la persona (Kg): "))
altura = float(input("Ingrese la altura de la persona (m): "))
print("Indice de masa corporal de la persona es: ", calc.calcular_IMC(peso, altura))
