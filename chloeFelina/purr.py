from typing import Union

def isQueryMatchKether(entry_string : str, txt_lines : tuple) -> bool:

    if not (len_txt_lines := len(txt_lines)):
        return False
    elif len_txt_lines == 1:
        try:
            current_line = txt_lines[0].decode().replace('\r','').replace('\n','')
        except UnicodeDecodeError:
            current_line = txt_lines[0].decode('latin-1',errors='replace').replace('\r','').replace('\n','')
        for word in tuple(current_line.lower().split(' ')):
            if entry_string in word:
                return True
    else:
        checked_index = -1
        for n in range(len_txt_lines-1):
            if n == checked_index:
                continue
            try:
                current_line = txt_lines[n].decode().replace('\r','').replace('\n','')
            except UnicodeDecodeError:
                current_line = txt_lines[n].decode('latin-1',errors='replace').replace('\r','').replace('\n','')
            try:
                next_line = txt_lines[n+1].decode().replace('\r','').replace('\n','')
            except UnicodeDecodeError:
                next_line = txt_lines[n+1].decode('latin-1',errors='replace').replace('\r','').replace('\n','')
            for word in tuple(current_line.lower().split(' ')+next_line.lower().split(' ')):
                if entry_string in word:
                    return True
            checked_index = n+1

    return False


def isQueryMatchBinah(entry_string : str, txt_lines : tuple) -> bool:

    if not (len_txt_lines := len(txt_lines)):
        return False
    elif len_txt_lines == 1:
        try: current_line = txt_lines[0].decode().replace('\r','').replace('\n','')
        except UnicodeDecodeError: current_line = txt_lines[0].decode('latin-1',errors='replace').replace('\r','').replace('\n','')
        current_line = current_line.lower()
        while entry_string in current_line:
            # prevents index-related error.
            max_index = len(current_line)-1
            if (temp_num := current_line.find(entry_string)+len(entry_string)) > max_index:
                return True
            elif not current_line[temp_num].isalnum():
                return True
    else:
        checked_index = -1
        for n in range(len_txt_lines-1):
            if n == checked_index:
                continue
            try: current_line = txt_lines[n].decode().replace('\r','').replace('\n','')
            except UnicodeDecodeError: current_line = txt_lines[n].decode('latin-1',errors='replace').replace('\r','').replace('\n','')
            try: next_line = txt_lines[n+1].decode().replace('\r','').replace('\n','')
            except UnicodeDecodeError: next_line = txt_lines[n+1].decode('latin-1',errors='replace').replace('\r','').replace('\n','')
            current_line_lower = current_line.lower() ; next_line_lower = next_line.lower()
            if entry_string in (temp_str := f'{current_line_lower}{next_line_lower}'):
                while entry_string in temp_str:
                    max_index = len(temp_str)-1
                    if (temp_num := temp_str.find(entry_string)+len(entry_string)) > max_index:
                        return True
                    elif not temp_str[temp_str].isalnum():
                        return True
                    temp_str = temp_str[temp_num:]
            elif entry_string in (temp_str := f'{current_line_lower} {next_line_lower}'):
                while entry_string in temp_str:
                    max_index = len(temp_str)-1
                    if (temp_num := temp_str.find(entry_string)+len(entry_string)) > max_index:
                        return True
                    elif not temp_str[temp_str].isalnum():
                        return True
                    temp_str = temp_str[temp_num:]
            checked_index = n+1

    return False

def isQueryMatchDaath(entry_string: str, entity_path : str, zf) -> bool:

    with zf.open(entity_path) as tf:
        while True:
            current_line = tf.readline()
            if not current_line:
                break
            try:
                current_line = current_line.decode().replace('\r','').replace('\n','')
            except UnicodeDecodeError:
                current_line = current_line.decode('latin-1',errors='replace').replace('\r','').replace('\n','')
            for item in tuple(current_line.lower().split('|')):
                for word in tuple(item.split(' ')):
                    if entry_string in word:
                        return True

    return False


def isQueryMatchChochmah(entry_string : str, entity_path : str, zf) -> bool:

    with zf.open(entity_path) as tf:
        while True:
            current_line = tf.readline()
            if not current_line:
                break
            try:
                current_line = current_line.decode().replace('\r','').replace('\n','')
            except UnicodeDecodeError:
                current_line = current_line.decode('latin-1',errors='replace').replace('\r','').replace('\n','')
            if entry_string in (current_line := current_line.lower()):
                while entry_string in current_line:
                    # Prevents index-related error.
                    max_index = len(current_line)-1
                    if (temp_num := current_line.find(entry_string)+len(entry_string)) > max_index:
                        return True
                    elif not current_line[temp_num].isalnum():
                        return True
                    current_line = current_line[temp_num:]

    return False


