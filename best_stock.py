# Вам даны текущие цены на акции. Вам необходимо выяснить за какие акции дают большую цену.

def best_stock(data):
    max_price = 0
    answer = ''

    for key in data:
        if data[s] > max_price:
            max_price = data[s]
            answer = key

    return answer
    return 'GOOG'


if __name__ == '__main__':
    print("Example:")
    print (best_stock({
        'CAC': 191.1,
        'ATX': 101.01,
        'TASI': 12.9
    }))