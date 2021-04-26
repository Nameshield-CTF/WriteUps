# We need you 2/5

By [Siorde](https://github.com/Siorde)

## Description
It must be their team name.

For this second step, find the user's name and password in clear text.

## Solution
I alredy had to do this in a previous CTF so i knew how to do it.
First we list the registry hive
```
$ vol.py --profile=Win7SP1x86_23418 -f ../capture.mem hivelist
Volatility Foundation Volatility Framework 2.6.1
Virtual    Physical   Name
---------- ---------- ----
0x8b0a1008 0x6b1ed008 \??\C:\Windows\ServiceProfiles\NetworkService\NTUSER.DAT
0x8b12d008 0x697f4008 \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT
0x9b1d89c8 0x79a459c8 \SystemRoot\System32\Config\SECURITY
0x9fee59c8 0x3c8ab9c8 \??\C:\Users\Razex\ntuser.dat
0x9fefc008 0x6fd89008 \??\C:\Users\Razex\AppData\Local\Microsoft\Windows\UsrClass.dat
0x823859c8 0x2b5d99c8 \SystemRoot\System32\Config\SAM
0x8940c5e8 0x2d5415e8 [no name]
0x8941a2c0 0x2d58d2c0 \REGISTRY\MACHINE\SYSTEM
0x89441008 0x2d436008 \REGISTRY\MACHINE\HARDWARE
0x894ca4c8 0x5fa804c8 \SystemRoot\System32\Config\DEFAULT
0x895975c0 0x2d4165c0 \Device\HarddiskVolume1\Boot\BCD
0x8a5fb008 0x13776008 \SystemRoot\System32\Config\SOFTWARE
0x8b04e9c8 0x3e6ad9c8 \??\C:\System Volume Information\Syscache.hve
```
Then we need to extract the hashes
```
$ vol.py --profile=Win7SP1x86_23418 -f ../capture.mem hashdump -y 0x8941a2c0 -s 0x823859c8 
Volatility Foundation Volatility Framework 2.6.1
Administrateur:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Invit:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Razex:1000:aad3b435b51404eeaad3b435b51404ee:78d9c7e905c695087ee3baa755ce43e4:::
```
We have the username, and going to https://crackstation.net gave me the password (you need to paste only the last part : 78d9c7e905c695087ee3baa755ce43e4)
So the flag is Hero{Razex:liverpoolfc123}.
