import googletrans
from googletrans import Translator
 
#print(googletrans.LANGUAGES)
translator = Translator()
result = translator.translate('Mikä on nimesi', dest='hi')
print(result.src)
print(result.dest)
print(result.origin)
print(result.text)
print(result.pronunciation)

