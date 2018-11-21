import vk_api
import botT
import fille
import threading
import time
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
vk_session = vk_api.VkApi(token = '4ccef41dfe9ecc1cf815552f0e994b4652b1b7b84be3b1f88c3e308f05321dcad56af5157f51f6cebd6e0')
#vk_session = vk_api.VkApi(token = 'fad3d76abe4c195a54916d631fc453b0ddf8005caa387269585af7c9fc522b22588b7f075a36114e61b69')
#vk_session = vk_api.VkApi(token = 'aeb7a7e62e220a95cf2c76702cf1b9c50735ab93b688a95a203c98c678e3d60d48ec521967c551a9c7b40') 11а
#vk_session = vk_api.VkApi(token = '973e44f4661ce7e6f56115203bdf7cffe2904eb0e6e29936ded6ee3a5055545e1e3dc2c4f834d19c7a881') записки
vk = vk_session.get_api()
keyboard = VkKeyboard()
keyboard.add_button('11а', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('11б', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('11в', color=VkKeyboardColor.DEFAULT)
keyboard.add_line()  # Переход на вторую строку
keyboard.add_button('10а', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('10б', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('10в', color=VkKeyboardColor.DEFAULT)
keyboard.add_line()
keyboard.add_button('Инфо, так сказать', color=VkKeyboardColor.NEGATIVE)
longpoll = VkLongPoll(vk_session)
last_date = ''
last_xd = ''
def checker():
    while(True):
        global last_xd
        xd = botT.get_hook()
        if last_xd != xd:
            vk.messages.send(user_id='75772038',message=xd,keyboard=keyboard.get_keyboard())
            last_xd = xd    
        print(1)        
        time.sleep(20)        
def main():
    while(True):
        global last_date
        result = botT.get_timetable2()
        if result[1]==0:
            print(1)
            time.sleep(360)
            continue            
        if last_date != result[1]:
            last_date = result[1]
            beta = 'Уведомление!\n'+result[1]+'\n__________________________\n'
            alfa = botT.get_book('11а')
            alfa = beta + alfa
            vk.messages.send(user_id='75772038',message=alfa,keyboard=keyboard.get_keyboard())
            vk.messages.send(chat_id='2',message=alfa)
            vk.messages.send(chat_id='3',message=alfa)
#            vk.messages.send(user_id='86658739',message=alfa,keyboard=keyboard.get_keyboard())        
        print(1)        
        time.sleep(360)



if __name__ == '__main__':
    main()
