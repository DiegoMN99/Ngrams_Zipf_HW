import pandas as pd
import time
import re

exclDonQuijote = pd.read_csv('CSVResultados/DonQuijote_normalized.csv') #Pandas nos deja manipular los datos de nuestros .csv
exclMarianela = pd.read_csv('CSVResultados/Marianela_normalized.csv')

first150_DonQuijote = list(exclDonQuijote['Unigrama'][0:150])   
first150_Marianela = list(exclMarianela['Unigrama'][0:150])

def excel_data_analyzer():        
    unigrams_in_common = []
    unigrams_only_DonQuijote = []
    unigrams_only_Marianela = []

    print('Extrayendo datos del excel...')
    time.sleep(1)
    print ('Datos obtenidos para Don Quijote!')
    print ('Datos obtenidos para Marianela!')
    time.sleep(1)
    print('Analizando data...')

    for unigram in first150_DonQuijote:
        if unigram in first150_Marianela:
            unigrams_in_common.append(unigram)
        else:
            unigrams_only_DonQuijote.append(unigram) 

    for unigram in first150_Marianela:
        if unigram not in unigrams_in_common:
            unigrams_only_Marianela.append(unigram)

    time.sleep(1)
    print('Resultados listos! 😎')

    print (f'Comparando los 150 unigramas mas frecuentes, encontramos que los textos coinciden en: {unigrams_in_common}\n')
    time.sleep(1)
    print (f'Los unigramas unicos a El Quijote son: {unigrams_only_DonQuijote}\n\nMientras que los unicos a Marianela son {unigrams_only_Marianela}')
    time.sleep(1)
    print (f'Esto resulto en una coincidencia del {round(((len(unigrams_in_common)/len(first150_Marianela))*100), 2)}% entre ambas listas')

    unigram_list = open('Analisis de unigramas Quijote-Marianela.txt','w+')
    unigram_list.write((f'Comparando los 150 unigramas mas frecuentes, encontramos que los textos coinciden en: {unigrams_in_common}\n'))
    unigram_list.write((f'Los unigramas unicos a El Quijote son: {unigrams_only_DonQuijote}\n\nMientras que los unicos a Marianela son {unigrams_only_Marianela}\n\n'))        
    unigram_list.write((f'Esto resulto en una coincidencia del {round(((len(unigrams_in_common)/len(first150_Marianela))*100), 2)}% entre ambas listas\n\n'))      
    unigram_list.close
    print("\nIncreible analisis 😱 los resultados estan almacenados en la carpeta")


excel_data_analyzer()
