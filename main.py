from classes import *
import csv


def write_contacts_to_file(contacts):
    for k in contacts.keys():
        b = k
    for i in contacts.values():
        a = i.split()

    with open('phonebook.csv', 'a', newline='') as fh:
        field_names = ['key', 'name', 'phone', 'birthday']
        writer = csv.DictWriter(fh, fieldnames=field_names)
        # writer.writeheader()
        writer.writerow({'key': b, 'name': a[0], 'phone': a[1], 'birthday': a[2]})


def read_contacts_from_file():
    with open('phonebook.csv', newline='') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            print(row['key'], row['name'], row['phone'], row['birthday'])

def unknown_command():
    print("Please repeat your command")

def f_add():
    pass

def f_show():
    pass

def f_find():
    pass

def f_change(old_value, new_value):

    with open('phonebook.csv', 'r') as fh:
        old_data = fh.read()

    new_data = old_data.replace(old_value, new_value)

    with open('phonebook.csv', 'a') as fh:
        fh.write(new_data)

def user_input_parser(user_input):
    global command, name, phone, birthday
    user_input_split = user_input.split()
    command = user_input_split[0]

    try:
        name = user_input_split[1]
    except IndexError:
        name = None

    try:
        birthday = user_input_split[-1]
    except ValueError:
        birthday = None

    try:
        phone = user_input_split[2]
    except IndexError:
        phone = None

commands = {

    "add": f_add,
    "show": f_show,
    "find": f_find,
    "change": f_change
}


def main():

    global user_input, phonebook

    phonebook = AddressBook()

    while True:
        user_input = input("Enter your command: ").lower()

        if user_input in (".", "good bye", "close", "exit"):
            print("Good bye!")
            break

        user_input_parser(user_input)
        handler = commands.get(command, unknown_command)

        if handler == unknown_command:
            handler()
        elif handler == f_add:
            new_record = Record(name, Phone(phone), Birthday(birthday))
            phonebook.add_record(new_record)
            write_contacts_to_file(phonebook.data)

        elif handler == f_show:
            read_contacts_from_file()

        elif handler == f_find:
            word_split =  user_input.split()
            word =  word_split[1]
            with open('phonebook.csv', newline='') as fh:
                for line in fh:
                    if word in line:
                        print(line, end='')

        elif handler == f_change:
            string_split = user_input.split()
            old_value = string_split[1]
            new_value = string_split[2]
            f_change(old_value,new_value)



main()

