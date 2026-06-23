Note: Certain things are deliberately unexplained due to not being advised to let the user use and/or interact with them directly.







Accepted **check\_type** inputs as a string or in a list of strings with one or more of the following:



any - Any and all types.



all - This is the same as "any".



every - This is the same as "any".



txt - Text files (.txt)



doc - Word Documents (.doc and/or .docx)



docx - This is the same as "doc".



pdf - PDFs (.pdf)



shp - Esri Shapefiles (.shp)



gdb - Esri File Geodatabase (.gdb)



img - Image files (So far, .tif, .tiff, .jpeg, .jpg, .png, and/or .webp)





Note: For example, ".txt" and ".TXT" are considered to be the same. So, the casing of a file extension is irrelevant.







**ChloeAI**



Purpose: Initialization of Chloe Felina



Parameters:



**database\_location** (*String* or *NoneType*) - This dictates the directory/folder where the database used by Chloe Felina will be generated. If this is not specified, it will try to default to the current user's Documents folder. Please note that specific locations on the user's local machine are forbidden from being used and will instead default to the current user's Documents folder if one of such locations is specified.



**database\_name** (*String*) - This will be the name of the database used by Chloe Felina. Anything name is acceptable. If a database has already been generated for Chloe Felina (and both **database\_location** and **database\_name** together point to it), it will get the necessary data from the pre-existing database instead of initializing a new one. By default "datenaro" is used as the name of the database. Datenaro is supposedly "database" in Esperanto.



**maximum\_pixels** (*Integer*) - This parameter only comes into effect if pillow/PIL (i.e., Python Image Library) module is installed/available. It dictates the maximum number of pixels an image is allowed to have before an error is thrown by the module. By default, the value is set to 10 billion pixels.



**histogram\_ratio\_precision** (*Integer*) - This parameter only comes into effect if pillow/PIL (i.e., Python Image Library) module is installed/available. When acquiring identifying data from image files, this value determines the number of decimal points that are kept for histogram ratio values. In short, higher values result in more "exact" values for histogram ratios while lower ones result in the inverse. By default, the value is 6 and is considered optimal.



**pdf\_max\_array\_out\_stream\_len**, **pdf\_max\_declared\_stream\_len**, **pdf\_jbig2\_max\_out\_len**, **pdf\_lzw\_max\_out\_len**, **pdf\_zlib\_max\_out\_len**, **pdf\_zlib\_recovery\_in\_len**, **pdf\_flate\_max\_columns**, **pdf\_flate\_max\_row\_len**, **pdf\_flate\_max\_buffer\_size**, **pdf\_run\_len\_max\_out\_len** (*Integer*s) - These parameters only come into effect if pypdf module is installed/available. These values directly set preset maximums for the pypdf module : pypdf.filters.MAX\_ARRAY\_BASED\_STREAM\_OUTPUT\_LENGTH, pypdf.filters.MAX\_DECLARED\_STREAM\_LENGTH, pypdf.filters.JBIG2\_MAX\_OUTPUT\_LENGTH, pypdf.filters.LZW\_MAX\_OUTPUT\_LENGTH, pypdf.filters.RUN\_LENGTH\_MAX\_OUTPUT\_LENGTH, pypdf.filters.ZLIB\_MAX\_OUTPUT\_LENGTH, pypdf.filters.ZLIB\_MAX\_RECOVERY\_INPUT\_LENGTH, pypdf.filters.FLATE\_MAX\_COLUMNS, pypdf.filters.FLATE\_MAX\_ROW\_LENGTH, and pypdf.filters.FLATE\_MAX\_BUFFER\_SIZE, respectively. If you are dealing with extremely large/long PDFs or experiencing an error related to one of the values, try increasing the default value to see if that helps.



**crintum\_obfuscation** (*Boolean*) - If a database for Chloe Felina already exists, it will expect that obfuscation has already been applied to the crintum\_pointer.txt and decode it during the session that Chloe Felina is being used. Otherwise, any added entry to crintum\_pointer.txt will be obfuscated via a custom obfuscation algorithm. This is False by default. Set to True if you want a minor amount of security; however, this may result in some minor slower initialization of Chloe Felina depending upon how many entries are in crintum\_pointer.txt.



