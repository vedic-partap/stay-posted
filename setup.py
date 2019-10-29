import os
import json


def get_account():
    user: str = input('email: ')
    pwd: str = input('password: ')
    acc = {'user': user, 'pwd': pwd}
    return acc


def get_setup():
    prename: str = input("prename: ")
    lastname: str = input("lastname: ")
    street: str = input("street: ")
    place: str = input("city: ")
    zip_code: str = input("plz: ")
    msg: str = input("message: ")
    setup = {'sender': {'prename': prename, 'lastname': lastname, 'street': street, 'place': place, 'zip_code': zip_code},
     'recipient': {'prename': prename, 'lastname': lastname, 'street': street, 'place': place, 'zip_code': zip_code}, 'message': msg}
    return setup


def setup():
    if not os.path.exists('config'):
        os.mkdir('./config')
    if not os.path.exists('images'):
        os.mkdir('./images')
    if not os.path.exists('logs'):
        os.mkdir('./logs')
    if not os.path.exists('./images/new'):
        os.mkdir('./images/new')
    if not os.path.exists('./images/sent'):
        os.mkdir('./images/sent')
    errorlog = open('./logs/error.log', 'w+')
    stayposted = open('./logs/stay-posted.log', 'w+')
    if not os.path.exists('./config/accounts.json'):
        with open('./config/accounts.json', 'w+') as outfile:
            json.dump(get_account(), outfile, indent=4)
    if not os.path.exists('./config/setup.json'):
        with open('./config/setup.json', 'w+') as outfile:
            json.dump(get_setup(), outfile, indent=4)


if __name__ == '__main__':
    setup()
