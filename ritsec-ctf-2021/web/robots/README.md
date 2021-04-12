# Robots

By [Siorde](https://github.com/Siorde)

## Description
Robots are taking over. Find out more.

## Solution
So i got a link with apparently nothing interesting on the page. But if i look at the sources i see that their is a blag "flag.txt" hidden. so i went to http://34.69.61.54:5247/flag.txt 
```
curl http://34.69.61.54:5247/flag.txt
VW05aWIzUnpJR0Z5WlNCMFlXdHBibWNnYjNabGNpQXVMaTQ9
```
It was a string encoded two time in base64
```
curl http://34.69.61.54:5247/flag.txt 2> /dev/null| base64 --decode | base64 --decode
Robots are taking over ...%
```
So it was not the flag...
</br>
From that string I tried the path /robots to see if i could get something but i got rickrolled. I had no more clue of where to look at, so i tried different path. And when I tried /flag I got the same redirection as the /robots. So i though maybe I should add .txt to the path /robots. I got a list of allow and disallow path. And while looking at it i found  :  
```
Allow: /flag/UlN7UjBib3RzX2FyM19iNGR9
```
So i decoded the string : 
```
echo UlN7UjBib3RzX2FyM19iNGR9  | base64 --decode
RS{R0bots_ar3_b4d}
```
And their was the flag ! 
