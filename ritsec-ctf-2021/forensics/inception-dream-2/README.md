# Inception CTF: Dream 2

By [Siorde](https://github.com/Siorde)

## Description
Unfortunately, the subconscious isn’t enough for this mission, we have to kidnap Fischer we need to go further into the system of the mind. Use the flag found to edit the PowerShell script, entering the Flag in line three in-between the single quotes. Run the PowerShell script and wait for it to complete its actions.

## Solution
Not much complicated either.
Once the archive is unziped, i cat the txt file :
```
cat Kidnap.txt
An idea is like a virus, resilient, highly contagious.
52 49 54 53 45 43 7b 57 61 74 65 72 55 6e 64 65 72 54 68 65 42 72 69 64 67 65 7d
```
Look like hex, so i tried to convert it to ascii
```
echo 52 49 54 53 45 43 7b 57 61 74 65 72 55 6e 64 65 72 54 68 65 42 72 69 64 67 65 7d | xxd -r -p
RITSEC{WaterUnderTheBridge}
```
And it was that simple.
