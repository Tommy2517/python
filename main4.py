# import ctypes
# import time
# import keyboard
# import pydirectinput
# import ctypes
#
#
# # Определение структур для использования в SendInput
# class KEYBDINPUT(ctypes.Structure):
#     _fields_ = [("wVk", ctypes.c_ushort),
#                 ("wScan", ctypes.c_ushort),
#                 ("dwFlags", ctypes.c_ulong),
#                 ("time", ctypes.c_ulong),
#                 ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]
#
#
# class INPUT(ctypes.Structure):
#     _fields_ = [("type", ctypes.c_ulong),
#                 ("ki", KEYBDINPUT)]
#
#
# # Определение констант
# INPUT_KEYBOARD = 1
# KEYEVENTF_KEYDOWN = 0x0000
# KEYEVENTF_KEYUP = 0x0002
#
#
# # Функция для эмуляции нажатия клавиши "A"
# def press_key_a():
#     ki = KEYBDINPUT(wVk=0x41,  # Виртуальный код клавиши "A"
#                     wScan=0,
#                     dwFlags=KEYEVENTF_KEYDOWN,
#                     time=0,
#                     dwExtraInfo=None)
#
#     input_struct = INPUT(type=INPUT_KEYBOARD, ki=ki)
#
#     ctypes.windll.user32.SendInput(1, ctypes.byref(input_struct), ctypes.sizeof(INPUT))
#
#     time.sleep(0.1)  # Добавляем небольшую задержку между нажатием и отпусканием клавиши
#
#     ki.dwFlags = KEYEVENTF_KEYUP
#     input_struct = INPUT(type=INPUT_KEYBOARD, ki=ki)
#
#     ctypes.windll.user32.SendInput(1, ctypes.byref(input_struct), ctypes.sizeof(INPUT))
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
#         keyboard.wait('5')
#
#     return False
#
#
# def main():
#     while True:
#         if check_key() == '5':
#             press_key_a()
#
#         if check_key() == '1':
#             print("Exiting the program.")
#             break
#
#
# if __name__ == "__main__":
#     main()
#
