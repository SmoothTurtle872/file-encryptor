from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Colors
import colorama
from colorama import Fore, Back, Style

# Init
colorama.init(autoreset=True)

salt = b"\xedq\x14\x16<i\x9f\xf7\xc3\x16h0\x01\xcf\x86\xda`\x9f\x84\x0b\x85\x08'\x98\xa7\xdc\xb9.^\x84a\xce"
password = "TestPassword"

key = PBKDF2(password, salt, dkLen=32)

# Function Init
def encrypt(fileName:str, UserPassword:str):

    key = PBKDF2(UserPassword, salt, dkLen=32)
    
    with open(f"{fileName}", "r") as f:
        msg = bytes(f.read(), "utf-8")

    cipher = AES.new(key, AES.MODE_CBC)

    ciphered_data = cipher.encrypt(pad(msg, AES.block_size))

    with open(f"{fileName}.bin", "wb") as f:
        f.write(cipher.iv)
        f.write(ciphered_data)
        
    print(f"{Fore.GREEN}File Encryptor{Fore.RESET}| {Fore.YELLOW}Encryption Complete{Fore.RESET}. Please Look Under {fileName}.bin")

def decrypt(fileName:str, UserPassword:str):
    key = PBKDF2(UserPassword, salt, dkLen=32)

    with open(f"{fileName}.bin", "rb") as f:
        iv = f.read(16)
        encrypted_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    originalStr = original.decode("utf-8")
    with open(f"{fileName}", "w") as f:
        f.writelines(originalStr)
        
    print(f"{Fore.GREEN}File Encryptor{Fore.RESET}| {Fore.GREEN}Decryption Complete{Fore.RESET}. Please Look Under {fileName}")
    
print(f"""{Fore.GREEN}File Encryptor{Fore.RESET}| Welcome To File Encryptor!
{Fore.GREEN}File Encryptor{Fore.RESET}| File Encryptor Makes Encrypting Files Easy!""")

loop = True
response = "Enter Response"

while loop:
    response = str(input(f"{Fore.GREEN}File Encryptor{Fore.RESET}| Would You Like To {Fore.YELLOW}Encrypt (E) {Fore.RESET}Or {Fore.BLUE}Decrypt (D) {Fore.RESET}A file Or {Fore.RED}Exit (X){Fore.RESET}? "))
    if response.upper() == "D":
        print(f"{Fore.GREEN}File Encryptor{Fore.RESET}| {Fore.GREEN}Decrypting")
        decrypt(input(f"{Fore.GREEN}File Encryptor{Fore.RESET}| What Is The Name Of Your File? (Your_File.bin (Don't Include The .bin)) "), input(f"{Fore.GREEN}File Encryptor{Fore.RESET}| What Is The Password You Used To Encrypt This File? "))
        loop = True
    elif response.upper() == "E":
        print(f"{Fore.GREEN}File Encryptor{Fore.RESET}| {Fore.YELLOW}Encrypting")
        encrypt(input(f"{Fore.GREEN}File Encryptor{Fore.RESET}| What Is The Name Of Your File? (Your_File.txt (Supported Formats Include: All Plain Text Files. Make Sure You Include The Extension)) "), input(f"{Fore.GREEN}File Encryptor{Fore.RESET}| What Is The Password You Wish To Use To Encrypt This File? "))
        loop = True
    elif response.upper() == "X":
        print(f"{Fore.GREEN}File Encryptor{Fore.RESET}| {Fore.RED}Exiting...")
        loop = False
    else:
        print(f"{Fore.GREEN}File Encryptor{Fore.RESET}| {Fore.RED}Sorry. File Encryptor Does Not Know The Command: {Fore.YELLOW}{response} {Fore.RED}Please Try Again.")
        loop = True