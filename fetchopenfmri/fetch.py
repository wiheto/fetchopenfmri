
# Script loads

import os
from bs4 import BeautifulSoup
import re
import zipfile
import tarfile
import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen, urlretrieve
elif sys.version_info[0] == 2:
    from urllib2 import urlopen
    from urllib import urlretrieve



def main():
    if len(sys.argv)==3:
        get_dataset(sys.argv[1],sys.argv[2])
    elif len(sys.argv)==4:
        get_dataset(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        raise ValueError('Inputs must be \">fetchopenfmri 123 ./path/to/save/\ [1/0]" where 123 corresponds with an openfmri dataset number (with or without zeros). The final argument is 0 or 1 and removes the compression.')



def untar_or_unzip(datasetDir,f):
    if zipfile.is_zipfile(datasetDir + f):
        zf=zipfile.ZipFile(datasetDir + f)
        zf.extractall(datasetDir)
        zf.close()
    elif tarfile.is_tarfile(datasetDir + f):
        with tarfile.open(datasetDir+f) as tf:
            tf.extractall(datasetDir)
            tf.close()


def get_dataset(ds,dataDir,removecompressed=1):

    """
    A function which attempts downloads and uncompresses the latest version of an openfmri.fmri dataset.

    PARAMETERS

    :ds: dataset number of the openfMRI.org dataset (integer) without zero padding. I.e. can just be 212 (doesn't need to be 000212).
    :dataDir: where to save the data. Will get saved in 'dataDir/openfmri/ds000XXX'
    :removecompressed: delete compressed data once unzipped. 1=yes. 0=no.

    NOTES
    There is no "default" way to download data from openfMRI so this solution is a little hacky. It may not be a universal functoin and it is best to verify that all necessary data has been downloaded.

    """
    #Convert input ds to string incase it is put in via function
    ds = str(ds)
    #The final character of the dataset can be a letter
    lettersuffix=''
    if re.search('[A-Za-z]$',ds):
        lettersuffix = ds[-1]
        ds = ds[:-1]
    openfMRI_dataset_string = '{0:06d}'.format(int(ds)) + lettersuffix
    #Some datasets include
    try:
        os.mkdir(dataDir)
    except:
        pass

    datasetDir = os.path.join(dataDir, 'openfmri/')

    try:
        os.mkdir(datasetDir)
    except:
        pass

    openfMRI_url = 'https://openfmri.org/dataset/ds' + openfMRI_dataset_string + '/'
    r = urlopen(openfMRI_url).read()
    soup = BeautifulSoup(r,'lxml')

    #Isolate only the links from the latest revision. The text "data associated with revision". If the website changes its static text, this  needs to be changed
    unformatted_soup=soup.prettify()
    firstOccurance=unformatted_soup.find('Data Associated with Revision')
    secondOccurancce=unformatted_soup[firstOccurance+1:].find('Data Associated with Revision')
    #If there is only one "Data Associated..." (i.e. only one revision) this returns -1. This should be kept. Otherwise add on the firstOccurance index
    if secondOccurancce != -1:
        secondOccurancce+=firstOccurance
    #The latest links are confined within this part of the text
    soup_latestversion = BeautifulSoup(unformatted_soup[firstOccurance:secondOccurancce],'lxml')

    # Loop through all links and dowload files
    filelist = []
    for a in soup_latestversion.find_all('a', href=True):
        #This assumes that all files include ds....
        if re.search('ds[A-Za-z_0-9.-]*$',a['href']):
            filename_start=re.search('ds[A-Za-z_0-9.-]*$',a['href']).start()
            filelist.append(a['href'][filename_start:])
            print('Downloading: ' + a['href'][filename_start:])
            urlretrieve(a['href'],datasetDir + a['href'][filename_start:])
    print('--- Download complete ---')
    for f in filelist:
        untar_or_unzip(datasetDir,f)
    print('--- Uncompressing complete ---')
    if removecompressed==1:
        for f in filelist:
            print('Clean up. Deleting: ' + f)
            os.remove(datasetDir+f)
        print('--- Clean up complete ---')
    print('NOTE: It is best to verify manually that all the correct data has been downloaded and uncompressed correctly. \n If data is used in any publication, see openfmri.org about how to appropriately cite/credit the data.')
    print('--- Script complete ---')


if __name__ == "__main__":
    main()
