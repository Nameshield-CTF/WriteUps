# Inception CTF: Dream 1

By [Siorde](https://github.com/Siorde)

## Description
The purpose of this CTF challenge is to identify common methods of hiding malicious files and code. In most cases adversaries will attempt to evade defenses in many cases by masquerading, hiding files, and more. There are five directories like the five levels in the movie Inception, Reality -> Van Chase -> The Hotel -> Snow Fortress -> Limbo. You will find one flag in each of the levels, that flag will also be the password to extract the next directory. Requirements: • You must have 7zip installed • Drop the InceptionCTF.7z on the Desktop as “InceptionCTF” • Use the option “Extract to "<name of directory>\” for the CTF to function properly Missing either of the above may result in complications which may cause issues when attempting to find flags.
</br>
NOTE: These challenges have a flag format of RITSEC{}
</br>
Dream 1: We have to get to their subconscious first, look for a hidden text file within the directory “Reality” this flag will unlock the next directory.

## Solution
I'm not even sure this is a challenge...
I unziped the archive ans the other archive inside it :
```
p7zip -d ./inceptionCTFRITSEC.7z
p7zip -d ./Reality.7z
```
I printed the .txt that was inside the archive
```
cat Subconscious.txt 
Wait a minute, whose subconscious are we going into, exactly? {dnalmaerD}CESTIR
```
And the flag is here in reverse : RITSEC{Dreamland}
