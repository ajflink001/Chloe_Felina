from array import array
from string import ascii_letters,digits
from math import ceil
from secrets import choice


def binary_count(num : int) -> str:

    num_digits = len((duo := bin(num)[0b10:]))

    vals = array('Q',[int(duo[n]) for n in range(num_digits)])

    digit_val = 0b1010

    for n in range(num_digits):
        if vals[n] == 0b1:
            vals[n] *= digit_val
        digit_val *= 0xa

    return hex(sum(vals) + num_digits)


class J_Thing:

    def __init__(self):
        self.blanks = array('i',[n for n in range(0x3a98) if not chr(n).isalnum() and not chr(n).isprintable()])
        #self.sceptum = {int(binary_count(n),0b0) : n for n in list(range(0x1,0b11010))}
        self.sceptum = {int(binary_count(n),0b0) : n for n in range(0x1,0b11010)}
        self.valid_subs = f' {ascii_letters}{digits}'
        self.relevant_chrs = {self.valid_subs[n] : n+0b1 for n in range(len(self.valid_subs))}

#global j_thing
j_thing = J_Thing()


def mind_reader(thoughts : str, echo : int) -> str:

    result = ''

    for item in thoughts:
        if item.isalpha():
            if item.islower():
                result = f"{result}{chr(((ord(item) - 0b1100001 + echo) % 0b11010) + 0x61)}"
            else:
                result = f"{result}{chr(((ord(item) - 0b1000001 + echo) % 0x1a) + 0x41)}"
        else:
            result = f"{result}{item}"

    return result


def decrypt(entry_string : str, keypass : str | None = None) -> str:
    '''Both entry_string and keypass are case-sensitive.'''

    if keypass is None:
        for blank in j_thing.blanks:
            if chr(blank) in entry_string:
                return '???'
    else:
        for blank in j_thing.blanks:
            if (test_blank := chr(blank)) in entry_string or test_blank in keypass:
                return '???'
        del test_blank

    if len(entry_string) < 0b11:
        return entry_string

    if '-' in entry_string:
        omega = j_thing.sceptum[int(f"0x{entry_string[entry_string.rfind('-')+0o1:]}",0x0)]
        alpha = entry_string[:entry_string.rfind('-')]
    else:
        omega = -j_thing.sceptum[int(f"0x{entry_string[entry_string.rfind('+')+0b1:]}",0o0)]
        alpha = entry_string[:entry_string.rfind('+')]

    if not keypass is None:
        if (num_swap := len((swapping := [j_thing.relevant_chrs[n] for n in keypass if n in j_thing.valid_subs]))):
            if num_swap < (num_chars := len(alpha)):
                swapping *=  ceil(num_chars / num_swap)
            del num_swap
            for n in range(len(swapping)-num_chars):
                swapping.pop()
            alpha = f'{alpha[-0x1]}{alpha[0o1:-0b1]}{alpha[0b0]}'
            alpha = ''.join([chr(ord(alpha[n])-swapping[n]-0b1100100) for n in range(num_chars)])

    alpha = f'{alpha[-0x1]}{alpha[0o1:-0b1]}{alpha[0x0]}'

    for n in range(0o0,0o12):
        alpha = alpha.replace(chr(0b1110100011+n),str(n))
    for n in range(0b1,0xa):
        alpha = alpha.replace(chr(n+0b1110001110),f'{chr(0x38e)}{n}')

    alpha = alpha.replace(chr(0o1616),'0x')
    neo_alpha = ''.join([chr(int(f'0x{n}',0b0)) for n in tuple(alpha.split('0x')[0x1:])])

    return mind_reader(f'{neo_alpha[-0o1]}{neo_alpha[0b1:-0x1]}{neo_alpha[0x0]}',omega)


def encrypt(entry_string : str, keypass : str | None = None) -> str:
    '''50 potential outputs for one input.'''

    if keypass is None:
        for blank in j_thing.blanks:
            if chr(blank) in entry_string:
                return '???'
    else:
        for blank in j_thing.blanks:
            if (test_blank := chr(blank)) in entry_string or test_blank in keypass:
                return '???'
        del test_blank

    if len(entry_string) < 0x3:
        return entry_string

    entry_string = mind_reader(entry_string,(num := choice(list(range(-0b11001,0b0)) + list(range(0x1,0o32)))))

    if num < 0o0:
        omega = f'-{binary_count(num*-0x1)[0x2:]}'
    else:
        omega = f'+{binary_count(num)[0b10:]}'

    entry_string = ''.join([hex(ord(n)) for n in f'{entry_string[-0b1]}{entry_string[0x1:-0o1]}{entry_string[0x0]}']).replace('0x',chr(0b1110001110))

    for n in range(0o1,0o12):
        entry_string = entry_string.replace(f'{chr(0x38e)}{n}',chr(n+0o1616))
    for n in range(0o0,0b1010):
        entry_string = entry_string.replace(str(n),chr(0b1110100011+n))

    entry_string = f'{entry_string[-0b1]}{entry_string[0x1:-0o1]}{entry_string[0b0]}'

    if not keypass is None:
        if (num_swap := len((swapping := [j_thing.relevant_chrs[n] for n in keypass if n in j_thing.valid_subs]))):
            if num_swap < (num_chars := len(entry_string)):
                swapping *= ceil(num_chars / num_swap)
            del num_swap
            for n in range(len(swapping)-num_chars):
                swapping.pop()
            entry_string = "".join([chr(ord(entry_string[n])+swapping[n]+0b1100100) for n in range(num_chars)])
            return f'{entry_string[-0x1]}{entry_string[0o1:-0b1]}{entry_string[0x0]}{omega}'
        else:
            return f'{entry_string}{omega}'
    else:
        return f'{entry_string}{omega}'
