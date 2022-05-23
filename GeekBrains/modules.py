from random import choice, sample
from functions import removing_punctustion
s = '''Выполните практическое задание для отработки пройденного материала.
Проверьте себя, посмотрев разбор задания в следующем уроке.
Проверка преподавателем в данном курсе не предусмотрена.'''

if __name__ == '__main__':
    removing_punctustion(s)
    print(s)
    print(sample(s.split(), 3))