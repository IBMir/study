# Алгоритм выводит в конце предложения следующую в алфавитном порядке букву, если она встречается в строке текста,
# а очередную строку отображает уже без этой буквы.
# Формат входных данных
# На вход программе подается одно слово, записанное строчными русскими буквами без буквы "ё".
# Формат выходных данных
# Программа должна вывести в соответствии с указанным алгоритмом строки, количество которых равно количеству разных букв в строке,
# которая получается путем конкатенации введенного слова и строки "запретил букву".

word = input()
sentence = 'запретил букву'
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
            'ч', 'ц', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
for i in alphabet:
    if i in word + sentence:
        print(f'{word} {sentence} {i}'.replace('  ', ' ').strip())
        word = word.replace(i, '')
        sentence = sentence.replace(i, '').strip()