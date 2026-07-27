# Chloe_Felina
Chloe Felina can be roughly classified as a hybrid of a rule-based expert system and data-driven inference engine.

Chloe Felina has been designed with the philosophy of being able to function fully offline and work on any computer with Windows OS installed on it as well as acting as a virtual helper/assistant. It is not as feature-rich as I desire it to be. Currently, the Dynamic Term Search Query System and the In-Depth Streamlined Duplicate Finding System are the only things fully implemented.

***

While Windows has a built-in feature for File Explorer that allows you to search file and folder names as well as their contents including metadata, you have to search within multiple folders to find what you are looking for or have it search the entirety of a drive, which tends to be slow, the Dynamic Term Search Query System is a lot faster and easier to use as it only requires Chloe Felina gathering data on a specified directory and/or nested directories for it to search for the existence of a term and then quickly check the database for any entities that have that term present. In addition, once a term has been search, if the term is search again or any future searches contain it, it will referenced the saved search results and use only those search results to check for the presence of the term. For example, say you inputted "plagioclase" as a search term and got the results for it. The entities found to have that term present will be saved for future reference. If you then inputted "plagioclase feldspar" as a search, instead of checking the entirety of Chloe Felina's database, it will note that "plagioclase" has already had its results determined and check for all the entities that have "plagioclase" in them for "plagioclase feldspar" allowing the execution time for finding entities that have the term to be cut to a fraction of what it would be if the entire database was checked. It will not search for "plagioclase" and "feldspar" separately. In addition, capitalization is ignored when conducting searches. You can turn off/disable this "terms searched caching" feature; however, it is extremely recommended that you leave it enabled by default. There is also the option to search file names only instead of checking the contents of files as well.

A more practicle use case for searchQuery would be the following example. Say you are wanting to find that document of that thesis paper you worked on for college cannot remember what it is called but do remember some keywords of what the thesis paper entailed. Also, you know that it is located somewhere in your Documents folder but you don't know where as it is a cluttered mess of random files and folders. With Chloe Felina, all you'd need to do, for example, is:

```python
from chloeFelina import cat

felia = cat.ChloeAI()
felia.getNestedDirectoryData("C:/Users/YOURUSERNAME/Documents")
felia.searchQuery("thesis",save_results_to_file=True,output_name="FindMyThesisPaper")
```

In order to properly utilize Chloe Felina, you must first initialize the database by:

```python
from chloeFelina import cat

felia = cat.CholeAI()
```

Having _ChloeAI_ without parameters will automatically create a database folder in the current user's Documents folder called "datenaro". If you want to specify where database will be and/or the name, you can input them in parameters.

```python
from chloeFelina import cat

felia = cat.ChloeAI(database_location="explict/path/to/directory", database_name="Custom Name Here")
```

***

The In-Depth Streamlined Duplicate Finding System is just a fancy way of saying a complex and dynamic algorithm that can very quickly find potential duplicate files/entities if the data is already within the Chloe Felina database that the user has generated. The reason "potential" is stressed for duplicates being found is that, despite efforts to minimize false positives as much as possible, there are still some extreme and niche scenarios where false positives will be produced, especially with image files since aside from applying more storage and resource straining methodologies black-and-white and/or grayscale image files run a high risk of producing false positives. Without getting into the minute details, despite what the code may look like at first glance, the process is very straightforward. Essentially, entities/files are grouped together based upon their type and the number of lines that the data extracted from them contains are used to prevent completely redundant comparisons between files/entities. A text file with 25 lines will never end up being a duplicate of another text file with 26 lines. In addition, the number of times files within the Chloe Felina database are accessed are minimized as much as possible to fully reduce execution time as well as skipping doing comparsions to files/entities that have already been matched with other files/entities.

***

It is extremely recommended to install the following modules via pip to get the most out of Chloe Felina:

- _pillow_ (handles image files)
- _openpyxl_ (allows creating outputs as Excel files)
- _docx_ (handles Word files)
- _docx2python_ (mainly helps with reading .doc files)
- _pypdf_ (handles PDFs)
- _win32api_ (required to utilize the full functionality of _chloeFelina.cat.ChloeAI.updateAndRefreshArchive_)
- _tqdm_ (for optional display of progress)

```
pip install pillow openpyxl docx docx2python pypdf pywin32 tqdm
```

**Note**: The only version requirements for these modules and their dependencies are compatibility with CPython 3.11+.

In order to apply and/or check for updates to the prior listed modules, use the following command for pip:

```
pip install pillow openpyxl docx docx2python pypdf pywin32 tqdm --upgrade
```

In order to better understand how to utilize Chloe Felina, please read and consult the Parameters_Guide.md file included with Chloe Felina.

***

Made in loving dedication and memory to my precious feline pet, friend, and family member: Chloe Link.

![alt text](https://github.com/ajflink001/Chloe_Felina/blob/main/chloeFelina/C02A98C0-53E0-4B02-B376-D47EA41D2232_1_105_c.jpeg?raw=True)
