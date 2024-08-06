# Частотный анализ - без него никуда

'''
from collections import Counter
import re

def count_letters(sentence):

    cleaned_sentence = re.sub(r'[^а-яё]', '', sentence.lower())
    
    letter_counts = Counter(cleaned_sentence)
    
    total_letters = sum(letter_counts.values())
    
    return total_letters, letter_counts

#sentence = "Г ЙМЦУГКРЬ ЫДФЫБ ФЦ УГЙЬ ЗЫЮЫЙ ПТЮ  - ЛЫМХ ЙОАМТЛ ОТФЫЙЬ. РЫЗДЦ О СЫЮФГИ ЙЬЮГ ЫФЦ ЗЫЮЫЙЬЮЦ, РЦМЦЙСУЫЧЦ ПТЮЦ ФЦ УГЙЬ ПТЮ ЫДЬФ ЙМЦУЬЯЫР ЬЩ ЮЬОЫУФЫ ЙЦЪТБ РУЫКЭЯФТБ О ЪЬУЭ ПЭЙЙСЫУФЫ ФЫ РЦРЫБ-МЫ ВЭФЫР УЦЩ ЭЗЫ СЫДЙМЭУЭЗ Ь ЙЫНУЦЮ ЙМЦУЬЯРЦ ЫЦ ЮЬОЫУФЫ"


total_letters_1, letter_counts_1 = count_letters(sentence_1)


sorted_letter_counts = sorted(letter_counts_1.items(), key=lambda item: item[1], reverse=True)

print(f"Общее количество букв: {total_letters_1}")
print("Частоты букв (отсортированы по убыванию):")
for letter, count in sorted_letter_counts:
    print(f"{letter}: {count}")
'''


# Выясняем размер ключа

'''
def count_unique_letters(sentence):
    # Создаем множество для хранения уникальных букв
    unique_letters = set(sentence)

    # Подсчитываем количество уникальных букв
    num_unique_letters = len(unique_letters)

    return num_unique_letters

if __name__ == "__main__":
    # Ваше предложение
    sentence = "Г ЙМЦУГКРЬ ЫДФЫБ ФЦ УГЙЬ ЗЫЮЫЙ ПТЮ  - ЛЫМХ ЙОАМТЛ ОТФЫЙЬ. РЫЗДЦ О СЫЮФГИ ЙЬЮГ ЫФЦ ЗЫЮЫЙЬЮЦ, РЦМЦЙСУЫЧЦ ПТЮЦ ФЦ УГЙЬ ПТЮ ЫДЬФ ЙМЦУЬЯЫР ЬЩ ЮЬОЫУФЫ ЙЦЪТБ РУЫКЭЯФТБ О ЪЬУЭ ПЭЙЙСЫУФЫ ФЫ РЦРЫБ-МЫ ВЭФЫР УЦЩ ЭЗЫ СЫДЙМЭУЭЗ Ь ЙЫНУЦЮ ЙМЦУЬЯРЦ ЫЦ ЮЬОЫУФЫ"

    # Подсчет уникальных букв
    unique_count = count_unique_letters(sentence)

    print(f"Уникальные буквы в предложении: {unique_count}")
'''


text = '''1. г ймцугкрь ыдфыб фц угйь зыюый птю  - лымх йоамтл отфыйь. рыздц о сыюфги йьюг ыфц зыюыйьюц, рцмцймуычц птюц фц угйь.

2. птю ыдьф ймцуьяыр ьщ юьоыуфы йцътб руыкэяфтб о ъьуэ пэййсыуфы фы рцрыб-мы вэфыр уцщ эзы сыдймэуэз ь йынуцю ймцуьярц ьщ юьоыуфы'''


print('Зашифрованный текст:\n', text)


text = text.replace('ы', 'О')
text = text.replace('р', 'К')
text = text.replace('м', 'Т')
text = text.replace('ц', 'А')
text = text.replace('б', 'Й')
text = text.replace('ф', 'Н')
text = text.replace('д', 'Д')
text = text.replace('ь', 'И')
text = text.replace('щ', 'З')
text = text.replace('з', 'Г')
text = text.replace('э', 'Е')
text = text.replace('у', 'Р')
text = text.replace('ю', 'Л')
text = text.replace('й', 'С')
text = text.replace('г', 'У')
text = text.replace('к', 'Ш')
text = text.replace('п', 'Б')
text = text.replace('т', 'Ы')
text = text.replace('с', 'П')
text = text.replace('я', 'Ч')
text = text.replace('ъ', 'М')
text = text.replace('о', 'В')
text = text.replace('н', 'Ж')
text = text.replace('а', 'а')
text = text.replace('л', 'л')
text = text.replace('и', 'Ю')
text = text.replace('ч', 'Ф')
text = text.replace('в', 'Щ')
text = text.replace('л', 'Х')
text = text.replace('х', 'Ь')
text = text.replace('а', 'Я')
print('Расшифрованный текст:\n', text)
