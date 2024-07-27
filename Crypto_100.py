from collections import Counter
import re


def count_letters(sentence):

    cleaned_sentence = re.sub(r'[^а-яё]', '', sentence.lower())
    letter_counts = Counter(cleaned_sentence)
    total_letters = sum(letter_counts.values())
    return total_letters, letter_counts


sentence = 'ЙОЯОС ЮУХЗ НХЮЙХСЫУ УО ЙЯХГОЯЫД, ТХЯХЦХ ДЫ ХУ ЭЩЙОЯ ГЮО СГОЯЫ... БЯЧЮЧ ЮЖОДЫ ПОЭ ЦМЗЩ ЙДОС, РОВЧЯО БХЮВАЗЩ Ы ПМЗЩНЫ Г ОНХ ЮОБЯОВОЯО. Г ЙЫЯХН ЙХГЩЯЩ - ЯХВХЭОЫ ЭЩЙОБДЫ МЯХФОУБМ ЮЫСУОЬ. ЮБГХЭШ БХЯБМ - Х МФЩЮ! - ХУЩ ГЧЦДЩ УЩЯМФМ Ы, ЭОГЩЬ, ГХЮБДЫБУМДЩ: <<НСО Ь?>>'
total_letters_1, letter_counts_1 = count_letters(sentence)

sorted_letter_counts = sorted(
    letter_counts_1.items(), key=lambda item: item[1], reverse=True)

print(f"Общее количество букв: {total_letters_1}")
print("Частоты букв (отсортированы по убыванию):")
for letter, count in sorted_letter_counts:
    print(f"{letter}: {count}")


text = '''
1. ЙОЯОС ЮУХЗ НХЮЙХСЫУ УО ЙЯХГОЯЫД, ТХЯХЦХ ДЫ ХУ ЭЩЙОЯ ГЮО СГОЯЫ... БЯЧЮЧ ЮЖОДЫ ПОЭ ЦМЗЩ ЙДОС, РОВЧЯО БХЮВАЗЩ Ы ПМЗЩНЫ Г ОНХ ЮОБЯОВОЯО.
2. Г ЙЫЯХН ЙХГЩЯЩ - ЯХВХЭОЫ ЭЩЙОБДЫ МЯХФОУБМ ЮЫСУОЬ. ЮБГХЭШ БХЯБМ - Х МФЩЮ! - ХУЩ ГЧЦДЩ УЩЯМФМ Ы, ЭОГЩЬ, ГХЮБДЫБУМДЩ: <<НСО Ь?>>
'''

print('Зашифрованный текст:\n', text)


print('Расшифрованный текст:')

text = text.replace('Г', 'в')
text = text.replace('Й', 'п')
text = text.replace('Ы', 'и')
text = text.replace('Я', 'р')
text = text.replace('Х', 'о')
text = text.replace('Ч', 'ы')
text = text.replace('Ц', 'ш')
text = text.replace('О', 'е')
text = text.replace('Т', 'х')
text = text.replace('Н', 'г')
text = text.replace('П', 'б')
text = text.replace('С', 'д')
text = text.replace('И', 'п')
text = text.replace('У', 'н')
text = text.replace('Щ', 'а')
text = text.replace('Ж', 'ъ')
text = text.replace('В', 'т')
text = text.replace('Ш', 'ь')
text = text.replace('А', 'ю')
text = text.replace('Р', 'ч')
text = text.replace('Э', 'з')
text = text.replace('М', 'у')
text = text.replace('Б', 'к')
text = text.replace('Ф', 'ж')
text = text.replace('Ь', 'я')
text = text.replace('Ю', 'с')
text = text.replace('З', 'м')
text = text.replace('Д', 'л')


print(text)
