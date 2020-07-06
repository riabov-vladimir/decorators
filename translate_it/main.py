from translate_it import translate_it


# # передаём два аргумента -- перевод с любого языка на русский (указание исходного языка вручную)
print(translate_it('habló', 'es'))
# передаём текст и пару "исходный язык - язык перевода" явно
print(translate_it('habló', 'es', 'en'))
# переводим файл с испанским текстом
translate_it(None, 'es', 'ru', 'ES.txt', 'ES_translated.txt')
# переводим файл с немецким текстом
translate_it(None, 'de', 'ru', 'DE.txt', 'DE_translated.txt')
# переводим файл с французским текстом
translate_it(None, 'fr', 'ru', 'FR.txt', 'FR_translated.txt')