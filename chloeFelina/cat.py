# Requires Python 3.10 (Official CPython Build) at least on Windows OS. Certain
# parts of the algorithm would need to be reworked/adjusted to work for MacOS
# and Linux builds like Ubuntu, Debian, and CachyOS, properly and without
# issues.

# Python 3.11+ (Official CPython Build) are recommended. Using the latest and
# stable version of Python 3 will result in the best performance and behavior
# of Chloe Felina.

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
try: from PIL import Image
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
try: from win32api import GetLocalDriveStrings
except ImportError: win32api_imported = False
except ModuleNotFoundError: win32api_imported = False

# Built-In Python Modules
import csv
from os import walk as walker
from os import getlogin,listdir,mkdir,chdir,getcwd,remove,chmod,rename
from os.path import exists,isfile,isdir
from locale import setlocale,LC_ALL
from zipfile import ZipFile,ZIP_DEFLATED
from shutil import rmtree
from string import ascii_letters,digits
from stat import S_IRWXU
from decimal import Decimal,localcontext
from array import array
from pathlib import Path

# Custom Python Modules
from chloeFelina.purr import isQueryMatchKether,isQueryMatchBinah,isQueryMatchDaath,isQueryMatchChochmah,isQueryMatchGewurah,forcedTxtFileWrite,getImageTypeName,decodeZipTxtLine
from chloeFelina.meow import randstr,createCopy,getSizeOfItem,unc_path,getBaselineMetadata,getCreatedDate,getModifiedDate,genSearchQueryResultFile,forbidden_dirs,backupGen
from chloeFelina.paxium import encrypt as pax_encrypt
from chloeFelina.paxium import decrypt as pax_decrypt

setlocale(LC_ALL,'')

