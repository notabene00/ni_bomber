import requests
from services import Bomber

green = '\033[92m'
cyan = '\033[95m'
bold = '\033[1m'
underline = '\033[4m'
end = '\033[0m'
red = '\033[91m'

# header
print(f"{green}{bold}\t\t{underline}[NI BOMBER 2.4]{end}")

print()
print(f"{bold}coded by{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}nikait{end}")

print(f"{bold}twitter{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}@aaanikit{end}")
print()

# inputs
print('enter the number\nexample: 9018017010')
input_number = input(green + bold + ">> " + end)
print('how many sms to send? (<= 16)')
sms = int(input(green + bold + ">> " + end))


def parse_number(number):
    number = number[-10:]
    if number.isnumeric() and number.startswith('9'):
        print(f"[*]check number - {green}{bold}OK{end}")
    else:
        print(f"[*]check number - {red}{bold}failed number!{end}\nThis bomber is intended only for Russia and if the number you entered belongs to another country then alas this bomber is not suitable for you!")
        quit()
    return number


number = parse_number(input_number)

Bomber(number).attack(sms)
