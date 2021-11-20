def message_print(func):
    def wrapper():
        print('Head message')
        func()
        print('Tail message')
    return wrapper


def function_print_society():
    print('Society Links')
    print('🚀 Социальные сети:')
    print('✅ Instagram: https://www.instagram.com/py_lounge')
    print('✅ Telegram: https://t.me/pylounge')
    print('✅ Группа ВКонтакте: https://vk.com/pylounge')
    print('✅ Канал PyLounge: https://www.youtube.com/channel/UCru5...')
    print('✅ Twitter: https://twitter.com/pylounge')


message_print(function_print_society)()

