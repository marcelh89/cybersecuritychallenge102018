```file matrioska```
unzip  manually --> bruteforce... :(

at the end get get 1 file "matrioska" 

```file matrioska```
matrioska: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "mkfs.fat", 
sectors/cluster 4, root entries 512, sectors 400 (volumes <=32 MB), 
Media descriptor 0xf8, sectors/FAT 1, sectors/track 32, heads 64, 
serial number 0xb4c0042a, unlabeled, FAT (12 bit)


```fdisk -l matrioska```
Festplatte matrioska.img: 200 KiB, 204800 Bytes, 400 Sektoren
Einheiten: Sektoren von 1 * 512 = 512 Bytes
Sektorgröße (logisch/physikalisch): 512 Bytes / 512 Bytes
E/A-Größe (minimal/optimal): 512 Bytes / 512 Bytes
Festplattenbezeichnungstyp: dos
Festplattenbezeichner: 0x00000000


https://unix.stackexchange.com/questions/82314/how-to-find-the-type-of-an-img-file-and-mount-it


mount device with ```sudo mount matrioska /mnt/tmp``` or use 7zip to open the content...

README.txt..    Ah-ah, too late! I've already deleted the secret file!

is of type MAR-archieve --> Mozilla ARchive