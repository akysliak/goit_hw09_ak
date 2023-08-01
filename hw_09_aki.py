ADDRESSBOOK = {}

def input_error(fnc):
    def inner(*args):
        try:
            result = fnc(*args)
            return result
        except IndexError:
            return "blalbalabala"

    return inner

@input_error
def add_handler(data): # takes *arguments: 0-unlimited
    name = data[0].title()
    phone = data[1]
    email = data[2]
    ADDRESSBOOK[name] = phone
    return name


def exit_handler(*args):
    return "Good bye"

def hello_handler(*args):
    return "Hello"


def command_parcer(raw_str: str) -> (callable,list):
    items = raw_str.split()
    for k, v in COMMANDS.items():
        if items[0].lower() in v:
            return k, items[1:]


COMMANDS = {
    add_handler: ["add", "+"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"]
}

@input_error
def main():
    while True:
        u_input = input(">>> ")
        func, data = command_parcer(u_input)
        result = func(data)
        print(result)
        if func == exit_handler:
            break
        print(ADDRESSBOOK)


if __name__ == "__main__":
    main()

