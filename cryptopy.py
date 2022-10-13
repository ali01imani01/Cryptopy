import os 
from subprocess import check_output
import subprocess
from traceback import print_tb
from cryptography.fernet import Fernet
import colorama 
from colorama import init , Fore
init(convert=True)
os.system("cls")
print(Fore.GREEN+"""
 ____    ____   ___  _   ____    _____    ____    ____   ___  _
/   _\  /  __\  \  \//  /  __\  /__ __\  /  _ \  /  __\  \  \//
|  /    |  \/|   \  /   |  \/|    / \    | / \|  |  \/|   \  / 
|  \_   |    /   / /    |  __/    | |    | \_/|  |  __/   / /  
\____/  \_/\_\  /_/     \_/       \_/    \____/  \_/     /_/   

                         """+Fore.LIGHTRED_EX+"""<<By SNP>>                                       
                                                                    
""")
print(Fore.MAGENTA,"1-Encrypt files(Enter 1)\n 2-Decrypt files(Enter 2)")
intro = int(input(" Number: "))
if intro == 1 :
    adr_file = str(input("Enter your folder adress: "))
    format = str(input("Enter your intended format to Encrypt (Enter * if you want to encrypt all files): "))
        # Key is created here
    key = Fernet.generate_key()
    print(f"Your key : {key}" )
        # Saving the key in txt file
    file = open("key.txt","wb")
    file.write(b"".join([b"'"+key+b"'"]))
    file.close()
    Encrypt = Fernet(key)
    if format=="*" :
        print(Fore.MAGENTA+"[+]"+Fore.GREEN+"Your key is saved in key.txt")
        for dirpath, dirs, files  in os.walk(adr_file):
            for f in files:
                    # Encrypt files and delete previous files
                    full_file=os.path.join(adr_file, f)
                    dirlist= open(full_file,"rb")
                    data = dirlist.read()
                    enc_data = Encrypt.encrypt(data)
                    new_file = open(full_file+".snoopy" , "wb")       
                    new_file.write(enc_data)
                    new_file.close()
                    dirlist.close()
                    os.remove(full_file)
                    os.rename(new_file.name, full_file.replace('.snoopy',''))
                    print(Fore.LIGHTGREEN_EX+full_file+" --------------->" "+" "{Encrypted}")
    else:
        print(Fore.MAGENTA+"[+]"+Fore.GREEN+"Your key is saved in key.txt")
        for dirpath, dirs, files  in os.walk(adr_file):
            for f in files:
                if f.endswith(format):
                    full_file=os.path.join(adr_file, f)
                    dirlist= open(full_file,"rb")
                    data = dirlist.read()
                    enc_data = Encrypt.encrypt(data)
                    new_file = open(full_file+".snoopy" , "wb")       
                    new_file.write(enc_data)
                    new_file.close()
                    dirlist.close()
                    os.remove(full_file)
                    os.rename(new_file.name, full_file.replace('.snoopy',''))
                    print(Fore.LIGHTGREEN_EX+full_file+" --------------->" "+" "{Encrypted}")

elif intro == 2 :
    print(Fore.CYAN+"Please enter your file adress \nExample: D:\pic\\temp\n",end='')
    adr_file_dec= str(input("Enter your file adress: "))
    format = input("Enter your intended format to Decrypt:")
    print(Fore.CYAN+"Please enter your key for decrypting \nExample: '4yA2Qvjdwz3mRySc1QX4AFoBahsqxnsNHo8pb8MVdRo='\n ",end='')
    dec_key=str(input("Enter your key: "))
    dencrypt = Fernet(dec_key)
    if format=="*" :
        for dirpath, dirs, files  in os.walk(adr_file_dec):
            for f in files:
                    full_file=os.path.join(adr_file_dec, f)
                    dirlist= open(full_file,"rb")
                    data = dirlist.read()
                    enc_data = dencrypt.decrypt(data)
                    new_file = open(full_file+".snoopy", "wb")       
                    new_file.write(enc_data)
                    new_file.close()
                    dirlist.close()
                    #Rename the file to the real name:
                    os.remove(full_file)
                    os.rename(new_file.name, full_file.replace('.snoopy',''))
                    print(Fore.LIGHTGREEN_EX+full_file+" --------------->" "+" "{Decrypted}")
    else:
        for dirpath, dirs, files  in os.walk(adr_file_dec):
            for f in files:
                if f.endswith(format):
                    full_file=os.path.join(adr_file_dec, f)
                    dirlist= open(full_file,"rb")
                    data = dirlist.read()
                    enc_data = dencrypt.decrypt(data)
                    new_file = open(full_file+".snoopy", "wb")       
                    new_file.write(enc_data)
                    new_file.close()
                    dirlist.close()
                    #Rename the file to the real name:
                    os.remove(full_file)
                    os.rename(new_file.name, full_file.replace('.snoopy',''))
                    print(Fore.LIGHTGREEN_EX+full_file+" --------------->" "+" "{Decrypted}")


