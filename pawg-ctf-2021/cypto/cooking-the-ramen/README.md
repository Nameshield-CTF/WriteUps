# Cookin the Ramen

By [Siorde](https://github.com/Siorde)

## Description
Apparently we made cookin the books too hard, here's some ramen to boil as a warmup: .--- ...- ...- . ....- ...- ... ..--- .. .-. .-- --. -.-. .-- -.- -.-- -. -... ..--- ..-. -.-. ...- ...-- ..- --. .--- ... ..- .. --.. -.-. .... -- ...- -.- . ..- -- - . -. ...- -. ..-. --- -.-- --.. - .-.. .--- --.. --. --. ...-- ... -.-. -.- ..... .--- ..- --- -. -.- -..- -.- --.. -.- ...- ..- .-- - -.. .--- -... .... ..-. --. --.. -.- -..- .. --.. .-- ...- ... -- ...-- --.- --. ..-. ... .-- --- .--. .--- .....

## Solution
It's clearly morse code, so i used online tool to decode it : https://morsedecoder.com/ </br>
I got : JVVE4VS2IRWGCWKYNB2FCV3UGJSUIZCHMVKEUMTENVNFOYZTLJZGG3SCK5JUONKXKZKVUWTDJBHFGZKXIZWVSM3QGFSWOPJ5 </br>
I tried to decode it as base64 but it wasn't that.</br>
I used the tool https://gchq.github.io/CyberChef/ with the "magic" option.</br>
It show me that the string is encode in base32 then in base64 and finally in base58.</br>
So i got the flag : DawgCTF{0k@y_r3al_b@by's_f1r5t}
