# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 19:48:23 2022

@author: Krzychu
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"Dane zostały pobrane z https://insights.stackoverflow.com/survey"




######## Wczytanie, filtrowanie danych #########

df_2022=pd.read_csv("survey_results_public2022.csv") #Wczytanie danych

df_2022=df_2022[df_2022['Country'] == "Poland"]  #Filtrowanie wyników dla Polski
df_2022=df_2022[df_2022['MainBranch'] == "I am a developer by profession"] #Filtorwanie wyników, tylko profesjonalisci
df_2022.reset_index(inplace=True, drop=True) #Reset indexów


####### Stworzenie listy wszystkich języków z ankiety przy pomocy pętli #########

list_2022=[]

for i in range(len(df_2022)): 
    list_2022= list_2022+(df_2022["LanguageHaveWorkedWith"][i].split(";"))
    
    
###### Pogrupowanie języków według liczby wystąpień w ankiecie (wsród profesjonalistów) ######
    
df_22 = pd.DataFrame(list_2022,columns =['Language'])  #Tworzę df z listy
grouped_2022 = df_22.groupby("Language")["Language"].count()  #Grupuję języki i liczę wystąpienia
grouped_2022.sort_values(inplace=True, ascending=False)  #Sortuję języki
grouped_2022=grouped_2022[:20]   #biorę pod uwagę 20 największych języków
grouped_2022=grouped_2022.to_frame() #Konwersja na Data_Frame
grouped_2022.set_axis(['Count'], axis='columns', inplace=True) #Zmiana nazwy kolumny na count

people_2022=len(df_2022) #Liczba ankietowanych spełniająca wymagania
grouped_2022["Percent"]=100*grouped_2022['Count']/people_2022

###### Tworzę wykres dla 20 najliczniejszych języków ######

plt.bar(grouped_2022.index, grouped_2022["Percent"])
plt.xticks(rotation=90)
plt.title("Procent ankietowanych posługujący się danym językiem w pracy w roku 2022")
plt.xlabel("[%]")
plt.ylabel(["Język"])
plt.grid(axis='y')
plt.show()
