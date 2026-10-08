from decimal import Decimal

# LE == less than or equal to
# L == less than
# E == equal to
# GE == greater than or equal to
# G == greater than

def convertDigitToBytes(entry_string : str) -> str | None:

    unit_first_chars = {'B','K','M','G','T','E','Z','Y','R','Q','b','k','m','g','t','e','z','y','r','q'}
    and_or_first_chars = {'A','O','a','o'}
    digital_units = {""}

    entry_string = entry_string.replace(",","")
    entry_string = entry_string.replace('S','')
    entry_string = entry_string.replace('s','')

    neo_str = ""

    while 'B' in entry_string or 'b' in entry_string:
        last_index = 0
        found_and_or = False
        for n in range(len(entry_string)):
            if entry_string[n] in unit_first_chars:
                last_index = n
                break
            elif entry_string[n] in and_or_first_chars:
                if entry_string[n] in ('A','a'):
                    last_index = n + 3
                else:
                    last_index = n + 2
                found_and_or = True
                break
        if found_and_or:
            try:
                neo_str = f"{neo_str}{entry_string[:last_index]}" ; entry_string = entry_string[last_index:]
            except IndexError:
                return None
        else:
            try:
                num = Decimal(float((og_num := "".join([n for n in entry_string[:last_index] if n.isdigit() or n == '.']))))
            except ValueError:
                return None
            relevant_portion = entry_string[last_index:] ; relevant_portion_lower = relevant_portion.lower()
            if relevant_portion_lower.startswith('band') or relevant_portion_lower.startswith('bor') or relevant_portion_lower == 'b':
                if entry_string[last_index] == 'b':
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(8)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    if len(entry_string[last_index:]) == 1:
                        break
                    else:
                        try: entry_string = entry_string[last_index+1:]
                        except IndexError: break
                else:
                    neo_str = f"{neo_str}{entry_string[:last_index]}"
                    try: entry_string = entry_string[last_index+1:]
                    except IndexError: break
            else:
                # Yes, this scary long if-elif-else is necessary.
                if relevant_portion_lower.startswith('byte'):
                    # Accounts for ".00001" or ".9999999" being included in the string.
                    if '.' in (neo_str := f"{neo_str}{entry_string[:last_index]}"):
                        if neo_str.count('.') > 1:
                            return None
                        first_num_index = -1
                        for n in range(len(neo_str)):
                            if neo_str[n].isdigit():
                                first_num_index = n
                                break
                        if first_num_index == -1:
                            return None
                        if first_num_index > neo_str.find('.'):
                            neo_str = neo_str.replace(neo_str[neo_str.find('.'):],"0")
                        else:
                            neo_str = neo_str[:neo_str.find('.')]
                    try: entry_string = entry_string[last_index+4:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('bit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num / Decimal(8)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion.startswith('kB') or relevant_portion.startswith('KB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('kilobyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('kb') or relevant_portion.startswith('Kb'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif  relevant_portion_lower.startswith('kilobit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('kibibyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1024)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('kibibit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(128)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('KiB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1024)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion.startswith('Kib'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(128)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('megabyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('MB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('megabit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Mb'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('mebibyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_048_576)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('MiB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_048_576)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('mebibit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(131_072)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Mib'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(131_072)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('gigabyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('GB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('gigabit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Gb'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('gibibyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_073_741_824)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('GiB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_073_741_824)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('gibibit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(134_217_728)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Gib'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(134_217_728)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('terabyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('TB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('terabit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Tb'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('tebibyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_099_511_627_776)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('TiB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_099_511_627_776)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('tebibit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(137_438_953_472)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Tib'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(137_438_953_472)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('petabyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('PB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('petabit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Pb'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('pebibyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_125_899_906_842_624)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('PiB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_125_899_906_842_624)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('pebibit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(140_737_488_355_328)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Pib'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(140_737_488_355_328)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('exabyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('EB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('exabit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+6:]
                    except IndexError: break
                elif relevant_portion.startswith('Eb'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('exbibyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_152_921_504_606_846_976)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('EiB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_152_921_504_606_846_976)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('exbibit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(144_115_188_075_855_872)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Eib'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(144_115_188_075_855_872)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('zettabyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+9:]
                    except IndexError: break
                elif relevant_portion.startswith('ZB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('zettabit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('Zb'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('zebibyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_152_921_504_606_846_976)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('ZiB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_152_921_504_606_846_976)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('zebibit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(147_573_952_589_676_412_928)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Zib'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(147_573_952_589_676_412_928)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('yottabyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+9:]
                    except IndexError: break
                elif relevant_portion.startswith('YB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('yottabit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('Yb'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('yobibyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_208_925_819_614_629_174_706_176)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('YiB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_208_925_819_614_629_174_706_176)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('yobibit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(151_115_727_451_828_646_838_272)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Yib'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(151_115_727_451_828_646_838_272)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('ronnabyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+9:]
                    except IndexError: break
                elif relevant_portion.startswith('RB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('ronnabit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('Rb'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('robibyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_237_940_039_285_380_274_899_124_224)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('RiB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_237_940_039_285_380_274_899_124_224)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('robibit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(154_742_504_910_672_534_362_390_528)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Rib'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(154_742_504_910_672_534_362_390_528)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('quettabyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+10:]
                    except IndexError: break
                elif relevant_portion.startswith('QB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_000_000_000_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('quettabit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+9:]
                    except IndexError: break
                elif relevant_portion.startswith('Qb'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(125_000_000_000_000_000_000_000_000_000)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+2:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('quebibyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_267_650_600_228_229_401_496_703_205_376)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+9:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('qubibyte'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_267_650_600_228_229_401_496_703_205_376)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion.startswith('QiB'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(1_267_650_600_228_229_401_496_703_205_376)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('quebibit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(158_456_325_028_528_675_187_087_900_672)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+8:]
                    except IndexError: break
                elif relevant_portion_lower.startswith('qubibit'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(158_456_325_028_528_675_187_087_900_672)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+7:]
                    except IndexError: break
                elif relevant_portion.startswith('Qib'):
                    relevant_portion = entry_string[:last_index].replace(og_num,str(int(round(float(num * Decimal(158_456_325_028_528_675_187_087_900_672)))))) ; neo_str = f"{neo_str}{relevant_portion}"
                    try: entry_string = entry_string[last_index+3:]
                    except IndexError: break
                else:
                    # Invalid statement found in query.
                    return None

    if len(entry_string):
        neo_str = f"{neo_str}{entry_string}"
    return neo_str


def getSizeQueryTuple(entry_string : str) -> tuple | None:

    entry_string = entry_string.replace(' ','')

    # Addresses potential typos
    while '===' in entry_string:
        entry_string = entry_string.replace('===','==')
    while '<<' in entry_string:
        entry_string = entry_string.replace('<<','<')
    while '>>' in entry_string:
        entry_string = entry_string.replace('>>','>')
    while '>==' in entry_string:
        entry_string = entry_string.replace('>==','>=')
    while '==>' in entry_string:
        entry_string = entry_string.replace('==>','=>')
    while '==<' in entry_string:
        entry_string = entry_string.replace('==<','=<')

    if (entry_string := convertDigitToBytes(entry_string)) is None:
        return None

    # Not including [] will result in a memory leak where it will keep in memory
    # all previous inputs for getSizeQueryTuple. Including [] "overwrites"
    # all previously determined queries.
    size_query = sizeSpecification(entry_string.upper(),[])

    if size_query is None:
        return None

    return size_query

def sizeSpecification(entry_string : str, queries : list = []) -> tuple | None:

    if entry_string.startswith('>=') or entry_string.startswith('=>'):
        if not entry_string[2].isdigit():
            return None
        else:
            entry_string = entry_string[2:]
            num = ""
            last_index = 0
            for n in entry_string:
                if n.isdigit():
                    num = f'{num}{n}'
                    last_index += 1
                else:
                    break
            if last_index == len(entry_string):
                queries.append(SizeLimit_GE(int(num)))
                return tuple(queries)
            else:
                entry_string = entry_string[last_index:]
                if entry_string.startswith('OR'):
                    queries.append(SizeLimit_GE(int(num)))
                    return sizeSpecification(entry_string[2:],queries)
                elif entry_string.startswith('AND'):
                    try:
                        entry_string = entry_string[3:]
                    except IndexError:
                        return None
                    if entry_string.startswith('<=') or entry_string.startswith('=<'):
                        if not entry_string[2].isdigit():
                            return None
                        else:
                            entry_string = entry_string[2:]
                            num2 = ""
                            last_index = 0
                            for n in entry_string:
                                if n.isdigit():
                                    num2 = f'{num2}{n}'
                                    last_index += 1
                                else:
                                    break
                            if last_index == len(entry_string):
                                if (num := int(num)) < (num2 := int(num2)):
                                    queries.append(SizeCompare_LE_GE(num,num2))
                                    return tuple(queries)
                                else:
                                    return None
                            else:
                                entry_string = entry_string[last_index:]
                                if entry_string.startswith('OR'):
                                    if (num := int(num)) < (num2 := int(num2)):
                                        queries.append(SizeCompare_LE_GE(num,num2))
                                        try:
                                            return sizeSpecification(entry_string[2:],queries)
                                        except IndexError:
                                            return None
                                    else:
                                        return None
                                else:
                                    return None
                    elif entry_string.startswith('<'):
                        if not entry_string[1].isdigit():
                            return None
                        else:
                            entry_string = entry_string[1:]
                            num2 = ""
                            last_index = 0
                            for n in entry_string:
                                if n.isdigit():
                                    num2 = f'{num2}{n}'
                                    last_index += 1
                                else:
                                    break
                            if last_index == len(entry_string):
                                if (num := int(num)) < (num2 := int(num2)):
                                    queries.append(SizeCompare_L_GE(num,num2))
                                    return tuple(queries)
                                else:
                                    return None
                            else:
                                entry_string = entry_string[last_index:]
                                if entry_string.startswith('OR'):
                                    if (num := int(num)) < (num2 := int(num2)):
                                        queries.append(SizeCompare_L_GE(num,num2))
                                        try:
                                            return sizeSpecification(entry_string[2:],queries)
                                        except IndexError:
                                            return None
                                    else:
                                        return None
                                else:
                                    return None
                    else:
                        return None
                else:
                    return None
    elif entry_string.startswith('<=') or entry_string.startswith('=<'):
        if not entry_string[2].isdigit():
            return None
        else:
            entry_string = entry_string[2:]
            num = ""
            last_index = 0
            for n in entry_string:
                if n.isdigit():
                    num = f'{num}{n}'
                    last_index += 1
                else:
                    break
            if last_index == len(entry_string):
                queries.append(SizeLimit_LE(int(num)))
                return tuple(queries)
            else:
                entry_string = entry_string[last_index:]
                if entry_string.startswith('OR'):
                    queries.append(SizeLimit_LE(int(num)))
                    return sizeSpecification(entry_string[2:],queries)
                elif entry_string.startswith('AND'):
                    try:
                        entry_string = entry_string[3:]
                    except IndexError:
                        return None
                    if entry_string.startswith('>=') or entry_string.startswith('=>'):
                        if not entry_string[2].isdigit():
                            return None
                        else:
                            entry_string = entry_string[2:]
                            num2 = ""
                            last_index = 0
                            for n in entry_string:
                                if n.isdigit():
                                    num2 = f'{num2}{n}'
                                    last_index += 1
                                else:
                                    break
                            if last_index == len(entry_string):
                                if (num := int(num)) > (num2 := int(num2)):
                                    queries.append(SizeCompare_LE_GE(num2,num))
                                    return tuple(queries)
                                else:
                                    return None
                            else:
                                entry_string = entry_string[last_index:]
                                if entry_string.startswith('OR'):
                                    if (num := int(num)) > (num2 := int(num2)):
                                        queries.append(SizeCompare_LE_GE(nu2,num))
                                        try:
                                            return sizeSpecification(entry_string[2:],queries)
                                        except IndexError:
                                            return None
                                    else:
                                        return None
                                else:
                                    return None
                    elif entry_string.startswith('>'):
                        if not entry_string[1].isdigit():
                            return None
                        else:
                            entry_string = entry_string[1:]
                            num2 = ""
                            last_index = 0
                            for n in entry_string:
                                if n.isdigit():
                                    num2 = f'{num2}{n}'
                                    last_index += 1
                                else:
                                    break
                            if last_index == len(entry_string):
                                if (num := int(num)) > (num2 := int(num2)):
                                    queries.append(SizeCompare_LE_G(num2,num))
                                    return tuple(queries)
                                else:
                                    return None
                            else:
                                entry_string = entry_string[last_index:]
                                if entry_string.startswith('OR'):
                                    if (num := int(num)) > (num2 := int(num2)):
                                        queries.append(SizeCompare_LE_G(num2,num))
                                        try:
                                            return sizeSpecification(entry_string[2:],queries)
                                        except IndexError:
                                            return None
                                    else:
                                        return None
                                else:
                                    return None
                    else:
                        return None
                else:
                    return None
    elif entry_string.startswith('>'):
        if not entry_string[1].isdigit():
            return None
        else:
            entry_string = entry_string[1:]
            num = ""
            last_index = 0
            for n in entry_string:
                if n.isdigit():
                    num = f'{num}{n}'
                    last_index += 1
                else:
                    break
            if last_index == len(entry_string):
                queries.append(SizeLimit_G(int(num)))
                return tuple(queries)
            else:
                entry_string = entry_string[last_index:]
                if entry_string.startswith('OR'):
                    queries.append(SizeLimit_G(int(num)))
                    return sizeSpecification(entry_string[2:],queries)
                elif entry_string.startswith('AND'):
                    try:
                        entry_string = entry_string[3:]
                    except IndexError:
                        return None
                    if entry_string.startswith('<=') or entry_string.startswith('=<'):
                        if not entry_string[2].isdigit():
                            return None
                        else:
                            entry_string = entry_string[2:]
                            num2 = ""
                            last_index = 0
                            for n in entry_string:
                                if n.isdigit():
                                    num2 = f'{num2}{n}'
                                    last_index += 1
                                else:
                                    break
                            if last_index == len(entry_string):
                                if (num := int(num)) < (num2 := int(num2)):
                                    queries.append(SizeCompare_LE_G(num,num2))
                                    return tuple(queries)
                                else:
                                    return None
                            else:
                                entry_string = entry_string[last_index:]
                                if entry_string.startswith('OR'):
                                    if (num := int(num)) < (num2 := int(num2)):
                                        queries.append(SizeCompare_LE_G(num,num2))
                                        try:
                                            return sizeSpecification(entry_string[2:],queries)
                                        except IndexError:
                                            return None
                                    else:
                                        return None
                                else:
                                    return None
                    elif entry_string.startswith('<'):
                        if not entry_string[1].isdigit():
                            return None
                        else:
                            entry_string = entry_string[1:]
                            num2 = ""
                            last_index = 0
                            for n in entry_string:
                                if n.isdigit():
                                    num2 = f'{num2}{n}'
                                    last_index += 1
                                else:
                                    break
                            if last_index == len(entry_string):
                                if (num := int(num)) < (num2 := int(num2)):
                                    queries.append(SizeCompare_L_G(num,num2))
                                    return tuple(queries)
                                else:
                                    return None
                            else:
                                entry_string = entry_string[last_index:]
                                if entry_string.startswith('OR'):
                                    if (num := int(num)) < (num2 := int(num2)):
                                        queries.append(SizeCompare_L_G(num,num2))
                                        try:
                                            return sizeSpecification(entry_string[2:],queries)
                                        except IndexError:
                                            return None
                                    else:
                                        return None
                                else:
                                    return None
                    else:
                        return None
                else:
                    return None
    elif entry_string.startswith('<'):
        if not entry_string[1].isdigit():
            return None
        else:
            entry_string = entry_string[1:]
            num = ""
            last_index = 0
            for n in entry_string:
                if n.isdigit():
                    num = f'{num}{n}'
                    last_index += 1
                else:
                    break
            if last_index == len(entry_string):
                queries.append(SizeLimit_L(int(num)))
                return tuple(queries)
            else:
                entry_string = entry_string[last_index:]
                if entry_string.startswith('OR'):
                    queries.append(SizeLimit_L(int(num)))
                    return sizeSpecification(entry_string[2:],queries)
                elif entry_string.startswith('AND'):
                    try:
                        entry_string = entry_string[3:]
                    except IndexError:
                        return None
                    if entry_string.startswith('>=') or entry_string.startswith('=>'):
                        if not entry_string[2].isdigit():
                            return None
                        else:
                            entry_string = entry_string[2:]
                            num2 = ""
                            last_index = 0
                            for n in entry_string:
                                if n.isdigit():
                                    num2 = f'{num2}{n}'
                                    last_index += 1
                                else:
                                    break
                            if last_index == len(entry_string):
                                if (num := int(num)) > (num2 := int(num2)):
                                    queries.append(SizeCompare_L_GE(num2,num))
                                    return tuple(queries)
                                else:
                                    return None
                            else:
                                entry_string = entry_string[last_index:]
                                if entry_string.startswith('OR'):
                                    if (num := int(num)) > (num2 := int(num2)):
                                        queries.append(SizeCompare_L_GE(nu2,num))
                                        try:
                                            return sizeSpecification(entry_string[2:],queries)
                                        except IndexError:
                                            return None
                                    else:
                                        return None
                                else:
                                    return None
                    elif entry_string.startswith('>'):
                        if not entry_string[1].isdigit():
                            return None
                        else:
                            entry_string = entry_string[1:]
                            num2 = ""
                            last_index = 0
                            for n in entry_string:
                                if n.isdigit():
                                    num2 = f'{num2}{n}'
                                    last_index += 1
                                else:
                                    break
                            if last_index == len(entry_string):
                                if (num := int(num)) > (num2 := int(num2)):
                                    queries.append(SizeCompare_L_G(num2,num))
                                    return tuple(queries)
                                else:
                                    return None
                            else:
                                entry_string = entry_string[last_index:]
                                if entry_string.startswith('OR'):
                                    if (num := int(num)) > (num2 := int(num2)):
                                        queries.append(SizeCompare_L_G(num2,num))
                                        try:
                                            return sizeSpecification(entry_string[2:],queries)
                                        except IndexError:
                                            return None
                                    else:
                                        return None
                                else:
                                    return None
                    else:
                        return None
                else:
                    return None
    elif entry_string.startswith('=='):
        if not entry_string[2].isdigit():
            return None
        else:
            entry_string = entry_string[2:]
            num = ""
            last_index = 0
            for n in entry_string:
                if n.isdigit():
                    num = f'{num}{n}'
                    last_index += 1
                else:
                    break
            if last_index == len(entry_string):
                queries.append(SizeLimit_E(int(num)))
                return tuple(queries)
            else:
                entry_string = entry_string[last_index:]
                if entry_string.startswith('OR'):
                    queries.append(SizeLimit_E(int(num)))
                    return sizeSpecification(entry_string[2:],queries)
                else:
                    # Logic Error
                    return None
    elif entry_string.startswith('='):
        if not entry_string[1].isdigit():
            return None
        else:
            entry_string = entry_string[1:]
            num = ""
            last_index = 0
            for n in entry_string:
                if n.isdigit():
                    num = f'{num}{n}'
                    last_index += 1
                else:
                    break
            if last_index == len(entry_string):
                queries.append(SizeLimit_E(int(num)))
                return tuple(queries)
            else:
                entry_string = entry_string[last_index:]
                if entry_string.startswith('OR'):
                    queries.append(SizeLimit_E(int(num)))
                    return sizeSpecification(entry_string[2:],queries)
                else:
                    # Logic Error
                    return None
    else:
        return None

class SizeCompare_LE_GE:

    def __init__(self, min_num : int, max_num : int):
        self.min_num = min_num
        self.max_num = max_num

    def range_check(self, size : int) -> bool:
        if size <= self.max_num and size >= self.min_num:
            return True
        return False

class SizeCompare_LE_G:

    def __init__(self, min_num : int, max_num : int):
        self.min_num = min_num
        self.max_num = max_num

    def range_check(self, size : int) -> bool:
        if size <= self.max_num and size > self.min_num:
            return True
        return False

class SizeCompare_L_GE:

    def __init__(self, min_num : int, max_num : int):
        self.min_num = min_num
        self.max_num = max_num

    def range_check(self, size : int) -> bool:
        if size < self.max_num and size >= self.min_num:
            return True
        return False

class SizeCompare_L_G:

    def __init__(self, min_num : int, max_num : int):
        self.min_num = min_num
        self.max_num = max_num

    def range_check(self, size : int) -> bool:
        if size < self.max_num and size > self.min_num:
            return True
        return False

class SizeLimit_E:

    def __init__(self, num : int):
        self.num = num

    def range_check(self, size : int) -> bool:
        if size == self.num:
            return True
        return False

class SizeLimit_LE:

    def __init__(self, num : int):
        self.num = num

    def range_check(self, size : int) -> bool:
        if size <= self.num:
            return True
        return False

class SizeLimit_L:

    def __init__(self, num : int):
        self.num = num

    def range_check(self, size : int) -> bool:
        if size < self.num:
            return True
        return False

class SizeLimit_GE:

    def __init__(self, num : int):
        self.num = num

    def range_check(self, size : int) -> bool:
        if size >= self.num:
            return True
        return False

class SizeLimit_G:

    def __init__(self, num : int):
        self.num = num

    def range_check(self, size : int) -> bool:
        if size < self.num:
            return True
        return False
