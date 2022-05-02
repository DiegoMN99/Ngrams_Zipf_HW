#Formatea el texto, eliminando elementos extra y dejandolo como una lista de unigramas mas facil de manipular
from formatted_text_generator import corpus_cleaner 

#Importamos NLTK para ahorrarnos trabajo, gracias a Steven Bird y Edward Loper de UPenn!
import nltk
from nltk.corpus import stopwords

palabrasfuncionales = stopwords.words('spanish') #Stopwords de NLTK

texto_completo = corpus_cleaner('Marianela.txt') #Pasamos nuestro archivo original
texto_normalizado = []


for palabra in texto_completo:              #Este for loop borra todas las stopwords del texto
    if palabra not in palabrasfuncionales:
        texto_normalizado.append(palabra)

print (f'Las palabras a ser eliminadas son {palabrasfuncionales}\n')
print ('Creando archivo normalizado...')

resultado = open('Texto normalizado.txt','w+') #Crea archivo txt nuevo
resultado.write(str(texto_normalizado))
resultado.close

print ('Se ha normalizado el texto! 🥳') 