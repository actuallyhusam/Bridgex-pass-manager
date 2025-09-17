import json
from pyfiglet import Figlet
from rich.console import Console
from rich.text import Text
import os

FILENAME_godfather = 'Data'
FILENAME_mail = f'{FILENAME_godfather}/mail.json'
FILENAME_minecraft = f'{FILENAME_godfather}/minecraft.json'
FILENAME_etc = f'{FILENAME_godfather}/etc.json'
FILENAME_phone = f'{FILENAME_godfather}/phone.json'
if os.path.isdir(FILENAME_godfather) == True:
    pass
else:
    os.mkdir(FILENAME_godfather)

mails = []
minecrafts = []
etcs = []
phones = []

class Mail:
    def __init__(self, username, password, phone, extra):
        self.username = username
        self.password = password
        self.phone = phone
        self.extra = extra

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'phone': self.phone,
            'extra': self.extra
        }


class Minecraft:
    def __init__(self, mail, password, extra):
        self.mail = mail
        self.password = password
        self.extra = extra

    def to_dict(self):
        return {
            'mail': self.mail,
            'password': self.password,
            'extra': self.extra
        }


class Etc:
    def __init__(self, display_name, mail, password, belongs_to, phone, extra):
        self.display_name = display_name
        self.mail = mail
        self.password = password
        self.belongs_to = belongs_to
        self.phone = phone
        self.extra = extra

    def to_dict(self):
        return {
            'display_name': self.display_name,
            'mail': self.mail,
            'password': self.password,
            'belongs_to': self.belongs_to,
            'phone': self.phone,
            'extra': self.extra
        }


class Phone:
    def __init__(self, name, number, extra):
        self.name = name
        self.number = number
        self.extra = extra

    def to_dict(self):
        return {
            'name': self.name,
            'number': self.number,
            'extra': self.extra
        }


def adder_mail():
    username = input('Email username: ')
    password = input('Email password: ')
    phone = input('Phone number: ')
    extra = input('extra: ')
    temp = Mail(username, password, phone, extra)
    mails.append(temp)
    saver_mail()
    print('success')
    return

def saver_mail():
    with open(FILENAME_mail, 'w')as f:
        json.dump([mail.to_dict() for mail in mails], f, indent=4)

def loader_mail():
    try:
        global mails
        mails.clear
        with open(FILENAME_mail, 'r')as f:
            data = json.load(f)
            mails = [Mail(account["username"], account["password"], account["phone"], account["extra"]) for account in data]
    except json.decoder.JSONDecodeError:
        print('nothing to be found!')
    except FileNotFoundError:
        mails = []

def mail():
    while True:
        global mails
        loader_mail()
        if mails == []:
            print('There are none! ')
            return
        print('0: exit')
        for i,mail in enumerate(mails, start=1):
            print(f'{i}: {mail.username}')
        choice = input(": ")
        if choice == '0':
            print('exiting...')
            return
        try:
            choice = int(choice)
            choice = choice - 1
            print(f'username: {mails[choice].username}')
            print(f'password: {mails[choice].password}')
            print(f'phone: {mails[choice].phone}')
            print(f'extra: {mails[choice].extra}')
            print('choose what u wanna do with the selected profile!')
            print('0: exit')
            print('1: delete profile')
            print('2: modify profile')
            choice_2 = input(': ')
            choice_2 = int(choice_2)
            if choice_2 > 3:
                print('Too high!')
            elif choice_2 == 0:
                print('exiting...')
                continue
            elif choice_2 == 1:
                choice_3 = input('are u sure u wanna delete this?(y/n): ').strip().lower()
                if choice_3 == 'y':
                    del mails[choice]
                    saver_mail()
                    print('Succesfuly deleted!')
                    continue
                elif choice_3 == 'n':
                    print('exiting...')
                    continue
                print('invalid anwser')
                continue
            elif choice_2 == 2:
                print('0: exit')
                print('1: username')
                print('2: password')
                print('3: phone')
                print('4: extra info')
                choice_4 = input('Please enter what u wanna edit: ').strip().lower()
                choice_4 = int(choice_4)
                if choice_4 > 4:
                    print('Too high!')
                elif choice_4 == 0:
                    print('exiting...')
                    continue
                elif choice_4 == 1:
                    mails[choice].username = input("new username: ")
                    saver_mail()
                    print('success')
                elif choice_4 == 2:
                    mails[choice].password = input('new password: ')
                    saver_mail()
                    print('success.')
                elif choice_4 == 3:
                    mails[choice].phone = input('new phone: ')
                    saver_mail()
                    print('success.')
                elif choice_4 == 4:
                    mails[choice].extra = input('new extra: ')
                    saver_mail()
                    print('success.')
        except ValueError:
            print("That's not a number!")
            continue
        except IndexError:
            print('The value is not in the list.')
            continue


