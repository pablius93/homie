# -*- coding: utf-8 -*-

import telebot
import datetime
import os
from picamera import PiCamera
from homie import settings
from homie.utils import *
from homie.security import *
from homie.classes import *

bot = telebot.TeleBot(settings.API_TOKEN)
camera = PiCamera()


@bot.message_handler(commands=['enviarvideo'])
def send_video(message):
    """
    Captures a new video, saves it and sends it
    """
    filename = '{}{}{}'.format(
        settings.OUTPUT_DIRECTORY, 
        get_filename_from_time(), 
        settings.VIDEO_EXTENSION
    )
    bot.send_message(message.chat.id, 'Grabando vídeo, esto puede llevar unos minutos...')
    camera.start_recording(filename)
    camera.wait_recording(settings.MAX_VIDEO_TIME)
    camera.stop_recording()
    bot.send_message(message.chat.id, 'Vídeo grabado, enviando...')
    bot.send_video(message.chat.id, open(filename, 'rb'))

    
@bot.message_handler(commands=['enviarfoto'])
def send_photo(message):
    """
    Captures a new image, saves it and sends it
    """
    filename ='{}{}{}'.format(
        settings.OUTPUT_DIRECTORY, 
        get_filename_from_time(), 
        settings.IMAGE_EXTENSION
    )
    bot.send_message(message.chat.id, 'Enviando foto...')
    camera.capture(filename)
    bot.send_photo(message.chat.id, open(filename, 'rb'))
    log = ('Foto ' + filename + ' guardada por ' + message.chat.first_name + ' ' 
                + message.chat.last_name + ' [' + str(message.chat.id) + ']')
    print(log)


    
def initialize():
    camera.rotation = settings.ROTATION.value
    camera.resolution = (
        settings.RESOLUTION.value['height'], 
        settings.RESOLUTION.value['width']
    )


if __name__ == '__main__':
    initialize()
    print('Bot listening!')
    bot.polling()
