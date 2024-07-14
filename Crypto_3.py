
from collections import Counter
import re


def count_letters(sentence):

    cleaned_sentence = re.sub(r'[^а-яё]', '', sentence.lower())
    letter_counts = Counter(cleaned_sentence)
    total_letters = sum(letter_counts.values())
    return total_letters, letter_counts


sentence = 'РВЭММЩМЩДЮН ДЪЦФЭК ЭО ВЭЪЖЮ БЩЖЩФЭВ ГДВЭ ДКЦЧГЪГ ЖЮ ЫЪЩ ТЩН МЩД РВЭММЩЖЦЪ Ж ЫГТ ЧГ Ш ЖЭМЩЖЦЪ МГ Ш ЪЦК ДЫЭЪЦЗ Ц ЖЮ  ЖВЦРГВЭПЦ ЖЭВВЮ Ж ДЦВЩМЭКЦИ ЛЮВЦ ЬРЭЖЭЪГВЙМЩ ЪЩМГМЙКЩН ОЦИЩЪГВЦ Ж СФЩИВЦРЬ ЭДСЭЪЙ ВЭТЩМЦРЬ Э ЬСЦВЦ Ж ЛЩКЦВ ДКЖЩОЙ ДЩВЩТЭМКЬ'

total_letters_1, letter_counts_1 = count_letters(sentence)

sorted_letter_counts = sorted(
    letter_counts_1.items(), key=lambda item: item[1], reverse=True)

print(f"Общее количество букв: {total_letters_1}")
print("Частоты букв (отсортированы по убыванию):")
for letter, count in sorted_letter_counts:
    print(f"{letter}: {count}")


text = '''
1. РВЭММЩМЩДЮН ДЪЦФЭК ЭО ВЭЪЖЮ БЩЖЩФЭВ: 'ГДВЭ ДКЦЧГЪГ ЖЮ, ЫЪЩ ТЩН МЩД РВЭММЩЖЦЪ, Ж ЫГТ ЧГ Ш ЖЭМЩЖЦЪ - МГ Ш ЪЦК ДЫЭЪЦЗ, Ц ЖЮ!'
2. ЖВЦРГВЭПЦ ЖЭВВЮ Ж ДЦВЩМЭКЦИ ЛЮВЦ ЬРЭЖЭЪГВЙМЩ ЪЩМГМЙКЩН. ОЦИЩЪГВЦ Ж СФЩИВЦРЬ ЭДСЭЪЙ ВЭТЩМЦРЬ - Э ЬСЦВЦ Ж ЛЩКЦВ ДКЖЩОЙ ДЩВЩТЭМКЬ
'''

print('Зашифрованный текст:\n', text)

text = text.replace('Щ', 'о')
text = text.replace('Ы', 'ч')
text = text.replace('Ъ', 'т')
text = text.replace('Ц', 'а')
text = text.replace('Э', 'и')
text = text.replace('Ш', 'я')
text = text.replace('К', 'к')
text = text.replace('М', 'н')
text = text.replace('З', 'л')
text = text.replace('Д', 'с')
text = text.replace('Ф', 'р')
text = text.replace('О', 'з')
text = text.replace('Ж', 'в')
text = text.replace('Ю', 'ы')
text = text.replace('Г', 'е')
text = text.replace('В', 'л')
text = text.replace('Л', 'б')
text = text.replace('Ч', 'ж')
text = text.replace('Р', 'д')
text = text.replace('Н', 'й')
text = text.replace('Б', 'г')
text = text.replace('Т', 'м')
text = text.replace('Й', 'ь')
text = text.replace('П', 'ц')
text = text.replace('Ь', 'у')
text = text.replace('С', 'п')
text = text.replace('И', 'х')

print('Расшифрованный текст:')
print(text)
