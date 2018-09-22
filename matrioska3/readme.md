Dependencies
===

sudo dnf install lbzip2 pbzip2 p7zip

Instruction
===

```unzip matrioska```

```cd dev/shm```

```file matrioska.tmp.kklgsp ```
matrioska.tmp.kklgsp: gzip compressed data, was "matrioska.tmp.EKdhx3", last modified: Tue Aug 28 08:44:32 2018, from Unix, original size 53321


```mv matrioska.tmp.kklgsp matrioska.tmp.kklgsp.gz```


```gunzip -rf matrioska.tmp.kklgsp```

```file matrioska.tmp.kklgsp ```
matrioska.tmp.kklgsp: bzip2 compressed data, block size = 900k

//TODO find out file type like bzip2, gzip, 7zip

```mv matrioska.tmp.kklgsp matrioska.tmp.kklgsp.bz2```
```lbzip2 -d my_file.bz2``` or 
```pbzip2 -d my_file.bz2```

matrioska.tmp.kklgsp: 7-zip archive data, version 0.

mv matrioska.tmp.kklgsp matrioska.tmp.kklgsp.7za

7za e <filename>


Types
===
* matrioska.tmp.tijddG: Zip archive data, at least v2.0 to extract
* matrioska.tmp.kklgsp: bzip2 compressed data, block size = 900k
* matrioska.tmp.kklgsp: 7-zip archive data, version 0.
* matrioska.tmp.kklgsp: gzip compressed data, was "matrioska.tmp.EKdhx3", last modified: Tue Aug 28 08:44:32 2018, from Unix, original size 53321
* README.txt: MAR archive data


Tools
===
* zip - ```unzip filename>```
* bz2 - ```pbzip2 -d filename>.bz2```
* 7za - ``` 7za e <filename>.7za```
* gz - ```gunzip -rf <filename>.gz```
