# Python 3.11+ (Official CPython Build) are recommended. Using the latest and
# stable version of Python 3 will result in the best performance and behavior
# of Chloe Felina.
# This has been designed specifically for Windows 10/11. Although, it may work
# on older versions of Windows if Python 3.11 or later are supported/usable on
# said iteration/version of Windows.

# Made in loving dedication and memory to my precious feline pet, friend, and
# family member: Chloe Link.

# TQDM
tqdm_imported = True
try:
    from tqdm import tqdm
    from os import system
    sys_clear = lambda : system('cls')
except ImportError:
    tqdm_imported = False
except ModuleNotFoundError:
    tqdm_imported = False

# Installed Python Modules
# ArcPy
# If you don't access to ArcPy via ArcGIS Pro, don't worry, unless you work
# with Esri file geodatabases or shapefiles, you don't need it.
arcpy_imported = True
try: import arcpy
except ImportError: arcpy_imported = False
except ModuleNotFoundError: arcpy_imported = False
except RuntimeError: arcpy_imported = False
# PyPDF
pypdf_imported = True
try:
    from pypdf import PdfReader,filters
    import logging
    logger = logging.getLogger("pypdf")
    logger.setLevel(logging.ERROR)
except ImportError:
    pypdf_imported = False
except ModuleNotFoundError:
    pypdf_imported = False
# Python Image Library (PIL)
pil_imported = True
try: from PIL import Image,ImageFile
except ImportError: pil_imported = False
except ModuleNotFoundError: pil_imported = False
# docx
docx_imported = True
try: from docx import Document
except ImportError: docx_imported = False
except ModuleNotFoundError: docx_imported = False
# docx2
docx2_imported = True
try: from docx2python import docx2python as docx2
except ImportError: docx2_imported = False
except ModuleNotFoundError: docx2_imported = False
# pywin32
win32api_imported = True
try: from win32api import GetLogicalDriveStrings
except ImportError: win32api_imported = False
except ModuleNotFoundError: win32api_imported = False

# Built-In Python Modules
import csv,logging,warnings
from os import walk as walker
from os import listdir,mkdir,chdir,getcwd,remove,chmod,rename
from os.path import exists,isfile,isdir
from locale import setlocale,LC_ALL
from zipfile import ZipFile,ZIP_DEFLATED
from shutil import rmtree
from string import ascii_letters,digits
from stat import S_IRWXU
from decimal import Decimal,localcontext
from array import array
from pathlib import Path
from winsound import PlaySound,SND_FILENAME
from secrets import choice

# Custom Python Modules
from chloeFelina.purr import isQueryMatchKether,isQueryMatchBinah,isQueryMatchDaath,isQueryMatchChochmah,isQueryMatchGewurah,forcedTxtFileWrite,getImageTypeName,decodeZipTxtLine,getTxtFileLines
from chloeFelina.meow import randstr,createCopy,getSizeOfItem,unc_path,getBaselineMetadata,getCreatedDate,getModifiedDate,genSearchQueryResultFile,forbidden_dirs,backupGen,genDuplicateFinderResultFile
from chloeFelina.paxium import encrypt as pax_encrypt
from chloeFelina.paxium import decrypt as pax_decrypt
from chloeFelina import _audio_file_pointer

# This attempts to stop logging messages from installed modules from displaying.
# However, depending on how said modules handle logging, logging messages may
# still end up being displayed for users.
if logging.root.manager.disable != 50:
    root = logging.getLogger()
    for h in tuple(root.handlers):
        root.removeHandler(h)
    root.propagate = False
    try:
        logging.disable(logging.CRITICAL)
    except Exception:
        try:
            logging.disable(logging.FATAL)
        except Exception:
            pass

warnings.simplefilter("ignore")

temp_path = _audio_file_pointer.__file__.replace("\\","/")

_chloe_voice_path = "%s/Chloe_True_Voice" % temp_path[:temp_path.rfind('/')]

del temp_path

def playChloeHappy(use_audio_wakeup_buffer : bool = False, audio_wakeup_buffer : int = 10) -> None:

    random_audio = choice(("chloe_meow_001.wav","chloe_meow_002.wav","chloe_meow_003.wav","chloe_meow_004.wav",'chloe_trill_001.wav','chloe_trill_002.wav','chloe_trill_003.wav'))

    if use_audio_wakeup_buffer:
        for _ in range(audio_wakeup_buffer):
            PlaySound(f'{_chloe_voice_path}/dummy_audio.wav',SND_FILENAME)
    PlaySound(f'{_chloe_voice_path}/{random_audio}',SND_FILENAME)

    return None

setlocale(LC_ALL,'')

