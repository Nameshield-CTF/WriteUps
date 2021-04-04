# Follow up

By [Siorde](https://github.com/Siorde)

## Description
We got a clue from one of our investigators that an interesting secret was transferred in our network. Help us find out the secret.

## Solution
So we have a PCAP file and we need to find the flag in there.
First thing first, i grep for the "shatkictf" flag format.
```
tcpdump -qns 0 -A -r network1.pcapng | grep -i shaktictf
```
I didn't find anything, so i just look at the content of the file to see if i can find anything.
```
tcpdump -qns 0 -A -r network1.pcapng
```
And at the end their was : 
```
18:51:06.192015 IP 192.168.0.184.8280 > 192.168.0.184.43154: tcp 30
E..R.$@.@........... X..-0..m..U...@.......
..+<..+%https://pastebin.com/4NXGaVbA
```
And the flag was here : shaktictf{Th15_w4s_eA5Y!!}
