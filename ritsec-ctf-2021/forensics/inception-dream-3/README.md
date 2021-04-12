# Inception CTF: Dream 3

By [Siorde](https://github.com/Siorde)

## Description
While the first two steps were easy it’s all hard from here on out, ThePointMan is the most crucial role of the mission he has to be presentable but without giving away our intentions. Use Alternate Dream State to find the flag before the kick.

## Solution
First thing i uncompressed the archived from the last challenge : 
```
p7zip -d TheHotel.7z
Everything is Ok

Files: 3
Size:       158141
Compressed: 158376
```
First thing i noticed is that their was 3 files unzip. Except that I only saw 2 file in my folder. So i used the -al option :
```
ls -al 
total 164
-rw-rw-r-- 1 siord siord    126 févr. 24 19:29 ‎
drwxrwxr-x  2 siord siord   4096 avril  9 23:46 .
drwxr-xr-x 33 siord siord   4096 avril  9 23:47 ..
-rw-rw-r-- 1 siord siord 156968 févr. 24 19:35 SnowFortress.7z
-rw-rw-r-- 1 siord siord   1047 févr. 24 19:25 ThePointMan.txt
```
Their is an file with a blank name. I cat it (using autocompletion)
```
cat <200e> 
You mean, a dream within a dream? NTIgNDkgNTQgNTMgNDUgNDMgN2IgNDYgNDAgMjEgMjEgNjkgNmUgNjcgNDUgNmMgNjUgNzYgNDAgNzQgNmYgNzIgN2Q=% 
```
I decoded the base64 strings : 
```
echo NTIgNDkgNTQgNTMgNDUgNDMgN2IgNDYgNDAgMjEgMjEgNjkgNmUgNjcgNDUgNmMgNjUgNzYgNDAgNzQgNmYgNzIgN2Q= | base64 --decode
52 49 54 53 45 43 7b 46 40 21 21 69 6e 67 45 6c 65 76 40 74 6f 72 7d
```
Another hex string that i decoded : 
```
echo 52 49 54 53 45 43 7b 46 40 21 21 69 6e 67 45 6c 65 76 40 74 6f 72 7d | xxd -r -p
RITSEC{F@!!ingElev@tor}%
```
Their is the flag. So I guess the other file is a bait.
