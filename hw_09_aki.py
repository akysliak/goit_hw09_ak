'''
Possible commands:
    "hello", "add", "change", "phone",
    "show all", "good bye", "close", "exit"
Commands must be at the beginning of the input string,
    alone or followed bye an empty space
Recognition of the commands is case insensitive,
    the arguments are treated with respect to their case
    (e.g. name "ann" != "Ann")
The format of phone numbers is not verified
    (e.g. no checking if only digits and '+" are included),
    an empty space is treated as the end of the provided number
Provided arguments which are irrelevant for the specified command
    will be ignored (the command will be executed)

Possible improvements:
    format checking of the phone numbers
    extended functionality: e.g. delete-option
'''

ADDRESSBOOK = {}


def hello_handler(*args):
    return "How can I help you?"

def exit_handler(*args):
    return "Good bye!"


def add_handler(args):  # takes *arguments: 0-unlimited
    if len(args) < 2:
        raise ValueError("Give me name and phone please")
        return None, None
    name = args[0]  # change to 1) args[0].title() if you want to always capitalize the 1st letter or to 2) args[0].lower().title()
    phone = args[1]
    ADDRESSBOOK[name] = phone
    return f"New contact '{name}' with the phone number '{phone}' successfully added"

def change_handler(args):
    if len(args) < 2:
        raise ValueError("Give me name and phone please")
    name = args[0]
    phone = args[1]
    if name not in ADDRESSBOOK:
        raise KeyError(f"The phone number cannot be changed: the user name '{name}' is not in the ADDRESS BOOK")
    ADDRESSBOOK[name] = phone
    return f"Phone number for the contact '{name}' was successfully changed. New phone number: '{phone}'"

def phone_handler(args):
    if not args:
        raise ValueError("Enter user name")
    name = args[0]
    if name not in ADDRESSBOOK:
        raise KeyError(f"The phone number cannot be shown: the user name '{name}' is not in the ADDRESS BOOK")
    return ADDRESSBOOK[name]

def show_all_handler(*args):
    res = "\n".join([f"{name}:\t{phone}" for name, phone in ADDRESSBOOK.items()]).strip()
    return res


COMMANDS = {
    hello_handler: ["hello"],
    add_handler: ["add"],
    change_handler: ["change"],

    phone_handler: ["phone"],
    show_all_handler: ["show all"],
    exit_handler: ["good bye", "close", "exit"]
}

def command_parcer(raw_str: str) -> (callable,list):
    case_insensitive = raw_str.lower()
    for handler, commands in COMMANDS.items():
        for command in commands:
            if case_insensitive == command or case_insensitive.startswith(command + " "):
                args = raw_str[len(command):].split()
                return handler, args
    return None, None

def input_error(fnc):
    def inner(*args):
        try:
            fnc(*args)
        except (IndexError, KeyError, ValueError) as e:
            print(str(e).replace('"', ""))
            inner()

    return inner

@input_error
def main():
    while True:
        u_input = input(">>> ")
        func, data = command_parcer(u_input)
        while not func:
            print("The command is not defined. Please, use a valid command")
            u_input = input(">>> ")
            func, data = command_parcer(u_input)
        result = func(data)
        print(result)
        if func == exit_handler:
            break


if __name__ == "__main__":
    main()
