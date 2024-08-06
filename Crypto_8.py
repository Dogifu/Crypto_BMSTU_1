from collections import Counter
import re


def count_letters(sentence):

    cleaned_sentence = re.sub(r'[^а-яё]', '', sentence.lower())
    letter_counts = Counter(cleaned_sentence)
    total_letters = sum(letter_counts.values())
    return total_letters, letter_counts


sentence = 'БЧФЙЧАЖН, РЛЧ БЭИТИ ЮИЖК СУКЭСЖТ, ЖКЭРЦИ ФЧРЖНУНДТ СЖЛЗЭСЖТ. МНЖБЦ ЗЭЫНЭИЦ С МЗЦЛУЗ... Ж, ЭСЪ, С ЗУКЭИДЛЦЛУ ЙДУЛ ЧН БЧЗДМЭП СЧКИУ СУКЭСЖТ.         Э ФЛЦЗЭОМЖ ЧАНЧГ НЦ ЗЭФЖ БЧИЧФ ЮЪИ - ЫЧЛД ФСТЛЪЫ СЪНЧФЖ. МЧБАЦ С ЙЧИНЭП ФЖИЭ ЧНЦ БЧИЧФЖИЦ, МЦЛЦФЛЗЧЯЦ ЮЪИЦ НЦ ЗЭФЖ.'
total_letters_1, letter_counts_1 = count_letters(sentence)

sorted_letter_counts = sorted(
    letter_counts_1.items(), key=lambda item: item[1], reverse=True)

print(f"Общее количество букв: {total_letters_1}")
print("Частоты букв (отсортированы по убыванию):")
for letter, count in sorted_letter_counts:
    print(f"{letter}: {count}")


text = '''
1. БЧФЙЧАЖН, РЛЧ БЭИТИ ЮИЖК СУКЭСЖТ, ЖКЭРЦИ ФЧРЖНУНДТ СЖЛЗЭСЖТ. МНЖБЦ ЗЭЫНЭИЦ С МЗЦЛУЗ... Ж, ЭСЪ, С ЗУКЭИДЛЦЛУ ЙДУЛ ЧН БЧЗДМЭП СЧКИУ СУКЭСЖТ.

2. Э ФЛЦЗЭОМЖ ЧАНЧГ НЦ ЗЭФЖ БЧИЧФ ЮЪИ - ЫЧЛД ФСТЛЪЫ СЪНЧФЖ. МЧБАЦ С ЙЧИНЭП ФЖИЭ ЧНЦ БЧИЧФЖИЦ, МЦЛЦФЛЗЧЯЦ ЮЪИЦ НЦ ЗЭФЖ.
'''

print('Зашифрованный текст:\n', text)


print('Расшифрованный текст:')


text = text.replace('Ч', 'о')

text = text.replace('Ц', 'а')

text = text.replace('Н', 'н')

text = text.replace('Г', 'й')

text = text.replace('А', 'д')

text = text.replace('Б', 'г')

text = text.replace('Ф', 'с')

text = text.replace('Й', 'п')

text = text.replace('Ж', 'и')

text = text.replace('И', 'л')

text = text.replace('Э', 'у')

text = text.replace('Л', 'т')

text = text.replace('З', 'р')

text = text.replace('Ю', 'б')

text = text.replace('О', 'ш')

text = text.replace('М', 'к')

text = text.replace('Ъ', 'ы')

text = text.replace('С', 'в')

text = text.replace('Ы', 'х')

text = text.replace('Д', 'ь')

text = text.replace('Т', 'я')

text = text.replace('П', 'ю')

text = text.replace('Я', 'ф')

text = text.replace('Р', 'ч')

text = text.replace('К', 'з')

text = text.replace('У', 'е')

print(text)
