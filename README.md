
#Fetchopenfmri

Small script I made that fetches datasets from openfmri.org

### Install:  

```
pip install fetchopenfmri
```

To run via command-line type:


### Run

```
fetchopenfmri <datasetnumber> /path/to/save
```

The dataset number can be with or without the zeros. I.e. 123 will download dataset 000123.

Files will get saved in `/path/to/save/openfmri/ds000123/`

__After running fetchopenfmri it is best to manually check via openfmri that all files were downloaded. There may be some reason that the script breaks on certain datasets. If that happens, leave an issue and I will fix it. Furthermore, the user should note which version of data they are using and how to appropriately credit openfmri and the data providers.__

Only tested to work on python 3 and Linux. In principle should work for other OS and python 2 but not tested. If anyone runs into any problems, leave an issue.

### How do I find the dataset number at openfmri?

It is called the "Accession Number".  Can be found on each individual dataset page or https://openfmri.org/dataset/

### Version and citation of openfmri

The latest available version is downloaded. At the moment it does not tell the user which version has been downloaded. Nor is there any information regarding the licence and how to cite from openfmri. At the moment is the user's own responsibility to find this out. Perhaps I will add a file about this in the future.
