phonebook = {}


def input_error(input_func):  
    def output_func(*args):  
        try:
            result = input_func(*args)
            return result
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "ValueError. Please enter the name and phone number."
        except IndexError:
            return "IndexError. Give me name and phone please."

    return output_func

@input_error
def add_contact(data):
    name = str(data[0])
    phone = int(data[1])
    if name not in phonebook.keys() and len(data[1]) == 10:
        phonebook.update({name: phone})
        return f"added new name: {name} and phone: {phone}"
    elif name in phonebook.keys():
        return f"name already added to phonebook"
    elif len(data[1]) != 10:
        return f"wrong number phone"

@input_error
def change_contact(data):
    name = str(data[0])
    phone = int(data[1])
    if name in phonebook.keys() and len(data[1]) == 10:
        phonebook.update({name: phone})
        return f"changed phone"
    elif name not in phonebook.keys():
        return f"name is not in phonebook"
    elif len(data[1]) != 10:
        return f"wrong number phone"
@input_error
def phone_info(data):
    data = data[0]
    return f"{phonebook[data]}"

@input_error
def show_all(data):
    result = ""
    for key, value in phonebook.items():
        f = f"{key}: {value}\n"
        result += f
    return f"{result}"

@input_error
def hello(data):
    return f"How can I help you?"


OPERATIONS = {
    'add': add_contact,
    'change': change_contact,
    'phone': phone_info,
    'show all': show_all,
    "hello": hello
}
exit_list = ["good bye", "close", "exit"]

help_message = "Please enter command:\n'show all'\n'phone (name)'\n'add (name phone)'\n'change (name new_phone)'"


def main():
    while True:
        value = input(F'Please enter command : ')
        func, data = parser(value)
        if func in exit_list:
            print("Good bye!")
            break
        elif func in OPERATIONS.keys():
            print(handle_operation(func)(data))
        else:
            print(help_message)

@input_error
def parser(input_):
    input_ = input_.strip()
    inp = input_.lower()
    for key in OPERATIONS.keys():
        if inp.startswith(key):
            f = input_[len(key) + 1:].split(" ")
            return key, f
    return input_, "not_working"


@input_error
def handle_operation(operator):
    return OPERATIONS[operator]


if __name__ == "__main__":
    main()