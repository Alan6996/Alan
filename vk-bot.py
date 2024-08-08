import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import time
import random

session = vk_api.VkApi(token="vk1.a.blrSiMy5NovC_ocVZvN2sxCuNDzQTKhmYVNTm7PQVcLgezEH9-1QiOcMfm5tbfQxb9n2THOL2xpjJQMfMATRUWQrVP90lC5wV_1PCxpJeNfn5JV2HRl89CvymO7nZwt4ppCuZe-zNJ7tKhdngCjAQvtpCxUDSjimg9WiFHR38cA6pxSHPsDquh8WcozK_K-z-YIK-6def5XxbrX80TQTZQ")
session_api = session.get_api()
longpoll = VkLongPoll (session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            print('Сообщение пришло в: ' + str(event.datetime))
            print('Текст сообщения: ' + str(event.text))

            response = event.text.lower()
            if event.from_user and not event.from_me:

                if response.find('привет')>= 0 or response.find("здравствуй") >= 0:
                    time.sleep(random.uniform(0.5,3))                 
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': 'И тебе привет',
                                                     'random_id':0})
                elif response.find('как дела')>= 0:
                    time.sleep(random.uniform(0.5,3))                 
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': 'Нормально',
                                                     'random_id':0})
                elif response.find('пока') >= 0 or response.find("до скорой встречи") >= 0:
                    time.sleep(random.uniform(0.5,3))                    
                    session.method('messages.send', {'user_id': event.user_id,
                                                     "sticker_id": 65,
                                                     'random_id':0})
                elif response.find('собака') >= 0:
                    time.sleep(random.uniform(0.5,3))                    
                    session.method('messages.send', {'user_id': event.user_id,
                                                     "attachment": "photo-206027701_457501649",
                                                     'random_id':0})                 
