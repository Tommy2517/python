# import pydirectinput
# import keyboard
# import time
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
#
# def main():
#     while True:
#         if check_key() == '5':
#             pydirectinput.press(['a', 's', 'd', 'q', 'w', 'b',
#                                  'w', 'q', 'b',
#                                  'w', 'q', 'b',
#                                  'w', 'q', 'b',
#                                  'w', 'q', 'b',
#                                  ], presses=1, interval=0.0, logScreenshot=None, _pause=False)
#
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