def isQueryMatchGewurah(entry_string : tuple, txt_lines : tuple, max_line_concat : int) -> bool:

    if not (len_txt_lines := len(txt_lines)):
        return False
    elif len_txt_lines == 1:
        try:
            current_line = txt_lines[0].decode().replace('\r','').replace('\n','')
        except UnicodeDecodeError:
            current_line = txt_lines[0].decode('latin-1',errors='replace').replace('\r','').replace('\n','')
        if entry_string in current_line.lower():
            return True
    elif len_txt_lines < max_line_concat:
        for n in range(len((txt_lines := list(txt_lines)))):
            try:
                txt_lines[n] = txt_lines[n].decode().replace('\r','').replace('\n','')
            except UnicodeDecodeError:
                txt_lines[n] = txt_lines[n].decode('latin-1',errors='replace').replace('\r','').replace('\n','')
        if entry_string in "".join((txt_lines := tuple(txt_lines))).lower() or " ".join(txt_lines).lower():
            return True
    else:
        for n in range(len_txt_lines-max_line_concat+1):
            current_lines = []
            for k in range(max_line_concat):
                try:
                    current_lines.append(txt_lines[n+k].decode().replace('\r','').replace('\n',''))
                except UnicodeDecodeError:
                    current_lines.append(txt_lines[n+k].decode('latin-1',errors='replace').replace('\r','').replace('\n',''))
            if entry_string in ''.join((current_lines := tuple(current_lines))).lower() or entry_string in ' '.join(current_lines).lower():
                return True

    return False


def forcedTxtFileWrite(output_path : str, lines : Union[list,tuple]) -> None:
    '''
    This forces a text file to be generated even with unexpected encodings being
    used.
    '''

    valid_encoding = False

    try:
        with open(output_path,'w',encoding='utf-8') as tf:
            tf.write(lines[0])
            for n in range(1,len(lines)):
                tf.write(f"\n{lines[n]}")
    except UnicodeEncodeError:
        try:
            with open(output_path,"w",encoding='latin-1') as tf:
                tf.write(lines[0])
                for n in range(1,len(lines)):
                    tf.write(f"\n{lines[n]}")
            valid_encoding = True
        except UnicodeEncodeError:
            with open(output_path,"w",encoding='cp1252') as tf:
                tf.write(lines[0])
                for n in range(1,len(lines)):
                    tf.write(f"\n{lines[n]}")
            valid_encoding = True

    # This is done in cases where a specific line is causing issues when being
    # writen to a text file. This skips the line and replaces it with placeholder
    # text indicate that it failed to be encoded to a text file.
    if not valid_encoding:
        try:
            with open(output_path,"w",encoding='utf-8') as tf:
                try:
                    tf.write(lines[0])
                except Exception:
                    tf.write("???UNABLE TO ENCODE LINE???")
                for n in range(1,len(lines)):
                    try:
                        tf.write(f"\n{lines[n]}")
                    except Exception:
                        tf.write("\n???UNABLE TO ENCODE LINE???")
            valid_encoding = True
        except Exception:
            pass

        if not valid_encoding:
            try:
                with open(output_path,"w",encoding='latin-1') as tf:
                    try:
                        tf.write(lines[0])
                    except Exception:
                        tf.write("???UNABLE TO ENCODE LINE???")
                    for n in range(1,len(lines)):
                        try:
                            tf.write(f"\n{lines[n]}")
                        except Exception:
                            tf.write("\n???UNABLE TO ENCODE LINE???")
                valid_encoding = True
            except Exception:
                pass

            if not valid_encoding:
                try:
                    with open(output_path,"w",encoding='cp1252') as tf:
                        try:
                            tf.write(lines[0])
                        except Exception:
                            tf.write("???UNABLE TO ENCODE LINE???")
                        for n in range(1,len(lines)):
                            try:
                                tf.write(f"\n{lines[n]}")
                            except Exception:
                                tf.write("\n???UNABLE TO ENCODE LINE???")
                    valid_encoding = True
                except Exception:
                    pass

                if not valid_encoding:
                    # This failsafe should reasonably never be executed.
                    with open(output_path,"w",encoding='utf-8') as tf:
                        tf.write('UNEXPECTED ENCODING(S) USED FOR TEXT')

    return None


def getImageTypeName(image_file_name : str) -> str:

    match image_file_name[image_file_name.rfind('.')+1:].lower():
        case 'tiff' | 'tif':
            return 'Tagged Image File Format (Image)'
        case 'png':
            return 'Portable Network Graphic (Image)'
        case 'jpeg' | 'jpg':
            return 'Joint Photographic Experts Group (Image)'
        case 'webp':
            return 'Google Web Photograph'
        case _:
            return 'UNKNOWN'
