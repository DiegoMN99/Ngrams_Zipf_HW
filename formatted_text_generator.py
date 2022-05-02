#Script para normalizar el texto, inspirado en el trabajo de Jorge Antonio Leoni de León -Diego Morales"


import re   # Carga  el paquete de las expresiones regulares
import string

# corpus_original = '[FILE NAME]'

#Formattear el texto, eliminando espacios y elementos innecesarios

def corpus_cleaner(corpus_original):
    with open(corpus_original, "r", encoding="utf8") as file:
        mi_texto = file.readlines()
        file.close
    mi_texto = [x.strip() for x in mi_texto] # Elimina espacio en blanco al final
    mi_texto = [x.lower() for x in mi_texto] # Convierte todas las mayúsculas en minúsculas
    mi_texto = [re.sub('arribaabajo|[?¿¡!,]', '', x, flags = re.M) for x in mi_texto]
    mi_texto = [re.sub('[0-9]+', '', x, flags = re.M) for x in mi_texto]
    mi_texto = [re.sub('—→', '', x, flags = re.M) for x in mi_texto]
    mi_texto = [re.sub('  ', '', x, flags = re.M) for x in mi_texto]
    mi_texto = list(filter(None, mi_texto))
    mi_texto = [x.translate(str.maketrans('', '', string.punctuation)) for x in mi_texto] 
    mi_texto = ' '.join(mi_texto).split() 
    texto_formateado = open(file.name[:len(file.name) - 4] + ' formatteado.txt','w+')
    texto_formateado.write(str(mi_texto))
    texto_formateado.close
    print("Archivo formatteado!🥳 Por favor checkear la carpeta")
    return mi_texto





        

