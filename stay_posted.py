import json
import operator
import os
from datetime import datetime

from postcard_creator.postcard_creator import PostcardCreator, Token, Sender, Recipient, Postcard


def read_config(path_to_config):
    config_file = open(path_to_config, 'r')
    credentials = json.load(config_file)
    username = credentials['user']
    password = credentials['pwd']
    return username, password


def setup_creator():
    credentials = read_config('./config/user.json')
    token = Token()
    token.fetch_token(username=credentials[0], password=credentials[1])
    if token.has_valid_credentials(username=credentials[0], password=credentials[1]):
        return PostcardCreator(token)


def create_sender_and_recipient(path_to_setup):
    setup_file = open(path_to_setup, 'r')
    setup_information = json.load(setup_file)
    sender_info = setup_information['sender']
    recipient_info = setup_information['recipient']
    my_sender = Sender(prename=sender_info['prename'], lastname=sender_info['lastname'], street=sender_info['street'],
                       place=sender_info['place'], zip_code=sender_info['zip_code'])
    my_recipient = Recipient(prename=recipient_info['prename'], lastname=recipient_info['lastname'],
                             street=recipient_info['street'], place=recipient_info['place'],
                             zip_code=recipient_info['zip_code'])

    return my_sender, my_recipient


def get_oldest_image(path):
    if len(os.listdir(path)) > 0:
        files_with_date = {}
        files = os.listdir(path)
        for file in files:
            created = os.stat(path + '/' + file)[9]
            files_with_date.update({file: str(created)})

        files_with_date = sorted(files_with_date.items(), key=operator.itemgetter(1))
        return files_with_date[0][0]
    else:
        with open("./logs/error.log", "a+") as error_log:
            error_log.write(datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' No image found\n')


my_creator = setup_creator()
sender_recipient = create_sender_and_recipient('./config/setup.json')
sender = sender_recipient[0]
recipient = sender_recipient[1]
image = get_oldest_image('./images')
try:
    with open('./images/' + image, 'rb') as my_image:
        card = Postcard(message='Hello', recipient=recipient, sender=sender, picture_stream=my_image)
        my_creator.send_free_card(postcard=card, mock_send=True, image_rotate=True)
    with open("./logs/stay-posted.log", "a+") as log:
        log.write(datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' Post card has successfully been sent!\n')
    os.remove('./images' + image)
except Exception as e:
    with open("./logs/error.log", "a+") as error_log:
        error_log.write(datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' ' + str(e) + '\n')
