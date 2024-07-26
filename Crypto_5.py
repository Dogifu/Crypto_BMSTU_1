from collections import Counter
import re


def count_letters(sentence):

    cleaned_sentence = re.sub(r'[^а-яё]', '', sentence.lower())
    letter_counts = Counter(cleaned_sentence)
    total_letters = sum(letter_counts.values())
    return total_letters, letter_counts


sentence = 'РУЬЦЛТРУНР ЛД ЬИЗИЧР ЫРЦЦР УР ПШЗШОЗЪУИЖ ЮЦШЖЕШ ЛЬЗРЦР; ЧФИШ ПКЕИН ГИЧЗЪЧ ЧЦЪ ПФИЛЫ ГИЗИПЪЕ ФПШ ЛЬЗРЦР ЧШФЛСР ЛД ЫРЦЦР.  Ф ГЛЗИЬ ГИФРЗР - ЗИЕИДШЛ ДРГШНЦЛ КЗИАШУНК ПЛЧУШЪ. ПНФИДЩ НИЗНК - И КАРП! - ИУР ФЯЭЦР УРЗКАК Л, ДШФРЪ, ФИПНЦЛНУКЦР: <<ЬЧШ Ъ?>>'
total_letters_1, letter_counts_1 = count_letters(sentence)

sorted_letter_counts = sorted(
    letter_counts_1.items(), key=lambda item: item[1], reverse=True)

print(f"Общее количество букв: {total_letters_1}")
print("Частоты букв (отсортированы по убыванию):")
for letter, count in sorted_letter_counts:
    print(f"{letter}: {count}")


text = '''
1. РУЬЦЛТРУНР ЛД ЬИЗИЧР ЫРЦЦР УР ПШЗШОЗЪУИЖ ЮЦШЖЕШ ЛЬЗРЦР; ЧФИШ ПКЕИН ГИЧЗЪЧ ЧЦЪ ПФИЛЫ ГИЗИПЪЕ ФПШ ЛЬЗРЦР ЧШФЛСР ЛД ЫРЦЦР.
2. Ф ГЛЗИЬ ГИФРЗР - ЗИЕИДШЛ ДРГШНЦЛ КЗИАШУНК ПЛЧУШЪ. ПНФИДЩ НИЗНК - И КАРП! - ИУР ФЯЭЦР УРЗКАК Л, ДШФРЪ, ФИПНЦЛНУКЦР: <<ЬЧШ Ъ?>>
'''

print('Зашифрованный текст:\n', text)


print('Расшифрованный текст:')

text = text.replace('Р', 'а')
text = text.replace('Ъ', 'я')
text = text.replace('И', 'о')
text = text.replace('У', 'н')
text = text.replace('Ч', 'д')
text = text.replace('Ц', 'л')
text = text.replace('Ь', 'г')
text = text.replace('Ш', 'е')
text = text.replace('Н', 'к')
text = text.replace('Л', 'и')
text = text.replace('Т', 'ч')
text = text.replace('Д', 'з')
text = text.replace('Ф', 'в')
text = text.replace('З', 'р')
text = text.replace('П', 'с')
text = text.replace('К', 'у')
text = text.replace('Г', 'п')
text = text.replace('А', 'ж')
text = text.replace('Щ', 'ь')
text = text.replace('О', 'б')
text = text.replace('Ж', 'й')
text = text.replace('Ю', 'ф')
text = text.replace('Е', 'т')
text = text.replace('Ы', 'х')
text = text.replace('С', 'ц')
text = text.replace('Я', 'ы')
text = text.replace('Э', 'ш')

print(text)