**chloe\_vocalization** (*Boolean*) - This is for an explicitly optional feature of Chloe Felina. Upon successfully completing certain functions in the **ChloeAI**, a randomly chosen audio clip of Chloe Link will be played of her either trilling or meowing happily by calling the **playChloeHappy** function. This is False by default.



**use\_audio\_wakeup\_buffer** (*Boolean*) - This parameter only comes into effect if **chloe\_vocalization** is True. This is False by default. This addresses a niche scenario where the user's computer is only using an audio device like plugged in headphones. If no audio is being played or has been played recently, the computer will, for a lack of better phrasing, put audio outputs into a "sleep mode" or "power saving mode". This means when the computer tries to play audio to the headphones it first needs to "wake up"; however, it does not halt anything audio related and will only start playing audio after it "wakes up" resulting in a very small moment where audio is technically playing as far as the machine is concerned but no audio is being outputted. At least, that's what I have come to understand on how this works. For the average users, this will not be an issue. However, if no audio is being played despite **chloe\_vocalization** being True, set this parameter as True. By default, this is False.



**audio\_wakeup\_buffer** (*Integer*) - This parameter only comes into effect if both **chloe\_vocalization** and **use\_audio\_wakeup\_buffer** are True. The value represents milliseconds of playing a silent dummy audio file that is used to "wake up" the audio device from "sleep mode". By default, the value is 10 (i.e., 10 milliseconds.). If the audio is still "muted" or it seems like only part of the audio is being played, try using a higher value.





**ChloeAI.updateAndRefreshDatabase**



Purpose: This checks the data in the database against the actual data that said data is referencing and makes appropriate changes by removing references to directories that no longer exist, items being modified, items being added, and/or items being removed. This ensures that the data in the Chloe Felina database is up to date and not referencing inaccurate and/or nonexistent data.



Parameters:



**keep\_db\_if\_no\_connection** (*Boolean*) - This requires the win32api (i.e., pywin32) module to be installed for this parameter to come into effect. If while getting data for the directory that a zip file in the database is referencing that the directory cannot be found or connection to it (i.e., the non-local drive) cannot be established, checks for that zip file are skipped and are assumed to be correct due to being unable to be verified. If this parameter is False, being unable to find the referenced directory or connect to the drive that the directory is located within will result in the zip file being deleted and its references removed from the database. By default, this is True.



**clear\_terms\_searched** (*Boolean*) - If the "\_terms\_searched" folder has been generated or exists within the Chloe Felina database, it will be deleted. This is done since keeping the cached search results from **ChloeAI.searchQuery** may result in an error due to being unable to find a referenced entity or potentially untested behavior from **ChloeAI.searchQuery**. By default, this is True.



**terminal\_progress\_display\_enabled** (*Boolean*) - This parameters only comes into effect if tqdm module is installed/available. This allows the display of progress bar for data being processed by Chloe Felina and archived if using a terminal / command prompt display if set to True. This will NOT display or work properly in something like the Python IDLE. It will also result in the Chloe Felina performing slower than it would otherwise. By default, this is False.





**ChloeAI.getNestedDirectoryData**



Purpose: This compiles data from entities (i.e., files and special folders) into the database starting with the specified directory and all folders/directories contained within said specified directory.



Parameters:



**top\_directory\_path** (*String*) - This is the specified full path to the directory the user wants Chloe Felina to start with getting data from and will get data from all nested folders/directories as well. An invalid explicit path will result in nothing happening.



**terminal\_progress\_display\_enabled** (*Boolean*) - This parameters only comes into effect if tqdm module is installed/available. This allows the display of progress bar for data being processed by Chloe Felina and archived if using a terminal / command prompt display if set to True. This will NOT display or work properly in something like the Python IDLE. It will also result in the Chloe Felina performing slower than it would otherwise. By default, this is False.





**ChloeAI.getDirectoryData**



Purpose: This compiles data from entities (i.e., files and special folders) into the database from a specified directory.



Parameters:



**reference\_directory** (*String*) - This is the specified full path to the directory the user wants Chloe Felina to get data from. An invalid explicit path will result in nothing happening.



**terminal\_progress\_display\_enabled** (*Boolean*) - This parameters only comes into effect if tqdm module is installed/available. This allows the display of progress bar for data being processed by Chloe Felina and archived if using a terminal / command prompt display if set to True. This will NOT display or work properly in something like the Python IDLE. It will also result in the Chloe Felina performing slower than it would otherwise. By default, this is False.





**ChloeAI.searchQuery**