def loader_minecraft():
    try:
        global minecrafts
        minecrafts.clear
        with open(FILENAME_minecraft, 'r')as f:
            data = json.load(f)
            minecrafts = [Minecraft(account["mail"], account["password"], account['extra']) for account in data]
    except json.decoder.JSONDecodeError:
        print('the file lowk empty!')
    except FileNotFoundError:
        minecrafts = []

def saver_minecraft():
    global minecrafts
    with open(FILENAME_minecraft, 'w')as f:
        json.dump([account.to_dict() for account in minecrafts], f, indent=4)

def adder_minecraft():
    gmail = input('gmail: ')
    password = input('password: ')
    extra = input('extra: ')
    temp = Minecraft(gmail, password, extra)
    minecrafts.append(temp)
    saver_minecraft()
    print('saved')

def minecraft():
    while True:
        global minecrafts
        loader_minecraft()
        if minecrafts == []:
            print('There are none! ')
            return
        print('0: exit')
        for i,minecraft in enumerate(minecrafts, start=1):
            print(f'{i}: {minecraft.mail}')
        choice = input(": ")
        if choice == '0':
            print('exiting...')
            return
        try:
            choice = int(choice)
            choice = choice - 1
            print(f'mail: {minecrafts[choice].mail}')
            print(f'password: {minecrafts[choice].password}')
            print(f'extra: {minecrafts[choice].extra}')
            print('choose what u wanna do with the selected profile!')
            print('0: exit')
            print('1: delete profile')
            print('2: modify profile')
            choice_2 = input(': ')
            choice_2 = int(choice_2)
            if choice_2 > 3:
                print('Too high!')
            elif choice_2 == 0:
                print('exiting...')
                continue
            elif choice_2 == 1:
                choice_3 = input('are u sure u wanna delete this?(y/n): ').strip().lower()
                if choice_3 == 'y':
                    del minecrafts[choice]
                    saver_minecraft()
                    print('Succesfuly deleted!')
                    continue
                elif choice_3 == 'n':
                    print('exiting...')
                    continue
                print('invalid anwser')
                continue
            elif choice_2 == 2:
                print('0: exit')
                print('1: mail')
                print('2: password')
                print('3: extra')
                choice_4 = input('Please enter what u wanna edit: ')
                choice_4 = int(choice_4)
                if choice_4 > 4:
                    print('Too high!')
                elif choice_4 == 0:
                    print('exiting...')
                    continue
                elif choice_4 == 1:
                    minecrafts[choice].mail = input("new mail: ")
                    saver_minecraft()
                    print('success')
                elif choice_4 == 2:
                    minecrafts[choice].password = input('new password: ')
                    saver_minecraft()
                    print('success.')
                elif choice_4 == 3:
                    minecrafts[choice].extra = input('new extra: ')
                    saver_minecraft()
                    print('success.')
        except ValueError:
            print("That's not a number!")
            continue
        except IndexError:
            print('The value is not in the list.')
            continue


def loader_etc():
    try:
        global etcs
        etcs = []
        with open(FILENAME_etc, 'r')as f:
            data = json.load(f)
            etcs = [Etc(account['display_name'], account['mail'], account['password'], account['belongs_to'], account['phone'], account['extra']) for account in data]
    except json.decoder.JSONDecodeError:
        print('the file lowk empty!')
    except FileNotFoundError:
        etcs = []

