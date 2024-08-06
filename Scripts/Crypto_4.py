from collections import Counter
import re


def count_letters(sentence):

    cleaned_sentence = re.sub(r'[^а-яё]', '', sentence.lower())
    letter_counts = Counter(cleaned_sentence)
    total_letters = sum(letter_counts.values())
    return total_letters, letter_counts


sentence = 'ЦЭЬЪЭИЭЬЭШ У ГКДД КС МЭИХЭЗШЧ ЪФЗ ЬЗКММОБ К ЭДЯИОБ ПОГ КЫЭЗШЧ МО ДГУНЧРДА МКГЧЗЭ КГ МЧ ЧИХО КЫИЧЗЧ ЭЬЧИОММЧР ГКДД КС МЭИХЭЗШЧ   Р ШИЧДЭБ МО ЪЗКДЯЧЗ МКШЭЫЬЧ Р МО ИЭСЧ ДШЭИОБ ЗОЪОЬЧ ЩЯЭ ГМО МО ЭЪКЬМЭ ГМО ДОЪР ЛОЬА МО ЛКЬМЭ ЛЭЯ ЬЗР ЛДЯИОПМФЙ ЯЧШ ЦИЧЛЬЧ ЪОЬЧ'
total_letters_1, letter_counts_1 = count_letters(sentence)

sorted_letter_counts = sorted(
    letter_counts_1.items(), key=lambda item: item[1], reverse=True)

print(f"Общее количество букв: {total_letters_1}")
print("Частоты букв (отсортированы по убыванию):")
for letter, count in sorted_letter_counts:
    print(f"{letter}: {count}")


text = '''
1. ЦЭЬЪЭИЭЬЭШ У ГКДД КС МЭИХЭЗШЧ ЪФЗ ЬЗКММОБ К ЭДЯИОБ, ПОГ КЫЭЗШЧ. МО ДГУНЧРДА МКГЧЗЭ, КГ МЧ ЧИХО КЫИЧЗЧ ЭЬЧИОММЧР ГКДД КС МЭИХЭЗШЧ
2. Р ШИЧДЭБ МО ЪЗКДЯЧЗ МКШЭЫЬЧ. Р МО ИЭСЧ, ДШЭИОБ, ЗОЪОЬЧ. ЩЯЭ ГМО МО ЭЪКЬМЭ - ГМО ДОЪР ЛОЬА МО ЛКЬМЭ. ЛЭЯ ЬЗР ЛДЯИОПМФЙ - ЯЧШ ЦИЧЛЬЧ, ЪОЬЧ
'''

print('Зашифрованный текст:\n', text)


text = text.replace('Г', 'м')
text = text.replace('К', 'и')
text = text.replace('Д', 'с')
text = text.replace('С', 'з')
text = text.replace('Э', 'о')
text = text.replace('М', 'н')
text = text.replace('О', 'е')
text = text.replace('Ч', 'а')
text = text.replace('Ъ', 'б')
text = text.replace('Ь', 'д')
text = text.replace('Л', 'в')
text = text.replace('Р', 'я')
text = text.replace('Щ', 'ч')
text = text.replace('Я', 'т')
text = text.replace('Ц', 'п')
text = text.replace('И', 'р')
text = text.replace('З', 'л')
text = text.replace('Ш', 'к')
text = text.replace('Ы', 'г')
text = text.replace('Б', 'й')
text = text.replace('П', 'ч')
text = text.replace('У', 'у')
text = text.replace('Х', 'ф')
text = text.replace('А', 'ь')
text = text.replace('Ф', 'ы')
text = text.replace('Й', 'х')
text = text.replace('Н', 'щ')


print('Расшифрованный текст:')

print(text)