Purpose: This is dynamic term searching system that scans the database for matches to an inputted term or phrase and can output the results as an organized Excel, text, or CSV file and/or return a tuple. Search results by default are saved for future searches for faster results as well as shortcutting the need to check the entirety of the database. For example, if "plagioclase" was already searched and the user inputs "plagioclase feldspar" into **ChloeAI.searchQuery**, only the saved results for "plagioclase" will be checked for any instance of "plagioclase feldspar" existing within said search results instead of the whole database. The only downside of this system is that there is no association between plural and singular versions of terms. So, "station" and "stations" are not considered to be the same thing by the system. This downside is only present due to allowing for any specified strings of characters being allowed to be searched for. So, having code in place to connect the search results of "station" with "stations" would be unnecessary.



Parameters:



**entry\_string** (*String*) - Input text to be searched across the database for instances of existing within files whose information has been archived in the database. Trailing spaces will be removed and multiple consecutive spaces will be simplified to single spaces. Capitalization does not matter. "day" and "Day" will be treated as the same thing. An empty string will result in no search being conducted. This also happens if a string is only 1 character.



**check\_type** (*String* or *Tuple* or *List* or *Set*) - This parameter results in slightly different behavior depending upon if a string is inputted or a tuple/list/set is given. If a string is given, it expects "all"/"any"/"every" to check all entity types for the existence of **entry\_string**. If "doc"/"docx", "pdf", "txt", "shp", "img", or "gdb" is given, only the specified file type of Word Document, PDF, text file, shapefile, image files (i.e., TIFF/TIF, PNG, JPEG/JPG, and WebP), or file geodatabase, respectively, will be checked. If a tuple/list/set is inputted instead, it will expect a combination of the mentioned types to be checked for the presence of **entry\_string**. By default, the string is "any".



**include\_entity\_name** (*Boolean*) - This determines if the name of the files themselves should be considered for being a valid match with **entry\_string**. By default, this is True.



**return\_tuple** (*Boolean*) - This determines if the function will return a tuple that lists all explicit paths of files in database containing the **entry\_string**. By default, this is False.



**max\_line\_concat** (*Integer*) - This variable name is shorthand for "maximum number of lines allowed for concatenation". This pertains to Word Document files, text files, and PDFs only. Due to how text can be formatted for these particular files, new lines in text can prevent long entry\_string inputs and/or any input with more than one "word" from correctly determining that a file contains the **entry\_string**. So, by default, it is set so that 3 lines (or less) will be concatenated before trying to determine if entry\_string is present within a file. For example, say if you give the entry string as "fossiliferous limestone". Well, for Word Document files, text files, and/or PDFs, one line ends with "fossilif" and then following line starts with "erous limestone". By concatenating subsequent lines, this oversight will not transpire. Any value inputted that is less than 2 will just set this parameter to 2 upon execution of the **ChloeAI.searchQuery**.



**save\_found\_matches** (*Boolean*) - This allows the storage of individual "words" having their search results being stored in the "\_terms\_searched" folder (with said folder being automatically created if not already existing) for faster look up in the database. For example, if "plagioclase" has already been searched, if "plagioclase" is **entry\_string**, the output will be identical to what is stored. However, continuing with this example, if "plagioclase feldspar" is **entry\_string**, only the results from "plagioclase" will be checked for any instance of "plagioclase feldspar". Although, "feldspar" will not have search results for it only be stored because it is redundant. In addition, if "plagioclase" and "feldspar" already have search results stored, it will only check files that appear in both "plagioclase" and "feldspar" for the presence of "plagioclase feldspar". This is True by default and highly recommended to be kept as True.



**save\_results\_to\_file** (*Boolean*) - This allows saving the results for files with instances of entry\_string to an organized output file that can be an Excel, CSV, or delineated text file. By default, this is False.



**output\_file\_type** (*String*) - This parameter only comes into effect if **save\_results\_to\_file** is True. This specifies the file type that the results will be saved to. "xlsx"/"excel" will result in an Excel file; "txt"/"text" will result in a delineated text file; and "csv" will result in a CSV file. By default, it is set as "excel" for an Excel file.



**output\_location** (*String* or *NoneType*) - This parameters only comes into effect if **save\_results\_to\_file** is True. This specifies the location on the computer where the output results file will be saved to. If nothing is given or the specified location does not exist, it will default to the current user's Documents folder. By default, this is None.



