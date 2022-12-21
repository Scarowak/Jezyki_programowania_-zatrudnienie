# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 19:48:23 2022

@author: Krzychu
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"Dane zostały pobrane z https://insights.stackoverflow.com/survey"

df_2022=pd.read_csv("survey_results_public2022.csv")



df_2022=df_2022[df_2022['Country'] == "Poland"]  #Filtrowanie wyników dla Polski


df_2022=df_2022[df_2022['MainBranch'] == "I am a developer by profession"] #Filtorwanie wyników, tylko profesjonalisci


df_2022.reset_index(inplace=True, drop=True)



print(df_2022["LanguageHaveWorkedWith"])


list_2022=[]

for i in range(len(df_2022)):
    list_2022= list_2022+(df_2022["LanguageHaveWorkedWith"][i].split(";"))
    
    
df_22 = pd.DataFrame(list_2022,columns =['Language'])

grouped_2022 = df_22.groupby("Language")["Language"].count()

grouped_2022.sort_values(inplace=True, ascending=False)
