# Triangle

By [Siorde](https://github.com/Siorde)

## Description
My friend encoded the flag with XOR but forgot the key! He remembers that its a 4 byte key. Can you recover the flag? 133f29027034094a33253126395b3704

## Solution
As the key is only 4 bytes long, it is easy to brut force. So i wrote a script in Python to do so.
The encypted message is in hexadecimal, so i thought that the result would be in hexadecimal too. And I knew that the flag would begin with "RTL{" and in hexadecimal it look like "\x52\x54\x4c\x7b". So I tried every 4 bytes keys and if the result contains "RTL{" I printed it.
```
#!/usr/bin/python
from itertools import cycle
import string

for a in string.printable:
    for b in string.printable:
        for c in string.printable:
            for d in string.printable:
                key = a+b+c+d
                #print(key)
                cryptedMessage = ''.join(chr(ord(c)^ord(k)) for c,k in zip("133f29027034094a33253126395b3704", cycle(key)))
                if "\x52\x54\x4c\x7b" in cryptedMessage :
                    print(cryptedMessage)
```
I ran it and I found the flag : RTL{1_l3rNT_x0R}
