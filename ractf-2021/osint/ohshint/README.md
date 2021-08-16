# OHSHINT

By [Siorde](https://github.com/Siorde)

## Description
Agent,

We've got an OSINT challenge for you. We've been tracking a suspect and found that he went on holiday within the UK recently. We've pulled a recent image from the suspect's social media.

Can you take a look and find out the rough location where this image was taken?

![alt image ot find](https://github.com/Nameshield-CTF/WriteUps/tree/master/ractf-2021/osint/ohshint/ressources/image.jpg?raw=true)

## Solution
We have a picture of a lake. It really doesn't help because a reverse search for the image just show a lot of different lake, and it's very hard to define if their is a match.

Instead I went for the metadata with exitfool : 
```
$ exiftool image.jpg 
ExifTool Version Number         : 11.88
File Name                       : image.jpg
Directory                       : .
File Size                       : 495 kB
File Modification Date/Time     : 2021:08:14 14:06:19+02:00
File Access Date/Time           : 2021:08:14 15:14:21+02:00
File Inode Change Date/Time     : 2021:08:14 14:06:19+02:00
File Permissions                : rwxrwx---
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Exif Byte Order                 : Big-endian (Motorola, MM)
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Artist                          : ractf{Help I'm stuck in this enterprise Java dev job and I'm slowly deteriorating}
Y Cb Cr Positioning             : Centered
GPS Version ID                  : 2.3.0.0
Description                     : Lodge North East of Lancaster, England. Big Lake
GPS Latitude                    : 45 deg 31' 32.65" N
GPS Longitude                   : 73 deg 35' 55.33" W
Author                          : Rick Astley
Comment                         : aHR0cHM6Ly93d3cueW91dHViZS5jb20vZW1iZWQvaEZjTHlEYjZuaUE/YXV0b3BsYXk9MSZjb250cm9scz0w
Image Width                     : 8284
Image Height                    : 1931
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 8284x1931
Megapixels                      : 16.0
GPS Latitude Ref                : North
GPS Longitude Ref               : West
GPS Position                    : 45 deg 31' 32.65" N, 73 deg 35' 55.33" W
```
Their is a location so I looked for it, but it was in Canada. It is a Ubisoft building, so I guessed it was a troll.

I also looked for the base64 comment : 
```
$ echo "aHR0cHM6Ly93d3cueW91dHViZS5jb20vZW1iZWQvaEZjTHlEYjZuaUE/YXV0b3BsYXk9MSZjb250cm9scz0w" |  base64 -d
https://www.youtube.com/embed/hFcLyDb6niA?autoplay=1&controls=0
```
It was a video about todd from Bethesda. So again,  a troll.

The last clue I had was the description. I looked for it on google, but I didn't found anything relevent. It seemed that their was no lake in Lancaster, but their is the lake disctrict on the north. I looked at the closest lake : Pine lake, and I felt like it was close to the picture we have. I tried this answer and I was right !
