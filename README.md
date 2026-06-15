# Chloe_Felina
Chloe Felina is approximately a Rule-Based Expert System designed with the philosophy of being configurable and being able to function without Cloud, Server, and/or Internet Connectivity. It is meant to be like a robust virtual assistant.

In order to properly utilize Chloe Felina, you must first initialize the database by:

```python
from chloeFelina import cat

felia = cat.CholeAI()
```

Having ChloeAI without parameters will automatically create a database folder in the current user's Documents folder called "datenaro". If you want to specify where database will be and/or the name, you can input them in parameters.

```python
from chloeFelina import cat

felia = cat.ChloeAI(database_location="explict/path/to/directory", database_name="Custom Name Here")
```

The main features of Chloe Felina are: finding items with a specified word/term/phrase embedded in them and scanning the database for duplicated instances of items.

It is extremely recommended to install the following modules via pip to get the most out of Chloe Felina:

- pillow (handles image files)
- openpyxl (allows creating outputs as Excel files)
- docx (handles Word files)
- docx2python (mainly helps with reading .doc files)
- pypdf (handles PDFs)

```
pip install pillow openpyxl docx docx2python pypdf
```

Made in loving dedication and memory to my precious feline pet, friend, and family member: Chloe Link.
