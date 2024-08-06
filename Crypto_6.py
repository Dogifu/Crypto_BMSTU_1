from collections import Counter
import re


def count_letters(sentence):

    cleaned_sentence = re.sub(r'[^а-яё]', '', sentence.lower())
    letter_counts = Counter(cleaned_sentence)
    total_letters = sum(letter_counts.values())
    return total_letters, letter_counts


sentence = 'ЪРЭРВЭРИЮФ ИРЦЩ, ГРА ОТЧ ЭТЧ, ЪТКЮ ЦТ ВРЯИЩ ОР ЦТЭТЧ, ВЮ ЪФУЮК Щ ЪТИПЕКП ОЮОЩЯЮИЮ ЧУЮЭПЕКП, ГУТД ОТЩУШ ЧЛТА ОРЯБЧИЩЯБА ОТЧ.            П ЧУЮЭПЕКЩ ТЦОТА ОЮ ЭПЧЩ ЬТИТЧ ДБИ - МТУШ ЧЛФУБМ ЛБОТЧЩ. КТЬЦЮ Л ЪТИОПЗ ЧЩИП ТОЮ ЬТИТЧЩИО, КЮУЮЧУЭТЙЮ ДБИЮ ОЮ ЭПЧЩ.'
total_letters_1, letter_counts_1 = count_letters(sentence)

sorted_letter_counts = sorted(
    letter_counts_1.items(), key=lambda item: item[1], reverse=True)

print(f"Общее количество букв: {total_letters_1}")
print("Частоты букв (отсортированы по убыванию):")
for letter, count in sorted_letter_counts:
    print(f"{letter}: {count}")


text = '''
1. ЪРЭРВЭРИЮФ ИРЦЩ, ГРА ОТЧ ЭТЧ, ЪТКЮ ЦТ ВРЯИЩ ОР ЦТЭТЧ, ВЮ ЪФУЮК Щ ЪТИПЕКП ОЮОЩЯЮИЮ ЧУЮЭПЕКП, ГУТД ОТЩУШ ЧЛТА ОРЯБЧИЩЯБА ОТЧ.

2. П ЧУЮЭПЕКЩ ТЦОТА ОЮ ЭПЧЩ ЬТИТЧ ДБИ - МТУШ ЧЛФУБМ ЛБОТЧЩ. КТЬЦЮ Л ЪТИОПЗ ЧЩИП ТОЮ ЬТИТЧЩИЮ, КЮУЮЧУЭТЙЮ ДБИЮ ОЮ ЭПЧЩ.
'''

print('Зашифрованный текст:\n', text)


print('Расшифрованный текст:')

text = text.replace('Т', 'о')


text = text.replace('Ю', 'а')


text = text.replace('О', 'н')

text = text.replace('Ч', 'с')

text = text.replace('Э', 'р')

text = text.replace('Ц', 'д')

text = text.replace('Р', 'е')

text = text.replace('Ъ', 'п')

text = text.replace('К', 'к')

text = text.replace('В', 'з')

text = text.replace('Я', 'м')

text = text.replace('Щ', 'и')

text = text.replace('И', 'л')


text = text.replace('Ф', 'я')


text = text.replace('У', 'т')


text = text.replace('Ь', 'г')


text = text.replace('Б', 'ы')

text = text.replace('А', 'й')


text = text.replace('Й', 'ф')

text = text.replace('П', 'у')


text = text.replace('Е', 'ш')

text = text.replace('Д', 'б')

text = text.replace('Л', 'в')

text = text.replace('М', 'х')


text = text.replace('З', 'ю')


text = text.replace('Ш', 'ь')

text = text.replace('Г', 'ч')


print(text)
