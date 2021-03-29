# notes

By [Siorde](https://github.com/Siorde)

## Description
The breach seems to have originated from this host. Can you find the user's mistake? Here is a memory image of their workstation from that day.

## Solution
All we got is a memory dump. So obviously i'm gonna use Volatility to try to get the flag.
```
vol.py imageinfo -f ../image.mem
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/siord/image.mem)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf80002a3b0a0L
          Number of Processors : 6
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002a3cd00L
                KPCR for CPU 1 : 0xfffff880009f1000L
                KPCR for CPU 2 : 0xfffff88002ea9000L
                KPCR for CPU 3 : 0xfffff88002f1f000L
                KPCR for CPU 4 : 0xfffff88002f95000L
                KPCR for CPU 5 : 0xfffff88002fcb000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2021-03-20 18:16:12 UTC+0000
     Image local date and time : 2021-03-20 13:16:12 -0500
```

Now that we have the profile, we can list the process that were in use : 
```
vol.py --profile=Win7SP1x64 -f ../image.mem pslist
Volatility Foundation Volatility Framework 2.6.1
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xfffffa8000ca0040 System                    4      0    173      526 ------      0 2021-03-20 18:57:47 UTC+0000
0xfffffa8002232b30 smss.exe                572      4      3       34 ------      0 2021-03-20 18:57:47 UTC+0000
0xfffffa80026287f0 csrss.exe               656    640     10      394      0      0 2021-03-20 18:57:49 UTC+0000
0xfffffa8001e6e7c0 wininit.exe             688    640      3       82      0      0 2021-03-20 18:57:49 UTC+0000
0xfffffa8000cae240 csrss.exe               708    696     10      249      1      0 2021-03-20 18:57:49 UTC+0000
0xfffffa8001ff4b30 services.exe            744    688      8      205      0      0 2021-03-20 18:57:49 UTC+0000
0xfffffa80020ecb30 lsass.exe               760    688      9      564      0      0 2021-03-20 18:57:49 UTC+0000
0xfffffa8001e497c0 lsm.exe                 768    688     10      149      0      0 2021-03-20 18:57:49 UTC+0000
0xfffffa8002195b30 svchost.exe             868    744     10      371      0      0 2021-03-20 18:57:49 UTC+0000
0xfffffa80022ce680 VBoxService.ex          928    744     13      146      0      0 2021-03-20 18:57:49 UTC+0000
0xfffffa8001f974e0 svchost.exe             988    744      8      268      0      0 2021-03-20 17:57:51 UTC+0000
0xfffffa8001e9d060 svchost.exe             604    744     20      476      0      0 2021-03-20 17:57:51 UTC+0000
0xfffffa80023e62d0 svchost.exe             736    744     17      458      0      0 2021-03-20 17:57:51 UTC+0000
0xfffffa80023eab30 svchost.exe             980    744     27      791      0      0 2021-03-20 17:57:51 UTC+0000
0xfffffa8002455b30 svchost.exe            1164    744     16      486      0      0 2021-03-20 17:57:51 UTC+0000
0xfffffa8002605890 svchost.exe            1264    744     16      426      0      0 2021-03-20 17:57:52 UTC+0000
0xfffffa8002623b30 spoolsv.exe            1356    744     12      311      0      0 2021-03-20 17:57:52 UTC+0000
0xfffffa8001f55890 svchost.exe            1384    744     17      317      0      0 2021-03-20 17:57:52 UTC+0000
0xfffffa800273d060 svchost.exe            1480    744     16      310      0      0 2021-03-20 17:57:52 UTC+0000
0xfffffa800274eb30 WLIDSVC.EXE            1572    744      8      257      0      0 2021-03-20 17:57:52 UTC+0000
0xfffffa8002b7a910 SearchIndexer.         1888    744     14      673      0      0 2021-03-20 17:57:52 UTC+0000
0xfffffa8002beb2e0 winlogon.exe           2004    696      3      116      1      0 2021-03-20 17:57:53 UTC+0000
0xfffffa8002cc7b30 WLIDSVCM.EXE            696   1572      3       58      0      0 2021-03-20 17:57:53 UTC+0000
0xfffffa8002da5060 taskhost.exe           2156    744      8      152      1      0 2021-03-20 17:57:53 UTC+0000
0xfffffa8002bbeb30 dwm.exe                2236    736      3       94      1      0 2021-03-20 17:57:54 UTC+0000
0xfffffa8002818060 explorer.exe           2288   2216     27      898      1      0 2021-03-20 17:57:54 UTC+0000
0xfffffa8002e1db30 VBoxTray.exe           2432   2288     15      156      1      0 2021-03-20 17:57:54 UTC+0000
0xfffffa8002de2b30 wmpnetwk.exe           2736    744      9      219      0      0 2021-03-20 17:58:00 UTC+0000
0xfffffa80010cc460 FTK Imager.exe         1552   2708     17      429      1      0 2021-03-20 17:59:24 UTC+0000
0xfffffa8000dd0060 notepad.exe            2696   2288      4      309      1      0 2021-03-20 17:59:34 UTC+0000
0xfffffa8000de7b30 mscorsvw.exe           2104    744      7       92      0      1 2021-03-20 17:59:53 UTC+0000
0xfffffa8002f82590 mscorsvw.exe           1724    744      7       87      0      0 2021-03-20 17:59:53 UTC+0000
0xfffffa8002773090 SearchProtocol         3292   1888      8      284      0      0 2021-03-20 18:15:53 UTC+0000
0xfffffa800213e4e0 SearchFilterHo         1740   1888      5      103      0      0 2021-03-20 18:15:53 UTC+0000
```

As the title of the challenge is "notes", i thought that we could have the next step in the notepad.exe. So i dumped the memory of this process.
```
vol.py --profile=Win7SP1x64 -f ../image.mem memdump --pid 2696 --dump-dir ./
Volatility Foundation Volatility Framework 2.6.1
************************************************************************
Writing notepad.exe [  2696] to 2696.dmp

```

Then, i looked in the .dmp to see i find a match with the flag format : 
```
strings -e l 2696.dmp | grep -i "umass" 
UMASS{$3CUR3_$70Rag3}
```

Challenge Validated
