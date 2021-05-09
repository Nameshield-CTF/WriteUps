# Crack IFS 

By [Siorde](https://github.com/Siorde)

## Description
The accounts in this QNX IFS have insecure passwords. Crack them to assemble the flag.</br>

https://www.qnx.com/developers/docs/7.0.0/#com.qnx.doc.neutrino.building/topic/intro/intro_ifs.html

## Solution
We have an IFS file. On the link they gave us, we understand that this is a file system image.</br>
I looked to uncompress the file, and found the tool dumpifs : https://github.com/askac/dumpifs
I dumped all the files in the ifs image : 
```
$ dumpifs ./DawgCTF.ifs -x -b
```
We got a shadow and passwd file. The password are crypted, but as i have done it in a previous CTF i knew how to brutforce it using john the ripper.
```
$ unshadow passwd shadow > unshadowed.txt
$ john --wordlist=../rockyou.txt unshadowed.txt
root:cram:0:0:Superuser:/root:/bin/sh
```
I got only one of the five password, but thought that every password would be 4 characters, so i can try the incremental way.</br>
I updated the conf file of john the ripper to look only for 4 characters password and run : 
```
$ john -incremental unshadowed.txt
$ john --show unshadowed.txt
root:cram:0:0:Superuser:/root:/bin/sh
user:CTF{:100:100::/home/user:/bin/sh
guest:ble}:101:100::/home/guest:/bin/sh
joe:un_s:102:100::/home/joe:/bin/sh
bob:Dawg:103:100::/home/bob:/bin/sh
```
So the flag is Dawg{un_scramble} ! 