def saver_etc():
    with open(FILENAME_etc, 'w')as f:
        json.dump([account.to_dict() for account in etcs], f, indent=4)

def adder_etc():
    display_name = input('display name: ')
    mail = input('mail: ')
    password = input('password: ')
    belongs_to = input('belongs to: ')
    phone = input('phone: ')
    extra = input('extra:')
    temp = Etc(display_name, mail, password, belongs_to, phone, extra)
    etcs.append(temp)
    saver_etc()
    print('succesfully saved.')

def etc():
    while True:
        loader_etc()
        if etcs == []:
            print('There are none! ')
            return
        print('0: exit')
        for i,etc in enumerate(etcs, start=1):
            print(f'{i}: {etc.display_name}')
        choice = input(": ")
        if choice == '0':
            print('exiting...')
            return
        try:
            choice = int(choice)
            choice = choice - 1
            print(f'display name: {etcs[choice].display_name}')
            print(f'mail: {etcs[choice].mail}')
            print(f'password: {etcs[choice].password}')
            print(f'belongs to: {etcs[choice].belongs_to}')
            print(f'phone: {etcs[choice].phone}')
            print(f'extra: {etcs[choice].extra}')
            print('choose what u wanna do with the selected profile!')
            print('0: exit')
            print('1: delete profile')
            print('2: modify profile')
            choice_2 = input(': ')
            choice_2 = int(choice_2)
            if choice_2 > 3:
                print('Too high!')
            elif choice_2 == 0:
                print('exiting...')
                continue
            elif choice_2 == 1:
                choice_3 = input('are u sure u wanna delete this?(y/n): ').strip().lower()
                if choice_3 == 'y':
                    del etcs[choice]
                    saver_etc()
                    print('Succesfuly deleted!')
                    continue
                elif choice_3 == 'n':
                    print('exiting...')
                    continue
                print('invalid anwser')
                continue
            elif choice_2 == 2:
                print('0: exit')
                print('1: display name')
                print('2: mail')
                print('3: password')
                print('4: belongs to')
                print('5: phone')
                print('6: extra')
                choice_4 = input('Please enter what u wanna edit: ')
                choice_4 = int(choice_4)
                if choice_4 > 4:
                    print('Too high!')
                elif choice_4 == 0:
                    print('exiting...')
                    continue
                elif choice_4 == 1:
                    etcs[choice].display_name = input('new display name: ')
                    saver_etc()
                    print('success.')
                elif choice_4 == 2:
                    etcs[choice].mail = input("new mail: ")
                    saver_etc()
                    print('success')
                elif choice_4 == 3:
                    etcs[choice].password = input('new password: ')
                    saver_etc()
                    print('success.')
                elif choice_4 == 4:
                    etcs[choice].belongs_to = input('new belongs to: ')
                    saver_etc()
                    print('success.')
                elif choice_4 == 5:
                    etcs[choice].phone = input('new phone: ')
                    saver_etc()
                    print('success.')
                elif choice_4 == 6:
                    etcs[choice].extra = input('new extra:')
                    saver_etc()
                    print('success')
        except ValueError:
            print("That's not a number!")
            continue
        except IndexError:
            print('The value is not in the list.')
            continue


def loader_phone():
    try:
        global phones
        phones = []
        with open(FILENAME_phone, 'r')as f:
            data = json.load(f)
            phones = [Phone(account['name'], account['number'], account['extra']) for account in data]
    except json.decoder.JSONDecodeError:
        print('the file lowk empty!')
    except FileNotFoundError:
        phones = []

def saver_phone():
    with open(FILENAME_phone, 'w')as f:
        json.dump([account.to_dict() for account in phones], f, indent=4)

def adder_phone():
    name = input('name: ')
    number = input('number: ')
    extra = input('extra:')
    temp = Etc(name, number, extra)
    etcs.append(temp)
    saver_phone()
    print('succesfully saved.')

