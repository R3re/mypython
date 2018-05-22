#Дана строка и нужно вывести её первое слово

def first_word(text):
    text = text.replace('.', ' ').replace(',', ' ')
    text = text.split()

    return text[0]

if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello.World"))