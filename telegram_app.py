import telebot
import os
from style_transfer import style_transfer

token = 'YOUR TOKEN'
bot = telebot.TeleBot(token)


def delete(user_id):
    if os.path.isfile(str(user_id) + '/style.jpg'):
        os.remove(str(user_id) + '/style.jpg')
    if os.path.isfile(str(user_id) + '/image.jpg'):
        os.remove(str(user_id) + '/image.jpg')
    if os.path.isfile(str(user_id) + '/stylized_image.jpg'):
        os.remove(str(user_id) + '/stylized_image.jpg')
    if os.path.exists(str(user_id)):
        os.rmdir(str(user_id))


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет, я бот-styletransfer! Для того, чтобы я смог работать отправь мне два изображения'
                                      ' отдельно: сначала изображение стиля, затем изображение, на которое этот стиль'
                                      ' нужно перенести! После этого нажми на команду /go и я через пару секунд выдам'
                                      ' результат.\n\nЕсли изображения отправлены ошибочно или бот сделал что-то не так -'
                                      ' нажми команду /delete и начни заново!')


@bot.message_handler(content_types=['photo'])
def photo_preparation(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    user_path = str(message.from_user.id)
    if not os.path.exists(user_path):
        os.makedirs(user_path)
    if not os.path.exists(str(message.from_user.id) + '/style.jpg'):
        with open(str(message.from_user.id) + '/style.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, 'Изображение стиля сохранено!')
    else:
        with open(str(message.from_user.id) + '/image.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, 'Редактируемое изображение сохранено!')


@bot.message_handler(commands=['go'])
def go(message):
    if os.path.exists(str(message.from_user.id) + '/style.jpg') and os.path.exists(str(message.from_user.id) + '/image.jpg'):
        bot.send_message(message.chat.id, 'Погнали')
        style_transfer(str(message.from_user.id) + '/image.jpg', str(message.from_user.id) + '/style.jpg', str(message.from_user.id))
        bot.send_photo(message.chat.id, open(str(message.from_user.id) + '/stylized_image.jpg', 'rb'))
        delete(message.from_user.id)
    else:
        bot.send_message(message.chat.id, 'Сначала загрузи изображения...')


@bot.message_handler(commands=['delete'])
def delete_images(message):
    bot.send_message(message.chat.id, 'Удаляем изображения...')
    delete(message.from_user.id)
    bot.send_message(message.chat.id, 'Успешно!')


bot.polling(none_stop=True)
