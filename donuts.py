def donuts(count: int):

    if count < 10:
        return ('Number of donuts:' + str(count))
    else:
        return ('Number of donuts: many')

def main():
    print(donuts(29)) #Вывод пишет None, что не так? Вроде решение есть..
    print(donuts(8)),

if __name__ == '__main__':
    main()