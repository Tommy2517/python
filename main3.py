#
# import keyboard
# import pydirectinput
# import time
# import ctypes
# user32 = ctypes.windll.user32
#
#
# def check_key():
#     start_time = time.time()
#     while time.time() - start_time < 1:  # Проверяем нажатие в течение 1 секунды
#         if keyboard.is_pressed('5'):
#             return '5'
#         elif keyboard.is_pressed('1'):
#             return '1'
#         # elif keyboard.is_pressed('q'):
#         #     return 'q'
#
#     return False
#
# def main():
#     while True:
#         if check_key() == '5':
#             key_a = 0x01
#             user32.keybd_event(key_a, 0, 0, 0)
#             time.sleep(0.15)
#             user32.keybd_event(key_a, 0, 0x2, 0)
#             # pydirectinput.press(['a', 's', 'd', 'q', 'w', 'b',
#             #                      'w', 'q', 'b',
#             #                      'w', 'q', 'b',
#             #                      'w', 'q', 'b',
#             #                      'w', 'q', 'b',
#             #                      ])
#             # break
#         # if check_key() == 'q':
#         #     pydirectinput.press(['k'])
#
#         if check_key() == '1':
#             print("Exiting the program.")
#             break
#
#
# if __name__ == "__main__":
#     main()

import keyboard
import ctypes
import time

user32 = ctypes.windll.user32


def check_key():
    start_time = time.time()
    while time.time() - start_time < 1:  # Проверяем нажатие в течение 1 секунды
        if keyboard.is_pressed('5'):
            return '5'
        elif keyboard.is_pressed('1'):
            return '1'

    return False


def main():
    while True:
        if check_key() == '5':
            VK_LBUTTON = 0x01
            user32.mouse_event(2, 0, 0, 0, 0)  # Нажатие левой кнопки мыши
            time.sleep(0.1)
            user32.mouse_event(4, 0, 0, 0, 0)  # Отпускание левой кнопки мыши

        if check_key() == '1':
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
