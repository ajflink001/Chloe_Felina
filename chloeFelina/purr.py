import re
from typing import AnyStr

forbidden_file_chars = ('\\','/','*','?','"',"<",">","|")

def fileNameFixer(entry_string : str) -> str:

    for char in forbidden_file_chars:
        entry_string = entry_string.replace(char,'')

    return entry_string

def decodeZipTxtLine(entry_string) -> str:

    try:
        return entry_string.decode().replace('\r','').replace('\n','')
    except UnicodeDecodeError:
        return entry_string.decode('latin-1',errors='replace').replace('\r','').replace('\n','')


def getTxtFileLines(txt_file_path : str, expected_encoding : str = 'utf-8') -> tuple[str] | None:

    for trial_encoding in tuple({expected_encoding,'utf-8','latin-1','cp1251','ascii'}):
        try:
            txt_lines = []
            with open(txt_file_path,encoding=trial_encoding) as tf:
                while True:
                    line = tf.readline()
                    if not line:
                        break
                    line = line.rstrip('\n')
                    line = line.strip()
                    while '  ' in line:
                        line = line.replace('  ',' ')
                    txt_lines.append(line)
            return tuple(txt_lines)
        except Exception:
            pass

    return None


def isQueryMatchKether(entry_string : str, txt_lines : tuple[AnyStr]) -> bool:

    if not (len_txt_lines := len(txt_lines)):
        return False
    elif len_txt_lines == 1:
        current_line = decodeZipTxtLine(txt_lines[0])
        for word in tuple(current_line.lower().split(' ')):
            if entry_string == "".join([segment for segment in tuple(re.split(r'[^a-zA-Z0-9]+',word)) if segment]):
                return True
    else:
        checked_index = -1
        for n in range(len_txt_lines-1):
            if n == checked_index:
                continue
            current_line = decodeZipTxtLine(txt_lines[n]) ; current_line_lower = current_line.lower()
            next_line = decodeZipTxtLine(txt_lines[n+1]) ; next_line_lower = next_line.lower()
            for item in tuple(set((current_line_lower+' '+next_line_lower).split(' ') + (current_line_lower+next_line_lower).split() + (current_line_lower.rstrip('-')+next_line_lower).split(' '))):
                if entry_string == "".join([segment for segment in tuple(re.split(r'[^a-zA-Z0-9]+',item)) if segment]):
                    return True
            checked_index = n+1

    return False


def isQueryMatchYesod(entry_string : str, txt_lines : tuple[AnyStr]) -> bool:

    if not (len_txt_lines := len(txt_lines)):
        return False
    elif len_txt_lines == 1:
        for word in tuple(decodeZipTxtLine(txt_lines[0]).lower().split(' ')):
            if entry_string == "".join([segment for segment in tuple(re.split(r'[^a-zA-Z0-9]+',word)) if segment]):
                return True
    else:
        for n in range(len_txt_lines):
            for word in tuple(decodeZipTxtLine(txt_lines[n]).lower().split(' ')):
                if entry_string == "".join([segment for segment in tuple(re.split(r'[^a-zA-Z0-9]+',word)) if segment]):
                    return True

    return False


def isQueryMatchDaath(entry_string: str, entity_path : str, zf) -> bool:

    with zf.open(entity_path) as tf:
        while True:
            current_line = tf.readline()
            if not current_line:
                break
            current_line = decodeZipTxtLine(current_line)
            for item in tuple(current_line.lower().split('|')):
                for word in tuple(set(item.split(' ') + item.replace('-','').split(' ') + item.replace('_','').split(' '))):
                    if entry_string == "".join([segment for segment in tuple(re.split(r'[^a-zA-Z0-9]+',word)) if segment]):
                        return True

    return False


def isQueryMatchChochmah(entry_string : str, entity_path : str, zf) -> bool:

    with zf.open(entity_path) as tf:
        while True:
            current_line = tf.readline()
            if not current_line:
                break
            current_line = decodeZipTxtLine(current_line)
            for group in tuple(current_line.lower().split('|')):
                if entry_string in ' '.join(["".join([segment for segment in tuple(re.split(r'[^a-zA-Z0-9]+',word)) if segment]) for word in tuple(group.split(' '))]):
                    return True

    return False


def isQueryMatchGewurah(entry_string : str, txt_lines : tuple[AnyStr], max_line_concat : int) -> bool:

    if not (len_txt_lines := len(txt_lines)):
        return False
    elif len_txt_lines == 1:
        txt_line = decodeZipTxtLine(txt_lines[0]).lower()
        if entry_string in " ".join(["".join([segment for segment in tuple(re.split(r'[^a-zA-Z0-9]+',item)) if segment]) for item in tuple(txt_line.split(' '))]):
            return True
    elif len_txt_lines < max_line_concat:
        concat_lines = " ".join([decodeZipTxtLine(txt_line).lower() for txt_line in txt_lines])
        if entry_string in " ".join(["".join([segment for segment in tuple(re.split(r'[^a-zA-Z0-9]+',word))]) for word in tuple(concat_lines.split(' '))]):
            return True
    else:
        for n in range(len_txt_lines-max_line_concat+1):
            if entry_string in " ".join(["".join([segment for segment in tuple(re.split(r'[^a-zA-Z0-9]+',word)) if segment]) for word in tuple(" ".join([decodeZipTxtLine(txt_lines[n+k]).lower() for k in range(max_line_concat)]).split(' '))]):
                return True

    return False


def forcedTxtFileWrite(output_path : str, lines : list[str] | tuple[str]) -> None:
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
