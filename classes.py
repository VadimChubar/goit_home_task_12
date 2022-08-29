from collections import UserDict
from datetime import datetime



class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    pass


class Phone(Field):
    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value):
        cnt = 0
        for i in value:
            if i in ("0","1","2","3","4","5","6","7","8","9"," "):
                cnt += 0
            else:
                cnt += 1
        if cnt == 0:
            self._value = value

        else:
            self._value = "380000000000"
            print(f"{value} phone is not number")


class Birthday(Field):
    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value):
        string_date = ""
        for i in value:
            if i in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                string_date += i
        if len(string_date) == 8:
            self._value = value
        else:
            self._value = None
            print(f"{value} Birthday is not valid , need format DD.MM.YYYY")


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.name: Name = name
        self.phones: list[Phone] = [phone.value] if phone is not None else []
        self.birthday = birthday.value if birthday.value is not None else None

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number.value)

    def change_phone(self, old_number: Phone, new_number: Phone):
        try:
            self.phones.remove(old_number)
            self.phones.append(new_number)
        except ValueError:
            return f"{old_number} does not exists"

    def delete_phone(self, phone: Phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print(f"{phone} does not exists")

    def days_to_birthday(self):
        cnt_day = (datetime.strptime(self.birthday, "%d.%m.%Y").replace(
            year=datetime.now().year) - datetime.now()).days
        if self.birthday is None:
            return "days to birthday is not defined"
        else:
            return f"{cnt_day} days to birthday" if cnt_day > 0 else f"birthday was {cnt_day*-1} days ago"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name] = f"{record.name}  {record.phones}  {record.birthday}"
        # self.data[record.name] = record

    # def __str__(self):
    #     return str(self.data)


class Iterable:
    part_of_a_book = 1

    def __init__(self, my_list: AddressBook):
        self.my_list = list(my_list.items())
        self.index = 0

    def __next__(self):

        if self.index >= len(self.my_list)/self.part_of_a_book:
            raise StopIteration
        element = self.my_list[self.index]
        self.index += 1
        return element

    def __iter__(self):
        return self


# book = AddressBook()
# new_record_1 = Record("Tom", Phone(None), Birthday(None))
# # # new_record_2 = Record("Tom", Phone("1111111111"), Birthday("01.11.2002"))
# # # new_record_3 = Record("Jack", Phone("2222222222"), Birthday("01.01.2003"))
# book.add_record(new_record_1)
# # # book.add_record(new_record_2)
# # # book.add_record(new_record_3)
# print(book.data)

# iterable = Iterable(book.data)
# for i in iterable:
#     print(i)

# # new_record.add_phone(Phone("1111111111"))
# # new_record.add_phone(Phone("2222222222"))
# # new_record.delete_phone("0000000000")
# # new_record.change_phone("2222222222", "3333333333")
# print(new_record.name, "--", new_record.phones, "--",
#       new_record.birthday, "--", new_record.days_to_birthday())
# print(new_record.name, "--", new_record.phones, "--", new_record.birthday)
