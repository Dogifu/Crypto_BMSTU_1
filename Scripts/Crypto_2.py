'''
from collections import Counter
import re

def count_letters(sentence):

    cleaned_sentence = re.sub(r'[^а-яё]', '', sentence.lower())
    
    letter_counts = Counter(cleaned_sentence)
    
    total_letters = sum(letter_counts.values())
    
    return total_letters, letter_counts

sentence = 'ИТЮ ВА ЦЙНФН ЦФАКТЗ Й МЩКЩУН ЭЩЙЩКТЮ ЩВ Я ОВАЮ МСФШ МНУН ЦЩЙС ФКТ БТИА Т БНФСКН ЦФКТИА ЦЙТЮТ ЭВНОУА Й ГЩНХ МЩКЩУН КАО ГНЦШН ТО ЦФКАВС ЦДКТВАГ Й ЬКЩБВСХ ЯПТЗ ОАЦДВДЮ ГАУАГ Т ВА ЬКЩЦШМД ЩФЗКЩХ ЩВ ЩФЙНФТЮ ВН ВЩХ ВАЙЦНЭУА ФС ЩЦФАВНЫШЦЯ ФАГ'


total_letters_1, letter_counts_1 = count_letters(sentence)


sorted_letter_counts = sorted(letter_counts_1.items(), key=lambda item: item[1], reverse=True)

print(f"Общее количество букв: {total_letters_1}")
print("Частоты букв (отсортированы по убыванию):")
for letter, count in sorted_letter_counts:
    print(f"{letter}: {count}")
'''

text = '''
1. ИТЮ ВА ЦЙНФН ЦФАКТЗ Й МЩКЩУН. ЭЩЙЩКТЮ ЩВ: 'Я ОВАЮ, МСФШ МНУН. УЙН ЦЩЙС, ФКТ БТИА Т БНФСКН ЦФКТИА ЦЙТЮТ ЭВНОУА Й ГЩНХ МЩКЩУН'
2. КАО ГНЦШН ТО ЦФКАВС ЦДКТВАГ Й ЬКЩБВСХ ЯПТЗ ОАЦДВДЮ ГАУАГ, Т ВА ЬКЩЦШМД: 'ЩФЗКЩХ!' ЩВ ЩФЙНФТЮ: 'ВН ВЩХ! ВАЙЦНЭУА ФС ЩЦФАВНЫШЦЯ ФАГ'
'''

print('Зашифрованный текст:\n', text)


text = text.replace('Щ', 'о')
text = text.replace('В', 'н')
text = text.replace('Н', 'е')
text = text.replace('А', 'а')
text = text.replace('Э', 'г')
text = text.replace('Й', 'в')
text = text.replace('К', 'р')
text = text.replace('Т', 'и')
text = text.replace('Ю', 'л')
text = text.replace('И', 'ж')
text = text.replace('О', 'з')
text = text.replace('Ф', 'т')
text = text.replace('Х', 'й')
text = text.replace('С', 'ы')
text = text.replace('Ц', 'с')
text = text.replace('З', 'к')
text = text.replace('У', 'д')
text = text.replace('Я', 'я')
text = text.replace('Ы', 'ш')
text = text.replace('Ш', 'ь')
text = text.replace('Б', 'ч')
text = text.replace('М', 'б')
text = text.replace('Г', 'м')
text = text.replace('Д', 'у')
text = text.replace('Ь', 'п')
text = text.replace('П', 'щ')


print('Расшифрованный текст:')
print(text)
