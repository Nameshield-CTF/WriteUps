# We need you 1/5

By [Siorde](https://github.com/Siorde)

## Description
Interpol and the FBI have been investigating for over a year now. They are trying to get their hands on two hackers very well known for their ransomware and their ultra efficient botnet.

After long months of investigation, they managed to get their hands on one of their servers. But, when they got it back the PC caught fire because of a defense mechanism set up by the two hackers.

The hard drive could not be saved, but they had time to put the RAM in liquid nitrogen and analyze it later.

You know what you have to do!

For this first step, find the name of the PC!

## Solution
We got a .mem file, it means volatility. First thing to do is to use the "imageinfo" on the file.
```
$ vol.py imageinfo -f ../capture.mem
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/siord/capture.mem)
                      PAE type : PAE
                           DTB : 0x185000L
                          KDBG : 0x82780c28L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0x82781c00L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2021-04-19 17:30:00 UTC+0000
     Image local date and time : 2021-04-19 19:30:00 +0200
```
We need to find the hostname of the PC, so i used the envvars option because i was pretty sure that the computeur name was in the environnement variables.
```
$ vol.py --profile=Win7SP1x86_23418 -f ../capture.mem envars | grep -i computername 
Volatility Foundation Volatility Framework 2.6.1
     408 wininit.exe          0x0028f658 COMPUTERNAME                   KANNIBAL

```
So the flag is Hero{KANNIBAL}.
