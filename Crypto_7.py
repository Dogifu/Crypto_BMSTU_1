from collections import Counter
import re


def count_letters(sentence):

    cleaned_sentence = re.sub(r'[^а-яё]', '', sentence.lower())
    letter_counts = Counter(cleaned_sentence)
    total_letters = sum(letter_counts.values())
    return total_letters, letter_counts


sentence = 'ФАОМНЧАМ ЮАЮ-ЗЯ ЕДС ЛИ ЕЯЫЮТБ ИА ЫЗЖЭЬФРН ЫДЬЖДВЛ. ДТБ! ЗА, ВЯЗЯТЭ ГАЖЦЛ, ЬЯ ЯШЛОЮР Т ЬРЦЛ ЛЫЬРЮМА ЕДСРФПЮА ЛИ ЕЯЫЮТБ.   ЬЯЧОЯЖЯЧЯЮ Д ЕЛЫЫ ЛИ ФЯЖКЯМЮА ОБМ ЧМЛФФРЙ Л ЯЫЗЖРЙ, ЦРЕ ЛВЯМЮА. ФР ЫЕДХАЭЫП ФЛЕАМЯ, ЛЕ ФА АЖКР ЛВЖАМА ЯЧАЖРФФАЭ ЕЛЫЫ ЛИ ФЯЖКЯМЮА '
total_letters_1, letter_counts_1 = count_letters(sentence)

sorted_letter_counts = sorted(
    letter_counts_1.items(), key=lambda item: item[1], reverse=True)

print(f"Общее количество букв: {total_letters_1}")
print("Частоты букв (отсортированы по убыванию):")
for letter, count in sorted_letter_counts:
    print(f"{letter}: {count}")


text = '''
1. ФАОМНЧАМ ЮАЮ-ЗЯ ЕДС ЛИ ЕЯЫЮТБ ИА ЫЗЖЭЬФРН ЫДЬЖДВЛ. ДТБ! ЗА, ВЯЗЯТЭ ГАЖЦЛ, ЬЯ ЯШЛОЮР Т ЬРЦЛ ЛЫЬРЮМА ЕДСРФПЮА ЛИ ЕЯЫЮТБ.

2. ЬЯЧОЯЖЯЧЯЮ Д ЕЛЫЫ ЛИ ФЯЖКЯМЮА ОБМ ЧМЛФФРЙ Л ЯЫЗЖРЙ, ЦРЕ ЛВЯМЮА. ФР ЫЕДХАЭЫП ФЛЕАМЯ, ЛЕ ФА АЖКР ЛВЖАМА ЯЧАЖРФФАЭ ЕЛЫЫ ЛИ ФЯЖКЯМЮА.
'''

print('Зашифрованный текст:\n', text)


print('Расшифрованный текст:')


text = text.replace('Ю', 'к')

text = text.replace('А', 'а')

text = text.replace('З', 'т')

text = text.replace('Я', 'о')

text = text.replace('Ф', 'н')


text = text.replace('Л', 'и')

text = text.replace('И', 'з')


text = text.replace('Е', 'м')


text = text.replace('М', 'л')


text = text.replace('Ы', 'с')

text = text.replace('Ж', 'р')

text = text.replace('К', 'ф')

text = text.replace('Р', 'е')

text = text.replace('Й', 'й')

text = text.replace('Ч', 'д')

text = text.replace('О', 'б')

text = text.replace('Ц', 'ч')

text = text.replace('В', 'г')

text = text.replace('Д', 'у')

text = text.replace('Ь', 'п')

text = text.replace('Б', 'ы')

text = text.replace('Т', 'в')

text = text.replace('Н', 'ю')

text = text.replace('Э', 'я')

text = text.replace('П', 'ь')

text = text.replace('Х', 'щ')

text = text.replace('С', 'ж')

text = text.replace('Г', 'х')

text = text.replace('Ш', 'ш')


print(text)
