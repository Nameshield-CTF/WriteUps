# Delete

By [Siorde](https://github.com/Siorde)

## Description
Sometimes what you see is not always true...

## Solution
We got a png file that couldn't be display. So the flag isn't in the picture, but hidden in the file.
First thing, i tried to do a "strings" on the file to see if the flag in the raw data.
```
strings chall.png | grep -i shaktictf
```
But their wasn't anything.
Second try, i looked for embedded files in the image
```
binwalk chall.png
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 264 x 191, 8-bit colormap, non-interlaced
48            0x30            PNG image, 1200 x 1200, 8-bit/color RGBA, non-interlaced
89            0x59            Zlib compressed data, default compression
```
I found this interresting second image (the 1200*1200 one) in the file. So i extreacted it : 
```
binwalk -D=".*" chall.png
```
And when i looked at the image, the flag was their : shakictf{Y0u_4R3_aM4z1nG!!!!}
