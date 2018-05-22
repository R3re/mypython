#Предложение всегда с заглавной буквы и заканчивается точкой

def correct_sentence(text):
    text = text[0].upper() + text[1:]

    if not text.endswith('.'):
        text += '.'
    return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("hello, world"))