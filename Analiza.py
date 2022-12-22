# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 19:48:23 2022

@author: Krzychu
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"Dane zostały pobrane z https://insights.stackoverflow.com/survey"




######## Wczytanie, filtrowanie danych dla poszczególnych lat przy pomocy pętli #########

for i in range(19,23):
    df_end=str(i)


    df_year=pd.read_csv("survey_results_public20"+df_end+".csv") #Wczytanie danych
    
    df_year=df_year[df_year['Country'] == "Poland"]  #Filtrowanie wyników dla Polski
    df_year=df_year[df_year['MainBranch'] == "I am a developer by profession"] #Filtorwanie wyników, tylko profesjonalisci
    df_year.reset_index(inplace=True, drop=True) #Reset indexów
    
    
    ####### Stworzenie listy wszystkich języków z ankiety przy pomocy pętli #########
    
    list_year=[]
    
    for i in range(len(df_year)): 
        try:
            list_year= list_year+(df_year["LanguageHaveWorkedWith"][i].split(";"))
     
        except:
            pass
        
        try: 
            list_year= list_year+(df_year["LanguageWorkedWith"][i].split(";"))
        except:
            pass
        
    ###### Pogrupowanie języków według liczby wystąpień w ankiecie (wsród profesjonalistów) ######
        
    df_22 = pd.DataFrame(list_year,columns =['Language'])  #Tworzę df z listy
    grouped_year = df_22.groupby("Language")["Language"].count()  #Grupuję języki i liczę wystąpienia
    grouped_year.sort_values(inplace=True, ascending=False)  #Sortuję języki
    grouped_year=grouped_year[:20]   #biorę pod uwagę 20 największych języków
    grouped_year=grouped_year.to_frame() #Konwersja na Data_Frame
    grouped_year.set_axis(['Count'], axis='columns', inplace=True) #Zmiana nazwy kolumny na count
    
    people_year=len(df_year) #Liczba ankietowanych spełniająca wymagania
    grouped_year["Percent"]=100*grouped_year['Count']/people_year
    
    ###### Tworzę wykres dla 20 najliczniejszych języków ######
    
    plt.bar(grouped_year.index, grouped_year["Percent"])
    plt.xticks(rotation=90)
    plt.title("Procent ankietowanych posługujący się danym językiem w pracy w roku 20"+df_end)
    plt.xlabel("[%]")
    plt.ylabel(["Język"])
    plt.grid(axis='y')
    plt.show()
    
    plt.savefig('Procent ankietowanych posługujący się danym językiem w pracy w roku 20'+df_end+'.jpg',dpi=300)
