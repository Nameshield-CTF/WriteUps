# We need you 3/5

By [Siorde](https://github.com/Siorde)

## Description
We know for sure that this server allowed to connect to infected machines. Can you check if a connection was instantiated?

## Solution
This one is about a connection so i tried to use the netscan module : 
```
$ vol.py --profile=Win7SP1x86_23418 -f ../capture.mem netscan
Volatility Foundation Volatility Framework 2.6.1
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0xaace668          TCPv4    -:49164                        192.168.1.1:443      CLOSED           3504     iexplore.exe
0xfae7330          TCPv4    -:49173                        13.107.13.80:80      CLOSED           3504     iexplore.exe
0x246fef50         UDPv6    ::1:51920                      *:*                                   1456     svchost.exe    2021-04-19 17:19:34 UTC+0000
0x7c707240         UDPv4    10.0.2.15:1900                 *:*                                   1456     svchost.exe    2021-04-19 17:19:34 UTC+0000
0x7df8d5a0         UDPv4    127.0.0.1:61225                *:*                                   3504     iexplore.exe   2021-04-19 17:23:25 UTC+0000
0x7e013298         UDPv4    10.0.2.15:138                  *:*                                   4        System         2021-04-19 17:17:38 UTC+0000
0x7e02f6d0         UDPv4    0.0.0.0:0                      *:*                                   1188     svchost.exe    2021-04-19 17:17:38 UTC+0000
0x7e02f6d0         UDPv6    :::0                           *:*                                   1188     svchost.exe    2021-04-19 17:17:38 UTC+0000
0x7e05a660         UDPv4    0.0.0.0:3702                   *:*                                   1456     svchost.exe    2021-04-19 17:17:44 UTC+0000
0x7e05a660         UDPv6    :::3702                        *:*                                   1456     svchost.exe    2021-04-19 17:17:44 UTC+0000
0x7e07cb10         UDPv6    ::1:1900                       *:*                                   1456     svchost.exe    2021-04-19 17:19:34 UTC+0000
0x7e08bd10         UDPv4    0.0.0.0:3702                   *:*                                   1456     svchost.exe    2021-04-19 17:17:44 UTC+0000
0x7e094aa0         UDPv4    127.0.0.1:1900                 *:*                                   1456     svchost.exe    2021-04-19 17:19:34 UTC+0000
0x7e0be550         UDPv4    0.0.0.0:5355                   *:*                                   1188     svchost.exe    2021-04-19 17:17:42 UTC+0000
0x7e094aa0         UDPv4    127.0.0.1:1900                 *:*                                   1456     svchost.exe    2021-04-19 17:19:34 UTC+0000
0x7e0be550         UDPv4    0.0.0.0:5355                   *:*                                   1188     svchost.exe    2021-04-19 17:17:42 UTC+0000
0x7e0c9c68         UDPv4    0.0.0.0:3702                   *:*                                   1456     svchost.exe    2021-04-19 17:17:44 UTC+0000
0x7e0c9c68         UDPv6    :::3702                        *:*                                   1456     svchost.exe    2021-04-19 17:17:44 UTC+0000
0x7e221230         UDPv6    fe80::61b0:3a44:7ba4:e7df:1900 *:*                                   1456     svchost.exe    2021-04-19 17:19:34 UTC+0000
0x7e278008         UDPv4    127.0.0.1:51921                *:*                                   1456     svchost.exe    2021-04-19 17:19:34 UTC+0000
0x7e295d78         UDPv4    0.0.0.0:5355                   *:*                                   1188     svchost.exe    2021-04-19 17:17:42 UTC+0000
0x7e295d78         UDPv6    :::5355                        *:*                                   1188     svchost.exe    2021-04-19 17:17:42 UTC+0000
0x7e35b008         UDPv4    0.0.0.0:3702                   *:*                                   1456     svchost.exe    2021-04-19 17:17:44 UTC+0000
0x7e3d23e8         UDPv4    0.0.0.0:56557                  *:*                                   1456     svchost.exe    2021-04-19 17:17:35 UTC+0000
0x7e3d23e8         UDPv6    :::56557                       *:*                                   1456     svchost.exe    2021-04-19 17:17:35 UTC+0000
0x7e3d2a00         UDPv4    0.0.0.0:56556                  *:*                                   1456     svchost.exe    2021-04-19 17:17:35 UTC+0000
0x7e3e8598         UDPv4    10.0.2.15:137                  *:*                                   4        System         2021-04-19 17:17:38 UTC+0000
0x7e0c9910         TCPv4    0.0.0.0:49156                  0.0.0.0:0            LISTENING        500      lsass.exe
0x7e0c9b38         TCPv4    0.0.0.0:49156                  0.0.0.0:0            LISTENING        500      lsass.exe
0x7e0c9b38         TCPv6    :::49156                       :::0                 LISTENING        500      lsass.exe
0x7e207aa0         TCPv4    0.0.0.0:49153                  0.0.0.0:0            LISTENING        800      svchost.exe
0x7e207aa0         TCPv6    :::49153                       :::0                 LISTENING        800      svchost.exe
0x7e2173b0         TCPv4    10.0.2.15:139                  0.0.0.0:0            LISTENING        4        System
0x7e2b5008         TCPv4    0.0.0.0:49154                  0.0.0.0:0            LISTENING        976      svchost.exe
0x7e2b59c8         TCPv4    0.0.0.0:49154                  0.0.0.0:0            LISTENING        976      svchost.exe
0x7e2b59c8         TCPv6    :::49154                       :::0                 LISTENING        976      svchost.exe
0x7e321500         TCPv4    0.0.0.0:49155                  0.0.0.0:0            LISTENING        492      services.exe
0x7e321500         TCPv6    :::49155                       :::0                 LISTENING        492      services.exe
0x7e3217d0         TCPv4    0.0.0.0:49155                  0.0.0.0:0            LISTENING        492      services.exe
0x7e3acc28         TCPv4    0.0.0.0:445                    0.0.0.0:0            LISTENING        4        System
0x7e3acc28         TCPv6    :::445                         :::0                 LISTENING        4        System
0x7e3d6db8         TCPv4    0.0.0.0:5357                   0.0.0.0:0            LISTENING        4        System
0x7e3d6db8         TCPv6    :::5357                        :::0                 LISTENING        4        System
0x7e117df8         TCPv4    -:49163                        192.168.1.1:443      CLOSED           3504     iexplore.exe
0x7e5bf1f0         TCPv4    0.0.0.0:135                    0.0.0.0:0            LISTENING        748      svchost.exe
0x7e5bf1f0         TCPv6    :::135                         :::0                 LISTENING        748      svchost.exe
0x7e5bfce8         TCPv4    0.0.0.0:135                    0.0.0.0:0            LISTENING        748      svchost.exe
0x7e5cd9a0         TCPv4    0.0.0.0:49152                  0.0.0.0:0            LISTENING        408      wininit.exe
0x7e5cdd90         TCPv4    0.0.0.0:49152                  0.0.0.0:0            LISTENING        408      wininit.exe
0x7e5cdd90         TCPv6    :::49152                       :::0                 LISTENING        408      wininit.exe
0x7e5ff4c0         TCPv4    0.0.0.0:49153                  0.0.0.0:0            LISTENING        800      svchost.exe
0x7f0277f0         UDPv4    127.0.0.1:62647                *:*                                   3404     iexplore.exe   2021-04-19 17:23:26 UTC+0000
0x7ee41538         TCPv4    10.0.2.15:49159                146.59.156.82:4444   ESTABLISHED      3296     nc.exe
0x7fc65290         UDPv4    0.0.0.0:0                      *:*                                   692      VBoxService.ex 2021-04-19 17:28:38 UTC+0000
0x7fc8a558         UDPv4    0.0.0.0:0                      *:*                                   692      VBoxService.ex 2021-04-19 17:28:53 UTC+0000
0x7fc96008         UDPv4    0.0.0.0:0                      *:*                                   692      VBoxService.ex 2021-04-19 17:28:48 UTC+0000
0x7fc9c8a0         UDPv4    0.0.0.0:0                      *:*                                   692      VBoxService.ex 2021-04-19 17:28:43 UTC+0000
0x7fcbee28         UDPv4    0.0.0.0:0                      *:*                                   692      VBoxService.ex 2021-04-19 17:29:58 UTC+0000
```
Their is not a lot of connection, and when i was diggin for the previous challenge i found that nc.exe was in a folder named "malw4r3", so that was pretty obvious that the 146.59.156.82:4444 was the answer.
So the flag is Hero{146.59.156.82:4444}.
