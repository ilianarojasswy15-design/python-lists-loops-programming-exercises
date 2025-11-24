spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }
# Your code here
#spanish_translations["love"]="amor"
#spanish_translations["code"]="codigo"
#spanish_translations["smart"]="inteligente"

english = ['love', 'code', 'smart']
spanish = ['amor', 'codigo', 'inteligente']

for word in english:
    spanish_translations[word] = spanish[english.index(word)]

# Don't touch the code below
print("Translation:", spanish_translations["dog"])
print(spanish_translations)
