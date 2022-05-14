from listen import listen
from say import say


def out(message):
    print(message)
    say(message)


if __name__ == '__main__':
    out("Say something!")
    out(listen())