def phone():
    while True:
        loader_phone()
        if phones == []:
            print('There are none! ')
            return
        print('0: exit')
        for i,phone in enumerate(phones, start=1):
            print(f'{i}: {phone.name}')
        choice = input(": ")
        if choice == '0':
            print('exiting...')
            return
        try:
            choice = int(choice)
            choice = choice - 1
            print(f'name: {phones[choice].name}')
            print(f'number: {phones[choice].number}')
            print(f'extra: {phones[choice].extra}')
            print('choose what u wanna do with the selected profile!')
            print('0: exit')
            print('1: delete profile')
            print('2: modify profile')
            choice_2 = input(': ')
            choice_2 = int(choice_2)
            if choice_2 > 3:
                print('Too high!')
            elif choice_2 == 0:
                print('exiting...')
                continue
            elif choice_2 == 1:
                choice_3 = input('are u sure u wanna delete this?(y/n): ').strip().lower()
                if choice_3 == 'y':
                    del phones[choice]
                    saver_phone()
                    print('Succesfuly deleted!')
                    continue
                elif choice_3 == 'n':
                    print('exiting...')
                    continue
                print('invalid anwser')
                continue
            elif choice_2 == 2:
                print('0: exit')
                print('1: name')
                print('2: number')
                print('3: extra')
                choice_4 = input('Please enter what u wanna edit: ')
                choice_4 = int(choice_4)
                if choice_4 > 4:
                    print('Too high!')
                elif choice_4 == 0:
                    print('exiting...')
                    continue
                elif choice_4 == 1:
                    phones[choice].name = input('new name: ')
                    saver_phone()
                    print('success.')
                elif choice_4 == 2:
                    phones[choice].number = input("new number: ")
                    saver_phone()
                    print('success')
                elif choice_4 == 3:
                    phones[choice].extra = input('new extra: ')
                    saver_phone()
                    print('success.')
        except ValueError:
            print("That's not a number!")
            continue
        except IndexError:
            print('The value is not in the list.')
            continue


def vault_text():
    console = Console()
    figlet = Figlet(font="slant")
    vault_text = figlet.renderText("bridgex")
    lines = vault_text.splitlines()
    rainbow_rgb = [
        (255, 0, 0),
        (255, 127, 0),
        (255, 255, 0),
        (0, 255, 0),
        (0, 0, 255),
        (75, 0, 130),
        (148, 0, 211)
    ]
    def interpolate_color(c1, c2, t):
        return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))

    def gradient_letter(char, length):
        text = Text()
        for i, c in enumerate(char):
            pos = i / max(1, length - 1)
            total = len(rainbow_rgb) - 1
            idx = pos * total
            idx_low = int(idx)
            idx_high = min(idx_low + 1, total)
            t = idx - idx_low
            r, g, b = interpolate_color(rainbow_rgb[idx_low], rainbow_rgb[idx_high], t)
            text.append(c, style=f"rgb({r},{g},{b})")
        return text
    for line in lines:
        console.print(gradient_letter(line, len(line)))


def main():
    while True:
        vault_text()
        print('for ALL ur info (;')
        print('0: exit')
        print('1: add a account')
        print('2: browse through existing accounts')
        choice = input(': ')
        if choice == '0':
            print('exiting')
            return
        if choice == '1':
            print('0: exit')
            print('1: mail')
            print('2: minecraft')
            print('3: etc')
            print('4: phone')
            choice_1 = input(': ')
            if choice_1 == '0':
                continue
            elif choice_1 == '1':
                adder_mail()
            elif choice_1 == '2':
                adder_minecraft()
            elif choice_1 == '3':
                adder_etc()
            elif choice_1 == '4':
                adder_phone()
        if choice == '2':
            print('0: exit')
            print('1: mail')
            print('2: minecraft')
            print('3: etc')
            print('4: phone')
            choice_2 = input(': ')
            if choice_2 == '0':
                print('exiting...')
                continue
            elif choice_2 == '1':
                mail()
            elif choice_2 == '2':
                minecraft()
            elif choice_2 == '3':
                etc()
            elif choice_2 == '4':
                phone()
main()
