def removing_punctustion(lists):
    marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
    for i in marks:
        if i in lists:
            lists = lists.replace(i, '')

if __name__ == '__main__':
    print('Неучь!! Ха, ха!!!')