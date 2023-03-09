# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:16:40 2023

@author: maidi
"""

def calcular_IMC(peso:float, altura:float)-> float:
    #Calcula el indice de masa corporal de una persona a partir de la ecuacion definida anteriormente
    return round(peso/pow(altura,2),2)

def calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float)-> float:
    #Calcula el porcentaje de grasa de una persona a partir de la ecuacion definida
    return round(1.2 * calcular_IMC(peso, altura)+ 0.23 * edad -5.4 -valor_genero, 2)

def calcular_calorias_en_reposo(peso:float, altura:float, edad:int, valor_genero: int)-> float:
    #Calcula la cantidad de calorias que quema una persona estando en reposo
    return round((10* peso) + (6.25*(altura)) - (5*edad)+ valor_genero,2)

def calcular_calorias_en_actividad(peso:float, altura:float, edad:int, valor_genero: int, valor_actividad:float)-> float:
    #Calcula la cantidad de calorias que quema una persona al realizar alguna actividad fisica
    return round(calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * valor_actividad,2)

def consumo__calorias_recomendado_para_adelgazar(peso:float, altura:float, edad:int, valor_genero:float)-> str:
    #Calcula la cantidad de calorias recomendado a una persona para adelgazar
    calorias_en_reposo = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    porcentaje_20 = calorias_en_reposo * 20 / 100
    porcentaje_15 = calorias_en_reposo * 15 /100
    return "Para adelgazar es recomendado que consumas entre: {0} y {1} calorias al dia. ".format(round(calorias_en_reposo - porcentaje_20,2), round(calorias_en_reposo-porcentaje_15,2))
    