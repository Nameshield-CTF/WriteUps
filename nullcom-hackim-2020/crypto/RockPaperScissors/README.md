# RockPaperScissors

By [MiniPierre](https://github.com/MiniPierre)

## Description
To get the flag you have to beat us in rock paper scissors but to make it fair we used a commitment base scheme
## Solution
When connecting to the server with nc, we get the following output:
```
Beat me in Rock Paper Scissors 20 consecutive times to get the flag
Here are the possible commitments, the first one is my move: 20cd72dedb83ea4dbee23d008ea4df8f a974ac78fdecb588a77f98b30c255733 f4ee9c46b69ed303efbfdd4221d81296
Your move:
```
No doubt that it is a very willing program (let's call it Billy), it even gives me its move, but I have to say that `39ee0a9dfffde648a376e23c494ffc6a` is not quite readable. The key point of this challenge is the commitment scheme: in short, Billy is giving us an obfuscated version of the move it chose, and will give us the key to decrypt its choice during the reveal phase (after we make our own choice). The security of this scheme lies in the fact that we  are supposed to have no idea of the algorithm it used to encrypt its choice.

We do not even know which kind of answer it is waiting for, but let's try to beat Billy:

```
Your move:rock
My move was: s Secret was: 71ec50565c6f0e5cbbadf98f52c9c31
You lose!
```
At least we tried... But at least can we see that Billy was waiting for a single letter : `r ` for Rock, `p` for Paper, `S` for Scissors. We also get the secret, but it's too late Billy, we already lost.

### Source code analysis
Sadly for the program, we have access to the server source code ! Let's have a look at it, starting with the `main` function :
```python
def main():
    print("Beat me in Rock Paper Scissors 20 consecutive times to get the flag")
    for i in range(20):
        secret, rps = gen_commitments()
        move = rps[0][0]
        print("Here are the possible commitments, the first one is my move:", " ".join(map(lambda s: s[1], rps)))
        inp = input("Your move:")
        res = check_win(move, inp)
        print("My move was:", move, "Secret was:", secret)
        if not res:
            print("You lose!")
            exit(0)

    print("You win")
    print("Your reward is", flag)
    exit(0)
```
Most of it is not very interesting, but we can see that it uses a `gen_commitments()` function that seems to give the secret used for obfuscation and the obfuscated options. It is the starting point of our solution !
#### gen_commitments
```python
def gen_commitments():
    secret = bytearray(Random.get_random_bytes(16))
    rc = hash(secret + b"r")
    pc = hash(secret + b"p")
    sc = hash(secret + b"s")
    secret = hex(bytes_to_int(secret))[2:]
    rps = [("r", rc), ("p", pc), ("s", sc)]
    random.shuffle(rps)
    return secret, rps
```
No surprises, the secret is a random array of 16 bytes, there are no way we can retrieve it. However, the `r`, `p` and `s` options are concatenated with this secret and hashed using the `hash` function. If this hash function is badly made, we may be able to reverse the hashing process and find the solution.
#### hash
```python
def hash(data):
    state = bytearray([208, 151, 71, 15, 101, 206, 50, 225, 223, 14, 14, 106, 22, 40, 20, 2])
    data = pad(data, 16)
    data = group(data)
    for roundkey in data:
        for _ in range(round):
            state = repeated_xor(state, roundkey)
            for i in range(len(state)):
                state[i] = sbox[state[i]]
            temp = bytearray(16)
            for i in range(len(state)):
                temp[p[i]] = state[i]
            state = temp
    return hex(bytes_to_int(state))[2:]
```
 Here comes the "hard" part of this challenge : we have to understand how this hash function works to reverse it. Let's go step by step:
 ```python
state = bytearray([208, 151, 71, 15, 101, 206, 50, 225, 223, 14, 14, 106, 22, 40, 20, 2])
```
Nothing special here, it is just an array of bytes. Yet, as this array is initialized at the beginning of the function, the same array will be used for each of the `r`, `p` and `s` options, that a good thing.
 ```python
data = pad(data, 16)
```
We will not go through every function in detail, this one does only add multiple `\x0f` bytes at the end of the data until its size reaches 32 bytes. As the secret is 16 bytes long and the option 1 byte long, it thus adds 32 - 16 - 1 = 15 bytes.
```python
data = group(data)
```
Same here, just know that this function split the padded data into multiple parts, here 2 different ones : first one is the secret and the other one is the option concatenated with the '\x0f' bytes (let's call it padded option part)
```
---------------------    ---------------------
|      Secret       |    | r/p/s + 15 * \xOf |
---------------------    ---------------------
<----- 16 bytes ---->    <----- 16 bytes ---->
```
And now comes the real obfuscation part ! It consists of three different steps :
###### XOR
```python
state = repeated_xor(state, roundkey)
```
`repeated_xor` make a bit by bit XOR between two array of bytes. Nothing more to say for this one.
###### Subtitution
```python
for i in range(len(state)):
    state[i] = sbox[state[i]]
```
This step is a substitution: for each byte `b` in the XORed byte array, it replaces this byte by the value located at index `b` in the `sbox` array. See [S-Box](https://fr.wikipedia.org/wiki/S-Box) for more information (`sbox` is not a real S-Box but the idea behind it is the same).
```
                              (c7)16 = (199)10
           ------------------------------------------------------
           |                      Step 1                        |
           |                                                    ↓
----------------------------                   -------------------------------
| \x03 | \xc7 | ... | \xa1 |                   | 56 | 45 | .. | 32 | .. | 76 |
----------------------------                   -------------------------------
<-------- 32 bytes -------->                      0    1        199       255
           ↑                                                    |
           |                       Step 2                       |
           ------------------------------------------------------
```
###### Permutation
```python
temp = bytearray(16)
for i in range(len(state)):
    temp[p[i]] = state[i]
state = temp
```
The final step is a permutation: the bytes are shuffled using an array `p` which tells at which index each byte should be stored. See [P-Box](https://fr.wikipedia.org/wiki/P-Box) for more information.
###### Final step
The obfuscation step are repeated 16 times for each subkey (the split parts of the padded data). After that, the byte array is converted to an hexadecimal representation.

### Weakness
You might wonder what is the weakness of this algorithm. It lies in the fact that, as we saw it, the padded data are split in two half, the secret part and the padded option part. As the secret is the same for each option, the first round of obfuscation (which use the secret part as a subkey) does produce the same output, whatever the option is. Thus, if we revert the obfuscation one time (with the padded option part as a subkey), we will retrieve the same thing for each of the option.
```
    First round               --------------------  |        Second round              -------------------- 
                              |   Initial_state  |  |                                 |      State_A     |
                              --------------------  |                                  --------------------
                                       |            |                                           |
                                       |            |                                           |
                                       ↓            |                                           ↓
---------------------        --------------------   |   ---------------------        --------------------
|      Secret       |  --->  |    Obfuscation   |   |   |   Padded option   |  --->  |    Obfuscation   |   
---------------------        --------------------   |   ---------------------        --------------------  
                                       |            |                                           |
                                       |            |                                           |
                                       ↓            |                                           ↓
                              --------------------  |                                  --------------------
                              |      State_A     |  |                                  |      State_B     |
                              --------------------  |                                  --------------------
```
In short, State_B will be different for each option, but State_A will be the same whatever the option.
As the hash function can be reverted, we only have to try the different possible combinations of `r`, `p` and `s` (`[r,p,s]` , `[p,s,r]`, ...) and find the one that gives the same State_A for each option .

### Solution code
```python
def dehash(data, action):
    padded_option = bytearray(str.encode(action)) + bytearray(b'\x0f') * 15
    state = long_to_bytes(int(data, 16))
    for i in range(16):
	# Reverse permutation
        temp = bytearray(16)
        for i in range(len(state)):
            temp[p2[i]] = state[i]
        state = temp
	# Reverse substitution
        for i in range(len(state)):
            state[i] = sbox.index(state[i])
	# Reverse XOR
        state = repeated_xor(state, padded_option)
    return state
```
Knowing the obfuscation algorithm, it is quite easy to revert it in order to find State_A.
```python
padded_option = bytearray(str.encode(action)) + bytearray(b'\x0f') * 15
```
We first recreate the padded option part
```python
state = long_to_bytes(int(data, 16))
```
We then convert the obfuscated option to a byte array in order to perform the revert operations
```python
# Reverse permutation
temp = bytearray(16)
for i in range(len(state)):
    temp[p2[i]] = state[i]
state = temp
```
```python
p2 = [6, 2, 15, 4, 9, 0, 14, 8, 3, 1, 12, 5, 7, 11, 10, 13]
```
We reverse the permutation by performing another permutation with a reverse P-Box
```python
# Reverse substitution
for i in range(len(state)):
    state[i] = sbox.index(state[i])
```
We reverse the substitution by finding the index of the byte value in the S-Box (original substitution = finding the new value of the bytes from its index equal to the original byte value)
```python
# Reverse XOR
state = repeated_xor(state, padded_option)
```
Finally, we reverse the original XOR by performing another XOR ( as ` ( A XOR B ) XOR B = A` )

These operations are repeated 16 times (just like obfuscation), and we thus retrieve State_A

```python
def solution(option1, option2, option3):
    perm = permutations(['r','p','s'])
    for p in list(perm):
        res1 = dehash(option1, p[0])
        res2 = dehash(option2, p[1])
        res3 = dehash(option3, p[2])
	# If secret is the same for all 3, print the winning option
        if(res1 == res2 and res2 == res3):
            if(p[0] == 'r'):
                print('p')
            elif(p[0] == 'p'):
                print('s')
            else:
                print('r')
```
We now try every possible combination of `r`, `p` and `s` using the value given by the server to find in which order they are, and the one giving the same State_A for each option is the correct one.
#### Example
```
Beat me in Rock Paper Scissors 20 consecutive times to get the flag
Here are the possible commitments, the first one is my move: 4532199b8d6cd9cfff50ad482ae1c335 1cbd710ead4efdb7e8870e5f857af371 e09d28d5fc5e0d293e7c56f72933e33f
Your move:
```
```python
> solution("4532199b8d6cd9cfff50ad482ae1c335", "1cbd710ead4efdb7e8870e5f857af371", "e09d28d5fc5e0d293e7c56f72933e33f")
r
```
```
Your move:r
My move was: s Secret was: 5fc28d84664d27885e8f24ff6f492ea
```
Repeat this 20 times and you get the flag : `hackim20{b4d_pr1mitiv3_beats_all!1!_7f65}`

