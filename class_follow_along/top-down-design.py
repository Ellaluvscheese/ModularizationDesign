# this program will convert a number to binary, octal, hexadecimal, or all
def main():
    number = get_num()
    format = get_format()
    display(convert_num(number, format))
    print("this works")
    return

def get_num():
    return 10

def get_format():
    return 'all'

def convert_num(num, format):
    binary = to_binary(num)
    octal = to_octal(num)
    hex = to_hex(num)
    return '01011'

def to_binary(num):
    return 'b011'

def to_octal(num):
    return '0347'

def to_hex(num):
    return '0xf'

def display(converted_num):
    return print(f"the number is {converted_num}")

main()