**output\_name** (*String* or *NoneType*) - This parameter only comes into effect if **save\_results\_to\_file** is True. This allows the output results file to have a specified name. If a file of the same name already exists in output\_location or the same **output\_file\_type**, a random string of characters will be appended to the end of the inputted output\_name to not overwrite any pre-existing file unless **overwrite\_existing\_output** is True. If nothing is given, it will generate a templated name for the output file. By default, this is None.



**overwrite\_existing\_output** (*Boolean*) - This parameter only comes into effect if **save\_results\_to\_file** is True. If True, if a pre-existing Excel file, text file, or CSV file already exists at the specified **output\_location**, it will be overwritten. By default, this is False.



**csv\_new\_line** (*String*) - This parameter only comes into effect if **output\_file\_type** is "csv" and **save\_results\_to\_file** is True.



**csv\_field\_size\_limit** (*Integer*) - This parameter only comes into effect if **output\_file\_type** is "csv" and **save\_results\_to\_file** is True.



**csv\_quotechar** (*String*) - This parameter only comes into effect if **output\_file\_type** is "csv" and **save\_results\_to\_file** is True.



**csv\_quoating\_minimal** (*Integer*) - This parameter only comes into effect if **output\_file\_type** is "csv" and **save\_results\_to\_file** is True.



**overwrite\_saved\_found\_matches** (*Boolean*) - This parameter only comes into effect if **save\_found\_matches** is True. Instead of the corresponding search result text file being used from "\_terms\_searched", said corresponding file will be overwritten if it exists. By default, this is False.



**terminal\_progress\_display\_enabled** (*Boolean*) - This parameters only comes into effect if tqdm module is installed/available. This allows the display of progress bar for data being processed by Chloe Felina and archived if using a terminal / command prompt display if set to True. This will NOT display or work properly in something like the Python IDLE. It will also result in the Chloe Felina performing slower than it would otherwise. By default, this is False.





**ChloeAI.clearSearchMemory**



Purpose: This will remove the "\_terms\_searched" folder that is used by **ChloeAI.searchQuery** in the database replace it with an empty folder of the same name.



Parameters:



N/A





**ChloeAI.findAllDuplicates**



NOT IMPLEMENTED YET





**ChloeAI.findEntityDuplicates**



NOT IMPLEMENTED YET







**ChloeAI.getTotalBytesRefEntities**



Purpose: This outputs the total size of the files that are being referenced in the database.



**check\_type** (*String* or *Tuple* or *List* or *Set*) - This parameter results in slightly different behavior depending upon if a string is inputted or a tuple/list/set is given. If a string is given, it expects "all"/"any"/"every" to check all entity types for the existence of entry\_string. If "doc"/"docx", "pdf", "txt", "shp", "img", or "gdb" is given, only the specified file type of Word Document, PDF, text file, shapefile, image files (i.e., TIFF/TIF, PNG, JPEG/JPG, and WebP), or file geodatabase, respectively, will be checked.



**terminal\_progress\_display\_enabled** (*Boolean*) - This parameters only comes into effect if tqdm module is installed/available. This allows the display of progress bar for data being processed by Chloe Felina and archived if using a terminal / command prompt display if set to True. This will NOT display or work properly in something like the Python IDLE. It will also result in the Chloe Felina performing slower than it would otherwise. By default, this is False.







**ChloeAI.getTotalNumRefEntities**



Purpose: This simply outputs an integer value of the number of items with referential data in the database.



**check\_type** (*String* or *Tuple* or *List* or *Set*) - This parameter results in slightly different behavior depending upon if a string is inputted or a tuple/list/set is given. If a string is given, it expects "all"/"any"/"every" to check all entity types for the existence of entry\_string. If "doc"/"docx", "pdf", "txt", "shp", "img", or "gdb" is given, only the specified file type of Word Document, PDF, text file, shapefile, image files (i.e., TIFF/TIF, PNG, JPEG/JPG, and WebP), or file geodatabase, respectively, will be checked.



**terminal\_progress\_display\_enabled** (*Boolean*) - This parameters only comes into effect if tqdm module is installed/available. This allows the display of progress bar for data being processed by Chloe Felina and archived if using a terminal / command prompt display if set to True. This will NOT display or work properly in something like the Python IDLE. It will also result in the Chloe Felina performing slower than it would otherwise. By default, this is False.

