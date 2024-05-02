

Steps for generating the JSON and files directory for the publication list. 


1. Export the library from Zotero:
    In Zotero, export "MyPapers" in BibTex format, ticking the "Export Files" option. 
    This generates a folder with a MyPapers.bib file, and subfolders labeled with numbers.

2. Convert the MyPapers.bib file to JSON:
    clone our fork of the bibtex2json python script
    > python /path/to/bibtex2bibjson.py MyPapers.bib 1> MyPapers.json
    ignore errors?

3. Copy PDFs into files root directory
   > find . -name "*.pdf" -type f -exec cp {} . \;