class ChloeAI:

    def __init__(self, database_location : str | None = None, database_name : str = 'datumbazo', maximum_pixels : int = 10_000_000_000, histogram_ratio_precision : int = 6, allow_truncating_images : bool = False, pdf_max_array_out_stream_len : int = 100_000_000, pdf_max_declared_stream_len : int = 100_000_000, pdf_jbig2_max_out_len : int = 75_000_000, pdf_lzw_max_out_len : int = 75_000_000, pdf_zlib_max_out_len : int = 75_000_000, pdf_zlib_recovery_in_len : int = 5_000_000, pdf_flate_max_columns : int = 250_000, pdf_flate_max_row_len : int = 4_000_000, pdf_flate_max_buffer_size : int = 75_000_000, pdf_run_len_max_out_len : int = 75_000_000, crintum_obfuscation : bool = False, chloe_vocalization : bool = False, use_audio_wakeup_buffer : bool = False, audio_wakeup_buffer : int = 10, allow_autoclear_terms : bool = False, corrupted_zip_check : bool = True):

        self.valid_check_types = {'txt','pdf','doc','img','gdb','shp','alia'}

        self.crintum_obfuscation = crintum_obfuscation
        self.database_name = database_name[:]

        user_path = str(Path.home()).replace('\\','/')

        if database_location is None or not exists(database_location):
            self.db_path = f'{user_path}/Documents/{database_name}'
            if not exists(self.db_path):
                try:
                    mkdir(self.db_path)
                except Exception:
                    database_name = 'datumbazo'
                    self.db_path = f'{user_path}/Documents/{database_name}'
                    mkdir(self.db_path)
        else:
            database_location = database_location.replace("\\","/")
            self.db_path = f'{database_location}/{database_name}'
            try:
                for registered_user in tuple(listdir('C:/Users')):
                    if self.db_path.startswith(f"C:/Users/{registered_user}/AppData"):
                        self.db_path = f"{user_path}/Documents/{database_name}"
                        break
            except Exception:
                pass
            if self.db_path.startswith("C:/Windows") or self.db_path in forbidden_dirs():
                self.db_path = f'{user_path}/Documents/{database_name}'

        if exists(self.db_path):
            if not 'crintum_pointer.txt' in (items := set(listdir(self.db_path))) and not '_backup_crintum_pointer.txt' in items and not len(items):
                ignore_empty_line = True
                with open(f'{self.db_path}/crintum_pointer.txt','w',encoding='utf-8') as tf:
                    pass
            elif not 'crintum_pointer.txt' in items and len(items):
                ignore_empty_line = True
                while database_name in listdir(database_location):
                    database_name = f"{database_name}_{randstr()}"
                self.db_path = f'{database_location}/{database_name}'
                mkdir(f'{database_location}/{database_name}')
                with open(f'{database_location}/{database_name}/crintum_pointer.txt','w',encoding='utf-8') as tf:
                    pass
            else:
                ignore_empty_line = False
                items = list(items)
                if '_terms_searched' in items:
                    items.remove('_terms_searched')
                if '_names_checked' in items:
                    items.remove('_names_checked')
                if 'crintum_pointer.txt' in items:
                    items.remove('crintum_pointer.txt')
                if '_backup_crintum_pointer.txt' in items:
                    items.remove('_backup_crintum_pointer.txt')
                if 'Windows_MetaInfo.zip' in items:
                    items.remove('Windows_MetaInfo.zip')
                for item in (items:= tuple(items)):
                    if isdir((item_path := f'{self.db_path}/{item}')):
                        try:
                            rmtree(item_path)
                        except Exception:
                            try:
                                remove(item_path)
                            except Exception:
                                pass
            if '_backup_crintum_pointer.txt' in (items := set(items)):
                if 'crintum_pointer.txt' in items:
                    remove('crintum_pointer.txt')
                    rename(f'{self.db_path}/_backup_crintum_pointer.txt',f'{self.db_path}/crintum_pointer.txt')
                else:
                    rename(f'{self.db_path}/_backup_crintum_pointer.txt',f'{self.db_path}/crintum_pointer.txt')
            del items
        else:
            ignore_empty_line = True
            try:
                mkdir(self.db_path)
            except Exception:
                mkdir(f'{user_path}/Documents/datumbazo')
            with open(f'{self.db_path}/crintum_pointer.txt','w',encoding='utf-8') as tf:
                pass

        self.crintum_pointer = {} ; self.path_pointer = {} ; empty_line_found = False

        if crintum_obfuscation:
            with open(f'{self.db_path}/crintum_pointer.txt',encoding='utf-8') as tf:
                while True:
                    obfuscated_line = tf.readline()
                    if not obfuscated_line:
                        break
                    if '|' in (line := pax_decrypt(obfuscated_line.rstrip('\n'))):
                        self.crintum_pointer[line[:line.find('|')]] = line[line.find('|')+1:]
                        self.path_pointer[line[line.find('|')+1:]] = line[:line.find('|')]
                    else:
                        empty_line_found = True
            existing_zips = {item for item in tuple(listdir(self.db_path)) if item.endswith('.zip')}
            previous_count = len(self.crintum_pointer.keys())
            for db_archive in tuple(self.path_pointer.keys()):
                if not f"{db_archive}.zip" in existing_zips:
                    del self.crintum_pointer[self.path_pointer[db_archive]]
                    del self.path_pointer[db_archive]
            if previous_count != (num_dbs := len((db_names := tuple(self.path_pointer.keys())))):
                with open(f'{self.db_path}/crintum_pointer.txt','w',encoding='utf-8') as tf:
                    tf.write(pax_encrypt(f"{self.path_pointer[db_names[0]]}|{db_names[0]}"))
                    for n in range(1,num_dbs):
                        tf.write("\n%s" % (pax_encrypt(f"{self.path_pointer[db_names[n]]}|{db_names[n]}")))
        else:
            with open(f'{self.db_path}/crintum_pointer.txt',encoding='utf-8') as tf:
                while True:
                    line = tf.readline()
                    if not line:
                        break
                    if '|' in (line := line.rstrip('\n')):
                        self.crintum_pointer[line[:line.find('|')]] = line[line.find('|')+1:].rstrip('\n')
                        self.path_pointer[line[line.find('|')+1:].rstrip('\n')] = line[:line.find('|')]
                    else:
                        empty_line_found = True
            existing_zips = {item for item in tuple(listdir(self.db_path)) if item.endswith('.zip')}
            previous_count = len(self.crintum_pointer.keys())
            for db_archive in tuple(self.path_pointer.keys()):
                if not f"{db_archive}.zip" in existing_zips:
                    del self.crintum_pointer[self.path_pointer[db_archive]]
                    del self.path_pointer[db_archive]
            if previous_count != (num_dbs := len((db_names := tuple(self.path_pointer.keys())))):
                with open(f'{self.db_path}/crintum_pointer.txt','w',encoding='utf-8') as tf:
                    tf.write(f"{self.path_pointer[db_names[0]]}|{db_names[0]}")
                    for n in range(1,num_dbs):
                        tf.write(f"\n{self.path_pointer[db_names[n]]}|{db_names[n]}")

        self.paths_in_db = set(self.crintum_pointer.keys())
        self.used_names = set(self.path_pointer.keys())

        if empty_line_found and not ignore_empty_line:
            backupGen(f'{self.db_path}/crintum_pointer.txt',(backup_crintum := f'{self.db_path}/_backup_crintum_pointer.txt'))
            with open(f'{self.db_path}/crintum_pointer.txt','w',encoding='utf-8') as tf:
                temp_pathways = tuple(self.paths_in_db)
                tf.write(f'{temp_pathways[0]}|{self.crintum_pointer[temp_pathways[0]]}')
                for n in range(1,len(temp_pathways)):
                    tf.write(f'\n{temp_pathways[n]}|{self.crintum_pointer[temp_pathways[n]]}')
            try: del temp_pathways
            except NameError: pass
            remove(backup_crintum)
            del backup_crintum

        if pypdf_imported:
            filters.MAX_DECLARED_STREAM_LENGTH = pdf_max_declared_stream_len
            # Set pdf_max_array_out_stream_len a higher value if an error is
            # produced due to it.
            filters.MAX_ARRAY_BASED_STREAM_OUTPUT_LENGTH = pdf_max_array_out_stream_len
            filters.JBIG2_MAX_OUTPUT_LENGTH = pdf_jbig2_max_out_len
            filters.LZW_MAX_OUTPUT_LENGTH = pdf_lzw_max_out_len
            filters.RUN_LENGTH_MAX_OUTPUT_LENGTH = pdf_run_len_max_out_len
            filters.ZLIB_MAX_OUTPUT_LENGTH = pdf_zlib_max_out_len
            filters.ZLIB_MAX_RECOVERY_INPUT_LENGTH = pdf_zlib_recovery_in_len
            filters.FLATE_MAX_COLUMNS = pdf_flate_max_columns
            filters.FLATE_MAX_ROW_LENGTH = pdf_flate_max_row_len
            filters.FLATE_MAX_BUFFER_SIZE = pdf_flate_max_buffer_size

        if pil_imported:
            # More file types will be added after thorough testing.
            self.accepted_image_extensions = {'.jpg','.JPG','.jpeg','.JPEG','.png','.PNG','.tif','.TIF','.tiff','.TIFF','.webp','.WEBP','.bmp','.BMP','.dib','.DIB','.icns','.ICNS','.ico','.ICO','.jp2','.JP2','.j2k','.J2K','.jpx','.JPX','.pcx','.PCX','.tga','.TGA','.xbm','.XBM'}
            self.image_types = ('jpg','jpeg','png','tif','tiff','webp','bmp','dib','icns','ico','jp2','j2k','jpx','pcx','tga','xbm')
            # Maximum number of pixels that an image can have until the PIL module
            # throws an error.
            Image.MAX_IMAGE_PIXELS = maximum_pixels
            ImageFile.LOAD_TRUNCATED_IMAGES = allow_truncating_images

        if arcpy_imported:
            arcpy.SetLogHistory(False)
            arcpy.SetLogMetadata(False)
            arcpy.env.autoCommit = 0
            # Setting processorType to CPU instead of GPU as the ArcPy module as
            # of writing only utilizes Nvidia GPUs exclusively.
            arcpy.env.processorType = "CPU"
            arcpy.env.parallelProcessingFactor = "75%"

        self.histogram_ratio_precision = histogram_ratio_precision
        # The following is required to heavily simplify and reduce storage space
        # requirements for saving histogram ratio data.
        self.subbing = {".a":'È','.b':'É','.c':'Ê','.d':'Ë','.f':'Ì','.g':'Í','.h':'Î','.i':'Ï','.j':'Ð','.k':'Ñ'}
        self.sub_keys = tuple(self.subbing.keys())
        self.shorthand = ['000', '00', '111111', '11111', '1111', '111', '11', '222222', '22222', '2222', '222', '22', '333333', '33333', '3333', '333', '33', '444444', '44444', '4444', '444', '44', '555555', '55555', '5555', '555', '55', '666666', '66666', '6666', '666', '66', '777777', '77777', '7777', '777', '77', '888888', '88888', '8888', '888', '88', '999999', '99999', '9999', '999', '99', 'e-', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '.0', '.1', '.2', '.3', '.4', '.5', '.6', '.7', '.8', '.9']
        self.short_ref = {'000': 'a', '00': 'b', '111111': 'c', '11111': 'd', '1111': 'f', '111': 'g', '11': 'h', '222222': 'i', '22222': 'j', '2222': 'k', '222': 'l', '22': 'm', '333333': 'n', '33333': 'o', '3333': 'p', '333': 'q', '33': 'r', '444444': 's', '44444': 't', '4444': 'u', '444': 'v', '44': 'w', '555555': 'x', '55555': 'y', '5555': 'z', '555': 'A', '55': 'B', '666666': 'C', '66666': 'D', '6666': 'E', '666': 'F', '66': 'G', '777777': 'H', '77777': 'I', '7777': 'J', '777': 'K', '77': 'L', '888888': 'M', '88888': 'N', '8888': 'O', '888': 'P', '88': 'Q', '999999': 'R', '99999': 'S', '9999': 'T', '999': 'U', '99': 'V', 'e-': 'W', '1.': 'X', '2.': 'Y', '3.': 'Z', '4.': '!', '5.': '@', '6.': '$', '7.': '?', '8.': '~', '9.': '&', '.0': '+', '.1': '=', '.2': '<', '.3': '>', '.4': '#', '.5': '`', '.6': '(', '.7': ')', '.8': '[', '.9': ']'}
        self.alphanum = tuple(f'{ascii_letters}{digits}')

        if corrupted_zip_check:
            for db_name in tuple(self.used_names):
                with ZipFile(f'{self.db_path}/{db_name}.zip') as zf:
                    if zf.testzip() != None:
                        self.removeCrintumEntry(self.path_pointer[db_name])
                        item_removed = True

        if allow_autoclear_terms:
            self.clearSearchQueryMemory()

        self.chloe_vocalization = chloe_vocalization
        self.wakeup_buffer = (use_audio_wakeup_buffer,audio_wakeup_buffer)

        if self.chloe_vocalization:
            playChloeHappy(self.wakeup_buffer[0],self.wakeup_buffer[1])


    def autoUpdateDatabase(self, keep_db_if_no_connection : bool = True, clear_terms_searched : bool = True, terminal_progress_display_enabled : bool = False) -> None:
        '''
        WIP
        '''

        if terminal_progress_display_enabled and tqdm_imported:
            sys_clear()

        # Note: Local drive refers to just the C drive. Any external or network
        # drive is considered a non-local drive. If you somehow managed to
        # rename the local drive to something other C, you are in for an
        # "interesting" time.

        ignored_items = {'crintum_pointer.txt','_terms_searched','_names_checked','Windows_MetaInfo.zip'}

        # Remove redundant files and folders.
        for item in tuple(listdir(self.db_path)):
            if isdir(f'{self.db_path}/{item}'):
                rmtree(f'{self.db_path}/{item}')
            elif not item.endswith('.zip') and not item in ignored_items:
                remove(f'{self.db_path}/{item}')

        if clear_terms_searched:
            self.clearSearchQueryMemory()

        # Remove redundant entries from crintum_pointer.txt and zip files not
        # referenced in crintum_pointer.txt
        existing_zips = listdir(self.db_path)
        for item in tuple(ignored_items):
            if item in existing_zips:
                existing_zips.remove(item)
        existing_zips = {item[:item.rfind('.')] for item in tuple(existing_zips)}
        if len((remove_entries := tuple([db_name for db_name in tuple(self.used_names) if not db_name in existing_zips]))):
            for db_name in remove_entries:
                self.removeCrintumEntry(self.path_pointer[db_name])
        del remove_entries
        if len((db_for_deletion := tuple([zip_db for zip_db in tuple(existing_zips) if not zip_db in self.used_names]))):
            for zip_db in db_for_deletion:
                remove(f"{self.db_path}/{zip_db}.zip")
        del db_for_deletion ; del existing_zips

        if win32api_imported:
            nonlocal_drives = GetLogicalDriveStrings().split('\000')[:-1]
            nonlocal_drives.remove('C:\\')
            nonlocal_drives = tuple([unc_path(drive) for drive in nonlocal_drives])
            redact_dbs = []
            if tqdm_imported:
                iterator = tqdm(tuple(self.used_names),disable = not terminal_progress_display_enabled, desc = "Finding and Removing Redundant References")
            else:
                iterator = tuple(self.used_names)
            if keep_db_if_no_connection:
                for db_name in iterator:
                    reference_directory = self.path_pointer[db_name]
                    if reference_directory.startswith('C:'):
                        if not exists(reference_directory):
                            redact_dbs.append(db_name)
                    else:
                        for explicit_drive in nonlocal_drives:
                            if reference_directory.startswith(explicit_drive):
                                if exists(explicit_drive):
                                    if not exists(reference_directory):
                                        redact_dbs.append(db_name)
            else:
                for db_name in iterator:
                    if not exists(self.path_pointer[db_name]):
                        redact_dbs.append(db_name)
            for redact_db in (redact_dbs := tuple(redact_dbs)):
                self.removeCrintumEntry(self.path_pointer[redact_db])
                remove(f'{self.db_path}/{redact_db}')
            del redact_dbs
            try: del reference_directory
            except NameError: pass

        return None


    def appendCrintumEntry(self, reference_directory : str, corresponding_folder : str) -> None:

        if self.crintum_obfuscation:
            if not len(self.used_names):
                with open(f'{self.db_path}/crintum_pointer.txt','w',encoding='utf-8') as tf:
                    tf.write(pax_encrypt(f"{reference_directory}|{corresponding_folder}"))
            else:
                with open(f'{self.db_path}/crintum_pointer.txt','a',encoding='utf-8') as tf:
                    tf.write("\n%s" % (pax_encrypt(f'{reference_directory}|{corresponding_folder}')))
        else:
            if not len(self.used_names):
                with open(f'{self.db_path}/crintum_pointer.txt','w',encoding='utf-8') as tf:
                    tf.write(f"{reference_directory}|{corresponding_folder}")
            else:
                with open(f'{self.db_path}/crintum_pointer.txt','a',encoding='utf-8') as tf:
                    tf.write(f"\n{reference_directory}|{corresponding_folder}")

        self.used_names.add(corresponding_folder)
        self.paths_in_db.add(reference_directory)
        self.crintum_pointer[reference_directory] = corresponding_folder
        self.path_pointer[corresponding_folder] = reference_directory

        return None


    def removeCrintumEntry(self, reference_directory : str) -> None:

        del self.crintum_pointer[reference_directory]

        # Failsafe
        backupGen(f'{self.db_path}/crintum_pointer.txt',(backup_crintum := f'{self.db_path}/_backup_crintum_pointer.txt'))

        self.path_pointer.clear()

        self.paths_in_db = set(self.crintum_pointer.keys())
        self.used_names = set([self.crintum_pointer[pathway] for pathway in tuple(self.paths_in_db)])
        self.path_pointer = {self.crintum_pointer[pathway] : pathway for pathway in tuple(self.paths_in_db)}

        temp_pathways = tuple(self.paths_in_db)

        if self.crintum_obfuscation:
            with open(f'{self.db_path}/crintum_pointer.txt','w',encoding='utf-8') as tf:
                tf.write(pax_encrypt(f"{temp_pathways[0]}|{self.crintum_pointer[temp_pathways[0]]}"))
                for n in range(1,len(temp_pathways)):
                    tf.write("\n%s" % (pax_encrypt(f'{temp_pathways[n]}|{self.crintum_pointer[temp_pathways[n]]}')))
        else:
            with open(f'{self.db_path}/crintum_pointer.txt','w',encoding='utf-8') as tf:
                tf.write(f"{temp_pathways[0]}|{self.crintum_pointer[temp_pathways[0]]}")
                for n in range(1,len(temp_pathways)):
                    tf.write(f"\n{temp_pathways[n]}|{self.crintum_pointer[temp_pathways[n]]}")

        remove(backup_crintum)

        return None


    def getNestedDirectoryData(self, top_directory_path : str, clear_terms_searched : bool = True, terminal_progress_display_enabled : bool = False) -> None:

        if not exists(top_directory_path):
            return None

        for root,dirs,files in walker(top_directory_path):
            if not "$RECYCLE.BIN" in (root := root.replace('\\','/')) and not self.db_path in root:
                self.getDirectoryData(root,clear_terms_searched,terminal_progress_display_enabled)

        if self.chloe_vocalization:
            playChloeHappy(self.wakeup_buffer[0],self.wakeup_buffer[1])

        return None


    def compressToZIP(self, archive_db_name : str) -> bool:

        current_dir = getcwd().replace('\\','/')

        chdir(f'{self.db_path}/{archive_db_name}')

        match len((items := tuple(listdir()))):
            case 0:
                chdir(current_dir)
                return False
            case 1:
                if items[0] != '_alia_dosieroj.txt':
                    chdir(current_dir)
                    return False
            case _:
                pass

        for item in tuple(listdir()):
            if isdir((test_path := f'{getcwd()}/{item}')):
                if not len(listdir(item)):
                    try:
                        remove(test_path)
                    except Exception:
                        rmtree(test_path)

        if len((items := tuple(listdir()))) <= 1:
            chdir(current_dir)
            return False

        # Best balance of compression and ability to quickly read data from
        # archival file.
        with ZipFile(f'{archive_db_name}.zip','w',ZIP_DEFLATED,True,9) as zf:
            for item in items:
                if isfile(item):
                    zf.write(item)
                else:
                    zf.write(item)
                    for sub_item in tuple(listdir(item)):
                        zf.write(f'{item}/{sub_item}')

        createCopy(f'{self.db_path}/{archive_db_name}/{archive_db_name}.zip',f'{self.db_path}/{archive_db_name}.zip')

        chdir(current_dir)

        rmtree(f'{self.db_path}/{archive_db_name}')

        return True


    def uncompressZIP(self, archive_db_name : str) -> None:

        original_dir = getcwd().replace('\\','/')

        mkdir(f'{self.db_path}/{archive_db_name}')

        zf = ZipFile(f'{self.db_path}/{archive_db_name}.zip')
        chdir(f'{self.db_path}/{archive_db_name}')
        zf.extractall()
        zf.close()

        chdir(original_dir)

        return None


    def getDirectoryData(self, reference_directory : str, clear_terms_searched : bool = True, terminal_progress_display_enabled : bool = False) -> None:

        if terminal_progress_display_enabled and tqdm_imported:
            sys_clear()

        reference_directory = reference_directory.replace('\\','/').rstrip("/")

        # This is to account for mapped network drives.
        if not exists((reference_directory := unc_path(reference_directory))):
            # Account for weird abnormality.
            return None

        if reference_directory in self.paths_in_db or reference_directory.lower().endswith('.gdb') or reference_directory == self.db_path:
            return None
        else:
            items = {}
            for name in tuple(listdir(reference_directory)):
                if isfile(f'{reference_directory}/{name}'):
                    if name.lower().endswith('.shp'):
                        items[name] = 'SHP'
                    elif name.lower().endswith('.txt'):
                        items[name] = 'TXT'
                    elif name.lower().endswith('.pdf'):
                        items[name] = 'PDF'
                    elif name.lower().endswith('.docx'):
                        items[name] = 'DOC'
                    elif name[name.rfind("."):] in self.accepted_image_extensions and '.' in name:
                        items[name] = 'IMG'
                    else:
                        items[name] = 'ALIA'
                elif name.lower().endswith('.gdb'):
                    items[name] = 'GDB'
            if len(items):
                archive_db_name = randstr(12)
                while archive_db_name in self.used_names:
                    archive_db_name = randstr(12)
                mkdir(f'{self.db_path}/{archive_db_name}')
                if tqdm_imported:
                    names = tqdm(tuple(items.keys()), disable = not terminal_progress_display_enabled, desc = reference_directory[reference_directory.rfind('/')+1:])
                else:
                    names = tuple(items.keys())
                for name in names:
                    match items[name]:
                        case 'GDB':
                            if arcpy_imported:
                                try:
                                    if not self.archive_gdb_data(f'{reference_directory}/{name}',archive_db_name):
                                        if exists(f'{self.db_path}/{archive_db_name}/{name[:name.rfind(".")]}_{name[name.rfind(".")+1:]}'):
                                            rmtree(f'{self.db_path}/{archive_db_name}/{name[:name.rfind(".")]}_{name[name.rfind(".")+1:]}')
                                except Exception:
                                    if exists(f'{self.db_path}/{archive_db_name}/{name[:name.rfind(".")]}_{name[name.rfind(".")+1:]}'):
                                        rmtree(f'{self.db_path}/{archive_db_name}/{name[:name.rfind(".")]}_{name[name.rfind(".")+1:]}')
                        case 'SHP':
                            if arcpy_imported:
                                try:
                                    if not self.archive_shp_data(f'{reference_directory}/{name}',archive_db_name):
                                        self.archive_alia_data(f'{reference_directory}/{name}',archive_db_name)
                                except Exception:
                                    if exists(f'{self.db_path}/{archive_db_name}/_shp_files/{name[:name.rfind(".")]}_{name[name.rfind(".")+1:]}.txt'):
                                        remove(f'{self.db_path}/{archive_db_name}/_shp_files/{name[:name.rfind(".")]}_{name[name.rfind(".")+1:]}.txt')
                                        if not len(listdir(f'{self.db_path}/{archive_db_name}/_shp_files')):
                                            rmtree(f'{self.db_path}/{archive_db_name}/_shp_files')
                                    self.archive_alia_data(f'{reference_directory}/{name}',archive_db_name)
                            else:
                                self.archive_alia_data(f'{reference_directory}/{name}',archive_db_name)
                        case 'TXT':
                            try:
                                if not self.archive_txt_data(f'{reference_directory}/{name}',archive_db_name):
                                    self.archive_alia_data(f'{reference_directory}/{name}',archive_db_name)
                            except Exception:
                                if exists(f'{self.db_path}/{archive_db_name}/_txt_files/{name[:name.rfind(".")]}_{name[name.rfind(".")+1:]}.txt'):
                                    remove(f'{self.db_path}/{archive_db_name}/_txt_files/{name[:name.rfind(".")]}_{name[name.rfind(".")+1:]}.txt')
                                    if not len(f'{self.db_path}/{archive_db_name}/_txt_files'):
                                        rmtree(f'{self.db_path}/{archive_db_name}/_txt_files')
                                self.archive_alia_data(f'{reference_directory}/{name}',archive_db_name)
                        case 'PDF':
                            if pypdf_imported and pil_imported:
                                try:
                                    if not self.archive_pdf_data(f'{reference_directory}/{name}',archive_db_name):
                                        self.archive_alia_data(f'{reference_directory}/{name}')
                                except Exception:
                                    # accounts for something going wrong when attempting to access information from PDFs
                                    if exists(f'{self.db_path}/{archive_db_name}/{name[:name.rfind(".")]}_{name[name.rfind(".")+1:]}'):
                                        rmtree(f'{self.db_path}/{archive_db_name}/{name[:name.rfind(".")]}_{name[name.rfind(".")+1:]}')
                                    self.archive_alia_data(f'{reference_directory}/{name}',archive_db_name)
                            else:
                                self.archive_alia_data(f'{reference_directory}/{name}',archive_db_name)
                        case 'DOC':
                            if docx_imported and docx2_imported and pil_imported:
                                try:
                                    self.archive_doc_data(f'{reference_directory}/{name}',archive_db_name)
                                except Exception:
                                    # accounts for something going wrong when attempting to access information from Word documents
                                    if exists(f'{self.db_path}/{archive_db_name}/{name[:name.rfind(".")]}_{name[name.rfind(".")+1:]}'):
                                        rmtree(f'{self.db_path}/{archive_db_name}/{name[:name.rfind(".")]}_{name[name.rfind(".")+1:]}')
                                    self.archive_alia_data(f'{reference_directory}/{name}',archive_db_name)
                            else:
                                self.archive_alia_data(f'{reference_directory}/{name}',archive_db_name)
                        case 'IMG':
                            if pil_imported:
                                if not self.archive_img_data(f'{reference_directory}/{name}',archive_db_name):
                                    self.archive_alia_data(f'{reference_directory}/{name}',archive_db_name)
                            else:
                                self.archive_alia_data(f'{reference_directory}/{name}',archive_db_name)
                        case _:
                            self.archive_alia_data(f'{reference_directory}/{name}',archive_db_name)
                if exists(f'{self.db_path}/{archive_db_name}/TeMp_FiLeGeOdAtAbAsE_6789_10.gdb'):
                    try:
                        arcpy.management.Delete(f'{self.db_path}/{archive_db_name}/TeMp_FiLeGeOdAtAbAsE_6789_10.gdb')
                    except Exception:
                        rmtree(f'{self.db_path}/{archive_db_name}/TeMp_FiLeGeOdAtAbAsE_6789_10.gdb')
                if self.compressToZIP(archive_db_name):
                    self.appendCrintumEntry(reference_directory,archive_db_name)
                    if clear_terms_searched:
                        self.clearSearchQueryMemory()
                if exists(f'{self.db_path}/{archive_db_name}'):
                    rmtree(f'{self.db_path}/{archive_db_name}')

        return None


    def compWinSysInfo(self, replace_existing_info : bool = False, terminal_progress_display_enabled : bool = False) -> None:

        if not replace_existing_info and exists(f'{self.db_path}/Windows_MetaInfo.zip'):
            return None

        if tqdm_imported and terminal_progress_display_enabled:
            sys_clear()

        import hashlib

        def md5_checksum(fname : str):
            hash_md5 = hashlib.md5()
            with open(fname, 'rb') as f:
                for chunk in iter(lambda : f.read(4096),b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()

        if not exists(f'{self.db_path}/Windows_MetaInfo'):
            mkdir(f'{self.db_path}/Windows_MetaInfo')

        def getBasicInfo(file_path : str) -> tuple:

            temp_list = []

            try: temp_list.append(getModifiedDate(file_path))
            except Exception: temp_list.append('UNKNOWN')

            try: temp_list.append(getCreatedDate(file_path))
            except Exception: temp_list.append('UNKNOWN')

            try: temp_list.append(str(getSizeOfItem(file_path)))
            except Exception: temp_list.append('UNKNOWN')

            try: temp_list.append(md5_checksum(file_path))
            except Exception:temp_list.append('UNKNOWN')

            return tuple(temp_list)

        path_index = {}

        if tqdm_imported:
            for prime_dir in ('C:/Windows','C:/Program Files','C:/Program Files (x86)','C:/ProgramData'):
                for root,dirs,files in walker(prime_dir):
                    if not "$RECYCLE.BIN" in (root := root.replace('\\','/')):
                        file_info = {}
                        for file in tqdm(tuple([item for item in tuple(listdir(root)) if isfile(f'{root}/{item}')]), disable = not terminal_progress_display_enabled, desc = root[root.rfind('/')+1:]):
                            file_info[file] = getBasicInfo(f'{root}/{file}')
                        if len((files := tuple(file_info.keys()))):
                            directory_name = randstr(12)
                            while directory_name in path_index.keys():
                                directory_name = randstr(12)
                            path_index[root] = directory_name
                            with open(f'{self.db_path}/Windows_MetaInfo/{directory_name}.txt','w',encoding='utf-8') as tf:
                                tf.write("%s|%s" % (files[0],'|'.join(file_info[files[0]])))
                                for n in range(1,len(files)):
                                    tf.write(f"\n%s|%s" % (files[n],'|'.join(file_info[files[n]])))
                        else:
                            directory_name = randstr(12)
                            while directory_name in path_index.keys():
                                directory_name = randstr(12)
                            path_index[root] = directory_name
                            with open(f'{self.db_path}/Windows_MetaInfo/{directory_name}.txt','w',encoding='utf-8') as tf:
                                pass
                if terminal_progress_display_enabled:
                    sys_clear()
            for user in tuple(listdir('C:/Users')):
                for root,dirs,files in walker(f'C:/Users/{user}/AppData'):
                    if not "$RECYCLE.BIN" in (root := root.replace('\\','/')):
                        file_info = {}
                        for file in tqdm(tuple([item for item in tuple(listdir(root)) if isfile(f'{root}/{item}')]), disable = not terminal_progress_display_enabled, desc = root[root.rfind('/')+1:]):
                            file_info[file] = getBasicInfo(f'{root}/{file}')
                        if len((files := tuple(file_info.keys()))):
                            directory_name = randstr(12)
                            while directory_name in path_index.keys():
                                directory_name = randstr(12)
                            path_index[root] = directory_name
                            with open(f'{self.db_path}/Windows_MetaInfo/{directory_name}.txt','w',encoding='utf-8') as tf:
                                tf.write("%s|%s" % (files[0],'|'.join(file_info[files[0]])))
                                for n in range(1,len(files)):
                                    tf.write(f"\n%s|%s" % (files[n],'|'.join(file_info[files[n]])))
                        else:
                            directory_name = randstr(12)
                            while directory_name in path_index.keys():
                                directory_name = randstr(12)
                            path_index[root] = directory_name
                            with open(f'{self.db_path}/Windows_MetaInfo/{directory_name}.txt','w',encoding='utf-8') as tf:
                                pass
            if terminal_progress_display_enabled:
                sys_clear()
        else:
            for prime_dir in ('C:/Windows','C:/Program Files','C:/Program Files (x86)','C:/ProgramData'):
                for root,dirs,files in walker(prime_dir):
                    if not "$RECYCLE.BIN" in (root := root.replace('\\','/')):
                        file_info = {}
                        for file in tuple([item for item in tuple(listdir(root)) if isfile(f'{root}/{item}')]):
                            file_info[file] = getBasicInfo(f'{root}/{file}')
                        if len((files := tuple(file_info.keys()))):
                            directory_name = randstr(12)
                            while directory_name in path_index.keys():
                                directory_name = randstr(12)
                            path_index[root] = directory_name
                            with open(f'{self.db_path}/Windows_MetaInfo/{directory_name}.txt','w',encoding='utf-8') as tf:
                                tf.write("%s|%s" % (files[0],'|'.join(file_info[files[0]])))
                                for n in range(1,len(files)):
                                    tf.write(f"\n%s|%s" % (files[n],'|'.join(file_info[files[n]])))
                        else:
                            directory_name = randstr(12)
                            while directory_name in path_index.keys():
                                directory_name = randstr(12)
                            path_index[root] = directory_name
                            with open(f'{self.db_path}/Windows_MetaInfo/{directory_name}.txt','w',encoding='utf-8') as tf:
                                pass
            for user in tuple(listdir('C:/Users')):
                for root,dirs,files in walker(f'C:/Users/{user}/AppData'):
                    if not "$RECYCLE.BIN" in (root := root.replace('\\','/')):
                        file_info = {}
                        for file in tuple([item for item in tuple(listdir(root)) if isfile(f'{root}/{item}')]):
                            file_info[file] = getBasicInfo(f'{root}/{file}')
                        if len((files := tuple(file_info.keys()))):
                            directory_name = randstr(12)
                            while directory_name in path_index.keys():
                                directory_name = randstr(12)
                            path_index[root] = directory_name
                            with open(f'{self.db_path}/Windows_MetaInfo/{directory_name}.txt','w',encoding='utf-8') as tf:
                                tf.write("%s|%s" % (files[0],'|'.join(file_info[files[0]])))
                                for n in range(1,len(files)):
                                    tf.write(f"\n%s|%s" % (files[n],'|'.join(file_info[files[n]])))
                        else:
                            directory_name = randstr(12)
                            while directory_name in path_index.keys():
                                directory_name = randstr(12)
                            path_index[root] = directory_name
                            with open(f'{self.db_path}/Windows_MetaInfo/{directory_name}.txt','w',encoding='utf-8') as tf:
                                pass

        path_index_paths = tuple(path_index.keys())

        with open(f'{self.db_path}/Windows_MetaInfo/_directory_reference.txt','w',encoding='utf-8') as tf:
            tf.write(f"{path_index_paths[0]}|{path_index[path_index_paths[0]]}")
            for n in range(1,len(path_index_paths)):
                tf.write(f'\n{path_index_paths[n]}|{path_index[path_index_paths[n]]}')

        current_dir = getcwd()
        try:
            chdir(f'{self.db_path}/Windows_MetaInfo')
            items = tuple(listdir(getcwd()))
            with ZipFile('Windows_MetaInfo.zip','w',ZIP_DEFLATED,True,9) as zf:
                for item in items:
                    if isfile(item):
                        zf.write(item)
            chdir(current_dir)
        except Exception:
            chdir(current_dir)

        if exists(f'{self.db_path}/Windows_MetaInfo.zip'):
            remove(f'{self.db_path}/Windows_MetaInfo.zip')

        createCopy(f'{self.db_path}/Windows_MetaInfo/Windows_MetaInfo.zip',f'{self.db_path}/Windows_MetaInfo.zip')
        rmtree(f'{self.db_path}/Windows_MetaInfo')
        if exists(f'{self.db_path}/Windows_MetaInfo'):
            remove(f'{self.db_path}/Windows_MetaInfo')

        return None


    def checkWinSysChanges(self, terminal_progress_display_enabled : bool = False) -> None:

        if not exists(f'{self.db_path}/Windows_MetaInfo.zip'):
            return None

        if tqdm_imported:
            sys_clear()

        winsys_folder_path = {}

        with ZipFile(f'{self.db_path}/Windows_MetaInfo.zip') as zf:
            with zf.open('_directory_reference.txt') as tf:
                while True:
                    line = tf.readline()
                    if not line:
                        break
                    line = decodeZipTxtLine(line).split('|')
                    winsys_folder_path[line[1]] = line[0]

        try: del line
        except NameError: pass

        missing_folders = []
        additional_folders = []
        missing_items = []
        additional_items = []
        modified_items = []

        existing_paths = {winsys_folder_path[folder] for folder in tuple(winsys_folder_path.keys())}

        for folder in tuple(winsys_folder_path.keys()):
            if not exists(folder):
                valid_new_folder = True
                for missing_folder in tuple(missing_folders):
                    if missing_folder.startswith(folder):
                        valid_new_folder = False
                        break
                if valid_new_folder:
                    missing_folders.append(folder)
            else:
                file_items = []
                for item in tuple(listdir((current_path := winsys_folder_path[folder]))):
                    if isfile(f'{current_path}/{item}'):
                        file_items.append(item)
                    elif not item in existing_paths:
                        additional_folders.append(item)
                if not len((file_items := tuple(file_items))):
                    pass
                else:
                    pass

        return None


    def getImageInformation(self, image_path : str) -> tuple[str] | None:

        # This seemingly overly complex algorithm for extracting histogram ratios
        # is necessary to condense the information into the fewest number of lines
        # possible while still making ratios "unique" to images, minimize storage
        # space, minimize active RAM usage, and to be as fast as possible.

        try:
            zero_counter = 0 ; histo_ratio = [] ; first_line = True
            with localcontext() as ctx:
                ctx.prec = self.histogram_ratio_precision
                with Image.open(image_path) as image_file:
                    total = Decimal(sum((histo_data := array('Q',image_file.histogram()))))
                deci_100 = Decimal(100)
                for num in histo_data:
                    if (val := float(Decimal(num) / total * deci_100)) == 0:
                        zero_counter += 1
                    else:
                        if (current_val := str(round(val,6))) in ('0.0','1'):
                            if (pnt_index := current_val.find('.')) != -1:
                                current_val = f'{current_val[:pnt_index+1]}{current_val[pnt_index+1:pnt_index+3]}{current_val[current_val.find("e-")]}'
                        if current_val.startswith("0."):
                            current_val = current_val[1:]
                        if "e-0" in current_val:
                            current_val = current_val.replace("e-0","e-")
                        if zero_counter == 0:
                            if first_line:
                                histo_ratio.append(current_val)
                                first_line = False
                            else:
                                histo_ratio.append(current_val)
                        else:
                            if first_line:
                                histo_ratio.append(f"0:{zero_counter-1}")
                                histo_ratio.append(current_val)
                                first_line = False
                            else:
                                histo_ratio[-1] = f"{histo_ratio[-1]}:{zero_counter}"
                                histo_ratio.append(current_val)
                            zero_counter = 0

            if zero_counter > 0:
                if histo_ratio[-1].find(":") != -1:
                    histo_ratio[-1] = f'{histo_ratio[-1]}:{int(histo_ratio[-1][histo_ratio[-1].find(":")+1:])+zero_counter}'
                else:
                    histo_ratio[-1] = f"{histo_ratio[-1]}:{zero_counter}"

            del deci_100 ; del zero_counter ; del histo_data ; del total ; del first_line

            try: del current_val
            except NameError: pass
            try: del val
            except NameError: pass
            try: del pnt_index
            except NameError: pass

        except Image.DecompressionBombError:
            return None
        except Exception:
            return None

        loop_variable = True ; start_index = 0

        while loop_variable:
            passed = True ; num_matches = 0
            try:
                for n in range(start_index,len(histo_ratio)-1):
                    if histo_ratio[n].find(":") != -1 and histo_ratio[n+1].find(":") != -1:
                        if histo_ratio[n] == histo_ratio[n+1]:
                            num_matches = 2
                            for x in range(n+2,len(histo_ratio)-1):
                                if histo_ratio[n] == histo_ratio[x]:
                                    num_matches += 1
                                else:
                                    histo_ratio[n] = f"{histo_ratio[n]}^{num_matches}"
                                    for z in range(num_matches-1):
                                        histo_ratio.pop(n+1)
                                    num_matches = 0 ; passed = False ; start_index = n+1
                                    break
                    elif histo_ratio[n].find(':') != -1:
                        continue
                    elif histo_ratio[n+1].find(":") == -1:
                        if histo_ratio[n] == histo_ratio[n+1]:
                            num_matches = 2
                            for x in range(n+2,len(histo_ratio)-1):
                                if histo_ratio[x].find(':') == -1:
                                    if histo_ratio[n] == histo_ratio[x]:
                                        num_matches += 1
                                    else:
                                        histo_ratio[n] = f"{histo_ratio[n]}*{num_matches}"
                                        for z in range(num_matches-1):
                                            histo_ratio.pop(n+1)
                                        num_matches = 0 ; passed = False ; start_index = n+1
                                        break
                                else:
                                    if histo_ratio[n] == histo_ratio[x][:histo_ratio[x].find(":")]:
                                        histo_ratio[n] = f"{histo_ratio[n]}*{num_matches+1}{histo_ratio[x][histo_ratio[x].find(':'):]}"
                                        for z in range(num_matches-1):
                                            histo_ratio.pop(n+1)
                                        num_matches = 0 ; passed = False ; start_index = n+1
                                        break
                                    else:
                                        histo_ratio[n] = f"{histo_ratio[n]}*{num_matches}"
                                        for z in range(num_matches-1):
                                            histo_ratio.pop(n+1)
                                        num_matches = 0 ; passed = False ; start_index = n+1
                                        break
                            if not passed:
                                break
                if passed:
                    break
            except IndexError:
                break

        del loop_variable ; del passed ; del start_index

        for n in range(len(histo_ratio)):
            for item in self.shorthand:
                if item in histo_ratio[n]:
                    histo_ratio[n] = histo_ratio[n].replace(item,self.short_ref[item])

        for n in range(len(histo_ratio)):
            if histo_ratio[n].startswith("."):
                for x in self.sub_keys:
                    if histo_ratio[n].startswith(x):
                        histo_ratio[n] = f'{self.subbing[x]}{histo_ratio[n][2:]}'

        adjacent_match = [[histo_ratio[0]]]
        current_index = 0

        for n in range(len(histo_ratio)-1):
            if histo_ratio[n][0] == histo_ratio[n+1][0] and not ':' in histo_ratio[n] and not '^' in histo_ratio[n] and not '*' in histo_ratio[n]:
                adjacent_match[current_index].append(histo_ratio[n+1])
            else:
                adjacent_match[-1] = tuple(adjacent_match[-1])
                adjacent_match.append([histo_ratio[n+1]])
                current_index += 1

        adjacent_match[-1] = tuple(adjacent_match[-1])
        adjacent_match = tuple(adjacent_match)

        histo_ratio = []

        for match in adjacent_match:
            if len(match) != 1:
                new_str = f"{match[0][0]}|"
                for item in match:
                    new_str = f"{new_str}{item[1:]}"
                histo_ratio.append(new_str)
            else:
                histo_ratio.append(match[0])

        return tuple(histo_ratio)


    def archive_txt_data(self, txt_path : str, archive_db_name : str) -> bool:

        if (baseline_metadata := getBaselineMetadata(txt_path)) is None:
            return False

        baseline_metadata = '|'.join(baseline_metadata)

        if not exists((txt_folder := f"{self.db_path}/{archive_db_name}/_txt_files")):
            mkdir(txt_folder)

        new_txt_file = f"{txt_folder}/{txt_path[txt_path.rfind('/')+1:]}"

        try:
            createCopy(txt_path,new_txt_file)

            # This is to disable txt files flagged as read-only. This does NOT
            # modify the permissions of the original txt file.
            chmod(new_txt_file,S_IRWXU)

            rename(new_txt_file,(renamed_txt_file := f'{new_txt_file[:new_txt_file.rfind("/")]}/{new_txt_file[new_txt_file.rfind("/")+1:new_txt_file.rfind(".")]}_{new_txt_file[new_txt_file.rfind(".")+1:]}.txt'))

            new_txt_file = renamed_txt_file[:]
            del renamed_txt_file

            if (txt_lines := getTxtFileLines(new_txt_file)) is None:
                if exists(txt_folder):
                    if not len(listdir(txt_folder)):
                        rmtree(txt_folder)
                return False

            counter = 0

            with open(new_txt_file,'w',encoding='utf-8') as tf:
                tf.write(txt_lines[0])
                counter += 1
                for n in range(1,len(txt_lines)):
                    tf.write(f"\n{txt_lines[n]}")
                    counter += 1

            del txt_lines

            if not exists((_metadata := f'{self.db_path}/{archive_db_name}/_metadata.txt')):
                try:
                    with open(_metadata,'w',encoding='utf-8') as tf:
                        tf.write(f"{new_txt_file[new_txt_file.rfind('/')+1:][:-4]}|TXT|{baseline_metadata}|{counter}")
                except UnicodeEncodeError:
                    with open(_metadata,'w',encoding='latin-1') as tf:
                        tf.write(f"{new_txt_file[new_txt_file.rfind('/')+1:][:-4]}|TXT|{baseline_metadata}|{counter}")
            else:
                try:
                    with open(_metadata,'a',encoding='utf-8') as tf:
                        tf.write(f"\n{new_txt_path[new_txt_path.rfind('/')+1:][:-4]}|TXT|{baseline_metadata}|{counter}")
                except UnicodeEncodeError:
                    with open(_metadata,'a',encoding='latin-1') as tf:
                        tf.write(f"\n{new_txt_path[new_txt_path.rfind('/')+1:][:-4]}|TXT|{baseline_metadata}|{counter}")
        except Exception:
            if exists(txt_folder):
                if not len(listdir(txt_folder)):
                    rmtree(txt_folder)
                else:
                    if exists(new_txt_file):
                        remove(new_txt_file)

        return True


    def archive_doc_data(self, doc_path : str, archive_db_name : str) -> bool:

        nulls = {"",0,None}

        if (baseline_metadata := getBaselineMetadata(doc_path)) is None:
            return False

        baseline_metadata = '|'.join(baseline_metadata)

        metadata_info = []

        try:
            word_doc = Document(doc_path)
            props = word_doc.core_properties
            if not (temp_str := props.title) in nulls:
                if temp_str == "<NULL>":
                    temp_str = '"<NULL>"'
                temp_str = str(temp_str).rstrip('\n')
                temp_str = temp_str.strip()
                while '  ' in temp_str:
                    temp_str = temp_str.replace('  ',' ')
                metadata_info.append(temp_str)
            else:
                metadata_info.append("<NULL>")
            if not (temp_str := props.author) in nulls:
                if temp_str == "<NULL>":
                    temp_str = '"<NULL>"'
                temp_str = str(temp_str).rstrip('\n')
                temp_str = temp_str.strip()
                while '  ' in temp_str:
                    temp_str = temp_str.replace('  ',' ')
                metadata_info.append(temp_str)
            else:
                metadata_info.append("<NULL>")
            if not (temp_str := props.subject) in nulls:
                if temp_str == "<NULL>":
                    temp_str = '"<NULL>"'
                temp_str = str(temp_str).rstrip('\n')
                temp_str = temp_str.strip()
                while '  ' in temp_str:
                    temp_str = temp_str.replace('  ',' ')
                metadata_info.append(temp_str)
            else:
                metadata_info.append("<NULL>")
            if not (temp_str := props.identifier) in nulls:
                if temp_str == "<NULL>":
                    temp_str = '"<NULL>"'
                temp_str = str(temp_str).rstrip('\n')
                temp_str = temp_str.strip()
                while '  ' in temp_str:
                    temp_str = temp_str.replace('  ',' ')
                metadata_info.append(temp_str)
            else:
                metadata_info.append("<NULL>")
            if not (temp_str := props.language) in nulls:
                if temp_str == "<NULL>":
                    temp_str = '"<NULL>"'
                temp_str = str(temp_str).rstrip('\n')
                temp_str = temp_str.strip()
                while '  ' in temp_str:
                    temp_str = temp_str.replace('  ',' ')
                metadata_info.append(temp_str)
            else:
                metadata_info.append("<NULL>")
            if not (temp_str := props.category) in nulls:
                if temp_str == "<NULL>":
                    temp_str = '"<NULL>"'
                temp_str = str(temp_str).rstrip('\n')
                temp_str = temp_str.strip()
                while '  ' in temp_str:
                    temp_str = temp_str.replace('  ',' ')
                metadata_info.append(temp_str)
            else:
                metadata_info.append("<NULL>")
            if not (temp_str := props.keywords) in nulls:
                if temp_str == "<NULL>":
                    temp_str = '"<NULL>"'
                temp_str = str(temp_str).rstrip('\n')
                temp_str = temp_str.strip()
                while '  ' in temp_str:
                    temp_str = temp_str.replace('  ',' ')
                metadata_info.append(temp_str)
            else:
                metadata_info.append("<NULL>")
            if not (temp_str := props.revision) in nulls:
                if temp_str == "<NULL>":
                    temp_str = '"<NULL>"'
                temp_str = str(temp_str).rstrip('\n')
                temp_str = temp_str.strip()
                while '  ' in temp_str:
                    temp_str = temp_str.replace('  ',' ')
                metadata_info.append(temp_str)
            else:
                metadata_info.append("<NULL>")
            if not (temp_str := props.version) in nulls:
                if temp_str == "<NULL>":
                    temp_str = '"<NULL>"'
                temp_str = str(temp_str).rstrip('\n')
                temp_str = temp_str.strip()
                while '  ' in temp_str:
                    temp_str = temp_str.replace('  ',' ')
                metadata_info.append(temp_str)
            else:
                metadata_info.append("<NULL>")

            metadata_info = tuple(metadata_info)
        except Exception:
            try:
                word_doc = docx2(doc_path)
                props = word_doc.core_properties
                if not (temp_str := props['title']) in nulls:
                    if temp_str == "<NULL>":
                        temp_str = '"<NULL>"'
                    temp_str = str(temp_str).rstrip('\n')
                    while '  ' in temp_str:
                        temp_str = temp_str.replace('  ',' ')
                    metadata_info.append(temp_str)
                else:
                    metadata_info.append("<NULL>")
                if not (temp_str := props["creator"]) in nulls:
                    if temp_str == "<NULL>":
                        temp_str = '"<NULL>"'
                    temp_str = str(temp_str).rstrip('\n')
                    while '  ' in temp_str:
                        temp_str = temp_str.replace('  ',' ')
                    metadata_info.append(temp_str)
                else:
                    metadata_info.append("<NULL>")
                if not (temp_str := props["subject"]) in nulls:
                    if temp_str == "<NULL>":
                        temp_str = '"<NULL>"'
                    temp_str = str(temp_str).rstrip('\n')
                    while '  ' in temp_str:
                        temp_str = temp_str.replace('  ',' ')
                    metadata_info.append(temp_str)
                else:
                    metadata_info.append("<NULL>")
                metadata_info.append("<NULL>") # unable to determine indentifier
                metadata_info.append("<NULL>") # unable to determine language
                metadata_info.append("<NULL>") # unable to determine category
                if not (temp_str := props["keywords"]) in nulls:
                    if temp_str == "<NULL>":
                        temp_str = '"<NULL>"'
                    temp_str = str(temp_str).rstrip('\n')
                    while '  ' in temp_str:
                        temp_str = temp_str.replace('  ',' ')
                    metadata_info.append(temp_str)
                else:
                    metadata_info.append("<NULL>")
                if not (temp_str := props["revision"]) in nulls:
                    if temp_str == "<NULL>":
                        temp_str = '"<NULL>"'
                    temp_str = str(temp_str).rstrip('\n')
                    while '  ' in temp_str:
                        temp_str = temp_str.replace('  ',' ')
                    metadata_info.append(temp_str)
                else:
                    metadata_info.append("<NULL>")
                metadata_info.append("<NULL>") # unable to determine version
            except Exception:
                pass

        del props
        try: del temp_str
        except NameError: pass

        mkdir((doc_folder := f'{self.db_path}/{archive_db_name}/{doc_path[doc_path.rfind("/")+1:doc_path.rfind(".")]}_{doc_path[doc_path.rfind(".")+1:]}'))
        mkdir((temp_folder := f'{doc_folder}/_temp_images'))

        if not len(metadata_info):
            with open(f'{doc_folder}/doc_metadata.txt','w',encoding='utf-8') as tf:
                tf.write("UNABLE TO EXTRACT METADATA")
        else:
            forcedTxtFileWrite(f"{doc_folder}/doc_metadata.txt",metadata_info)

        del metadata_info

        try:
            with docx2(doc_path,temp_folder) as doc_content:
                doc_text = doc_content.text
            while '\n\n' in doc_text:
                doc_text = doc_text.replace('\n\n','\n')
            doc_text = doc_text.replace('\t','')
            for n in range(len((doc_text := doc_text.split('\n')))):
                while '  ' in doc_text[n]:
                    doc_text[n] = doc_text[n].replace('  ',' ')
                doc_text[n] = doc_text[n].strip()
            if len((doc_text := tuple(doc_text))):
                with open(f'{doc_folder}/doc_extracted_text.txt','w',encoding='utf-8') as tf:
                    tf.write(doc_text[0])
                    for n in range(1,len(doc_text)):
                        tf.write(f"\n{doc_text[n]}")
            else:
                with open(f'{doc_folder}/doc_extracted_text.txt','w',encoding='utf-8') as tf:
                    pass
        except Exception:
            with open(f'{doc_folder}/doc_extracted_text.txt','w',encoding='utf-8') as tf:
                tf.write("UNABLE TO EXTRACT TEXT")

        try: del doc_text
        except NameError: pass

        if len((temp_images := tuple(listdir(temp_folder)))):
            with open(f'{doc_folder}/image_histogram_data.txt','w',encoding='utf-8') as tf:
                tf.write(temp_images[0])
                if not (histo_ratio := self.getImageInformation(f'{temp_folder}/{temp_images[0]}')) is None:
                    for num in histo_ratio:
                        tf.write(f'\n{num}')
                    try: entropy_val = round(Image.open(f'{temp_folder}/{temp_images[0]}').entropy(),8)
                    except Exception: entropy_val = 0
                    tf.write(f"\n{entropy_val}")
                else:
                    tf.write("\nNO DATA")
                for n in range(1,len(temp_images)):
                    tf.write(f"\n{temp_images[n]}")
                    if not (histo_ratio := self.getImageInformation(f'{temp_folder}/{temp_images[n]}')) is None:
                        for num in histo_ratio:
                            tf.write(f"\n{num}")
                        try: entropy_val = round(Image.open(f'{temp_folder}/{temp_images[n]}').entropy(),8)
                        except Exception: entropy_val = 0
                        tf.write(f"\n{entropy_val}")
                    else:
                        tf.write("\nNO DATA")

        try:
            remove(temp_folder)
        except Exception:
            rmtree(temp_folder)

        counters = [0,0]

        if exists(f'{doc_folder}/doc_extracted_text.txt'):
            with open(f'{doc_folder}/doc_extracted_text.txt','r',encoding='utf-8') as tf:
                while True:
                    line = tf.readline()
                    if not line:
                        break
                    counters[0] += 1
        if exists(f'{doc_folder}/image_histogram_data.txt'):
            with open(f'{doc_folder}/image_histogram_data.txt','r',encoding='utf-8') as tf:
                while True:
                    line = tf.readline()
                    if not line:
                        break
                    counters[1] += 1

        if not exists((_metadata := f'{self.db_path}/{archive_db_name}/_metadata.txt')):
            try:
                with open(_metadata,'w',encoding='utf-8') as tf:
                    tf.write(f'{doc_path[doc_path.rfind("/")+1:doc_path.rfind(".")]}_{doc_path[doc_path.rfind(".")+1:]}|DOC|{baseline_metadata}|{counters[0]}|{counters[1]}')
            except UnicodeEncodeError:
                with open(_metadata,'w',encoding='latin-1') as tf:
                    tf.write(f'{doc_path[doc_path.rfind("/")+1:doc_path.rfind(".")]}_{doc_path[doc_path.rfind(".")+1:]}|DOC|{baseline_metadata}|{counters[0]}|{counters[1]}')
        else:
            try:
                with open(_metadata,'a',encoding='utf-8') as tf:
                    tf.write(f'\n{doc_path[doc_path.rfind("/")+1:doc_path.rfind(".")]}_{doc_path[doc_path.rfind(".")+1:]}|DOC|{baseline_metadata}|{counters[0]}|{counters[1]}')
            except UnicodeEncodeError:
                with open(_metadata,'a',encoding='latin-1') as tf:
                    tf.write(f'\n{doc_path[doc_path.rfind("/")+1:doc_path.rfind(".")]}_{doc_path[doc_path.rfind(".")+1:]}|DOC|{baseline_metadata}|{counters[0]}|{counters[1]}')

        return True


    def archive_shp_data(self, shp_path : str, archive_db_name : str) -> bool:

        if (baseline_metadata := getBaselineMetadata(shp_path)) is None:
            return False

        baseline_metadata = '|'.join(baseline_metadata)

        redundant_fields = {'created_user','created_date','last_edited_user','last_edited_date','shape','annotation class id','symbol id','element'}
        # Yes, this is weirdly necessary.
        sql_keywords_set = set((sql_keywords := ('add','add constraint','all','alter','alter column','alter table','and','any','as','asc','backup database','between','case','check','column','constraint','create','create database','create index','create or replace view','create table','create procedure','create unique index',' create view','database','default','delete','desc','distinct','drop','drop column','drop constraint','drop database','drop default','drop index','drop table','drop view','exec','exists','foreign key','from','full outer join','group by','having','in','index','inner join','insert into','insert into select','is null','is not null','join','left join','like','limit','not','not null','or','order by','outer join','primary key','procedure','right join','rownum','select','select distinct','select into','select top','set','table','top','truncate table','union','union all','unique','update','values','view','where')))

        arcpy.env.workspace = shp_path[:shp_path.rfind("/")]

        shapefile_name = shp_path[shp_path.rfind("/")+1:]

        item_info = {} ; oid_name = None
        try:
            for field in arcpy.ListFields(shapefile_name,field_type='OID'):
                oid_name = field.name[:]
                break
        except Exception:
            # Shapefile cannot be read via ArcPy for unknown reasons.
            return False
        if oid_name is None:
            return False
        fields = [field.name for field in tuple(arcpy.ListFields(shapefile_name)) if not field.name.lower() in redundant_fields]
        fields.remove(oid_name)
        fields = sorted(fields)
        fields.insert(0,oid_name)
        # prevent a weird bug where arcpy thinks a field named matching a SQL keyword is
        # actually an SQL query despite documentation implying this is not
        # supposed to happen.
        sql_fields = []
        for field in fields:
            temp_field = field.lower()
            if temp_field in sql_keywords_set:
                sql_fields.append(field)
                fields.remove(field)
            else:
                for sql_keyword in sql_keywords:
                    if f" {sql_keyword} " in temp_field or temp_field.startswith(f"{sql_keyword} ") or temp_field.endswith(f" {sql_keyword}"):
                        sql_fields.append(field)
                        fields.remove(field)
                        break
        try: del temp_field
        except NameError: pass
        if not len(sql_fields):
            ranger = range(1,len(fields))
            for row in arcpy.da.SearchCursor(shapefile_name,fields):
                temp_list = []
                for item in [row[n] for n in ranger]:
                    if item is None:
                        temp_list.append("<Null>")
                    elif item == '<Null>':
                        temp_list.append('"<Null>"')
                    else:
                        temp_item = str(item).replace("\n"," ")
                        temp_item = temp_item.rstrip('\n')
                        temp_item = temp_item.strip()
                        while '  ' in temp_item:
                            temp_item = temp_item.replace('  ',' ')
                        temp_list.append(temp_item)
                item_info[row[0]] = '|'.join(tuple(temp_list))
                # item_info[row[0]] = '|'.join(tuple(["<Null>" if item is None else '"<Null>"' if item == '<Null>' else str(item).replace("\n"," ") for item in [row[n] for n in ranger]]))
        else:
            arcpy.env.overwriteOutput = True
            arcpy.management.CopyFeatures(f'{arcpy.env.workspace}/{shapefile_name}',(temp_shp := f'{self.db_path}/{archive_db_name}/{shapefile_name}'))
            arcpy.env.overwriteOutput = False
            alter_fields = fields[:]
            for field in arcpy.ListFields(temp_shp):
                if not field.name in fields and not field.name.lower() in redundant_fields:
                    alter_fields.append(field.name)
            fields = fields + sql_fields
            ranger = range(1,len(sql_fields))
            for row in arcpy.da.SearchCursor(temp_shp,alter_fields):
                temp_list = []
                for item in [row[n] for n in ranger]:
                    if item is None:
                        temp_list.append("<Null>")
                    elif item == '<Null>':
                        temp_list.append('"<Null>"')
                    else:
                        temp_item = str(item).replace("\n"," ")
                        temp_item = temp_item.rstrip('\n')
                        temp_item = temp_item.strip()
                        while '  ' in temp_item:
                            temp_item = temp_item.replace('  ',' ')
                        temp_list.append(temp_item)
                item_info[row[0]] = '|'.join(tuple(temp_list))
                # item_info[row[0]] = '|'.join(tuple(["<Null>" if item is None else '"<Null>"' if item == '<Null>' else str(item).replace("\n"," ") for item in [row[n] for n in ranger]]))
            arcpy.management.Delete(temp_shp)
        if not exists((shp_folder := f'{self.db_path}/{archive_db_name}/_shp_files')):
            mkdir(shp_folder)
        with open(f'{shp_folder}/{shapefile_name[:shapefile_name.rfind(".")]}_{shapefile_name[shapefile_name.rfind(".")+1:]}.txt','w',encoding='utf-8') as tf:
            tf.write(r'|'.join(fields[1:]))
            counter = 1
            for oid in tuple(sorted(item_info.keys())):
                tf.write(f'\n{item_info[oid]}')
                counter += 1

        if not exists((_metadata := f'{self.db_path}/{archive_db_name}/_metadata.txt')):
            try:
                with open(_metadata,'w',encoding='utf-8') as tf:
                    tf.write(f"{shapefile_name[:shapefile_name.rfind('.')]}_{shapefile_name[shapefile_name.rfind('.')+1:]}|SHP|{baseline_metadata}|{counter}")
            except UnicodeEncodeError:
                with open(_metadata,'w',encoding='latin-1') as tf:
                    tf.write(f"{shapefile_name[:shapefile_name.rfind('.')]}_{shapefile_name[shapefile_name.rfind('.')+1:]}|SHP|{baseline_metadata}|{counter}")
        else:
            try:
                with open(_metadata,'a',encoding='utf-8') as tf:
                    tf.write(f"\n{shapefile_name[:shapefile_name.rfind('.')]}_{shapefile_name[shapefile_name.rfind('.')+1:]}|SHP|{baseline_metadata}|{counter}")
            except UnicodeEncodeError:
                with open(_metadata,'a',encoding='latin-1') as tf:
                    tf.write(f"\n{shapefile_name[:shapefile_name.rfind('.')]}_{shapefile_name[shapefile_name.rfind('.')+1:]}|SHP|{baseline_metadata}|{counter}")

        return True


    def archive_gdb_data(self, gdb_path : str, archive_db_name : str) -> bool:

        # Views, Relationship Classes, Mosaic Datasets, Raster Datasets,
        # Trajectory Datasets, Catalog Datasets, and Oriented Imagery Datasets
        # are ignored.

        try:
            gdb_files = {}
            for gdb_item in tuple(listdir(gdb_path)):
                if not gdb_item.lower().endswith('.lock'):
                    if (item_size := getSizeOfItem(f"{gdb_path}/{gdb_item}")) is None:
                        return False
                    gdb_files[gdb_item] = (getModifiedDate(f'{gdb_path}/{gdb_item}')[4:],getCreatedDate(f'{gdb_path}/{gdb_item}')[4:],item_size)
            del item_size
        except Exception:
            return False

        mkdir((output_subfolder := f'{self.db_path}/{archive_db_name}/{gdb_path[gdb_path.rfind("/")+1:gdb_path.rfind(".")]}_{gdb_path[gdb_path.rfind(".")+1:]}'))

        arcpy.env.workspace = gdb_path[:]

        redundant_fields = {'created_user','created_date','last_edited_user','last_edited_date','shape','annotation class id','symbol id','element'}
        # Yes, this is weirdly necessary.
        sql_keywords_set = set((sql_keywords := ('add','add constraint','all','alter','alter column','alter table','and','any','as','asc','backup database','between','case','check','column','constraint','create','create database','create index','create or replace view','create table','create procedure','create unique index',' create view','database','default','delete','desc','distinct','drop','drop column','drop constraint','drop database','drop default','drop index','drop table','drop view','exec','exists','foreign key','from','full outer join','group by','having','in','index','inner join','insert into','insert into select','is null','is not null','join','left join','like','limit','not','not null','or','order by','outer join','primary key','procedure','right join','rownum','select','select distinct','select into','select top','set','table','top','truncate table','union','union all','unique','update','values','view','where')))

        object_counters = []

        def processGDBEntity(entity_name : str, dataset_name : str = '') -> str:

            if dataset_name != '':
                # $ is used to denote a separator and indicate the item is
                # within a dataset within a file geodatabase. You normally
                # cannot use non-alphanumeric characters such as $ to name
                # datasets in ArcGIS Pro.
                dataset_name = f'{dataset_name}$'

            item_info = {} ; oid_name = None
            try:
                for field in arcpy.ListFields(entity_name,field_type='OID'):
                    oid_name = field.name[:]
                    break
            except Exception:
                # Item cannot be read via ArcPy for unknown reasons.
                return False
            if oid_name is None:
                return False
            fields = [field.name for field in tuple(arcpy.ListFields(entity_name)) if not field.name.lower() in redundant_fields]
            fields.remove(oid_name)
            fields = sorted(fields)
            fields.insert(0,oid_name)
            # prevent a weird bug where arcpy thinks a field named matching a SQL keyword is
            # actually an SQL query despite documentation implying this is not
            # supposed to happen.
            sql_fields = []
            for field in fields:
                temp_field = field.lower()
                if temp_field in sql_keywords_set:
                    sql_fields.append(field)
                    fields.remove(field)
                else:
                    for sql_keyword in sql_keywords:
                        if f" {sql_keyword} " in temp_field or temp_field.startswith(f"{sql_keyword} ") or temp_field.endswith(f" {sql_keyword}"):
                            sql_fields.append(field)
                            fields.remove(field)
                            break
            try: del temp_field
            except NameError: pass
            if not len(sql_fields):
                ranger = range(1,len(fields))
                for row in arcpy.da.SearchCursor(entity_name,fields):
                    temp_list = []
                    for item in [row[n] for n in ranger]:
                        if item is None:
                            temp_list.append("<Null>")
                        elif item == '<Null>':
                            temp_list.append('"<Null>"')
                        else:
                            temp_item = str(item).replace("\n"," ")
                            temp_item = temp_item.rstrip('\n')
                            temp_item = temp_item.strip()
                            while '  ' in temp_item:
                                temp_item = temp_item.replace('  ',' ')
                            temp_list.append(temp_item)
                    item_info[row[0]] = '|'.join(tuple(temp_list))
                    # item_info[row[0]] = '|'.join(tuple(["<Null>" if item is None else '"<Null>"' if item == '<Null>' else str(item).replace("\n"," ") for item in [row[n] for n in ranger]]))
            else:
                if not exists((temp_gdb := f'{self.db_path}/{archive_db_name}/TeMp_FiLeGeOdAtAbAsE_6789_10.gdb')):
                    arcpy.management.CreateFileGDB(f'{self.db_path}/{archive_db_name}','TeMp_FiLeGeOdAtAbAsE_6789_10','CURRENT')
                arcpy.env.overwriteOutput = True
                arcpy.management.Copy(f'{arcpy.env.workspace}/{entity_name}',f'{temp_gdb}/{entity_name}')
                arcpy.env.overwriteOutput = False
                alter_fields = fields[:]
                for field in arcpy.ListFields(f'{temp_gdb}/{entity_name}'):
                    if not field.name in fields and not field.name.lower() in redundant_fields:
                        alter_fields.append(field.name)
                fields = fields + sql_fields
                ranger = range(1,len(sql_fields))
                for row in arcpy.da.SearchCursor(f'{temp_gdb}/{entity_name}',alter_fields):
                    temp_list = []
                    for item in [row[n] for n in ranger]:
                        if item is None:
                            temp_list.append("<Null>")
                        elif item == '<Null>':
                            temp_list.append('"<Null>"')
                        else:
                            temp_item = str(item).replace("\n"," ")
                            temp_item = temp_item.rstrip('\n')
                            temp_item = temp_item.strip()
                            while '  ' in temp_item:
                                temp_item = temp_item.replace('  ',' ')
                            temp_list.append(temp_item)
                    item_info[row[0]] = '|'.join(tuple(temp_list))
                    # item_info[row[0]] = '|'.join(tuple(["<Null>" if item is None else '"<Null>"' if item == '<Null>' else str(item).replace('\n',' ') for item in [row[n] for n in ranger]]))
            with open(f'{output_subfolder}/{dataset_name}{entity_name}.txt','w',encoding='utf-8') as tf:
                tf.write(r'|'.join(fields[1:]))
                counter = 1
                for oid in tuple(sorted(item_info.keys())):
                    tf.write(f'\n{item_info[oid]}')
                    counter += 1
            return f'{dataset_name}{entity_name} {counter}'


        for f_t in ('Point','Polyline','Polygon','Annotation'):
            if not (list_feature_classes := arcpy.ListFeatureClasses(feature_type=f_t)) is None:
                for fc in list_feature_classes:
                    object_counters.append(processGDBEntity(fc))

        if not (list_tables := arcpy.ListTables()) is None:
            for table in list_tables:
                object_counters.append(processGDBEntity(table))

        for dataset in tuple(arcpy.ListDatasets()):
            arcpy.env.workspace = f'{gdb_path}/{dataset}'
            for f_t in ('Point','Polyline','Polygon','Annotation'):
                if not (list_feature_classes := arcpy.ListFeatureClasses(feature_type=f_t)) is None:
                    for fc in list_feature_classes:
                        object_counters.append(processGDBEntity(fc,dataset))
            if not (list_tables := arcpy.ListTables()) is None:
                for table in arcpy.ListTables():
                    object_counters.append(processGDBEntity(table,dataset))

        if not len(object_counters):
            rmtree(output_subfolder)
            return False

        try:
            object_counters = '|'.join(sorted(object_counters))
        except TypeError:
            # implies a file geodatabase with empty items
            object_counters = "<|NONE|>"
        try:
            with open(f'{self.db_path}/{archive_db_name}/{gdb_path[gdb_path.rfind("/")+1:gdb_path.rfind(".")]}_{gdb_path[gdb_path.rfind(".")+1:]}_metadata.txt','w',encoding='utf-8') as tf:
                gdb_items = tuple(gdb_files.keys())
                tf.write(f'{object_counters}\n{gdb_items[0]}|{gdb_files[gdb_items[0]][0]}|{gdb_files[gdb_items[0]][1]}|{gdb_files[gdb_items[0]][2]}')
                for n in range(1,len(gdb_items)):
                    tf.write(f"\n{gdb_items[n]}|{gdb_files[gdb_items[n]][0]}|{gdb_files[gdb_items[n]][1]}|{gdb_files[gdb_items[n]][2]}")
        except UnicodeEncodeError:
            with open(f'{self.db_path}/{archive_db_name}/{gdb_path[gdb_path.rfind("/")+1:gdb_path.rfind(".")]}_{gdb_path[gdb_path.rfind(".")+1:]}_metadata.txt','w',encoding='latin-1') as tf:
                gdb_items = tuple(gdb_files.keys())
                tf.write(f'{object_counters}\n{gdb_items[0]}|{gdb_files[gdb_items[0]][0]}|{gdb_files[gdb_items[0]][1]}|{gdb_files[gdb_items[0]][2]}')
                for n in range(1,len(gdb_items)):
                    tf.write(f"\n{gdb_items[n]}|{gdb_files[gdb_items[n]][0]}|{gdb_files[gdb_items[n]][1]}|{gdb_files[gdb_items[n]][2]}")

        return True


    def archive_img_data(self, image_path : str, archive_db_name : str) -> bool:

        if (baseline_metadata := getBaselineMetadata(image_path)) is None:
            return False

        baseline_metadata = '|'.join(baseline_metadata)

        if (histo_ratio := self.getImageInformation(image_path)):
            if not exists((img_folder := f'{self.db_path}/{archive_db_name}/_images')):
                mkdir(img_folder)
            with open(f'{img_folder}/{image_path[image_path.rfind("/")+1:image_path.rfind(".")]}_{image_path[image_path.rfind(".")+1:]}.txt','w',encoding='utf-8') as tf:
                tf.write(histo_ratio[0])
                if exists((firstline_images := f'{self.db_path}/{archive_db_name}/_firstline_image_files.txt')):
                    with open(firstline_images,'a',encoding='utf-8') as f:
                        f.write(f'\n{image_path[image_path.rfind("/")+1:image_path.rfind(".")]}_{image_path[image_path.rfind(".")+1:]} {histo_ratio[0]}')
                else:
                    with open(firstline_images,'w',encoding='utf-8') as f:
                        f.write(f'{image_path[image_path.rfind("/")+1:image_path.rfind(".")]}_{image_path[image_path.rfind(".")+1:]} {histo_ratio[0]}')
                counter = 1
                for n in range(1,len(histo_ratio)):
                    tf.write(f'\n{histo_ratio[n]}')
                    counter += 1
        else:
            return False

        del histo_ratio

        try: del img_folder
        except NameError: pass

        if not exists((_metadata := f'{self.db_path}/{archive_db_name}/_metadata.txt')):
            try:
                with open(_metadata,'w',encoding='utf-8') as tf:
                    tf.write(f'{image_path[image_path.rfind("/")+1:image_path.rfind(".")]}_{image_path[image_path.rfind(".")+1:]}|IMG|{baseline_metadata}|{counter}')
            except UnicodeEncodeError:
                with open(_metadata,'w',encoding='latin-1') as tf:
                    tf.write(f'{image_path[image_path.rfind("/")+1:image_path.rfind(".")]}_{image_path[image_path.rfind(".")+1:]}|IMG|{baseline_metadata}|{counter}')
        else:
            try:
                with open(_metadata,'a',encoding='utf-8') as tf:
                    tf.write(f'\n{image_path[image_path.rfind("/")+1:image_path.rfind(".")]}_{image_path[image_path.rfind(".")+1:]}|IMG|{baseline_metadata}|{counter}')
            except UnicodeEncodeError:
                with open(_metadata,'a',encoding='latin-1') as tf:
                    tf.write(f'\n{image_path[image_path.rfind("/")+1:image_path.rfind(".")]}_{image_path[image_path.rfind(".")+1:]}|IMG|{baseline_metadata}|{counter}')

        return True


    def archive_pdf_data(self, pdf_path : str, archive_db_name : str) -> bool:

        nulls = {"",0,None}

        if (baseline_metadata := getBaselineMetadata(pdf_path)) is None:
            return False

        baseline_metadata = '|'.join(baseline_metadata)

        try:
            reader = PdfReader(pdf_path)
        except Exception:
            return False

        metadata_info = []

        if not (meta_pdf := reader.metadata) is None:
            if (meta_item := meta_pdf.title):
                if meta_item == "<NULL>":
                    meta_item = '"<NULL>"'
                meta_item = str(meta_item).rstrip('\n')
                meta_item = meta_item.strip()
                while '  ' in meta_item:
                    meta_item = meta_item.replace('  ',' ')
                metadata_info.append(meta_item)
            else:
                metadata_info.append("<NULL>")
            if (meta_item := meta_pdf.author):
                if meta_item == "<NULL>":
                    meta_item = '"<NULL>"'
                meta_item = str(meta_item).rstrip('\n')
                meta_item = meta_item.strip()
                while '  ' in meta_item:
                    meta_item = meta_item.replace('  ',' ')
                metadata_info.append(meta_item)
            else:
                metadata_info.append("<NULL>")
            if (meta_item := meta_pdf.creator):
                if meta_item == "<NULL>":
                    meta_item = '"<NULL>"'
                meta_item = str(meta_item).rstrip('\n')
                meta_item = meta_item.strip()
                while '  ' in meta_item:
                    meta_item = meta_item.replace('  ',' ')
                metadata_info.append(meta_item)
            else:
                metadata_info.append('<NULL>')
            if (meta_item := meta_pdf.producer):
                if meta_item == "<NULL>":
                    meta_item = '"<NULL>"'
                meta_item = str(meta_item).rstrip('\n')
                meta_item = meta_item.strip()
                while '  ' in meta_item:
                    meta_item = meta_item.replace('  ',' ')
                metadata_info.append(meta_item)
            else:
                metadata_info.append('<NULL>')
            if (meta_item := meta_pdf.subject):
                if meta_item == "<NULL>":
                    meta_item = '"<NULL>"'
                meta_item = str(meta_item).rstrip('\n')
                meta_item = meta_item.strip()
                while '  ' in meta_item:
                    meta_item = meta_item.replace('  ',' ')
                metadata_info.append(meta_item)
            else:
                metadata_info.append('<NULL>')
            del meta_item
        else:
            metadata_info = ['<NULL>' for n in range(5)]

        mkdir((pdf_folder := f'{self.db_path}/{archive_db_name}/{pdf_path[pdf_path.rfind("/")+1:pdf_path.rfind(".")]}_{pdf_path[pdf_path.rfind(".")+1:]}'))

        forcedTxtFileWrite(f"{pdf_folder}/pdf_metadata.txt",metadata_info)

        del metadata_info

        # Technically, you could create a PDF with more pages than this; however,
        # unless you are trying to compile vast amounts of human knowledge into
        # a single PDF file, this limit will never be reached for practical purposes.
        # So, 4,294,967,296 should be considered a hard cap.

        extracted_text_path = f"{pdf_folder}/pdf_extracted_text.txt"

        for n in range(4_294_967_296):
            try:
                pdf_info = reader.pages[n]
            except Exception:
                # All pages have been iterated or unable to be read.
                break
            if not (txt := pdf_info.extract_text()) in nulls:
                txt = txt.replace(" \n"," ")
                txt = txt.replace("\n"," ")
                while '  ' in txt:
                    txt = txt.replace('  ',' ')
                txt = txt.strip()
                if not exists(extracted_text_path):
                    with open(extracted_text_path,"w",encoding='utf-8') as tf:
                        tf.write(txt)
                else:
                    with open(extracted_text_path,"a",encoding='utf-8') as tf:
                        tf.write(f"\n{txt}")
            try:
                for count,image_file_object in enumerate(pdf_info.images):
                    with open((temp_image_file := f'{pdf_folder}/{count}{image_file_object.name}'),'wb') as fp:
                        fp.write(image_file_object.data)
                    if (histo_info := self.getImageInformation(temp_image_file)):
                        if not exists((image_histogram_data := f"{pdf_folder}/image_histogram_data.txt")):
                            with open(image_histogram_data,'w',encoding='utf-8') as tf:
                                tf.write(f"{count}{image_file_object.name}")
                                for line in histo_info:
                                    tf.write(f'\n{line}')
                                try: entropy_val = round(Image.open(temp_image_file).entropy(),8)
                                except Exception: entropy_val = 0
                                tf.write(f"\n{entropy_val}")
                        else:
                            with open(image_histogram_data,'a',encoding='utf-8') as tf:
                                tf.write(f"\n{count}{image_file_object.name}")
                                for line in histo_info:
                                    tf.write(f'\n{line}')
                                try: entropy_val = round(Image.open(temp_image_file).entropy(),8)
                                except Exception: entropy_val = 0
                                tf.write(f'\n{entropy_val}')
                    else:
                        if not exists((image_histogram_data := f"{pdf_folder}/image_histogram_data.txt")):
                            with open(image_histogram_data,'w',encoding='utf-8') as tf:
                                tf.write(f"{count}{image_file_object.name}\nNO DATA")
                        else:
                            with open(image_histogram_data,'a',encoding='utf-8') as tf:
                                tf.write(f"\n{count}{image_file_object.name}\nNO DATA")
                    remove(temp_image_file)
            except Exception:
                try:
                    remove(temp_image_file)
                except Exception:
                    pass

        try: del txt
        except NameError: pass
        try: del temp_folder
        except NameError: pass
        try: del img_info
        except NameError: pass
        try: del image_histogram_data
        except NameError: pass

        counters = [0,0]

        if exists(f'{pdf_folder}/pdf_extracted_text.txt'):
            with open(f'{pdf_folder}/pdf_extracted_text.txt','r',encoding='utf-8') as tf:
                while True:
                    line = tf.readline()
                    if not line:
                        break
                    counters[0] += 1
            if counters[0] == 1:
                # This prevents PDFs that are forms from being processed.
                if line.startswith('Please wait... If this message is not eventually replaced by the proper contents of the document, your PDF viewer may not be able to display this type of document.'):
                    rmtree(pdf_folder)
                    return False
        if exists(f'{pdf_folder}/image_histogram_data.txt'):
            with open(f'{pdf_folder}/image_histogram_data.txt','r',encoding='utf-8') as tf:
                while True:
                    line = tf.readline()
                    if not line:
                        break
                    counters[1] += 1

        if not exists((_metadata := f'{self.db_path}/{archive_db_name}/_metadata.txt')):
            try:
                with open(_metadata,'w',encoding='utf-8') as tf:
                    tf.write(f'{pdf_path[pdf_path.rfind("/")+1:pdf_path.rfind(".")]}_{pdf_path[pdf_path.rfind(".")+1:]}|PDF|{baseline_metadata}|{counters[0]}|{counters[1]}')
            except UnicodeEncodeError:
                with open(_metadata,'w',encoding='latin-1') as tf:
                    tf.write(f'{pdf_path[pdf_path.rfind("/")+1:pdf_path.rfind(".")]}_{pdf_path[pdf_path.rfind(".")+1:]}|PDF|{baseline_metadata}|{counters[0]}|{counters[1]}')
        else:
            try:
                with open(_metadata,'a',encoding='utf-8') as tf:
                    tf.write(f'\n{pdf_path[pdf_path.rfind("/")+1:pdf_path.rfind(".")]}_{pdf_path[pdf_path.rfind(".")+1:]}|PDF|{baseline_metadata}|{counters[0]}|{counters[1]}')
            except UnicodeEncodeError:
                with open(_metadata,'a',encoding='latin-1') as tf:
                    tf.write(f'\n{pdf_path[pdf_path.rfind("/")+1:pdf_path.rfind(".")]}_{pdf_path[pdf_path.rfind(".")+1:]}|PDF|{baseline_metadata}|{counters[0]}|{counters[1]}')

        return True


    def archive_alia_data(self, alia_path : str, archive_db_name : str) -> bool:

        if (baseline_metadata := getBaselineMetadata(alia_path)) is None:
            return False

        baseline_metadata = '|'.join(baseline_metadata)

        if not exists(f'{self.db_path}/{archive_db_name}/_alia_dosieroj.txt'):
            with open(f'{self.db_path}/{archive_db_name}/_alia_dosieroj.txt','w',encoding='utf-8') as tf:
                tf.write(f'{alia_path[alia_path.rfind("/")+1:]}|{baseline_metadata}')
        else:
            with open(f'{self.db_path}/{archive_db_name}/_alia_dosieroj.txt','a',encoding='utf-8') as tf:
                tf.write(f'\n{alia_path[alia_path.rfind("/")+1:]}|{baseline_metadata}')

        return True


    def searchQuery(self, entry_string : str, check_type : str | tuple[str] | list[str] | set[str] = 'any', include_entity_name : bool = True, entity_names_only : bool = False, return_tuple : bool = False, max_line_concat : int = 3, save_found_matches : bool = True, save_results_to_file : bool = False, output_file_type : str = 'excel', output_location : str | None = None, output_name : str | None = None, overwrite_existing_output : bool = False, csv_field_size_limit : int = 131_072, csv_delimiter : str = ',', overwrite_saved_found_matches : bool = False, terminal_progress_display_enabled : bool = False) -> tuple[str] | None:
        '''
        This allows, by default, the searching for the presence of specific
        term(s) in entities with data in the database as well as the name of the
        file, or the ability to check for entities of a specific name without
        needing to consider capitalization, the presence of certain random
        alphanumeric characters making things harder to find, and the file
        extension, unless designated.
        '''

        def getTestName(sub_entry_string : str) -> str:

            test_name = sub_entry_string.lower().strip()

            while '  ' in test_name:
                test_name = test_name.replace('  ',' ')

            for n in "[]+=@#!$%^&;{}(),":
                test_name = test_name.replace(n,' ')

            return test_name


        if terminal_progress_display_enabled and tqdm_imported:
            sys_clear()

        if max_line_concat < 2:
            max_line_concat = 2

        entry_string = entry_string.lower().strip()

        temp_entry_string = entry_string[:]

        for n in "[]+=@#!$%^&;{}(),":
            temp_entry_string = temp_entry_string.replace(n,' ')

        if not len((temp_entry_string := temp_entry_string.strip())):
            if return_tuple:
                return ()
            return None

        while '  ' in entry_string:
            entry_string = entry_string.replace('  ',' ')

        if len(entry_string) < 2:
            if return_tuple:
                return ()
            return None

        if output_name is None:
            if entry_string[0].isdigit() or not entry_string[0].isalnum():
                output_name = f"searched_term_query_{entry_string}"
            else:
                output_name = entry_string[:]
        elif (output_name := output_name.strip()) == '':
            if entry_string[0].isdigit() or not entry_string[0].isalnum():
                output_name = f"searched_term_query_{entry_string}"
            else:
                output_name = entry_string[:]

        for n in ('.','/','\\'):
            if n in output_name:
                output_name = output_name.replace(n,'_')

        output_file_type = output_file_type.lower().strip()
        output_file_type = output_file_type.replace(' ','')

        if not output_file_type in {'excel','xlsx','csv','text','txt'}:
            output_file_type = 'excel'
        if not exists(f'{self.db_path}/_terms_searched'):
            mkdir(f'{self.db_path}/_terms_searched')
        elif overwrite_saved_found_matches:
            pass
        elif entity_names_only:
            test_str = f'{temp_entry_string}$names'
            for previous_search in tuple([txt_file[:txt_file.rfind(".")] for txt_file in tuple(listdir(f'{self.db_path}/_terms_searched')) if txt_file.endswith('$names.txt')]):
                if test_str == previous_search:
                    if isinstance(check_type,str):
                        if (check_type := check_type.lower()) == 'docx':
                            check_type = 'doc'
                        match check_type:
                            case 'txt':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.txt'):
                                            found_name_matches.append(entity)
                            case 'pdf':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.pdf'):
                                            found_name_matches.append(entity)
                            case 'doc':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.docx'):
                                            found_name_matches.append(entity)
                            case 'shp':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.shp'):
                                            found_name_matches.append(entity)
                            case 'gdb':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.gdb'):
                                            found_name_matches.append(entity)
                            case 'img':
                                temp_extensions = tuple(self.accepted_image_extensions)
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        for extension in temp_extensions:
                                            if entity.lower().endswith(extension):
                                                found_name_matches.append(entity)
                                                break
                                del temp_extensions
                            case 'alia':
                                temp_extensions = tuple(list(self.image_types) + ['txt','pdf','docx','shp','gdb'])
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        for extension in temp_extensions:
                                            if not entity.lower()[entity.rfind(".")+1:].endswith(extension) or not '.' in entity:
                                                found_name_matches.append(entity)
                                                break
                                del temp_extensions
                            case _:
                                if return_tuple:
                                    return ()
                                return None
                        names_found = True
                    elif isinstance(check_type,(set,list,tuple)):
                        check_type = {item.lower() for item in tuple(check_type)}
                        if 'docx' in check_type:
                            check_type.remove('docx')
                            check_type.add('doc')
                        if 'img' in check_type:
                            check_type.remove('img')
                            for extension in self.image_types:
                                check_type.add(extension)
                        #irrelevant_extensions = {'txt','gdb','pdf','docx','shp'} + (image_types_set := set(self.image_types))
                        with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                            while True:
                                entity = tf.readline()
                                if not entity:
                                    break
                                entity = decodeZipTxtLine(entity).split('|')[0]
                                if (extension := entity[entity.rfind('.')+1:].lower()) in check_type:
                                    match extension:
                                        case 'txt':
                                            found_name_matches.append(entity)
                                        case 'pdf':
                                            found_name_matches.append(entity)
                                        case 'doc':
                                            found_name_matches.append(entity)
                                        case 'shp':
                                            found_name_matches.append(entity)
                                        case 'gdb':
                                            found_name_matches.append(entity)
                                        case _:
                                            if extension in image_types_set:
                                                found_name_matches.append(entity)
                                            elif "alia" in check_type:
                                                found_name_matches.append(entity)
                    elif return_tuple:
                        return ()
                    else:
                        return None
                    if len((found_matches := tuple(found_name_matches))):
                        if save_results_to_file:
                            genSearchQueryResultFile(found_matches,output_type,output_location,output_name,csv_field_size_limit,csv_delimiter,overwriteOutput,set(self.image_types))
                        if return_tuple:
                            return found_matches
                        return None
                    elif return_tuple:
                        return ()
                    else:
                        return None
        else:
            contents_found = False ; names_found = False
            test_contents_str = f'{temp_entry_string}$contents' ; test_name_str = f'{temp_entry_string}$names'
            found_matches = [] ; found_name_matches = []
            for previous_search in tuple([txt_file[:txt_file.rfind(".")] for txt_file in tuple(listdir(f'{self.db_path}/_terms_searched'))]):
                if test_contents_str == previous_search:
                    if isinstance(check_type,str):
                        if (check_type := check_type.lower()) == 'docx':
                            check_type = 'doc'
                        match check_type:
                            case 'txt':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.txt'):
                                            found_matches.append(entity)
                            case 'pdf':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.pdf'):
                                            found_matches.append(entity)
                            case 'doc':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.docx'):
                                            found_matches.append(entity)
                            case 'shp':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.shp'):
                                            found_matches.append(entity)
                            case 'gdb':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.gdb'):
                                            found_matches.append(entity)
                            case 'img':
                                temp_extensions = tuple(self.accepted_image_extensions)
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        for extension in temp_extensions:
                                            if entity.lower().endswith(extension):
                                                found_matches.append(entity)
                                                break
                                del temp_extensions
                            case 'alia':
                                temp_extensions = tuple(list(self.image_types) + ['txt','pdf','docx','shp','gdb'])
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        for extension in temp_extensions:
                                            if not entity.lower()[entity.rfind(".")+1:].endswith(extension) or not '.' in entity:
                                                found_matches.append(entity)
                                                break
                                del temp_extensions
                            case _:
                                if return_tuple:
                                    return ()
                                return None
                        contents_found = True
                    elif isinstance(check_type,(tuple,set,list)):
                        check_type = {item.lower() for item in tuple(check_type)}
                        if 'docx' in check_type:
                            check_type.remove('docx')
                            check_type.add('doc')
                        if 'img' in check_type:
                            check_type.remove('img')
                            for extension in self.image_types:
                                check_type.add(extension)
                        irrelevant_extensions = {'txt','gdb','pdf','docx','shp'} + (image_types_set := set(self.image_types))
                        with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                            while True:
                                entity = tf.readline()
                                if not entity:
                                    break
                                entity = decodeZipTxtLine(entity).split('|')[0]
                                if (extension := entity[entity.rfind('.')+1:].lower()) in check_type:
                                    match extension:
                                        case 'txt':
                                            found_matches.append(entity)
                                        case 'pdf':
                                            found_matches.append(entity)
                                        case 'doc':
                                            found_matches.append(entity)
                                        case 'shp':
                                            found_matches.append(entity)
                                        case 'gdb':
                                            found_matches.append(entity)
                                        case _:
                                            if extension in image_types_set:
                                                found_matches.append(entity)
                                            elif not extension in irrelevant_extensions and "alia" in check_type:
                                                found_matches.append(entity)
                    elif return_tuple:
                        return ()
                    else:
                        return None
                if test_name_str == previous_search:
                    if isinstance(check_type,str):
                        if (check_type := check_type.lower()) == 'docx':
                            check_type = 'doc'
                        match check_type:
                            case 'txt':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.txt'):
                                            found_name_matches.append(entity)
                            case 'pdf':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.pdf'):
                                            found_name_matches.append(entity)
                            case 'doc':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.docx'):
                                            found_name_matches.append(entity)
                            case 'shp':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.shp'):
                                            found_name_matches.append(entity)
                            case 'gdb':
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity.lower().endswith('.gdb'):
                                            found_name_matches.append(entity)
                            case 'img':
                                temp_extensions = tuple(self.accepted_image_extensions)
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        for extension in temp_extensions:
                                            if entity.lower().endswith(extension):
                                                found_name_matches.append(entity)
                                                break
                                del temp_extensions
                            case 'alia':
                                temp_extensions = tuple(list(self.image_types) + ['txt','pdf','docx','shp','gdb'])
                                with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        for extension in temp_extensions:
                                            if not entity.lower()[entity.rfind(".")+1:].endswith(extension):
                                                found_name_matches.append(entity)
                                                break
                                del temp_extensions
                            case _:
                                if return_tuple:
                                    return ()
                                return None
                        names_found = True
                    elif isinstance(check_type,(set,list,tuple)):
                        check_type = {item.lower() for item in tuple(check_type)}
                        if 'docx' in check_type:
                            check_type.remove('docx')
                            check_type.add('doc')
                        if 'img' in check_type:
                            check_type.remove('img')
                            for extension in self.image_types:
                                check_type.add(extension)
                        irrelevant_extensions = {'txt','gdb','pdf','docx','shp'} + (image_types_set := set(self.image_types))
                        with open(f'{self.db_path}/_terms_searched/{previous_search}.txt',encoding='utf-8') as tf:
                            while True:
                                entity = tf.readline()
                                if not entity:
                                    break
                                entity = decodeZipTxtLine(entity).split('|')[0]
                                if (extension := entity[entity.rfind('.')+1:].lower()) in check_type:
                                    match extension:
                                        case 'txt':
                                            found_name_matches.append(entity)
                                        case 'pdf':
                                            found_name_matches.append(entity)
                                        case 'doc':
                                            found_name_matches.append(entity)
                                        case 'shp':
                                            found_name_matches.append(entity)
                                        case 'gdb':
                                            found_name_matches.append(entity)
                                        case _:
                                            if extension in image_types_set:
                                                found_name_matches.append(entity)
                                            elif not extension in irrelevant_extensions and "alia" in check_type:
                                                found_name_matches.append(entity)
                    elif return_tuple:
                        return ()
                    else:
                        return None
                if contents_found and names_found:
                    break
            if len(found_matches := tuple(set(list(found_matches)+list(found_name_matches)))) and any((contents_found,names_found)):
                if save_results_to_file:
                    genSearchQueryResultFile(found_matches,output_type,output_location,output_name,csv_field_size_limit,csv_delimiter,overwriteOutput,set(self.image_types))
                if return_tuple:
                    return found_matches
                return None

        found_matches = []
        found_name_matches = []
        if tqdm_imported:
            iterator = tqdm(tuple(self.used_names), disable = not terminal_progress_display_enabled, desc = f"Searching for instances of {entry_string}")
        else:
            iterator = tuple(self.used_names)
        if not entity_names_only:
            if not ' ' in entry_string:
                for used_name in iterator:
                    extracted_data = {}
                    with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                        for item in (items := tuple(zf.namelist())):
                            if '/' in item[:-1]:
                                if not (folder_name := item[:item.find("/")]) in extracted_data.keys():
                                    extracted_data[folder_name] = [item[item.find("/")+1:]]
                                else:
                                    extracted_data[folder_name].append(item[item.find("/")+1:])
                        try: del folder_name
                        except NameError: pass
                        if '_alia_dosieroj.txt' in items:
                            with zf.open('_alia_dosieroj.txt') as tf:
                                while True:
                                    entity = tf.readline()
                                    if not entity:
                                        break
                                    if temp_entry_string in getTestName((entity := decodeZipTxtLine(entity).split('|')[0])):
                                        found_name_matches.append(entity)
                        try: del items
                        except NameError: pass
                        for classify in tuple(extracted_data.keys()):
                            if classify == '_txt_files':
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                    if isQueryMatchKether(entry_string,tuple(zf.open(f'_txt_files/{txt_file}').readlines())):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                            elif classify == '_shp_files':
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                    if isQueryMatchDaath(entry_string,f'_shp_files/{txt_file}',zf):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                            elif classify.lower().endswith('_gdb'):
                                found_equal = False
                                if temp_entry_string in getTestName(classify):
                                    found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                for txt_file in extracted_data[classify]:
                                    if isQueryMatchDaath(entry_string,f'{classify}/{txt_file}',zf):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                        break
                            elif classify.lower().endswith('_pdf'):
                                if temp_entry_string in getTestName(classify):
                                    found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                if 'image_histogram_data.txt' in extracted_data[classify]:
                                    extracted_data[classify].remove('image_histogram_data.txt')
                                for txt_file in extracted_data[classify]:
                                    if isQueryMatchKether(entry_string,tuple(zf.open(f'{classify}/{txt_file}').readlines())):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                        break
                            elif classify.lower().endswith('_docx'):
                                if temp_entry_string in getTestName(classify):
                                    found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                                if 'image_histogram_data.txt' in extracted_data[classify]:
                                    extracted_data[classify].remove('image_histogram_data.txt')
                                for txt_file in extracted_data[classify]:
                                    if isQueryMatchKether(entry_string,tuple(zf.open(f'{classify}/{txt_file}').readlines())):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                                        break
                            elif classify == '_images':
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_name_matches.append("%s\\%s%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:txt_file.rfind(".")],txt_file[txt_file.rfind("."):]))
                if save_found_matches:
                    if len((found_matches := tuple(sorted(found_matches)))):
                        with open(f'{self.db_path}/_terms_searched/{entry_string}$contents.txt','w',encoding='utf-8') as tf:
                            tf.write(found_matches[0])
                            for n in range(1,len(found_matches)):
                                tf.write(f'\n{found_matches[n]}')
                    else:
                        with open(f'{self.db_path}/_terms_searched/{entry_string}$contents.txt','w',encoding='utf-8') as tf:
                            pass
                    if len((found_name_matches := tuple(sorted(found_name_matches)))):
                        with open(f'{self.db_path}/_terms_searched/{entry_string}$names.txt','w',encoding='utf-8') as tf:
                            tf.write(found_name_matches[0])
                            for n in range(1,len(found_name_matches)):
                                tf.write(f'\n{found_name_matches[n]}')
                    else:
                        with open(f'{self.db_path}/_terms_searched/{entry_string}$names.txt','w',encoding='utf-8') as tf:
                            pass
            else:
                terms = tuple(entry_string.split(' '))
                if save_found_matches:
                    term_memories = {term : [] for term in terms}
                    term_name_memories = {term : [] for term in terms}
                for used_name in iterator:
                    extracted_data = {}
                    with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                        for item in (items := tuple(zf.namelist())):
                            if '/' in item[:-1]:
                                if not (folder_name := item[:item.find("/")]) in extracted_data.keys(): extracted_data[folder_name] = [item[item.find("/")+1:]]
                                else: extracted_data[folder_name].append(item[item.find("/")+1:])
                        try: del folder_name
                        except NameError: pass
                        if '_alia_dosieroj.txt' in items:
                            with zf.open(f'_alia_dosieroj.txt') as tf:
                                while True:
                                    entity = tf.readline()
                                    if not entity:
                                        break
                                    entity = decodeZipTxtLine(entity).split('|')[0]
                                    if temp_entry_string in (test_name := getTestName(entity)):
                                        found_name_matches.append("%s\\%s" % (self.path_pointer[used_name].replace('/','\\'),entity))
                                    for term in terms:
                                        if term in test_name:
                                            term_name_memories[term].append("%s\\%s" % (self.path_pointer[used_name].replace('/','\\'),entity))
                        try: del items
                        except NameError: pass
                        for classify in tuple(extracted_data.keys()):
                            if classify == '_txt_files':
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                    if isQueryMatchGewurah(entry_string,(txt_lines := tuple(zf.open(f'_txt_files/{txt_file}').readlines())),max_line_concat):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                    if save_found_matches:
                                        for term in terms:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_name_memories.append("%s\\%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file))
                                            if isQueryMatchKether(term,txt_lines):
                                                term_memories[term].append("%s\\%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file))
                                    del txt_lines
                            elif classify == '_shp_files':
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                    if isQueryMatchChochmah(entry_string,f'_shp_files/{txt_file}',zf):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                    if save_found_matches:
                                        for term in terms:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_name_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                            if isQueryMatchDaath(term,f'_shp_files/{txt_file}',zf):
                                                term_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                            elif classify.lower().endswith('_gdb'):
                                if temp_entry_string in getTestName(classify):
                                    found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                for txt_file in extracted_data[classify]:
                                    if isQueryMatchChochmah(entry_string,f'{classify}/{txt_file}',zf):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                        break
                                if save_found_matches:
                                    for term in terms:
                                        for txt_file in extracted_data[classify]:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_name_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                            if isQueryMatchDaath(term,f'{classify}/{txt_file}',zf):
                                                term_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                            elif classify.lower().endswith('_pdf'):
                                if temp_entry_string in getTestName(classify):
                                    found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                if 'image_histogram_data.txt' in extracted_data[classify]:
                                    extracted_data[classify].remove('image_histogram_data.txt')
                                for txt_file in extracted_data[classify]:
                                    if isQueryMatchGewurah(entry_string,tuple(zf.open(f'{classify}/{txt_file}').readlines()),max_line_concat):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                        break
                                if save_found_matches:
                                    for term in terms:
                                        for txt_file in extracted_data[classify]:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_name_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                            if isQueryMatchKether(term,tuple(zf.open(f'{classify}/{txt_file}').readlines())):
                                                term_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                            elif classify.lower().endswith('_docx'):
                                if temp_entry_string in getTestName(classify):
                                    found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                                if 'image_histogram_data.txt' in extracted_data[classify]:
                                    extracted_data[classify].remove('image_histogram_data.txt')
                                for txt_file in extracted_data[classify]:
                                    if isQueryMatchGewurah(entry_string,tuple(zf.open(f'{classify}/{txt_file}').readlines()),max_line_concat):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                                        break
                                if save_found_matches:
                                    for term in terms:
                                        for txt_file in extracted_data[classify]:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_name_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                                            if isQueryMatchKether(term,tuple(zf.open(f'{classify}/{txt_file}').readlines())):
                                                term_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                            elif classify == '_images':
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in (test_name := getTestName(txt_file)):
                                        found_name_matches.append("%s\\%s%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:txt_file.rfind(".")],txt_file[txt_file.rfind("."):]))
                                    if save_found_matches:
                                        for term in terms:
                                            if term.replace('_',' ') in test_name:
                                                term_name_memories[term].append("%s\\%s%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:txt_file.rfind(".")],txt_file[txt_file.rfind("."):]))
                if save_found_matches:
                    for term in terms:
                        if not len(term_memories[term]):
                            del term_memories[term]
                            with open(f'{self.db_path}/_terms_searched/{term}$contents.txt','w',encoding='utf-8') as tf:
                                pass
                        else:
                            term_memories[term] = tuple(sorted(term_memories[term]))
                            with open(f'{self.db_path}/_terms_searched/{term}$contents.txt','w',encoding='utf-8') as tf:
                                tf.write(term_memories[term][0])
                                for n in range(1,len(term_memories[term])):
                                    tf.write(f'\n{term_memories[term][n]}')
                        if not len(term_name_memories[term]):
                            del term_name_memories[term]
                            with open(f'{self.db_path}/_terms_searched/{term}$names.txt','w',encoding='utf-8') as tf:
                                pass
                        else:
                            term_name_memories[term] = tuple(sorted(term_name_memories[term]))
                            with open(f'{self.db_path}/_terms_searched/{term}$names.txt','w',encoding='utf-8') as tf:
                                tf.write(term_name_memories[term][0])
                                for n in range(1,len(term_name_memories[term])):
                                    tf.write(f'\n{term_name_memories[term][n]}')
        else:
            if not ' ' in entry_string:
                for used_name in iterator:
                    extracted_data = {}
                    with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                        for item in (items := tuple(zf.namelist())):
                            if '/' in item[:-1]:
                                if not (folder_name := item[:item.find("/")]) in extracted_data.keys():
                                    extracted_data[folder_name] = [item[item.find("/")+1:]]
                                else:
                                    extracted_data[folder_name].append(item[item.find("/")+1:])
                        try: del folder_name
                        except NameError: pass
                        if '_alia_dosieroj.txt' in items:
                            if '_alia_dosieroj.txt' in items:
                                with zf.open(f'_alia_dosieroj.txt',encoding='utf-8') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        if temp_entry_string in (test_name := getTestName((entity := decodeZipTxtLine(entity).split('|')[0]))):
                                            found_name_matches.append("%s\\%s" % (self.path_pointer[used_name].replace('/','\\'),entity))
                        try: del items
                        except NameError: pass
                        try: del entity ; del test_name
                        except NameError: pass
                        for classify in tuple(extracted_data.keys()):
                            if classify == '_txt_files':
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                            elif classify == '_shp_files':
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                            elif classify.lower().endswith('_gdb'):
                                found_equal = False
                                if temp_entry_string in getTestName(classify):
                                    found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                            elif classify.lower().endswith('_pdf'):
                                if temp_entry_string in getTestName(classify):
                                    found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                            elif classify.lower().endswith('_docx'):
                                if temp_entry_string in getTestName(classify):
                                    found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                            elif classify == '_images':
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_name_matches.append("%s\\%s%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:txt_file.rfind(".")],txt_file[txt_file.rfind("."):]))
                if save_found_matches:
                    if len((found_name_matches := tuple(sorted(found_name_matches)))):
                        with open(f'{self.db_path}/_terms_searched/{entry_string}$names.txt','w',encoding='utf-8') as tf:
                            tf.write(found_name_matches[0])
                            for n in range(1,len(found_name_matches)):
                                tf.write(f'\n{found_name_matches[n]}')
                    else:
                        with open(f'{self.db_path}/_terms_searched/{entry_string}$names.txt','w',encoding='utf-8') as tf:
                            pass
            else:
                terms = tuple(entry_string.split(' '))
                if save_found_matches:
                    term_memories = {term : [] for term in terms}
                    term_name_memories = {term : [] for term in terms}
                for used_name in iterator:
                    extracted_data = {}
                    with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                        for item in (items := tuple(zf.namelist())):
                            if '/' in item[:-1]:
                                if not (folder_name := item[:item.find("/")]) in extracted_data.keys(): extracted_data[folder_name] = [item[item.find("/")+1:]]
                                else: extracted_data[folder_name].append(item[item.find("/")+1:])
                        try: del folder_name
                        except NameError: pass
                        if '_alia_dosieroj.txt' in items:
                            with zf.open(f'_alia_dosieroj.txt',encoding='utf-8') as tf:
                                while True:
                                    entity = tf.readline()
                                    if not entity:
                                        break
                                    if temp_entry_string in (test_name := getTestName((entity := decodeZipTxtLine(entity).split('|')[0]))):
                                        found_name_matches.append("%s\\%s" % (self.path_pointer[used_name].replace('/','\\'),entity))
                                    for term in terms:
                                        if term in test_name:
                                            term_name_memories[term].append("%s\\%s" % (self.path_pointer[used_name].replace('/','\\'),entity))
                        try: del items
                        except NameError: pass
                        try: del entity ; del test_name
                        except NameError: pass
                        for classify in tuple(extracted_data.keys()):
                            if classify == '_txt_files':
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                    if save_found_matches:
                                        for term in terms:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_name_memories.append("%s\\%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file))
                                    del txt_lines
                            elif classify == '_shp_files':
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                    if save_found_matches:
                                        for term in terms:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_name_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                            elif classify.lower().endswith('_gdb'):
                                if temp_entry_string in getTestName(classify):
                                    found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                if save_found_matches:
                                    for term in terms:
                                        for txt_file in extracted_data[classify]:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_name_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                            elif classify.lower().endswith('_pdf'):
                                if temp_entry_string in getTestName(classify):
                                    found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                if save_found_matches:
                                    for term in terms:
                                        for txt_file in extracted_data[classify]:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_name_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                            elif classify.lower().endswith('_docx'):
                                if temp_entry_string in getTestName(classify):
                                    found_name_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                                if save_found_matches:
                                    for term in terms:
                                        for txt_file in extracted_data[classify]:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_name_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                            elif classify == '_images':
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in (test_name := getTestName(txt_file)):
                                        found_name_matches.append("%s\\%s%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:txt_file.rfind(".")],txt_file[txt_file.rfind("."):]))
                                    if save_found_matches:
                                        for term in terms:
                                            if term.replace('_',' ') in test_name:
                                                term_name_memories[term].append("%s\\%s%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:txt_file.rfind(".")],txt_file[txt_file.rfind("."):]))
                if save_found_matches:
                    for term in terms:
                        if not len(term_name_memories[term]):
                            del term_name_memories[term]
                            with open(f'{self.db_path}/_terms_searched/{term}$names.txt','w',encoding='utf-8') as tf:
                                pass
                        else:
                            term_name_memories[term] = tuple(sorted(term_name_memories[term]))
                            with open(f'{self.db_path}/_terms_searched/{term}$names.txt','w',encoding='utf-8') as tf:
                                tf.write(term_name_memories[term][0])
                                for n in range(1,len(term_name_memories[term])):
                                    tf.write(f'\n{term_name_memories[term][n]}')

        try: del extracted_data
        except NameError: pass
        try: del extracted_data_keys
        except NameError: pass
        try: del txt_lines
        except NameError: pass

        if isinstance(check_type,str):
            check_type = check_type.lower()
            match check_type:
                case 'all' | 'any' | 'every':
                    pass
                case 'txt':
                    if entity_names_only:
                        found_matches = tuple([found_name_match for found_name_match in found_name_matches if found_name_match.lower().endswith('.txt')])
                    else:
                        found_matches = tuple([found_match for found_match in found_matches if found_match.lower().endswith('.txt')] + [found_name_match for found_name_match in found_name_matches if found_name_match.lower().endswith('.txt')])
                case 'pdf':
                    if entity_names_only:
                        found_matches = tuple([found_name_match for found_name_match in found_name_matches if found_name_match.lower().endswith('.pdf')])
                    else:
                        found_matches = tuple([found_match for found_match in found_matches if found_match.lower().endswith('.pdf')] + [found_name_match for found_name_match in found_name_matches if found_name_match.lower().endswith('.pdf')])
                case 'gdb':
                    if entity_names_only:
                        found_matches = tuple([found_name_match for found_name_match in found_name_matches if found_name_match.lower().endswith('.gdb')])
                    else:
                        found_matches = tuple([found_match for found_match in found_matches if found_match.lower().endswith('.gdb')] + [found_name_match for found_name_match in found_name_matches if found_name_match.lower().endswith('.gdb')])
                case 'shp':
                    if entity_names_only:
                        found_matches = tuple([found_name_match for found_name_match in found_name_matches if found_name_match.lower().endswith('.shp')])
                    else:
                        found_matches = tuple([found_match for found_match in found_matches if found_match.lower().endswith('.shp')] + [found_name_match for found_name_match in found_name_matches if found_name_match.lower().endswith('.shp')])
                case 'doc':
                    if entity_names_only:
                        found_matches = tuple([found_name_match for found_name_match in found_name_matches if found_name_match.lower().endswith('.docx')])
                    else:
                        found_matches = tuple([found_match for found_match in found_matches if found_match.lower().endswith('.docx')] + [found_name_match for found_name_match in found_name_matches if found_name_match.lower().endswith('.docx')])
                case 'img':
                    if not include_entity_name:
                        if return_tuple:
                            return ()
                        return None
                    check_type = set(self.image_types)
                    found_matches = tuple([found_name_match for found_name_match in found_name_matches if found_name_match.lower()[found_name_match.rfind('.'):] in check_type])
                case _:
                    if not include_entity_name:
                        if return_tuple:
                            return ()
                        return None
                    irrelevant_extensions = {'txt','pdf','docx','shp','gdb'} + set(self.image_types)
                    found_matches = tuple([found_name_match for found_name_match in found_name_matches if found_name_match.lower()[found_name_match.rfind(".")+1:]])
            if not len(found_matches):
                if return_tuple:
                    return ()
                return None
        elif isinstance(check_type,(tuple,list,set)):
            check_type = {item.lower().replace(' ','') for item in tuple(check_type)}
            if 'img' in check_type:
                for img_type in self.image_types:
                    check_type.add(img_type)
                check_type.remove('img')
            if 'doc' in check_type:
                check_type.remove('doc')
                check_type.add('docx')
            if entity_names_only:
                if 'alia' in check_type:
                    check_type.remove('alia')
                    irrelevant_extensions = {'txt','pdf','docx','shp','gdb'} + set(self.image_types)
                    alia_check_extensions = {irrelevant_extension for irrelevant_extension in tuple(irrelevant_extensions) if not irrelevant_extension in check_type}
                    found_matches = []
                    for found_name_match in found_name_matches:
                        if (extension := found_name_match[found_name_match.rfind('.')+1:]) in check_type or extension in alia_check_extensions:
                            found_matches.append(found_name_match)
                else:
                    found_matches = tuple([found_name_match for found_name_match in found_name_matches if found_name_match.lower()[found_name_match.rfind('.')+1:] in check_type])
            elif include_entity_name:
                if 'alia' in check_type:
                    check_type.remove('alia')
                    irrelevant_extensions = {'txt','pdf','docx','shp','gdb'} + set(self.image_types)
                    alia_check_extensions = {irrelevant_extension for irrelevant_extension in tuple(irrelevant_extensions) if not irrelevant_extension in check_type}
                    neo_found_matches = []
                    for found_match in tuple(set(list(found_name_matches)+list(found_matches))):
                        if (extension := found_match[found_match.rfind('.')+1:]) in check_type or extension in alia_check_extensions:
                            neo_found_matches.append(found_match)
                    found_matches = tuple(neo_found_matches)
                    del neo_found_matches
                else:
                    found_matches = tuple([found_name_match for found_name_match in found_name_matches if found_name_match.lower()[found_name_match.rfind('.')+1:] in check_type] + [found_match for found_match in found_matches if found_match.lower()[found_match.rfind('.')+1:] in check_type])
            else:
                if 'alia' in check_type:
                    check_type.remove('alia')
                    irrelevant_extensions = {'txt','pdf','docx','shp','gdb'} + set(self.image_types)
                    alia_check_extensions = {irrelevant_extension for irrelevant_extension in tuple(irrelevant_extensions) if not irrelevant_extension in check_type}
                    neo_found_matches = []
                    for found_match in found_matches:
                        if (extension := found_match[found_match.rfind('.')+1:]) in check_type or extension in alia_check_extensions:
                            neo_found_matches.append(found_match)
                    found_matches = tuple(neo_found_matches)
                    del neo_found_matches
                else:
                    found_matches = tuple([found_match for found_match in found_matches if found_match.lower()[found_match.rfind('.')+1:] in check_type])
            if not len(found_matches):
                if return_tuple:
                    return ()
                return None
        else:
            if return_tuple:
                return ()
            return None

        try: del found_name_matches
        except NameError: pass

        # Account for not selecting all on first run
        if save_results_to_file:
            genSearchQueryResultFile(found_matches,output_file_type,output_location,output_name,csv_field_size_limit,csv_delimiter,overwrite_existing_output,set(self.image_types))

        if self.chloe_vocalization:
            playChloeHappy(self.wakeup_buffer[0],self.wakeup_buffer[1])

        if return_tuple:
            return found_matches

        return None


    def clearSearchQueryMemory(self) -> None:

        if exists((search_results_folder := f'{self.db_path}/_terms_searched')):
            rmtree(search_results_folder)
            mkdir(search_results_folder)

        return None


    def findAllDuplicates(self, include_other_entities : bool = False, return_tuple : bool = False, save_results_to_file : bool = False, output_file_type : str = 'excel', output_location : str | None = None, output_name : str | None = None, overwrite_existing_output : bool = False, csv_field_size_limit : int = 131_072, csv_delimiter : str = ',', terminal_progress_display_enabled : bool = False) -> None | tuple[tuple]:
        '''
        Check items of matching type against each other and can optionally be
        outputted and viewed by the user.
        '''

        output_file_type = output_file_type.lower().strip()
        output_file_type = output_file_type.replace(' ','')

        if not output_file_type in {'excel','xlsx','csv','text','txt'}:
            output_file_type = 'excel'

        checked = set() ; found_duplicates = []
        num_dbs = len((db_names := tuple(self.used_names)))
        if tqdm_imported:
            if terminal_progress_display_enabled:
                sys_clear()
            iterator = tqdm(range(num_dbs-1), disable = not terminal_progress_display_enabled, desc = f"Checking for duplicates in {self.database_name}")
        else:
            iterator = range(num_dbs-1)
        # This enables greater redundancy reduction.
        type_checker = {"TXT":set(),"IMG":set(),"SHP":set(),"DOC":set(),"PDF":set(),"GDB":set()}
        for db_name in db_names:
            with ZipFile(f"{self.db_path}/{db_name}.zip") as zf:
                if '_metadata.txt' in (metadata_files := [item for item in tuple(zf.namelist()) if not '/' in item and item.endswith('_metadata.txt')]):
                    with zf.open('_metadata.txt') as tf:
                        while True:
                            line = tf.readline()
                            if not line:
                                break
                            line = decodeZipTxtLine(line).split('|')
                            type_checker[line[1]].add(db_name)
                    try: del line
                    except NameError: pass
                    metadata_files.remove('_metadata.txt')
                if len((metadata_files := tuple(metadata_files))):
                    for metadata_file in metadata_files:
                        if metadata_file.lower().endswith('_gdb_metadata.txt'):
                            type_checker['GDB'].add(db_name)
                            break
        try: del metadata_files
        except NameError: pass
        # This enables even greater redundancy reduction.
        line_num_checker = {}
        for db_name in db_names:
            with ZipFile(f"{self.db_path}/{db_name}.zip") as zf:
                if '_metadata.txt' in (metadata_files := [item for item in tuple(zf.namelist()) if not '/' in item and item.endswith('_metadata.txt')]):
                    with zf.open('_metadata.txt') as tf:
                        while True:
                            line = tf.readline()
                            if not line:
                                break
                            line = decodeZipTxtLine(line).split('|')
                            if line[1] in ('PDF','DOC'):
                                if not f'{line[5]}|{line[6]}|{line[1]}' in line_num_checker.keys():
                                    line_num_checker[f'{line[5]}|{line[6]}|{line[1]}'] = {db_name}
                                else:
                                    line_num_checker[f'{line[5]}|{line[6]}|{line[1]}'].add(db_name)
                            else:
                                if not f"{line[5]}|{line[1]}" in line_num_checker.keys():
                                    line_num_checker[f"{line[5]}|{line[1]}"] = {db_name}
                                else:
                                    line_num_checker[f"{line[5]}|{line[1]}"].add(db_name)
                    try: del line
                    except NameError: pass
                    metadata_files.remove('_metadata.txt')
                for metadata_file in (metadata_files := tuple(metadata_files)):
                    if metadata_file.lower().endswith('_gdb_metadata.txt'):
                        if (num_id := "|".join([gdb_item[gdb_item.rfind(" ")+1:] for gdb_item in tuple(decodeZipTxtLine(zf.open(metadata_file).readline()).split('|'))])) in line_num_checker.keys():
                            line_num_checker[num_id].add(db_name)
                        else:
                            line_num_checker[num_id] = {db_name}
        for a in iterator:
            current_db_name = db_names[a]
            current_entities = {} ; img_firstlines = {}
            with ZipFile(f'{self.db_path}/{current_db_name}.zip') as zf:
                if '_metadata.txt' in (metadata_files := [item for item in tuple(zf.namelist()) if not '/' in item and item.endswith("_metadata.txt")]):
                    with zf.open("_metadata.txt") as tf:
                        while True:
                            entity = tf.readline()
                            if not entity:
                                break
                            entity = decodeZipTxtLine(entity).split('|')
                            if f'{current_db_name}|{entity[0]}' in checked:
                                checked.remove(f'{current_db_name}|{entity[0]}')
                                continue
                            if entity[1] in current_entities.keys():
                                if entity[1] in ('PDF','DOC'):
                                    if f'{entity[5]}|{entity[6]}' in current_entities[entity[1]].keys():
                                        current_entities[entity[1]][f'{entity[5]}|{entity[6]}'].append(entity[0])
                                    else:
                                        current_entities[entity[1]] = {f'{entity[5]}|{entity[6]}':[entity[0]]}
                                elif entity[5] in current_entities[entity[1]].keys():
                                    current_entities[entity[1]][entity[5]].append(entity[0])
                                else:
                                    current_entities[entity[1]] = {entity[5]:[entity[0]]}
                            elif entity[1] in ('PDF','DOC'):
                                current_entities[entity[1]] = {f'{entity[5]}|{entity[6]}':[entity[0]]}
                            else:
                                current_entities[entity[1]] = {entity[5]:[entity[0]]}
                    metadata_files.remove('_metadata.txt')
                if len((metadata_files := tuple(metadata_files))):
                    current_entities['GDB'] = {}
                    for metadata_file in metadata_files:
                        if metadata_file.lower().endswith('_gdb_metadata.txt'):
                            current_entities['GDB'][metadata_file[:metadata_file.rfind('_')]] = {item[:item.rfind(" ")] : item[item.rfind(' ')+1:] for item in decodeZipTxtLine(zf.open(metadata_file).readline()).split('|')}
                    if len(current_entities['GDB'].keys()):
                        del current_entities['GDB']
                if 'IMG' in current_entities.keys():
                    with zf.open('_firstline_image_files.txt') as tf:
                        while True:
                            line = tf.readline()
                            if not line:
                                break
                            line = decodeZipTxtLine(line)
                            img_firstlines[line[:line.rfind(' ')]] = line[line.rfind(' ')+1:]
                try: del metadata_files
                except NameError: pass
                for current_entity_type in tuple(current_entities.keys()):
                    if current_entity_type == 'GDB':
                        num_current_gdbs = len((current_gdbs := tuple(current_entities[current_entity_type].keys())))
                        for b in range(num_current_gdbs-1):
                            if f"{current_db_name}|{current_gdbs[b]}" in checked:
                                checked.remove(f'{current_db_name}|{current_gdbs[b]}')
                                continue
                            current_gdb_num_id = '|'.join([current_entities[current_entity_type][current_gdbs[b]][gdb_item] for gdb_item in tuple(current_entities[current_entity_type][current_gdbs[b]].keys())])
                            current_gdb_name_id = '|'.join([gdb_item for gdb_item in tuple(current_entities[current_entity_type][current_gdbs[b]].keys())])
                            found_duplicates.append([f'{current_db_name}|{current_gdbs[b]}'])
                            checked.add(f'{current_db_name}|{current_gdbs[b]}')
                            for c in range(b+1,num_current_gdbs):
                                if f'{current_db_name}|{current_gdbs[c]}' in checked or current_gdb_num_id != '|'.join([current_entities[current_entity_type][current_gdbs[c]][gdb_item] for gdb_item in tuple(current_entities[current_entity_type][current_gdbs[c]].keys())]) or current_gdb_name_id != '|'.join([gdb_item for gdb_item in tuple(current_entities[current_entity_type][current_gdbs[c]].keys())]):
                                    continue
                                duplicate_match = True
                                for gdb_item in tuple(current_gdb_name_id.split('|')):
                                    current_lines = []
                                    with zf.open(f"{current_gdbs[b]}/{gdb_item}.txt") as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            current_lines.append(decodeZipTxtLine(line))
                                    num_lines = len((current_lines := tuple(current_lines)))
                                    other_lines = []
                                    with zf.open(f"{current_gdbs[c]}/{gdb_item}.txt") as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            other_lines.append(decodeZipTxtLine(line))
                                    try: del line
                                    except NameError: pass
                                    other_lines = tuple(other_lines)
                                    for d in range(num_lines):
                                        if current_lines[d] != other_lines[d]:
                                            duplicate_match = False
                                            break
                                if duplicate_match:
                                    found_duplicates[-1].append(f'{current_db_name}|{current_gdbs[c]}')
                                    checked.add(f'{current_db_name}|{current_gdbs[c]}')
                            for c in range(a+1,num_dbs):
                                if not (other_db_name := db_names[c]) in type_checker['GDB'] or not other_db_name in line_num_checker[current_gdb_num_id]:
                                    continue
                                other_entities = {}
                                with ZipFile(f"{self.db_path}/{other_db_name}.zip") as zf2:
                                    if '_metadata.txt' in (metadata_files := [item for item in tuple(zf2.namelist()) if not '/' in item and item.endswith("_metadata.txt")]):
                                        metadata_files.remove('_metadata.txt')
                                    if len((metadata_files := tuple(metadata_files))):
                                        for metadata_file in metadata_files:
                                            if not metadata_file.lower().endswith('_gdb_metadata.txt'):
                                                continue
                                            current_gdb = metadata_file[:metadata_file.rfind('_')]
                                            if not f'{other_db_name}|{current_gdb}' in checked:
                                                other_entities[current_gdb] = {item[:item.rfind(" ")] : item[item.rfind(" ")+1:] for item in decodeZipTxtLine(zf2.open(metadata_file).readline()).split('|')}
                                try: del metadata_files
                                except NameError: pass
                                try: del current_gdb
                                except NameError: pass
                                for other_entity in tuple(other_entities.keys()):
                                    other_gdb_num_id = '|'.join([other_entities[other_entity][item] for item in other_entities[other_entity].keys()])
                                    other_gdb_name_id = '|'.join([item for item in other_entities[other_entity].keys()])
                                    if other_gdb_num_id == current_gdb_num_id and other_gdb_name_id == current_gdb_name_id:
                                        duplicate_match = True
                                        for gdb_item in tuple(other_gdb_name_id.split('|')):
                                            current_lines = []
                                            with zf.open(f'{current_gdbs[b]}/{gdb_item}.txt') as tf:
                                                while True:
                                                    line = tf.readline()
                                                    if not line:
                                                        break
                                                    current_lines.append(line)
                                            num_lines = len((current_lines := tuple(current_lines)))
                                            other_lines = []
                                            with ZipFile(f'{self.db_path}/{other_db_name}.zip') as zf2:
                                                with zf2.open(f'{other_entity}/{gdb_item}.txt') as tf:
                                                    while True:
                                                        line = tf.readline()
                                                        if not line:
                                                            break
                                                        other_lines.append(line)
                                            other_lines = tuple(other_lines)
                                            for d in range(num_lines):
                                                if current_lines[d] != other_lines[d]:
                                                    duplicate_match = False
                                                    break
                                            if not duplicate_match:
                                                break
                                        if duplicate_match:
                                            found_duplicates[-1].append(f'{other_db_name}|{other_entity}')
                                            checked.add(f'{other_db_name}|{other_entity}')
                            if len(found_duplicates[-1]) == 1:
                                del found_duplicates[-1]
                            else:
                                found_duplicates[-1] = tuple(found_duplicates[-1])
                            for type_shorthand in type_checker.keys():
                                if current_db_name in type_checker[type_shorthand]:
                                    type_checker[type_shorthand].remove(current_db_name)
                        continue
                    nums = tuple(current_entities[current_entity_type].keys())
                    for b in range(len(nums)):
                        num_items = len((items := tuple(current_entities[current_entity_type][nums[b]])))
                        for c in range(num_items-1):
                            if f'{current_db_name}|{items[c]}' in checked:
                                checked.remove(f'{current_db_name}|{items[c]}')
                                continue
                            found_duplicates.append([f'{current_db_name}|{items[c]}'])
                            checked.add(f'{current_db_name}|{items[c]}')
                            match current_entity_type:
                                case 'TXT':
                                    current_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'_txt_files/{items[c]}.txt').readlines())])
                                    current_line_count = int(nums[b])
                                    for d in range(c+1,num_items):
                                        if f'{current_db_name}|{items[d]}' in checked:
                                            checked.remove(f'{current_db_name}|{items[d]}')
                                            continue
                                        other_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'_txt_files/{items[d]}.txt').readlines())])
                                        duplicate_match = True
                                        for e in range(current_line_count):
                                            if current_lines[e] != other_lines[e]:
                                                duplicate_match = False
                                                break
                                        del other_lines
                                        if duplicate_match:
                                            found_duplicates[-1].append(f'{current_db_name}|{items[d]}')
                                            checked.add(f'{current_db_name}|{items[d]}')
                                    for d in range(a+1,num_dbs):
                                        relevant_entities = []
                                        if not (other_db_name := db_names[d]) in type_checker['TXT'] or not other_db_name in line_num_checker[f'{current_line_count}|TXT']:
                                            continue
                                        line_num_checker[f'{current_line_count}|TXT'].remove(other_db_name)
                                        with ZipFile(f'{self.db_path}/{other_db_name}.zip') as zf2:
                                            if not '_metadata.txt' in set(zf2.namelist()):
                                                continue
                                            with zf2.open('_metadata.txt') as tf:
                                                while True:
                                                    line = tf.readline()
                                                    if not line:
                                                        break
                                                    line = tuple(decodeZipTxtLine(line).split('|'))
                                                    if line[1] == 'TXT':
                                                        if int(line[5]) == current_line_count:
                                                            if not f"{other_db_name}|{line[0]}" in checked:
                                                                relevant_entities.append(line[0])
                                            for relevant_entity in (relevant_entities := tuple(relevant_entities)):
                                                other_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf2.open(f'_txt_files/{relevant_entity}.txt').readlines())])
                                                duplicate_match = True
                                                for f in range(current_line_count):
                                                    if current_lines[f] != other_lines[f]:
                                                        duplicate_match = False
                                                        break
                                                del other_lines
                                                if duplicate_match:
                                                    found_duplicates[-1].append(f'{other_db_name}|{relevant_entity}')
                                                    checked.add(f'{other_db_name}|{relevant_entity}')
                                case 'IMG':
                                    current_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'_images/{items[c]}.txt').readlines())])
                                    current_line_count = int(nums[b])
                                    current_firstline = img_firstlines[items[c]]
                                    for d in range(c+1,num_items):
                                        if current_firstline != img_firstlines[items[d]]:
                                            continue
                                        other_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'_images/{items[d]}.txt').readlines())])
                                        duplicate_match = True
                                        for e in range(current_line_count):
                                            if current_lines[e] != other_lines[e]:
                                                duplicate_match = False
                                                break
                                        del other_lines
                                        if duplicate_match:
                                            found_duplicates[-1].append(f'{current_db_name}|{items[d]}')
                                            checked.add(f'{current_db_name}|{items[d]}')
                                    for d in range(a+1,num_dbs):
                                        relevant_entities = []
                                        if not (other_db_name := db_names[d]) in type_checker['IMG'] or not other_db_name in line_num_checker[f'{current_line_count}|IMG']:
                                            continue
                                        line_num_checker[f'{current_line_count}|IMG'].remove(other_db_name)
                                        other_img_firstlines = {}
                                        with ZipFile(f'{self.db_path}/{other_db_name}.zip') as zf2:
                                            if not '_metadata.txt' in set(zf2.namelist()):
                                                continue
                                            with zf2.open('_firstline_image_files.txt') as tf:
                                                while True:
                                                    line = tf.readline()
                                                    if not line:
                                                        break
                                                    line = decodeZipTxtLine(line)
                                                    other_img_firstlines[line[:line.rfind(' ')]] = line[line.rfind(' ')+1:]
                                            with zf2.open('_metadata.txt') as tf:
                                                while True:
                                                    line = tf.readline()
                                                    if not line:
                                                        break
                                                    line = tuple(decodeZipTxtLine(line).split('|'))
                                                    if line[1] == 'IMG':
                                                        if other_img_firstlines[line[0]] == current_firstline:
                                                            if int(line[5]) == current_line_count:
                                                                if not f"{other_db_name}|{line[0]}" in checked:
                                                                    relevant_entities.append(line[0])
                                            try: del other_img_firstlines
                                            except NameError: pass
                                            for relevant_entity in (relevant_entities := tuple(relevant_entities)):
                                                other_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf2.open(f'_images/{relevant_entity}.txt').readlines())])
                                                duplicate_match = True
                                                for f in range(current_line_count):
                                                    if current_lines[f] != other_lines[f]:
                                                        duplicate_match = False
                                                        break
                                                del other_lines
                                                if duplicate_match:
                                                    found_duplicates[-1].append(f'{other_db_name}|{relevant_entity}')
                                                    checked.add(f'{other_db_name}|{relevant_entity}')
                                case 'SHP':
                                    current_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'_shp_files/{items[c]}.txt').readlines())])
                                    current_line_count = int(nums[b])
                                    for d in range(c+1,num_items):
                                        if f'{current_db_name}|{items[d]}' in checked:
                                            checked.remove(f'{current_db_name}|{items[d]}')
                                            continue
                                        other_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'_shp_files/{items[d]}.txt').readlines())])
                                        duplicate_match = True
                                        for e in range(current_line_count):
                                            if current_lines[e] != other_lines[e]:
                                                duplicate_match = False
                                                break
                                        del other_lines
                                        if duplicate_match:
                                            found_duplicates[-1].append(f'{current_db_name}|{items[d]}')
                                            checked.add(f'{current_db_name}|{items[d]}')
                                        for e in range(a+1,num_dbs):
                                            relevant_entities = []
                                            if not (other_db_name := db_names[e]) in type_checker['SHP'] or not other_db_name in line_num_checker[f'{current_line_count}|SHP']:
                                                continue
                                            line_num_checker[f'{current_line_count}|SHP'].remove(other_db_name)
                                            with ZipFile(f'{self.db_path}/{other_db_name}.zip') as zf2:
                                                if not '_metadata.txt' in set(zf2.namelist()):
                                                    continue
                                                with zf2.open('_metadata.txt') as tf:
                                                    while True:
                                                        line = tf.readline()
                                                        if not line:
                                                            break
                                                        line = tuple(decodeZipTxtLine(line).split('|'))
                                                        if line[1] == 'SHP':
                                                            if int(line[5]) == current_line_count:
                                                                if not f"{other_db_name}|{line[0]}" in checked:
                                                                    relevant_entities.append(line[0])
                                                for relevant_entity in (relevant_entities := tuple(relevant_entities)):
                                                    other_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf2.open(f'_shp_files/{relevant_entity}.txt').readlines())])
                                                    duplicate_match = True
                                                    for f in range(current_line_count):
                                                        if current_lines[f] != other_lines[f]:
                                                            duplicate_match = False
                                                            break
                                                    del other_lines
                                                    if duplicate_match:
                                                        found_duplicates[-1].append(f'{other_db_name}|{relevant_entity}')
                                                        checked.add(f'{other_db_name}|{relevant_entity}')
                                case 'DOC':
                                    current_lines = [] ; current_line_count = []
                                    if nums[b][:nums[b].find('|')] == '0':
                                        current_lines.append(None)
                                        current_line_count.append(0)
                                    else:
                                        current_lines.append(tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'{items[c]}/doc_extracted_text.txt').readlines())]))
                                        current_line_count.append(len(current_lines[0]))
                                    if nums[b][nums[b].find('|')+1:] == '0':
                                        current_lines.append(None)
                                        current_line_count.append(0)
                                    else:
                                        current_lines.append(tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'{items[c]}/image_histogram_data.txt').readlines())]))
                                        current_line_count.append(len(current_lines[1]))
                                    if current_line_count[0] == 0 and current_line_count[1] == 0:
                                        del found_duplicates[-1]
                                        continue
                                    current_lines = tuple(current_lines) ; current_line_count = tuple(current_line_count)
                                    for d in range(c+1,num_items):
                                        if f'{current_db_name}|{items[d]}' in checked:
                                            checked.remove(f'{current_db_name}|{items[d]}')
                                            continue
                                        other_lines = [] ; other_line_count = []
                                        if nums[b][:nums[b].find('|')] == '0':
                                            other_lines.append(None)
                                            other_line_count.append(0)
                                        else:
                                            other_lines.append(tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'{items[d]}/doc_extracted_text.txt').readlines())]))
                                            other_line_count.append(len(other_lines[0]))
                                        if nums[b][nums[b].find('|')+1:] == '0':
                                            other_lines.append(None)
                                            other_line_count.append(0)
                                        else:
                                            other_lines.append(tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'{items[d]}/image_histogram_data.txt').readlines())]))
                                            other_line_count.append(len(other_lines[1]))
                                        duplicate_match = True
                                        for e in range(current_line_count[0]):
                                            if current_lines[0][e] != other_lines[0][e]:
                                                duplicate_match = False
                                                break
                                        if duplicate_match:
                                            for e in range(current_line_count[1]):
                                                if current_lines[1][e] != other_lines[1][e]:
                                                    duplicate_match = False
                                                    break
                                            if duplicate_match:
                                                found_duplicates[-1].append(f'{current_db_name}|{items[d]}')
                                                checked.add(f'{current_db_name}|{items[d]}')
                                    for d in range(a+1,num_dbs):
                                        relevant_entities = []
                                        if not (other_db_name := db_names[d]) in type_checker['DOC'] or not other_db_name in line_num_checker[f'{current_line_count[0]}|{current_line_count[1]}|DOC']:
                                            continue
                                        line_num_checker[f'{current_line_count[0]}|{current_line_count[1]}|DOC'].remove(other_db_name)
                                        with ZipFile(f'{self.db_path}/{other_db_name}.zip') as zf2:
                                            if not '_metadata.txt' in set(zf2.namelist()):
                                                continue
                                            with zf2.open('_metadata.txt') as tf:
                                                while True:
                                                    line = tf.readline()
                                                    if not line:
                                                        break
                                                    line = tuple(decodeZipTxtLine(line).split('|'))
                                                    if line[1] == 'DOC':
                                                        if f"{line[5]}|{line[6]}" == f"{current_line_count[0]}|{current_line_count[1]}":
                                                            if not f"{other_db_name}|{line[0]}" in checked:
                                                                relevant_entities.append(line[0])
                                            for relevant_entity in (relevant_entities := tuple(relevant_entities)):
                                                duplicate_match = True
                                                if current_line_count[0]:
                                                    other_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf2.open(f"{relevant_entity}/doc_extracted_text.txt").readlines())])
                                                    for f in range(current_line_count[0]):
                                                        if current_lines[0][f] != other_lines[f]:
                                                            duplicate_match = False
                                                            break
                                                if not duplicate_match:
                                                    continue
                                                if current_line_count[1]:
                                                    other_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf2.open(f"{relevant_entity}/image_histogram_data.txt").readlines())])
                                                    for f in range(current_line_count[1]):
                                                        if current_lines[1][f] != other_lines[f]:
                                                            duplicate_match = False
                                                            break
                                                if duplicate_match:
                                                    found_duplicates[-1].append(f'{other_db_name}|{relevant_entity}')
                                                    checked.add(f'{other_db_name}|{relevant_entity}')
                                case 'PDF':
                                    current_lines = [] ; current_line_count = []
                                    if nums[b][:nums[b].find('|')] == '0':
                                        current_lines.append(None)
                                        current_line_count.append(0)
                                    else:
                                        current_lines.append(tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'{items[c]}/pdf_extracted_text.txt').readlines())]))
                                        current_line_count.append(len(current_lines[0]))
                                    if nums[b][nums[b].find('|')+1:] == '0':
                                        current_lines.append(None)
                                        current_line_count.append(0)
                                    else:
                                        current_lines.append(tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'{items[c]}/image_histogram_data.txt').readlines())]))
                                        current_line_count.append(len(current_lines[1]))
                                    if current_line_count[0] == 0 and current_line_count[1] == 0:
                                        del found_duplicates[-1]
                                        continue
                                    current_lines = tuple(current_lines) ; current_line_count = tuple(current_line_count)
                                    for d in range(c+1,num_items):
                                        if f'{current_db_name}|{items[d]}' in checked:
                                            checked.remove(f'{current_db_name}|{items[d]}')
                                            continue
                                        other_lines = [] ; other_line_count = []
                                        if nums[b][:nums[b].find('|')] == '0':
                                            other_lines.append(None)
                                            other_line_count.append(0)
                                        else:
                                            other_lines.append(tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'{items[d]}/pdf_extracted_text.txt').readlines())]))
                                            other_line_count.append(len(other_lines[0]))
                                        if nums[b][nums[b].find('|')+1:] == '0':
                                            other_lines.append(None)
                                            other_line_count.append(0)
                                        else:
                                            other_lines.append(tuple([decodeZipTxtLine(line) for line in tuple(zf.open(f'{items[d]}/image_histogram_data.txt').readlines())]))
                                            other_line_count.append(len(other_lines[1]))
                                        duplicate_match = True
                                        for e in range(current_line_count[0]):
                                            if current_lines[0][e] != other_lines[0][e]:
                                                duplicate_match = False
                                                break
                                        if duplicate_match:
                                            for e in range(current_line_count[1]):
                                                if current_lines[1][e] != other_lines[1][e]:
                                                    duplicate_match = False
                                                    break
                                        if duplicate_match:
                                            found_duplicates[-1].append(f'{current_db_name}|{items[d]}')
                                            checked.add(f'{current_db_name}|{items[d]}')
                                    for d in range(a+1,num_dbs):
                                        relevant_entities = []
                                        if not (other_db_name := db_names[d]) in type_checker['PDF'] or not other_db_name in line_num_checker[f'{current_line_count[0]}|{current_line_count[1]}|PDF']:
                                            continue
                                        line_num_checker[f'{current_line_count[0]}|{current_line_count[1]}|PDF'].remove(other_db_name)
                                        with ZipFile(f'{self.db_path}/{other_db_name}.zip') as zf2:
                                            if not '_metadata.txt' in set(zf2.namelist()):
                                                continue
                                            with zf2.open('_metadata.txt') as tf:
                                                while True:
                                                    line = tf.readline()
                                                    if not line:
                                                        break
                                                    line = tuple(decodeZipTxtLine(line).split('|'))
                                                    if line[1] == 'PDF':
                                                        if f"{line[5]}|{line[6]}" == f"{current_line_count[0]}|{current_line_count[1]}":
                                                            if not f"{other_db_name}|{line[0]}" in checked:
                                                                relevant_entities.append(line[0])
                                            for relevant_entity in (relevant_entities := tuple(relevant_entities)):
                                                duplicate_match = True
                                                if current_line_count[0]:
                                                    other_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf2.open(f"{relevant_entity}/pdf_extracted_text.txt").readlines())])
                                                    for f in range(current_line_count[0]):
                                                        if current_lines[0][f] != other_lines[f]:
                                                            duplicate_match = False
                                                            break
                                                if not duplicate_match:
                                                    continue
                                                if current_line_count[1]:
                                                    other_lines = tuple([decodeZipTxtLine(line) for line in tuple(zf2.open(f"{relevant_entity}/image_histogram_data.txt").readlines())])
                                                    for f in range(current_line_count[1]):
                                                        if current_lines[1][f] != other_lines[f]:
                                                            duplicate_match = False
                                                            break
                                                if duplicate_match:
                                                    found_duplicates[-1].append(f'{other_db_name}|{relevant_entity}')
                                                    checked.add(f'{other_db_name}|{relevant_entity}')
                                case _:
                                    # indication of Chloe Felina database being
                                    # tampered
                                    if return_tuple:
                                        return ()
                                    return None
                            if len(found_duplicates[-1]) == 1:
                                del found_duplicates[-1]
                            else:
                                found_duplicates[-1] = tuple(found_duplicates[-1])
                            for type_shorthand in type_checker.keys():
                                if current_db_name in type_checker[type_shorthand]:
                                    type_checker[type_shorthand].remove(current_db_name)
            for item in tuple(checked):
                if item.startswith(f"{current_db_name}|"):
                    checked.remove(item)

        alia_found_duplicates = []

        if include_other_entities:
            checked = set()
            found_extensions = {}
            no_extensions = set()
            for used_name in (aliaj := tuple([used_name for used_name in tuple(self.used_names) if '_alia_dosieroj.txt' in set(ZipFile(f'{self.db_path}/{used_name}.zip').namelist())])):
                with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                    with zf.open('_alia_dosieroj.txt') as tf:
                        found_extensions[used_name] = set()
                        while True:
                            entity = tf.readline()
                            if not entity:
                                break
                            entity = decodeZipTxtLine(line).split('|')[0]
                            if not '.' in entity:
                                no_extensions.add(used_name)
                            else:
                                found_extensions[used_name].add(entity.lower()[entity.rfind('.')+1:])
            num_dbs = len((aliaj := tuple(found_extensions.keys())))
            if tqdm_imported:
                if terminal_progress_display_enabled:
                    sys_clear()
                iterator = tqdm(range(num_dbs-1), disable = not terminal_progress_display_enabled, desc = f"Checking for vague potential duplicates in {self.database_name}")
            else:
                iterator = range(num_dbs-1)
            if num_dbs:
                for a in iterator:
                    del found_extensions[(current_db_name := aliaj[a])]
                    with ZipFile(f'{self.db_path}/{current_db_name}.zip') as zf:
                        extensions_item_date = {}
                        with zf.open('_alia_dosieroj.txt') as tf:
                            while True:
                                line = tf.readline()
                                if not line:
                                    break
                                line = decodeZipTxtLine(line).split('|')
                                if not f"{current_db_name}|{line[0]}" in checked:
                                    if '.' in line[0]:
                                        if not (extension := line[0].lower()[line[0].rfind(".")+1:]) in extensions_item_date.keys():
                                            extensions_item_date[extension] = [(line[0],line[1],line[3])]
                                        else:
                                            extensions_item_date[extension].append((line[0],line[1],line[3]))
                                else:
                                    checked.remove(f'{current_db_name}|{line[0]}')
                    try: del line
                    except NameError: pass
                    if len(extensions_item_date.keys()):
                        for extension in tuple(extensions_item_date.keys()):
                            num_items = len((items := tuple(extensions_item_date[extension])))
                            for b in range(num_items-1):
                                if f'{current_db_name}|{items[b][0]}' in checked:
                                    checked.remove(f'{current_db_name}|{items[b][0]}')
                                    continue
                                alia_found_duplicates.append([f'{current_db_name}|{items[b][0]}'])
                                modified_date = items[b][1]
                                size = items[b][2]
                                for c in range(b+1,num_items):
                                    if not f'{current_db_name}|{items[c][0]}' in checked:
                                        if modified_date == items[c][1]:
                                            if size == items[c][2]:
                                                alia_found_duplicates[-1].append(f'{current_db_name}|{items[c][0]}')
                                                checked.add(f'{current_db_name}|{items[c][0]}')
                                current_extension = items[b][0].lower()[items[b][0].rfind('.')+1:]
                                for c in range(a+1,num_dbs):
                                    if current_extension in found_extensions[(other_db_name := aliaj[c])]:
                                        with ZipFile(f'{self.db_path}/{other_db_name}.zip') as zf:
                                            with zf.open('_alia_dosieroj.txt') as tf:
                                                while True:
                                                    line = tf.readline()
                                                    if not line:
                                                        break
                                                    line = decodeZipTxtLine(line).split('|')
                                                    if not f'{other_db_name}|{line[0]}' in checked:
                                                        if line[0].lower().endswith(f'.{current_extension}'):
                                                            if line[1] == modified_date:
                                                                if line[3] == size:
                                                                    alia_found_duplicates[-1].append(f'{other_db_name}|{line[0]}')
                                                                    checked.add(f'{other_db_name}|{line[0]}')
                                if len((alia_found_duplicates[-1])) == 1:
                                    del alia_found_duplicates[-1]
                                else:
                                    alia_found_duplicates[-1] = tuple(alia_found_duplicates[-1])
                try: del extensions_item_date
                except NameError: pass
            del found_extensions
            num_dbs = len((aliaj := tuple(no_extensions)))
            del no_extensions
            if tqdm_imported:
                if terminal_progress_display_enabled:
                    sys_clear()
                iterator = tqdm(range(num_dbs-1), disable = not terminal_progress_display_enabled, desc = f"Checking for vague potential duplicates in {self.database_name}")
            else:
                iterator = range(num_dbs-1)
            checked = set()
            for a in iterator:
                current_db_name = aliaj[a]
                with ZipFile(f'{self.db_path}/{current_db_name}.zip') as zf:
                    item_date_size = {}
                    with zf.open('_alia_dosieroj.txt') as tf:
                        while True:
                            line = tf.readline()
                            if not line:
                                break
                            line = decodeZipTxtLine(line).split('|')
                            if not f"{current_db_name}|{line[0]}" in checked:
                                if not '.' in line[0]:
                                    item_date_size[line[0]] = (line[1],line[3])
                            else:
                                checked.remove(f'{current_db_name}|{line[0]}')
                try: del line
                except NameError: pass
                if (num_items := len((items := tuple(item_date_size.keys())))):
                    for b in range(num_items-1):
                        if f'{current_db_name}|{items[b]}' in checked:
                            checked.remove(f'{current_db_name}|{items[b]}')
                            continue
                        alia_found_duplicates.append([f'{current_db_name}|{items[b]}'])
                        modified_date = item_date_size[(current_item := items[b])][0]
                        size = item_date_size[current_item][1]
                        for c in range(b+1,num_items):
                            if not f'{current_db_name}|{items[c]}' in checked:
                                if modified_date == item_date_size[items[c]][0]:
                                    if size == item_date_size[items[c]][1]:
                                        alia_found_duplicates[-1].append(f'{current_db_name}|{items[c]}')
                                        checked.add(f'{current_db_name}|{items[c]}')
                        for c in range(a+1,num_dbs):
                            other_db_name = aliaj[c]
                            with ZipFile(f'{self.db_path}/{other_db_name}.zip') as zf:
                                with zf.open('_alia_dosieroj.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        line = decodeZipTxtLine(line).split('|')
                                        if not f'{other_db_name}|{line[0]}' in checked:
                                            if modified_date == line[1]:
                                                if size == line[3]:
                                                    alia_found_duplicates[-1].append(f'{other_db_name}|{line[0]}')
                                                    checked.add(f'{other_db_name}|{line[0]}')
                        if len(alia_found_duplicates[-1]) == 1:
                            del alia_found_duplicates[-1]
                        else:
                            alia_found_duplicates[-1] = tuple(alia_found_duplicates[-1])
            try: del aliaj
            except NameError: pass
            for n in range(len(alia_found_duplicates)):
                alia_found_duplicates[n] = list(alia_found_duplicates[n])
                for x in range(len(alia_found_duplicates[n])):
                    alia_found_duplicates[n][x] = "%s\\%s" % (self.path_pointer[alia_found_duplicates[n][x][:alia_found_duplicates[n][x].find('|')]].replace('/','\\'),alia_found_duplicates[n][x][alia_found_duplicates[n][x].find('|')+1:])
                alia_found_duplicates[n] = tuple(alia_found_duplicates[n])

        if self.chloe_vocalization:
            playChloeHappy(self.wakeup_buffer[0],self.wakeup_buffer[1])

        if return_tuple or save_results_to_file:
            for n in range(len(found_duplicates)):
                found_duplicates[n] = list(found_duplicates[n])
                for x in range(len(found_duplicates[n])):
                    found_duplicates[n][x] = "%s\\%s.%s" % (self.path_pointer[found_duplicates[n][x][:found_duplicates[n][x].find("|")]].replace('/','\\'),found_duplicates[n][x][found_duplicates[n][x].find("|")+1:found_duplicates[n][x].rfind("_")],found_duplicates[n][x][found_duplicates[n][x].rfind("_")+1:])
                found_duplicates[n] = tuple(found_duplicates[n])

            if len((found_duplicates := tuple(found_duplicates + alia_found_duplicates))) and save_results_to_file:
                genDuplicateFinderResultFile(found_duplicates,output_file_type,output_location,output_name,csv_field_size_limit,csv_delimiter,overwrite_existing_output,set(self.image_types))
            if return_tuple:
                return found_duplicates

        return None


    def findEntityDuplicates(self, entity_path : str, return_tuple : bool = False, save_results_to_file : bool = False, terminal_progress_display_enabled : bool = False) -> tuple[str] | None:

        if not exists((entity_path := entity.path.replace('\\','/'))):
            return None

        if not '.' in entity_path[entity_path.rfind('/')+1:]:
            pass
        else:
            pass

        return None


    def compileEntitiesOnTime(self, year : str | int |list | tuple | set, month : str | int | list | tuple | set, day_number : str | int | list | tuple | set, day_of_week : int | str, terminal_progress_display_enabled : bool = False) -> None:

        return None


    def compileEntitiesOnSize(self, compare_sign : str, size_bytes : int, terminal_progress_display_enabled : bool = False) -> None:

        return None


    def compileAllEntities(self, terminal_progress_display_enabled : bool = False) -> None:

        return None


    def getTotalSizeOfActualRefEntities(self, check_type : str | tuple[str] | list[str] | set[str] = 'any', include_other_entities : bool = False, terminal_progress_display_enabled : bool = False) -> int:
        '''
        The total size of actual referenced entities themselves in bytes.
        '''

        total_size = Decimal(0)

        if tqdm_imported:
            if terminal_progress_display_enabled:
                sys_clear()
            iterator = tqdm(tuple(self.used_names), disable = not terminal_progress_display_enabled, desc = "Getting Total Size of Actual Referenced")
        else:
            iterator = tuple(self.used_names)

        if isinstance(check_type,str):
            match (check_type := check_type.lower().strip()):
                case 'any' | 'all' | 'every':
                    if include_other_entities:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_alia_dosieroj.txt' in (items := tuple(zf.namelist())):
                                    with zf.open('_alia_dosieroj.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line)
                                            total_size += Decimal(line[line.rfind('|')+1:])
                                if '_metadata.txt' in (metadata_files :=  [item for item in items if not '/' in item and item.endswith('_metadata.txt')]):
                                    with zf.open('_metadata.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line)
                                            total_size += Decimal(line[line.rfind('|')+1:])
                                    metadata_files.remove('_metadata.txt')
                                if len((metadata_files := tuple(metadata_files))):
                                    for metadata_file in metadata_files:
                                        with zf.open(metadata_file) as tf:
                                            line = tf.readline()
                                            while True:
                                                if not line:
                                                    break
                                                total_size += Decimal(line[line.rfind('|')+1:])
                    else:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_metadata.txt' in (metadata_files :=  [item for item in tuple(zf.namelist()) if not '/' in item and item.endswith('_metadata.txt')]):
                                    with zf.open('_metadata.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line)
                                            total_size += Decimal(line[line.rfind('|')+1:])
                                    metadata_files.remove('_metadata.txt')
                                if len((metadata_files := tuple(metadata_files))):
                                    for metadata_file in metadata_files:
                                        with zf.open(metadata_file) as tf:
                                            line = tf.readline()
                                            while True:
                                                if not line:
                                                    break
                                                total_size += Decimal(line[line.rfind('|')+1:])
                case 'txt' | 'pdf' | 'shp' | 'doc' | 'img':
                    if include_other_entities:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_metadata.txt' in (items := set(zf.namelist())):
                                    with zf.open('_metadata.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line).lower().split('|')
                                            if check_type == line[1]:
                                                total_size += Decimal(line[-1])
                                if '_alia_dosieroj.txt' in items:
                                    with zf.open('_alia_dosieroj.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line)
                                            total_size += Decimal(line[line.rfind('|')+1:])
                    else:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_metadata.txt' in set(zf.namelist()):
                                    with zf.open('_metadata.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line).lower().split('|')
                                            if check_type == line[1]:
                                                total_size += Decimal(line[-1])
                case 'gdb':
                    if include_other_entities:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_alia_dosieroj.txt' in (items := tuple(zf.namelist())):
                                    with zf.open('_alia_dosieroj.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line)
                                            total_size += Decimal(line[line.rfind('|')+1:])
                                if '_metadata.txt' in (metadata_files := [item for item in items if not '/' and item.endswith('_metadata.txt')]):
                                    metadata_files.remove('_metadata.txt')
                                if len((metadata_files := tuple(metadata_files))):
                                    for metadata_file in metadata_files:
                                        with zf.open(metadata_file) as tf:
                                            line = tf.readline()
                                            while True:
                                                line = tf.readline()
                                                if not line:
                                                    break
                                                line = decodeZipTxtLine(line)
                                                total_size += Decimal(line[line.rfind('|')+1:])
                    else:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_metadata.txt' in (metadata_files := [item for item in tuple(zf.namelist()) if not '/' and item.endswith('_metadata.txt')]):
                                    metadata_files.remove('_metadata.txt')
                                if len((metadata_files := tuple(metadata_files))):
                                    with zf.open(metadata_file) as tf:
                                        line = tf.readline()
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line)
                                            total_size += Decimal(line[line.rfind('|')+1:])
                case _:
                    if include_other_entities:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_alia_dosieroj.txt' in set(zf.namelist()):
                                    with zf.open('_alia_dosieroj.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line)
                                            total_size += Decimal(line[line.rfind('|')+1:])
                    else:
                        return 0
        elif isinstance(check_type,(tuple,list,set)):
            check_type = {item.lower().replace(' ','') for item in tuple(check_type)}
            if 'img' in check_type:
                for img_type in self.image_types:
                    check_type.add(img_type)
                check_type.remove('img')
            if include_other_entities or 'alia' in check_type:
                if 'alia' in check_type:
                    check_type.remove('alia')
                if 'gdb' in check_type:
                    check_type.remove('gdb')
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            if '_alia_dosieroj.txt' in (items := tuple(zf.namelist())):
                                with zf.open('_alia_dosieroj.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        line = decodeZipTxtLine(line)
                                        total_size += Decimal(line[line.rfind('|')+1:])
                            if '_metadata.txt' in (metadata_files := [item for item in items if not '/' in item and '_metadata.txt' in item]):
                                with zf.open('_metadata.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        line = decodeZipTxtLine(line).lower().split('|')
                                        if line[1] in check_type:
                                            total_size += Decimal(line[-1])
                                metadata_files.remove('_metadata.txt')
                            for metadata_file in (metadata_files := tuple(metadata_files)):
                                with zf.open(metadata_file) as tf:
                                    line = tf.readline()
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        line = decodeZipTxtLine(line)
                                        total_size += Decimal(line[line.rfind('|')+1:])
                else:
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            if '_alia_dosieroj.txt' in (items := tuple(zf.namelist())):
                                with zf.open('_alia_dosieroj.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        line = decodeZipTxtLine(line)
                                        total_size += Decimal(line[line.rfind('|')+1:])
                            if '_metadata.txt' in items:
                                with zf.open('_metadata.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        line = decodeZipTxtLine(line).lower().split('|')
                                        if line[1] in check_type:
                                            total_size += Decimal(line[-1])
            else:
                if 'gdb' in check_type:
                    check_type.remove('gdb')
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            if '_metadata.txt' in (metadata_files := [item for item in tuple(zf.namelist()) if not '/' in item and '_metadata.txt' in item]):
                                with zf.open('_metadata.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        line = decodeZipTxtLine(line).lower().split('|')
                                        if line[1] == check_type:
                                            total_size += Decimal(line[-1])
                                metadata_files.remove('_metadata.txt')
                            for metadata_file in (metadata_files := tuple(metadata_files)):
                                with zf.open(metadata_file) as tf:
                                    line = tf.readline() # First line is redundant in this case.
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        line = decodeZipTxtLine(line)
                                        total_size += Decimal(line[line.rfind('|')+1:])
                else:
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            if '_metadata.txt' in set(zf.namelist()):
                                with zf.open('_metadata.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        line = decodeZipTxtLine(line).lower().split('|')
                                        if line[1] == check_type:
                                            total_size += Decimal(line[-1])
        else:
            # invalid input.
            return 0

        if self.chloe_vocalization:
            playChloeHappy(self.wakeup_buffer[0],self.wakeup_buffer[1])

        return int(total_size)


    def getTotalNumRefEntities(self, check_type : str | tuple[str] | list[str] | set[str] = 'any', include_other_entities : bool = False, terminal_progress_display_enabled : bool = False) -> int:
        '''
        Number of entities in database.
        '''

        entity_counter = 0

        if tqdm_imported:
            if terminal_progress_display_enabled:
                sys_clear()
            iterator = tqdm(tuple(self.used_names), disable = not terminal_progress_display_enabled, desc = "Counting Referenced Entities")
        else:
            iterator = tuple(self.used_names)

        if isinstance(check_type,str):
            if (check_type := check_type.lower().strip()) == 'doc':
                check_type = 'docx'
            match (checking_type := check_type.lower().strip()):
                case 'any' | 'all' | 'every':
                    if include_other_entities:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_metadata.txt' in (entities := set(zf.namelist())):
                                    with zf.open('_metadata.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            entity_counter += 1
                                    entities.remove('_metadata.txt')
                                entity_counter += len([item for item in tuple(entities) if not '/' in item and item.endswith('_metadata.txt')])
                                if '_alia_dosieroj.txt' in entities:
                                    with zf.open('_alia_dosieroj.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            entity_counter += 1
                    else:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_metadata.txt' in (entities := set(zf.namelist())):
                                    with zf.open('_metadata.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            entity_counter += 1
                                    entities.remove('_metadata.txt')
                                entity_counter += len([item for item in tuple(entities) if not '/' in item and item.endswith('_metadata.txt')])
                case 'gdb':
                    if include_other_entities:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_alia_dosieroj.txt' in (items := tuple(zf.namelist())):
                                    with zf.open('_alia_dosieroj.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            entity_counter += 1
                                if '_metadata.txt' in (metadata_files := [item for item in items if not '/' in item and item.endswith('_metadata.txt')]):
                                    entity_counter += len(metadata_files)-1
                                else:
                                    entity_counter += len(metadata_files)
                    else:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_metadata.txt' in (metadata_files := [item for item in tuple(zf.namelist()) if not '/' in item and item.endswith('_metadata.txt')]):
                                    entity_counter += len(metadata_files)-1
                                else:
                                    entity_counter += len(metadata_files)
                case 'img':
                    if include_other_entities:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_metadata.txt' in (items := set(zf.namelist())):
                                    with zf.open('_metadata.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line)
                                            if f".{line[line.rfind('_')+1:line.rfind('.')]}" in self.accepted_image_extensions:
                                                entity_counter += 1
                                if '_alia_dosieroj.txt' in items:
                                    with zf.open('_alia_dosieroj.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            entity_counter += 1
                    else:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_metadata.txt' in set(zf.namelist()):
                                    with zf.open('_metadata.txt') as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line)
                                            if f".{line[line.rfind('_')+1:line.rfind('.')]}" in self.accepted_image_extensions:
                                                entity_counter += 1
                case 'alia':
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            if '_alia_dosieroj.txt' in (items := set(zf.namelist())):
                                with zf.open('_alia_dosieroj.txt') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity_counter += 1
                case _:
                    # text files, shapefiles, PDFs, and Word Documents.
                    if include_other_entities:
                        for used_name in iterator:
                            with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                                if '_metadata.txt' in (items := set(zf.namelist())):
                                    with zf.open('_metadata.txt') as tf:
                                        while True:
                                            entity = tf.readline()
                                            if not entity:
                                                break
                                            entity = decodeZipTxtLine(entity).split('|')[0]
                                            if entity.lower()[entity.rfind('.')+1:] == check_type:
                                                entity_counter += 1
                                if '_alia_dosieroj.txt' in items:
                                    with zf.open('_alia_dosieroj.txt') as tf:
                                        while True:
                                            entity = tf.readline()
                                            if not entity:
                                                break
                                            entity_counter += 1
        elif isinstance(check_type,(set,tuple,list)):
            check_type = {item.lower().strip() for item in tuple(check_type)}
            if 'img' in check_type:
                check_type.remove('img')
                for img_type in self.image_types:
                    check_type.add(img_type)
            if 'doc' in check_type:
                check_type.remove('doc')
                check_type.add('docx')
            if include_other_entities or 'alia' in check_type:
                if 'alia' in check_type:
                    check_type.remove('alia')
                if 'gdb' in check_type:
                    check_type.remove('gdb')
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            if '_alia_dosieroj.txt' in (items := set(zf.namelist())):
                                with zf.open('_alia_dosieroj.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        entity_counter += 1
                            if '_metadata.txt' in (metadata_files := [item for item in tuple(items) if not '/' in item and item.endswith('_metadata.txt')]):
                                with zf.open('_metadata.txt') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity[entity.rfind('.')+1:] in check_type:
                                            entity_counter += 1
                                metadata_files.remove('_metadata.txt')
                            for metadata_file in (metadata_files := tuple(metadata_files)):
                                if metadata_file.lower().endswith('_gdb_metadata.txt'):
                                    entity_counter += 1
                else:
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            if '_alia_dosieroj.txt' in (items := set(zf.namelist())):
                                with zf.open('_alia_dosieroj.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        entity_counter += 1
                            if '_metadata.txt' in items:
                                with zf.open('_metadata.txt') as tf:
                                    while True:
                                        entity = tf.readline()
                                        if not entity:
                                            break
                                        entity = decodeZipTxtLine(entity).split('|')[0]
                                        if entity[entity.rfind('.')+1:] in check_type:
                                            entity_counter += 1
            elif 'gdb' in check_type:
                check_type.remove('gdb')
                for used_name in iterator:
                    with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                        if '_metadata.txt' in (metadata_files := [item for item in tuple(zf.namelist()) if not '/' in item and item.endswith('_metadata.txt')]):
                            with zf.open('_metadata.txt') as tf:
                                while True:
                                    entity = tf.readline()
                                    if not entity:
                                        break
                                    entity = decodeZipTxtLine(entity).split('|')[0]
                                    if entity[entity.rfind('.')+1:] in check_type:
                                        entity_counter += 1
                            metadata_files.remove('_metadata.txt')
                        for metadata_file in (metadata_files := tuple(metadata_files)):
                            if metadata_file.lower().endswith('_gdb_metadata.txt'):
                                entity_counter += 1
            else:
                for used_name in iterator:
                    with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                        if '_metadata.txt' in set(zf.namelist()):
                            with zf.open('_metadata.txt') as tf:
                                while True:
                                    entity = tf.readline()
                                    if not entity:
                                        break
                                    entity = decodeZipTxtLine(entity).split('|')[0]
                                    if entity[entity.rfind('.')+1:] in check_type:
                                        entity_counter += 1
        else:
            # invalid input.
            return 0

        if self.chloe_vocalization:
            playChloeHappy(self.wakeup_buffer[0],self.wakeup_buffer[1])

        return entity_counter
