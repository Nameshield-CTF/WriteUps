# Expic

By [Siorde](https://github.com/Siorde)

## Description
https://drive.google.com/file/d/1JkkUxmz5Y3DpcbnY2Ens0_ove_2asiMu/view?usp=sharing

## Solution
We got a link to a google drive that point to a zip file. The zip file. I extracted it : 
```
$ unzip ex.zip
```
In the zip file there was a fiel named "photo" (with no extension). I used "file" to determined which type of file it was : 
```
$ file photo
photo: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, progressive, precision 8, 1000x667, components 3
```
Then I used exiftool to see the metadatas of the file : 
```
$ exiftool photo
ExifTool Version Number         : 11.88
File Name                       : photo
Directory                       : .
File Size                       : 136 kB
File Modification Date/Time     : 2021:07:05 12:19:49+02:00
File Access Date/Time           : 2021:07:31 21:53:21+02:00
File Inode Change Date/Time     : 2021:07:31 21:41:31+02:00
File Permissions                : rwxrwx---
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 12.16
Author                          : p4ul
Number                          : 68747470733a2f2f706173746562696e2e636f6d2f514632557a6a56590a
Profile CMM Type                : Linotronic
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 1998:02:09 06:49:00
Profile File Signature          : acsp
Primary Platform                : Microsoft Corporation
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Hewlett-Packard
Device Model                    : sRGB
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Hewlett-Packard
Profile ID                      : 0
Profile Copyright               : Copyright (c) 1998 Hewlett-Packard Company
Profile Description             : sRGB IEC61966-2.1
Media White Point               : 0.95045 1 1.08905
Media Black Point               : 0 0 0
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Device Mfg Desc                 : IEC http://www.iec.ch
Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB
Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1
Viewing Cond Illuminant         : 19.6445 20.3718 16.8089
Viewing Cond Surround           : 3.92889 4.07439 3.36179
Viewing Cond Illuminant Type    : D50
Luminance                       : 76.03647 80 87.12462
Measurement Observer            : CIE 1931
Measurement Backing             : 0 0 0
Measurement Geometry            : Unknown
Measurement Flare               : 0.999%
Measurement Illuminant          : D65
Technology                      : Cathode Ray Tube Display
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
Image Width                     : 1000
Image Height                    : 667
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1000x667
Megapixels                      : 0.667
```
The "number" was really odd and it looked like hexa, so I tried to convert it to ascii : 
```
$ echo 68747470733a2f2f706173746562696e2e636f6d2f514632557a6a56590a | xxd -r -p
https://pastebin.com/QF2UzjVY
```
The pastbin link gave us : "T0tLIApSVEx7MTBiYmE5YTUyNDE3MDk1ZGU1MWRiOTQ1NjM2MWQ3NDR9Cg==", which is totally base64 : 
```
$ echo "T0tLIApSVEx7MTBiYmE5YTUyNDE3MDk1ZGU1MWRiOTQ1NjM2MWQ3NDR9Cg" | base64 -d
OKK
RTL{10bba9a52417095de51db9456361d744}
```
So here we got the flag.
