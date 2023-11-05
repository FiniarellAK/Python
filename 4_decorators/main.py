def decorator(func):
    def wrapper():
        print('Начал')
        func()
        print('Закончил')
    return wrapper()


@decorator
def main():
    for i in range(11):
        print('Работаю')


if __name__ == '__main__':
    main()
