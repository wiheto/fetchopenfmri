
#Fetchopenfmri

Small script I made that fetches datasets from www.openfmri.org

### Install:  

```
pip install fetchopenfmri
```

To run via command-line type:


### Run

```
fetchopenfmri <datasetnumber> /path/to/save [0/1]
```

The dataset number can be with or without the zeros. I.e. 123 will download dataset 000123.

Uncompressed files will get saved in `/path/to/save/openfmri/ds000<datasetnumber>/`. Compressed files, if kept, are found in `/path/to/save/openfmri/`

The final argument is optional and is either a 0 or 1 (1 is the default). If 1, the compressed files will be deleted after they are uncompressed. 0 will keep them.

__After running fetchopenfmri it is best to manually check via openfmri that all files were downloaded. There may be some reason that the script breaks on certain datasets. If that happens, leave an issue and I will fix it. Furthermore, the user should note which version of data they are using and how to appropriately credit openfmri and the data providers.__

Only tested to work on python 3 and Linux. In principle should work for other OSX (Need to double check a few thinks for windows) and should work for python 2. None of these are tested though. If anyone runs into any problems, leave an issue.


### How do I find the dataset number at openfmri?

It is called the "Accession Number".  Can be found on each individual dataset page or https://openfmri.org/dataset/

### How does it work?

As different versions of datasets get new their download links modified and different datasets have different amount of links,  the solution is a little hacky, but it seems to work.

First, the script "scrapes" the openfmri dataset page with BeautifulSoup. It then splits the page by finding all instances of "Data Associated with Revision" and takes all the download links that occur from the first instance of this phrase to the second (or the end of the page if there is only one release). This is a static phrase that appears before every release for each dataset. The script cycles through the links and downloads the corresponding file.

These files will always be compressed so the script also automatically uncompresses them (only tar or zip files). If the compression is of any other file type (which may be the case, but I havn't seen them yet) the files will remain compressed. (In such cases, it is best to add a 0 in the third argument so that the compressed files are not deleted.)

### Version and citation of openfmri

The latest available version is downloaded. At the moment it does not tell the user which version has been downloaded. Nor is there any information regarding the licence and how to cite from openfmri. At the moment is the user's own responsibility to find this out. Perhaps I will add a file about this in the future.
