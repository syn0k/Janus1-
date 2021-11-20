print('Exapmle 1'*3)
def message_print(func):
    def wrapper(*args, **kwargs):
        print('Head message')
        func(*args, **kwargs)
        print('Tail message')
    return wrapper

@message_print
def function_print_society(inst, tel, vk, yt, tv):
    print(f'''Society Links
        🚀 Социальные сети:
        ✅ Instagram: {inst}
        ✅ Telegram: {tel}
        ✅ Группа ВКонтакте: {vk}
        ✅ Канал PyLounge: {yt}
        ✅ Twitter: {tv}''')


function_print_society('https://www.instagram.com/py_lounge', 'https://t.me/pylounge', 'https://vk.com/pylounge',
              'https://www.youtube.com/channel/UCru5', 'https://twitter.com/pylounge')

print('Exapmle 2'*3)
def message_print(hi_mess, by_mess):
    def message_1(func):
        def wrapper(*args, **kwargs):
            print(hi_mess)
            func(*args, **kwargs)
            print(by_mess)
        return wrapper
    return message_1

@message_print('Head message','Tail message')
def function_print_society(inst, tel, vk, yt, tv):
    print(f'''Society Links
        🚀 Социальные сети:
        ✅ Instagram: {inst}
        ✅ Telegram: {tel}
        ✅ Группа ВКонтакте: {vk}
        ✅ Канал PyLounge: {yt}
        ✅ Twitter: {tv}''')


function_print_society('https://www.instagram.com/py_lounge', 'https://t.me/pylounge', 'https://vk.com/pylounge',
              'https://www.youtube.com/channel/UCru5', 'https://twitter.com/pylounge')




print('Exapmle 3'*3)
def i_am_top(func):
    def wrapper(*args, **kwargs):
        print('I am TOP')
        func(*args, **kwargs)
    return wrapper


def message_print(hi_mess, by_mess):
    def message_1(func):
        def wrapper(*args, **kwargs):
            print(hi_mess)
            func(*args, **kwargs)
            print(by_mess)
        return wrapper
    return message_1

@i_am_top
@message_print('Head message','Tail message')
def function_print_society(inst, tel, vk, yt, tv):
    print(f'''Society Links
        🚀 Социальные сети:
        ✅ Instagram: {inst}
        ✅ Telegram: {tel}
        ✅ Группа ВКонтакте: {vk}
        ✅ Канал PyLounge: {yt}
        ✅ Twitter: {tv}''')


function_print_society('https://www.instagram.com/py_lounge', 'https://t.me/pylounge', 'https://vk.com/pylounge',
              'https://www.youtube.com/channel/UCru5', 'https://twitter.com/pylounge')