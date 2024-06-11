

Steps for generating the JSON and files directory for the publication list. 

0. Clone bibtex2bibjson from forked reposistory - https://github.com/internaut/bibtex2bibjson
    This doesn't need to be `pip installed`, but the `bibtexparser` dependency likely does.

1. Export the library from Zotero:
    In Zotero, export "MyPapers" in BibTex format, ticking the "Export Files" option. 
    This generates a folder with a MyPapers.bib file, and subfolders labeled with numbers.

2. Convert the MyPapers.bib file to JSON:
    clone our fork of the bibtex2json python script
    > python /path/to/bibtex2bibjson.py MyPapers.bib 1> MyPapers.json

    If there are any documents that are erroring, they are put into the first 
    rows of the generated JSON document. Delete them.

3. Copy PDFs into files root directory
    The following command will copy all PDFs into the directory its called from.
    > find . -name "*.pdf" -type f -exec cp {} . \;

4. Copy the PDFs into the `content/pubs` directory. Copy the JSON file into `data/publications.json`.