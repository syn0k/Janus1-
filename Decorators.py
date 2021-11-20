#Здесь decorator_function() является функцией-декоратором.
# Как вы могли заметить, она является функцией высшего порядка, так как принимает функцию в качестве аргумента,
# а также возвращает функцию.
# Внутри decorator_function() мы определили другую функцию, обёртку, так сказать,
# которая обёртывает функцию-аргумент и затем изменяет её поведение.
# Декоратор возвращает эту обёртку. Теперь посмотрим на декоратор в действии: m4


def decorator_function(func):
    def wrapper():
        print('1 Функция-обёртка!')
        print('2 Оборачиваемая функция: -> {}'.format(func))
        print('3 Выполняем обёрнутую функцию...')
        func()
        print(' 5 Выходим из обёртки')
    return wrapper


@decorator_function
def hello_world():
    print(f' hello_world() Hello world!')

@decorator_function
def hello_world2():
    print(f' hello_world2() Hello world!')

hello_world()
hello_world2()


def message_print(func):
    def wrapper():
        print('Head message')
        func()
        print('Tail message')
    return wrapper

@message_print
def function_print_society():
    print('Society Links')
    print('🚀 Социальные сети:')
    print('✅ Instagram: https://www.instagram.com/py_lounge')
    print('✅ Telegram: https://t.me/pylounge')
    print('✅ Группа ВКонтакте: https://vk.com/pylounge')
    print('✅ Канал PyLounge: https://www.youtube.com/channel/UCru5...')
    print('✅ Twitter: https://twitter.com/pylounge')


function_print_society()