class ChloeAI:

    def __init__(self, database_location : str | None = None, database_name : str = 'datenaro', maximum_pixels : int = 10_000_000_000, histogram_ratio_precision : int = 6, pdf_max_array_out_stream_len : int = 100_000_000, pdf_max_declared_stream_len : int = 100_000_000, pdf_jbig2_max_out_len : int = 75_000_000, pdf_lzw_max_out_len : int = 75_000_000, pdf_zlib_max_out_len : int = 75_000_000, pdf_zlib_recovery_in_len : int = 5_000_000, pdf_flate_max_columns : int = 250_000, pdf_flate_max_row_len : int = 4_000_000, pdf_flate_max_buffer_size : int = 75_000_000, pdf_run_len_max_out_len : int = 75_000_000, crintum_obfuscation : bool = False):

        self.crintum_obfuscation = crintum_obfuscation

        if database_location is None or not exists(database_location):
            self.db_path = f'C:/Users/{getlogin()}/Documents/{database_name}'
        else:
            database_location = database_location.replace("\\","/")
            self.db_path = f'{database_location}/{database_name}'
            if not isdir(self.db_path):
                raise TypeError
            if self.db_path.startswith("C:/Windows") or self.db_path in forbidden_dirs():
                raise BlockingIOError

        if exists(self.db_path):
            if not 'crintum_pointer.txt' in (items := set(listdir(self.db_path))) and not '_backup_crintum_pointer.txt' in items:
                ignore_empty_line = True
                while database_name in listdir(database_location):
                    database_name = f"{database_name}_{randstr()}"
                self.db_path = f'{self.db_path[:self.db_path.rfind("/")]}/{database_name}'
                with open(f'{self.db_path}/crintum_pointer.txt','w',encoding='utf-8') as tf:
                    pass
            else:
                ignore_empty_line = False
                items = list(items)
                if '_terms_searched' in items:
                    items.remove('_terms_searched')
                if 'crintum_pointer.txt' in items:
                    items.remove('crintum_pointer.txt')
                if '_backup_crintum_pointer.txt' in items:
                    items.remove('_backup_crintum_pointer.txt')
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
            mkdir(self.db_path)
            with open(f'{self.db_path}/crintum_pointer.txt','w',encoding='utf-8') as tf:
                pass

        self.crintum_pointer = {}
        self.path_pointer = {}
        empty_line_found = False
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

        self.accepted_suffixes = {'txt'}

        if docx_imported and docx2_imported:
            self.accepted_suffixes.add('doc')
            self.accepted_suffixes.add('docx')

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

            self.accepted_suffixes.add('pdf')

        if pil_imported:
            # More file types will be added after thorough testing.
            self.accepted_image_extensions = {'.jpg','.JPG','.jpeg','.JPEG','.png','.PNG','.tif','.TIF','.tiff','.TIFF','.webp','.WEBP'}
            # Maximum number of pixels that an image can have until the PIL module
            # throws an error.
            Image.MAX_IMAGE_PIXELS = maximum_pixels

            for extension in tuple(self.accepted_image_extensions):
                self.accepted_suffixes.add(extension[1:].lower())

        if arcpy_imported:
            arcpy.SetLogHistory(False)
            arcpy.SetLogMetadata(False)
            arcpy.env.autoCommit = 0
            # Setting processorType to CPU instead of GPU as the ArcPy module as
            # of writing only utilizes Nvidia GPUs exclusively.
            arcpy.env.processorType = "CPU"
            arcpy.env.parallelProcessingFactor = "75%"

            self.accepted_suffixes.add('shp')
            self.accepted_suffixes.add('gdb')

        self.histogram_ratio_precision = histogram_ratio_precision
        # The following is required to heavily simplify and reduce storage space
        # requirements for saving histogram ratio data.
        self.subbing = {".a":'È','.b':'É','.c':'Ê','.d':'Ë','.f':'Ì','.g':'Í','.h':'Î','.i':'Ï','.j':'Ð','.k':'Ñ'}
        self.sub_keys = tuple(self.subbing.keys())
        self.shorthand = ['000', '00', '111111', '11111', '1111', '111', '11', '222222', '22222', '2222', '222', '22', '333333', '33333', '3333', '333', '33', '444444', '44444', '4444', '444', '44', '555555', '55555', '5555', '555', '55', '666666', '66666', '6666', '666', '66', '777777', '77777', '7777', '777', '77', '888888', '88888', '8888', '888', '88', '999999', '99999', '9999', '999', '99', 'e-', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '.0', '.1', '.2', '.3', '.4', '.5', '.6', '.7', '.8', '.9']
        self.short_ref = {'000': 'a', '00': 'b', '111111': 'c', '11111': 'd', '1111': 'f', '111': 'g', '11': 'h', '222222': 'i', '22222': 'j', '2222': 'k', '222': 'l', '22': 'm', '333333': 'n', '33333': 'o', '3333': 'p', '333': 'q', '33': 'r', '444444': 's', '44444': 't', '4444': 'u', '444': 'v', '44': 'w', '555555': 'x', '55555': 'y', '5555': 'z', '555': 'A', '55': 'B', '666666': 'C', '66666': 'D', '6666': 'E', '666': 'F', '66': 'G', '777777': 'H', '77777': 'I', '7777': 'J', '777': 'K', '77': 'L', '888888': 'M', '88888': 'N', '8888': 'O', '888': 'P', '88': 'Q', '999999': 'R', '99999': 'S', '9999': 'T', '999': 'U', '99': 'V', 'e-': 'W', '1.': 'X', '2.': 'Y', '3.': 'Z', '4.': '!', '5.': '@', '6.': '$', '7.': '?', '8.': '~', '9.': '&', '.0': '+', '.1': '=', '.2': '<', '.3': '>', '.4': '#', '.5': '`', '.6': '(', '.7': ')', '.8': '[', '.9': ']'}
        self.alphanum = tuple(f'{ascii_letters}{digits}')


    def updateAndRefreshDatabase(self, keep_if_no_connection : bool = True, terminal_progress_display_enabled : bool = False) -> None:
        '''
        WIP
        Checks data in database against referenced files for any new additions,
        removals, and/or modifications and updates the database appropriately.
        '''

        if terminal_progress_display_enabled and tqdm_imported:
            sys_clear()

        # Note: Local drive refers to just the C drive. Any external or network
        # drive is considered a non-local drive. If you somehow managed to
        # rename the local drive to something other C, you are in for an
        # "interesting" time.

        ignored_items = {'crintum_pointer.txt','_terms_searched'}

        # Remove redundant files and folders.
        for item in tuple(listdir(self.db_path)):
            if isdir(f'{self.db_path}/{item}'):
                rmtree(f'{self.db_path}/{item}')
            elif not item.endswith('.zip') and not item in ignored_items:
                remove(f'{self.db_path}/{item}')

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
            explicit_drives = GetLocalDriveStrings().split('\000')[:-1]
            explicit_drives.remove('C:\\')
            explicit_drives = tuple([unc_path(drive) for drive in explicit_drives])
            redact_dbs = []
            if not keep_if_no_connection:
                for db_name in tuple(self.db_names):
                    pass
            else:
                pass

        return None


    def compressToZIP(self, archive_db_name : str) -> bool:

        current_dir = getcwd().replace('\\','/')

        chdir(f'{self.db_path}/{archive_db_name}')

        if len((items := tuple(listdir()))) <= 1:
            chdir(current_dir)
            return False

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


    def getNestedDirectoryData(self, top_directory_path : str, terminal_progress_display_enabled : bool = False) -> None:

        if not exists(top_directory_path):
            return None

        for root,dirs,files in walker(top_directory_path):
            if not "$RECYCLE.BIN" in (root := root.replace('\\','/')) and not self.db_path in root:
                self.getDirectoryData(root,terminal_progress_display_enabled)

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


    def getDirectoryData(self, reference_directory : str, terminal_progress_display_enabled : bool = False) -> None:

        if terminal_progress_display_enabled and tqdm_imported:
            sys_clear()

        reference_directory = reference_directory.replace('\\','/')

        # This is to account for mapped network drives.
        if not exists((reference_directory := unc_path(reference_directory))):
            # Account for weird abnormality.
            return None

        if reference_directory in self.paths_in_db or reference_directory.lower().endswith('.gdb') or reference_directory == self.db_path:
            return None
        else:
            items = {}
            for name in listdir(reference_directory):
                if name.lower().endswith('.gdb'):
                    items[name] = 'GDB'
                elif name.lower().endswith('.shp'):
                    items[name] = 'SHP'
                elif name.lower().endswith('.txt'):
                    items[name] = 'TXT'
                elif name.lower().endswith('.pdf'):
                    items[name] = 'PDF'
                elif name.lower().endswith('.docx') or name.lower().endswith('.doc'):
                    items[name] = 'DOC'
                elif name.lower().endswith('.csv'):
                    items[name] = 'CSV'
                elif name[name.rfind("."):] in self.accepted_image_extensions:
                    items[name] = 'IMG'
            if len(items):
                archive_db_name = randstr(12)
                while archive_db_name in self.used_names:
                    archive_db_name = randstr(12)
                mkdir((output_db_folder := f'{self.db_path}/{archive_db_name}'))
                if tqdm_imported:
                    names = tqdm(tuple(items.keys()), disable = not terminal_progress_display_enabled, desc = reference_directory[:])
                else:
                    names = tuple(items.keys())
                for name in names:
                    match items[name]:
                        case 'GDB':
                            # This allows the algorithm to function without the
                            # ArcPy module being installed. Open source
                            # alternatives to ArcPy should be considered.
                            if arcpy_imported:
                                self.archive_gdb_data(f'{reference_directory}/{name}',archive_db_name)
                        case 'SHP':
                            if arcpy_imported:
                                self.archive_shp_data(f'{reference_directory}/{name}',archive_db_name)
                        case 'TXT':
                            self.archive_txt_data(f'{reference_directory}/{name}',archive_db_name)
                        case 'PDF':
                            if pypdf_imported and pil_imported:
                                self.archive_pdf_data(f'{reference_directory}/{name}',archive_db_name)
                        case 'DOC':
                            if docx_imported and docx2_imported:
                                self.archive_doc_data(f'{reference_directory}/{name}',archive_db_name)
                        case 'CSV':
                            pass
                        case 'IMG':
                            if pil_imported:
                                self.archive_img_data(f'{reference_directory}/{name}',archive_db_name)
                        case _:
                            pass
                if exists(f'{self.db_path}/{archive_db_name}/TeMp_FiLeGeOdAtAbAsE_6789_10.gdb'):
                    try:
                        arcpy.management.Delete(f'{self.db_path}/{archive_db_name}/TeMp_FiLeGeOdAtAbAsE_6789_10.gdb')
                    except Exception:
                        rmtree(f'{self.db_path}/{archive_db_name}/TeMp_FiLeGeOdAtAbAsE_6789_10.gdb')
                if self.compressToZIP(archive_db_name):
                    self.appendCrintumEntry(reference_directory,archive_db_name)
                if exists(f'{self.db_path}/{archive_db_name}'):
                    rmtree(f'{self.db_path}/{archive_db_name}')

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


    def archive_txt_data(self, txt_path : str, archive_db_name : str) -> None:

        if (baseline_metadata := getBaselineMetadata(txt_path)) is None:
            return None

        baseline_metadata = '|'.join(baseline_metadata)

        try:
            if not exists((txt_folder := f"{self.db_path}/{archive_db_name}/_txt_files")):
                mkdir(txt_folder)

            createCopy(txt_path,(new_txt_file := f"{txt_folder}/{txt_path[txt_path.rfind('/')+1:]}"))

            # This is to disable txt files flagged as read-only. This does NOT
            # modify the permissions of the original txt file.
            chmod(new_txt_file,S_IRWXU)

            rename(new_txt_file,(renamed_txt_file := f'{new_txt_file[:new_txt_file.rfind("/")]}/{new_txt_file[new_txt_file.rfind("/")+1:new_txt_file.rfind(".")]}_{new_txt_file[new_txt_file.rfind(".")+1:]}.txt'))

            new_txt_file = renamed_txt_file[:]
            del renamed_txt_file

            issued_encountered = True

            try:
                txt_lines = []
                with open(new_txt_file,encoding='utf-8') as tf:
                    while True:
                        line = tf.readline()
                        if not line:
                            break
                        line = line.rstrip('\n')
                        line = line.strip()
                        while '  ' in line:
                            line = line.replace('  ',' ')
                        txt_lines.append(line)
                issued_encountered = False
            except Exception:
                txt_lines = []
                with open(new_txt_file,encoding='latin-1') as tf:
                    while True:
                        line = tf.readline()
                        if not line:
                            break
                        line = line.rstrip('\n')
                        line = line.strip()
                        while '  ' in line:
                            line = line.replace('  ',' ')
                        txt_lines.append(line)
                issued_encountered = False

            if issued_encountered:
                txt_lines = []
                try:
                    with open(new_txt_file,encoding='cp1251') as tf:
                        while True:
                            line = tf.readline()
                            if not line:
                                break
                            line = line.rstrip('\n')
                            line = line.strip()
                            while '  ' in line:
                                line = line.replace('  ',' ')
                            txt_lines.append(line)
                except Exception:
                    if exists(txt_folder):
                        if not len(listdir(txt_folder)):
                            rmtree(txt_folder)
                    return None

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

        return None


    def archive_doc_data(self, doc_path : str, archive_db_name : str) -> None:

        nulls = {"",0,None}

        if (baseline_metadata := getBaselineMetadata(doc_path)) is None:
            return None

        baseline_metadata = '|'.join(baseline_metadata)

        try:
            word_doc = Document(doc_path)
        except Exception:
            return None

        metadata_info = []

        try:
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
            metadata_info = None

        del props
        try: del temp_str
        except NameError: pass

        mkdir((doc_folder := f'{self.db_path}/{archive_db_name}/{doc_path[doc_path.rfind("/")+1:doc_path.rfind(".")]}_{doc_path[doc_path.rfind(".")+1:]}'))
        mkdir((temp_folder := f'{doc_folder}/_temp_images'))

        if metadata_info is None:
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
            doc_images = f'{doc_folder}/image_histogram_data.txt'
            with open(f'{temp_folder}/{doc_images[0]}','w',encoding='utf-8') as tf:
                tf.write(doc_images[0])
                if not (histo_ratio := self.getImageInformation(f'{temp_folder}/{temp_images[0]}')) is None:
                    for num in histo_ratio:
                        tf.write(f'\n{num}')
                else:
                    tf.write("\nNO DATA")
                for n in range(1,len(temp_images)):
                    tf.write(f"\n{temp_images[n]}")
                    if not (histo_ratio := self.getImageInformation(f'{temp_folder}/{temp_images[n]}')) is None:
                        for num in histo_ratio:
                            tf.write(f"\n{num}")

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

        return None


    def archive_shp_data(self, shp_path : str, archive_db_name : str) -> None:

        if (baseline_metadata := getBaselineMetadata(shp_path)) is None:
            return None

        baseline_metadata = '|'.join(baseline_metadata)

        redundant_fields = {'created_user','created_date','last_edited_user','last_edited_date','shape','annotation class id','symbol id','element'}
        # Yes, this is weirdly necessary.
        sql_keywords_set = set((sql_keywords := ('add','add constraint','all','alter','alter column','alter table','and','any','as','asc','backup database','between','case','check','column','constraint','create','create database','create index','create or replace view','create table','create procedure','create unique index',' create view','database','default','delete','desc','distinct','drop','drop column','drop constraint','drop database','drop default','drop index','drop table','drop view','exec','exists','foreign key','from','full outer join','group by','having','in','index','inner join','insert into','insert into select','is null','is not null','join','left join','like','limit','not','not null','or','order by','outer join','primary key','procedure','right join','rownum','select','select distinct','select into','select top','set','table','top','truncate table','union','union all','unique','update','values','view','where')))

        arcpy.env.workspace = shp_path[:shp_path.rfind("/")]

        shapefile_name = shp_path[shp_path.rfind("/")+1:]

        item_info = {}
        oid_name = None
        try:
            for field in arcpy.ListFields(shapefile_name,field_type='OID'):
                oid_name = field.name[:]
                break
        except Exception:
            # Shapefile cannot be read via ArcPy for unknown reasons.
            return None
        if oid_name is None:
            return None
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

        return None


    def archive_gdb_data(self, gdb_path : str, archive_db_name : str) -> None:

        # Views, Relationship Classes, Mosaic Datasets, Raster Datasets,
        # Trajectory Datasets, Catalog Datasets, and Oriented Imagery Datasets
        # are ignored.

        try:
            gdb_files = {}
            for gdb_item in tuple(listdir(gdb_path)):
                if not gdb_item.lower().endswith('.lock'):
                    if (item_size := getSizeOfItem(f"{gdb_path}/{gdb_item}")) is None:
                        return None
                    gdb_files[gdb_item] = (getCreatedDate(f'{gdb_path}/{gdb_item}')[4:],getModifiedDate(f'{gdb_path}/{gdb_item}')[4:],item_size)
            del item_size
        except Exception:
            return None

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

            item_info = {}
            oid_name = None
            try:
                for field in arcpy.ListFields(entity_name,field_type='OID'):
                    oid_name = field.name[:]
                    break
            except Exception:
                # Item cannot be read via ArcPy for unknown reasons.
                return None
            if oid_name is None:
                return None
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
            return f'{entity_name} {counter}'


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
            return None

        object_counters = '|'.join(sorted(object_counters))

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

        return None


    def archive_img_data(self, image_path : str, archive_db_name : str) -> None:

        if (baseline_metadata := getBaselineMetadata(image_path)) is None:
            return None

        baseline_metadata = '|'.join(baseline_metadata)

        if (histo_ratio := self.getImageInformation(image_path)):
            if not exists((img_folder := f'{self.db_path}/{archive_db_name}/_images')):
                mkdir(img_folder)
            with open(f'{img_folder}/{image_path[image_path.rfind("/")+1:image_path.rfind(".")]}_{image_path[image_path.rfind(".")+1:]}.txt','w',encoding='utf-8') as tf:
                tf.write(histo_ratio[0])
                counter = 1
                for n in range(1,len(histo_ratio)):
                    tf.write(f'\n{histo_ratio[n]}')
                    counter += 1
        else:
            return None

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

        return None


    def archive_pdf_data(self, pdf_path : str, archive_db_name : str) -> None:

        nulls = {"",0,None}

        if (baseline_metadata := getBaselineMetadata(pdf_path)) is None:
            return None

        baseline_metadata = '|'.join(baseline_metadata)

        try:
            reader = PdfReader(pdf_path)
        except Exception:
            return None

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

        for n in range(4294967296):
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
                        else:
                            with open(image_histogram_data,'a',encoding='utf-8') as tf:
                                tf.write(f"\n{count}{image_file_object.name}")
                                for line in histo_info:
                                    tf.write(f'\n{line}')
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

        return None


    def searchQuery(self, entry_string : str, check_type : str | tuple[str] | list[str] | set[str] = 'any', include_entity_name : bool = True, return_tuple : bool = False, max_line_concat : int = 3, save_found_matches : bool = True, save_results_to_file : bool = False, output_file_type : str = 'excel', output_location : str | None = None, output_name : str | None = None, overwrite_existing_output : bool = False, csv_newline : str = '', csv_field_size_limit : int = 131_072, csv_delimiter : str = ',', csv_quotechar : str = '|', csv_quoting_minimal : int = 0, overwrite_saved_found_matches : bool = False, terminal_progress_display_enabled : bool = False) -> tuple[str] | None:
        '''
        output_file_type can be the following:
        "xlsx" or "excel" (for Excel file)
        "txt" or "text" (for delinated text file)
        "csv" (for csv file)
        '''

        def getTestName(entry_string : str) -> str:

            test_name = entry_string.replace('_',' ') ; test_name = test_name.lower().strip()

            while '  ' in test_name:
                test_name = test_name.replace('  ',' ')

            return test_name


        if terminal_progress_display_enabled and tqdm_imported:
            sys_clear()

        if max_line_concat < 2:
            max_line_concat = 2

        entry_string = entry_string.lower().strip() ; temp_entry_string = entry_string.replace('_'," ")

        while '  ' in entry_string:
            entry_string = entry_string.replace('  ',' ')

        if len(entry_string) < 2:
            if return_tuple:
                return ()
            return None

        if output_name is None:
            if entry_string[0].isdigit() or not entry_string[0].isalnum():
                output_name = f"searched_query_{entry_string}"
            else:
                output_name = entry_string[:]
        elif (output_name := output_name.strip()) == '':
            if entry_string[0].isdigit() or not entry_string[0].isalnum():
                output_name = f"searched_query_{entry_string}"
            else:
                output_name = entry_string[:]

        for n in ('.','/','\\'):
            if n in output_name:
                output_name = output_name.replace(n,'_')

        output_file_type = output_file_type.lower().strip() ; output_file_type = output_file_type.replace(' ','')

        if not exists((search_results_folder := f'{self.db_path}/_terms_searched')):
            mkdir(search_results_folder)
        elif not overwrite_saved_found_matches:
            found_matches = []
            if not ' ' in entry_string:
                for previous_search in tuple([txt_file[:txt_file.rfind(".")] for txt_file in tuple(listdir(search_results_folder))]):
                    if previous_search in entry_string:
                        if isinstance(check_type,str):
                            match check_type.lower().replace(' ',''):
                                case 'all' | 'any' | 'every':
                                    found_matches = tuple([line.rstrip('\n') for line in open(f'{search_results_folder}/{previous_search}.txt','r',encoding='utf-8').readlines()])
                                case 'txt':
                                    found_matches = tuple([line.rstrip('\n') for line in open(f'{search_results_folder}/{previous_search}.txt','r',encoding='utf-8').readlines() if line.rstrip('\n').lower().endswith('.txt')])
                                case 'pdf':
                                    found_matches = tuple([line.rstrip('\n') for line in open(f'{search_results_folder}/{previous_search}.txt','r',encoding='utf-8').readlines() if line.rstrip('\n').lower().endswith('.pdf')])
                                case 'gdb':
                                    found_matches = tuple([line.rstrip('\n') for line in open(f'{search_results_folder}/{previous_search}.txt','r',encoding='utf-8').readlines() if line.rstrip('\n').lower().endswith('.gdb')])
                                case 'shp':
                                    found_matches = tuple([line.rstrip('\n') for line in open(f'{search_results_folder}/{previous_search}.txt','r',encoding='utf-8').readlines() if line.rstrip('\n').lower().endswith('.shp')])
                                case 'doc' | 'docx':
                                    found_matches = tuple([line.rstrip('\n') for line in open(f'{search_results_folder}/{previous_search}.txt','r',encoding='utf-8').readlines() if line.rstrip('\n').lower().endswith('.doc') or line.rstrip('\n').lower().endswith('.docx')])
                                case 'img':
                                    if not include_entity_name:
                                        return None
                                    check_type = {'jpeg','jpg','tif','tiff','png','webp'}
                                    found_matches = tuple([line.rstrip('\n') for line in open(f'{search_results_folder}/{previous_search}.txt','r',encoding='utf-8').readlines() if line.rstrip('\n').lower()[:line.rfind('.')] in check_type])
                                case _:
                                    return None
                        elif isinstance(check_type,(tuple,list,set)):
                            try:
                                if 'img' in (check_type := {item.lower().replace(' ','') for item in tuple(check_type)}):
                                    for img_type in ('jpeg','jpg','tif','tiff','png','webp'):
                                        check_type.add(img_type)
                                    check_type.remove('img')
                            except TypeError:
                                return None
                            found_matches = tuple([line.rstrip('\n') for line in open(f'{search_results_folder}/{previous_search}.txt','r',encoding='utf-8').readlines() if line.rstrip('\n')[item.rfind('.')+1:].lower() if check_type])
                        else:
                            return None
                        if save_results_to_file:
                            genSearchQueryResultFile(found_matches,output_file_type,output_location,output_name,csv_field_size_limit,csv_delimiter,csv_quotechar,csv_quoting_minimal,csv_newline,overwrite_existing_output)
                        if return_tuple:
                            return found_matches
                        else:
                            return None
            else:
                counter = 0 ; end_num = len(entry_string.split(' ')) ; relevant_memories = []
                for previous_search in tuple([txt_file[:txt_file.rfind(".")] for txt_file in tuple(listdir(search_results_folder))]):
                    if previous_search in entry_string:
                        relevant_memories.append(f"{previous_search}.txt")
                        counter += 1
                        if counter == end_num:
                            break
                del counter
                relevant_file_paths = {}
                for relevant_memory in (relevant_memories := tuple(relevant_memories)):
                    for line in (open(f'{search_results_folder}/{relevant_memory}','r',encoding='utf-8').readlines()):
                        if (current_line := line.rstrip('\n')) in relevant_file_paths.keys():
                            relevant_file_paths[current_line] += 1
                        else:
                            relevant_file_paths[current_line] = 0
                for file_name in tuple(relevant_file_paths.keys()):
                    if not relevant_file_paths[file_name] != end_num:
                        del relevant_file_paths[file_name]
                if len((relevant_file_paths := tuple(relevant_file_paths.keys()))):
                    # If all "words" do not appear in an entity, they are to be
                    # ignored as possible matches.
                    zip_file_path_to_files = {}
                    for relevant_file_path in relevant_file_paths:
                        if (current_path := relevant_file_path[:relevant_file_path.rfind("/")]) in self.paths_in_db:
                            if current_path in zip_file_path_to_files.keys():
                                zip_file_path_to_files[current_path].append(relevant_file_path[relevant_file_path.rfind("/")+1:])
                            else:
                                zip_file_path_to_files[current_path] = [relevant_file_path[relevant_file_path.rfind("/")+1:]]
                    del end_num
                    if tqdm_imported:
                        item_file_paths = tqdm(tuple(zip_file_path_to_files.keys()), disable = not terminal_progress_display_enabled, desc = f"Searching for instances of {entry_string}")
                    else:
                        item_file_paths = tuple(zip_file_path_to_files.keys())
                    if isinstance(check_type,str):
                        match check_type.lower().replace(' ',''):
                            case 'any' | 'all' | 'every':
                                for item_file_path in item_file_paths:
                                    with ZipFile(f'{self.db_path}/{self.crintum_pointer[item_file_path]}.zip') as zf:
                                        for item in zip_file_path_to_files[item_file_path]:
                                            match item[item.rfind(".")+1:].lower():
                                                case 'txt':
                                                    if include_entity_name:
                                                        if temp_entry_string in getTestName(item):
                                                            found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                            continue
                                                    if isQueryMatchKether(entry_string,tuple(zf.open(f'_txt_files/{item}').readlines())):
                                                        found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                case 'pdf' | 'doc' | 'docx':
                                                    starting_name = f'{item[:item.rfind(".")]}_{item[item.rfind(".")+1:]}/'
                                                    for relevant_archived_file in tuple([archived_file for archived_file in tuple(zf.namelist()) if archived_file.startswith(starting_name)]):
                                                        if include_entity_name:
                                                            if temp_entry_string in getTestName(relevant_archived_file):
                                                                found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                                break
                                                        if isQueryMatchKether(entry_string,tuple(zf.open(f'{starting_name}{relevant_archived_file}').readlines())):
                                                            found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                            break
                                                case 'shp':
                                                    starting_name = f'{item[:item.rfind(".")]}_{item[item.rfind(".")+1:]}/'
                                                    for relevant_archived_file in tuple([archived_file for archived_file in tuple(zf.namelist()) if archived_file.startswith(starting_name)]):
                                                        if include_entity_name:
                                                            if temp_entry_string in getTestName(relevant_archived_file):
                                                                found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                                continue
                                                        if isQueryMatchDaath(entry_string,f'{starting_name}{relevant_archived_file}',zf):
                                                            found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                case 'gdb':
                                                    starting_name = f'{item[:item.rfind(".")]}_{item[item.rfind(".")+1:]}/'
                                                    for relevant_archived_file in tuple([archived_file for archived_file in tuple(zf.namelist()) if archived_file.startswith(starting_name)]):
                                                        if include_entity_name:
                                                            if temp_entry_string in getTestName(relevant_archived_file):
                                                                found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                                break
                                                        if isQueryMatchDaath(entry_string,f'{starting_name}{relevant_archived_file}',zf):
                                                            found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                            break
                                                case 'jpg' | 'jpeg' | 'tif' | 'tiff' | 'png' | 'webp':
                                                    if include_entity_name:
                                                        if temp_entry_string in getTestName(item):
                                                            found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                case _:
                                                    # placeholder
                                                    continue
                            case 'txt':
                                for item_file_path in item_file_paths:
                                    with ZipFile(f'{self.db_path}/{self.crintum_pointer[item_file_path]}.zip') as zf:
                                        for item in zip_file_path_to_files[item_file_path]:
                                            if include_entity_name:
                                                if temp_entry_string in getTestName(relevant_archived_file):
                                                    found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                    continue
                                            if isQueryMatchKether(entry_string,tuple(zf.open(f'_txt_files/{item}').readlines())):
                                                found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                            case 'pdf' | 'doc' | 'docx':
                                for item_file_path in item_file_paths:
                                    with ZipFile(f'{self.db_path}/{self.crintum_pointer[item_file_path]}.zip') as zf:
                                        for item in zip_file_path_to_files[item_file_path]:
                                            starting_name = f'{item[:item.rfind(".")]}_{item[item.rfind(".")+1:]}/'
                                            for relevant_archived_file in tuple([archived_file for archived_file in tuple(zf.namelist()) if archived_file.startswith(starting_name)]):
                                                if include_entity_name:
                                                    if temp_entry_string in getTestName(relevant_archived_file):
                                                        found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                        break
                                                if isQueryMatchKether(entry_string,tuple(zf.open(f'{starting_name}{relevant_archived_file}').readlines())):
                                                    found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                    break
                            case 'shp':
                                for item_file_path in item_file_paths:
                                    with ZipFile(f'{self.db_path}/{self.crintum_pointer[item_file_path]}.zip') as zf:
                                        for item in zip_file_path_to_files[item_file_path]:
                                            starting_name = f'{item[:item.rfind(".")]}_{item[item.rfind(".")+1:]}/'
                                            for relevant_archived_file in tuple([archived_file for archived_file in tuple(zf.namelist()) if archived_file.startswith(starting_name)]):
                                                if include_entity_name:
                                                    if temp_entry_string in getTestName(relevant_archived_file):
                                                        found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                        continue
                                                if isQueryMatchDaath(entry_string,f'{starting_name}{relevant_archived_file}',zf):
                                                    found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                            case 'gdb':
                                for item_file_path in item_file_paths:
                                    with ZipFile(f'{self.db_path}/{self.crintum_pointer[item_file_path]}.zip') as zf:
                                        for item in zip_file_path_to_files[item_file_path]:
                                            starting_name = f'{item[:item.rfind(".")]}_{item[item.rfind(".")+1:]}/'
                                            for relevant_archived_file in tuple([archived_file for archived_file in tuple(zf.namelist()) if archived_file.startswith(starting_name)]):
                                                if include_entity_name:
                                                    if temp_entry_string in getTestName(relevant_archived_file):
                                                        found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                        break
                                                if isQueryMatchDaath(entry_string,f'{starting_name}/{relevant_archived_file}',zf):
                                                    found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                    break
                            case 'jpeg' | 'jpg' | 'tif' | 'tiff' | 'png' | 'webp':
                                for item_file_path in item_file_paths:
                                    with ZipFile(f'{self.db_path}/{self.crintum_pointer[item_file_path]}.zip') as zf:
                                        for item in zip_file_path_to_files[item_file_path]:
                                            if include_entity_name:
                                                if temp_entry_string in getTestName(item):
                                                    found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                            case _:
                                return None
                    elif isinstance(check_type,(tuple,list,set)):
                        try:
                            if 'img' in (check_type := {item.lower().replace(' ','') for item in tuple(check_type)}):
                                for img_type in ('jpeg','jpg','tif','tiff','png','webp'):
                                    check_type.add(img_type)
                                check_type.remove('img')
                        except TypeError:
                            return None
                        for item_file_path in item_file_paths:
                            with ZipFile(f'{self.db_path}/{self.crintum_pointer[item_file_path]}.zip') as zf:
                                for item in zip_file_path_to_files[item_file_path]:
                                    if (entity_type := item.lower()[item.rfind(".")+1:]) in check_type:
                                        match entity_type:
                                            case 'txt':
                                                for relevant_archived_file in tuple([archived_file for archived_file in tuple(zf.namelist()) if archived_file.startswith('_txt_files/')]):
                                                    if include_entity_name:
                                                        if temp_entry_string in getTestName(relevant_archived_file):
                                                            found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                            continue
                                                    if isQueryMatchKether(entry_string,tuple(zf.open(f'_txt_files/{item}').readlines())):
                                                        found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                            case 'pdf':
                                                starting_name = f'{item[:item.rfind(".")]}_{item[item.rfind(".")+1:]}/'
                                                for relevant_archived_file in tuple([archived_file for archived_file in tuple(zf.namelist()) if archived_file.startswith(starting_name)]):
                                                    if include_entity_name:
                                                        if temp_entry_string in getTestName(relevant_archived_file):
                                                            found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                            break
                                                    if isQueryMatchKether(entry_string,tuple(zf.open(f'{starting_name}{relevant_archived_file}').readlines())):
                                                        found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                        break
                                            case 'shp':
                                                for relevant_archived_file in tuple([archived_file for archived_file in tuple(zf.namelist()) if archived_file.startswith('_shp_files/')]):
                                                    if include_entity_name:
                                                        if temp_entry_string in getTestName(relevant_archived_file):
                                                            found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                            continue
                                                    if isQueryMatchDaath(entry_string,f'_shp_files/{relevant_archived_file}',zf):
                                                        found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                            case 'gdb':
                                                starting_name = f'{item[:item.rfind(".")]}_{item[item.rfind(".")+1:]}/'
                                                for relevant_archived_file in tuple([archived_file for archived_file in tuple(zf.namelist()) if archived_file.startswith(starting_name)]):
                                                    if include_entity_name:
                                                        if temp_entry_string in getTestName(relevant_archived_file):
                                                            found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                            break
                                                    if isQueryMatchDaath(entry_string,f'{starting_name}{relevant_archived_file}',zf):
                                                        found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                        break
                                            case 'doc' | 'docx':
                                                starting_name = f'{item[:item.rfind(".")]}_{item[item.rfind(".")+1:]}/'
                                                for relevant_archived_file in tuple([archived_file for archived_file in tuple(zf.namelist()) if archived_file.startswith(starting_name)]):
                                                    if include_entity_name:
                                                        if temp_entry_string in getTestName(relevant_archived_file):
                                                            found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                            break
                                                    if isQueryMatchKether(entry_string,tuple(zf.open(f'{starting_name}{relevant_archived_file}').readlines())):
                                                        found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                                        break
                                            case 'jpeg' | 'jpg' | 'png' | 'tif' | 'tiff' | 'webp':
                                                for relevant_archived_file in tuple([archived_file for archived_file in tuple(zf.namelist()) if archived_file.startswith('_images/')]):
                                                    if include_entity_name:
                                                        if temp_entry_string in getTestName(relevant_archived_file):
                                                            found_matches.append("%s\\%s" % (item_file_path.replace("/","\\"),item))
                                            case _:
                                                # Placeholder
                                                pass
                    else:
                        return None
                    if save_results_to_file:
                        genSearchQueryResultFile(found_matches,output_file_type,output_location,output_name,csv_field_size_limit,csv_delimiter,csv_quotechar,csv_quoting_minimal,csv_newline,overwrite_existing_output)
                    if return_tuple:
                        return found_matches
                    else:
                        return None

        del search_results_folder

        found_matches = []
        # memory overhead needs to be reduced.
        if tqdm_imported:
            iterator = tqdm(tuple(self.used_names), disable = not terminal_progress_display_enabled, desc = f"Searching for instances of {entry_string}")
        else:
            iterator = tuple(self.used_names)
        if not ' ' in entry_string:
            for used_name in iterator:
                extracted_data = {}
                with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                    for item in tuple(zf.namelist()):
                        if '/' in item[:-1]:
                            if not (folder_name := item[:item.find("/")]) in extracted_data.keys():
                                extracted_data[folder_name] = [item[item.find("/")+1:]]
                            else:
                                extracted_data[folder_name].append(item[item.find("/")+1:])
                    try: del folder_name
                    except NameError: pass
                    for classify in tuple(extracted_data.keys()):
                        if classify == '_txt_files':
                            for txt_file in extracted_data[classify]:
                                if include_entity_name:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                        continue
                                if isQueryMatchKether(entry_string,tuple(zf.open(f'_txt_files/{txt_file}').readlines())):
                                    found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                        elif classify == '_shp_files':
                            for txt_file in extracted_data[classify]:
                                if include_entity_name:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                        continue
                                if isQueryMatchDaath(entry_string,f'_shp_files/{txt_file}',zf):
                                    found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                        elif classify.lower().endswith('_gdb'):
                            found_equal = False
                            for txt_file in extracted_data[classify]:
                                if include_entity_name:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                        break
                                if isQueryMatchDaath(entry_string,f'{classify}/{txt_file}',zf):
                                    found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                    break
                        elif classify.lower().endswith('_pdf') or classify.lower().endswith('_doc'):
                            for txt_file in extracted_data[classify]:
                                if include_entity_name:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                        break
                                if isQueryMatchKether(entry_string,tuple(zf.open(f'{classify}/{txt_file}').readlines())):
                                    found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                    break
                        elif classify.lower().endswith('_docx'):
                            for txt_file in extracted_data[classify]:
                                if include_entity_name:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                                        break
                                if isQueryMatchKether(entry_string,tuple(zf.open(f'{classify}/{txt_file}').readlines())):
                                    found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                                    break
                        elif classify == '_images':
                            if include_entity_name:
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:txt_file.rfind(".")],txt_file[txt_file.rfind("."):]))
            if save_found_matches:
                if len((found_matches := tuple(sorted(found_matches)))):
                    with open(f'{self.db_path}/_terms_searched/{entry_string}.txt','w',encoding='utf-8') as tf:
                        tf.write(found_matches[0])
                        for n in range(1,len(found_matches)):
                            tf.write(f'\n{found_matches[n]}')
                else:
                    # No matches found.
                    with open(f'{self.db_path}/_terms_searched/{entry_string}.txt','w',encoding='utf-8') as tf:
                        pass
        else:
            terms = tuple(entry_string.split(' '))
            if save_found_matches:
                term_memories = {term : [] for term in terms}
            for used_name in iterator:
                extracted_data = {}
                with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                    for item in tuple(zf.namelist()):
                        if '/' in item[:-1]:
                            if not (folder_name := item[:item.find("/")]) in extracted_data.keys(): extracted_data[folder_name] = [item[item.find("/")+1:]]
                            else: extracted_data[folder_name].append(item[item.find("/")+1:])
                    try: del folder_name
                    except NameError: pass
                    for classify in tuple(extracted_data.keys()):
                        if classify == '_txt_files':
                            for txt_file in extracted_data[classify]:
                                if include_entity_name:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                        continue
                                if isQueryMatchGewurah(entry_string,(txt_lines := tuple(zf.open(f'_txt_files/{txt_file}').readlines())),max_line_concat):
                                    found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                if save_found_matches:
                                    for term in terms:
                                        if include_entity_name:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                found_matches.append("%s\\%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file))
                                                continue
                                        if isQueryMatchKether(term,txt_lines):
                                            term_memories[term].append("%s\\%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file))
                                del txt_lines
                        elif classify == '_shp_files':
                            for txt_file in extracted_data[classify]:
                                if include_entity_name:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                        continue
                                if isQueryMatchChochmah(entry_string,f'_shp_files/{txt_file}',zf):
                                    found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                if save_found_matches:
                                    for term in terms:
                                        if include_entity_name:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                                                continue
                                        if isQueryMatchDaath(term,f'_shp_files/{txt_file}',zf):
                                            term_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:-8],txt_file[txt_file.rfind('_')+1:txt_file.rfind('.')]))
                        elif classify.lower().endswith('_gdb'):
                            for txt_file in extracted_data[classify]:
                                if include_entity_name:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                        break
                                if isQueryMatchChochmah(entry_string,f'{classify}/{txt_file}',zf):
                                    found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                    break
                            if save_found_matches:
                                for term in terms:
                                    for txt_file in extracted_data[classify]:
                                        if include_entity_name:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                                break
                                        if isQueryMatchDaath(term,f'{classify}/{txt_file}',zf):
                                            term_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                            break
                        elif classify.lower().endswith('_pdf') or classify.lower().endswith('_doc'):
                            for txt_file in extracted_data[classify]:
                                if include_entity_name:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                        break
                                if isQueryMatchGewurah(entry_string,tuple(zf.open(f'{classify}/{txt_file}').readlines()),max_line_concat):
                                    found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                    break
                            if save_found_matches:
                                for term in terms:
                                    for txt_file in extracted_data[classify]:
                                        if include_entity_name:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                                break
                                        if isQueryMatchKether(term,tuple(zf.open(f'{classify}/{txt_file}').readlines())):
                                            term_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-4],classify[-3:]))
                                            break
                        elif classify.lower().endswith('_docx'):
                            for txt_file in extracted_data[classify]:
                                if include_entity_name:
                                    if temp_entry_string in getTestName(txt_file):
                                        found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                                        break
                                if isQueryMatchGewurah(entry_string,tuple(zf.open(f'{classify}/{txt_file}').readlines()),max_line_concat):
                                    found_matches.append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                                    break
                            if save_found_matches:
                                for term in terms:
                                    for txt_file in extracted_data[classify]:
                                        if include_entity_name:
                                            if term.replace('_',' ') in getTestName(txt_file):
                                                term_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                                                break
                                        if isQueryMatchKether(term,tuple(zf.open(f'{classify}/{txt_file}').readlines())):
                                            term_memories[term].append("%s\\%s.%s" % (self.path_pointer[used_name].replace("/","\\"),classify[:-5],classify[-4:]))
                                            break
                        elif classify == '_images':
                            if include_entity_name:
                                for txt_file in extracted_data[classify]:
                                    if temp_entry_string in (test_name := getTestName(txt_file)):
                                        found_matches.append("%s\\%s%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:txt_file.rfind(".")],txt_file[txt_file.rfind("."):]))
                                    if save_found_matches:
                                        for term in terms:
                                            if term.replace('_',' ') in test_name:
                                                term_memories[term].append("%s\\%s%s" % (self.path_pointer[used_name].replace("/","\\"),txt_file[:txt_file.rfind(".")],txt_file[txt_file.rfind("."):]))
            if save_found_matches:
                for term in terms:
                    if not len(term_memories[term]):
                        del term_memories[term]
                    else:
                        term_memories[term] = tuple(sorted(term_memories[term]))
                        with open(f'{self.db_path}/_terms_searched/{term}.txt','w',encoding='utf-8') as tf:
                            tf.write(term_memories[term][0])
                            for n in range(1,len(term_memories[term])):
                                tf.write(f'\n{term_memories[term][n]}')

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
                    found_matches = tuple([found_match for found_match in found_matches if found_match.lower().endswith('.txt')])
                case 'pdf':
                    found_matches = tuple([found_match for found_match in found_matches if found_match.lower().endswith('.pdf')])
                case 'gdb':
                    found_matches = tuple([found_match for found_match in found_matches if found_match.lower().endswith('.gdb')])
                case 'shp':
                    found_matches = tuple([found_match for found_match in found_matches if found_match.lower().endswith('.shp')])
                case 'doc' | 'docx':
                    found_matches = tuple([found_match for found_match in found_matches if found_match.lower().endswith('.doc') or found_match.lower().endswith('.docx')])
                case 'img':
                    if not include_entity_name:
                        return None
                    check_type = {'.jpeg','.jpg','.tif','.tiff','.png','.webp'}
                    found_matches = tuple([found_match for found_match in found_matches if found_match.lower()[found_match.rfind('.'):] in check_type])
                case _:
                    # Invalid output type.
                    return None
        elif isinstance(check_type,(tuple,list,set)):
            check_type = {item.lower().replace(' ','') for item in tuple(check_type)}
            if 'img' in check_type:
                for img_type in ('jpeg','jpg','tif','tiff','png','webp'):
                    check_type.add(img_type)
                check_type.remove('img')
            found_matches = tuple([found_match for found_match in found_matches if found_match.lower()[found_match.rfind('.')+1:] in check_type])
        else:
            return None

        # Account for not selecting all on first run
        if save_results_to_file:
            genSearchQueryResultFile(found_matches,output_file_type,output_location,output_name,csv_field_size_limit,csv_delimiter,csv_quotechar,csv_quoting_minimal,csv_newline,overwrite_existing_output)

        if return_tuple:
            return found_matches

        return None


    def clearSearchQueryMemory(self) -> None:

        if exists((search_results_folder := f'{self.db_path}/_terms_searched')):
            rmtree(search_results_folder)
            mkdir(search_results_folder)

        return None


    def findAllDuplicates(self, check_type : str | tuple[str] | list[str] | set[str] = 'any', return_tuple : bool = False, terminal_progress_display_enabled : bool = False) -> None | tuple:
        '''
        Check items of matching type against each other.
        WIP
        '''

        if terminal_progress_display_enabled and tqdm_imported:
            sys_clear()

        if isinstance(check_type,str):
            pass
        elif isinstance(check_type,(tuple,list,set)):
            pass
        else:
            return None

        return None


    def findEntityDuplicate(self, item_path : str, return_tuple : bool = False, save_results_to_file : bool = True, output_file_type : str = 'excel', output_location : str | None = None, output_name : str | None = None, overwrite_existing_output : bool = False, csv_newline : str = '', csv_field_size_limit : int = 131_072, csv_delimiter : str = ',', csv_quotechar : str = '|', csv_quoting_minimal : int = 0, terminal_progress_display_enabled : bool = False) -> tuple[tuple[str]] | None:
        '''
        Check specified item against items of matching type.
        WIP
        '''

        if not exists(item_path):
            return None

        if terminal_progress_display_enabled and tqdm_imported:
            sys_clear()

        return None


    def getTotalSizeOfActualRefEntities(self, check_type : str | tuple[str] | list[str] | set[str] = 'any', terminal_progress_display_enabled : bool = False) -> int:
        '''
        The total size of actual referenced entities themselves.
        '''

        total_size = Decimal(0)

        if terminal_progress_display_enabled and tqdm_imported:
            sys_clear()

        if tqdm_imported:
            iterator = tqdm(tuple(self.used_names), disable = not terminal_progress_display_enabled, desc = "Getting Total Size of Actual Referenced")
        else:
            iterator = tuple(self.used_names)

        if isinstance(check_type,str):
            match (check_type := check_type.lower().strip()):
                case 'any' | 'all' | 'every':
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            for metadata_file in tuple([item for item in tuple(zf.namelist()) if not '/' in item and '_metadata.txt' in item]):
                                if metadata_file == '_metadata.txt':
                                    with zf.open(metadata_file) as tf:
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line)
                                            for _ in range(4):
                                                line = line[line.find('|')+1:]
                                            total_size += Decimal(line[:line.find('|')])
                                else:
                                    # GDBs
                                    with zf.open(metadata_file) as tf:
                                        line = tf.readline() # First line is redundant in this case.
                                        while True:
                                            line = tf.readline()
                                            if not line:
                                                break
                                            line = decodeZipTxtLine(line)
                                            total_size += Decimal(line[line.rfind('|')+1:])
                case 'txt' | 'pdf' | 'shp':
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            if '_metadata.txt' in set(zf.namelist()):
                                with zf.open('_metadata.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        line = decodeZipTxtLine(line).lower()
                                        if line[:line.rfind('.')].endswith(f'_{check_type}'):
                                            for _ in range(4):
                                                line = line[line.find('|')+1:]
                                            total_size += Decimal(line[:line.find("|")])
                case 'doc' | 'docx':
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            if '_metadata.txt' in set(zf.namelist()):
                                with zf.open('_metadata.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        line = decodeZipTxtLine(line).lower()
                                        if line[:line.rfind('.')].endswith('_doc') or line[:line.rfind('.')].endswith('_docx'):
                                            for _ in range(4):
                                                line = line[line.find('|')+1:]
                                            total_size += Decimal(line[:line.find("|")])
                case 'gdb':
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            metadata_files = [item for item in tuple(zf.namelist()) if not '/' in item and '_metadata.txt' in item]
                            if '_metadata.txt' in metadata_files:
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
                case _:
                    # assumed to be img
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
                                            for _ in range(4):
                                                line = line[line.find('|')+1:]
                                            total_size += Decimal(line[:line.find("|")])
        elif isinstance(check_type,(tuple,list,set)):
            check_type = {item.lower().replace(' ','') for item in tuple(check_type)}
            if 'img' in check_type:
                for img_type in ('jpeg','jpg','tif','tiff','png','webp'):
                    check_type.add(img_type)
                check_type.remove('img')
            for used_name in iterator:
                with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                    if '_metadata.txt' in (metadata_files := [item for item in tuple(zf.namelist()) if not '/' in item and '_metadata.txt' in item]):
                        with zf.open('_metadata.txt') as tf:
                            while True:
                                line = tf.readline()
                                if not line:
                                    break
                                line = decodeZipTxtLine(line)
                                temp_line = line[:line.find('|')]
                                if temp_line[temp_line.find('_')+1:temp_line.rfind('.')].lower() in check_type:
                                    for _ in range(4):
                                        line = line[line.find('|')+1:]
                                    total_size += Decimal(line[:line.find('|')])
                        metadata_files.remove('_metadata.txt')
                    if 'gdb' in check_type:
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
            # invalid input.
            return 0


        return int(total_size)


    def getTotalNumRefEntities(self, check_type : str | tuple[str] | list[str] | set[str] = 'any', terminal_progress_display_enabled : bool = False) -> int:
        '''
        Number of entities in database.
        '''

        if terminal_progress_display_enabled and tqdm_imported:
            sys_clear()

        def genRefCountFunc(archive_db_path : str, exclusive_ending : str) -> int:

            counter = 0

            with ZipFile(archive_db_path) as zf:
                if '_metadata.txt' in set(zf.namelist()):
                    with zf.open('_metadata.txt') as tf:
                        while True:
                            line = tf.readline()
                            if not line:
                                break
                            line = decodeZipTxtLine(line).lower()
                            if line[:line.find('|')].endswith(exclusive_ending):
                                counter += 1

            return counter


        entity_counter = 0

        if tqdm_imported:
            iterator = tqdm(tuple(self.used_names), disable = not terminal_progress_display_enabled, desc = "Counting Referenced Entities")
        else:
            iterator = tuple(self.used_names)

        if isinstance(check_type,str):
            match (checking_type := check_type.lower().strip()):
                case 'any' | 'all' | 'every':
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            # accounts for GDB reference metadata files.
                            entities = set(zf.namelist())
                            entity_counter += len([item for item in tuple(entities) if not '/' in item and '_metadata.txt' in item])-1
                            if '_metadata.txt' in entities:
                                with zf.open('_metadata.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        entity_counter += 1
                case 'doc' | 'docx':
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            if '_metadata.txt' in set(zf.namelist()):
                                with zf.open('_metadata.txt') as tf:
                                    while True:
                                        line = tf.readline()
                                        if not line:
                                            break
                                        line = decodeZipTxtLine(line).lower()
                                        if line[:line.find('|')].endswith('_doc') or line[:line.find('|')].endswith('_docx'):
                                            entity_counter += 1
                case 'gdb':
                    for used_name in iterator:
                        with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                            entity_counter += len([item for item in tuple(zf.namelist()) if not '/' in item and '_metadata.txt' in item])-1
                case 'img':
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
                case _:
                    # text files, shapefiles, and PDFs.
                    for used_name in iterator:
                        entity_counter += genRefCountFunc(f'{self.db_path}/{used_name}.zip',checking_type)
        elif isinstance(check_type,(set,tuple,list)):
            check_type = {item.lower().replace(' ','') for item in tuple(check_type)}
            if 'img' in check_type:
                for img_type in ('jpeg','jpg','tif','tiff','png','webp'):
                    check_type.add(img_type)
                check_type.remove('img')
            for used_name in iterator:
                with ZipFile(f'{self.db_path}/{used_name}.zip') as zf:
                    entities = set(zf.namelist())
                    if 'gdb' in check_type:
                        entity_counter += len([item for item in tuple(entities) if not '/' in item and '_metadata.txt' in item])-1
                    if '_metadata.txt' in entities:
                        with zf.open('_metadata.txt') as zf:
                            while True:
                                line = tf.readline()
                                if not line:
                                    break
                                line = decodeZipTxtLine(line)
                                line = line[:line.find('|')]
                                if line[line.rfind("_")+1:] in check_type:
                                    entity_counter += 1
        else:
            # invalid input.
            return 0

        return entity_counter
