import os 
from subprocess import check_output
import subprocess
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
                                                                 
                                                                    
""")
print(Fore.MAGENTA,"1-encrypting(enter 1)\n 2-decrypting(enter 2)")
intro = int(input(" number:"))
if intro == 1 :
    print(Fore.CYAN+"Please enter youre file adress \nExample: e: && cd deadpool && cd scan && dir /S /B *.txt\n",end='')
    # The file address is taken here
    adr_file = str(input("enter youre file adress: "))
    # Key is created here
    key = Fernet.generate_key()
    print(f"your kay : {key}" )
    # Saving the key in txt file
    file = open("key.txt","wb")
    file.write(b"".join([b"'"+key+b"'"]))
    file.close()
    print(Fore.MAGENTA+"[+]"+Fore.GREEN+"youre key saved in key.txt")

    Encrypt = Fernet(key)
    cmd = check_output(adr_file , shell = True ).decode().split()
    # Encrypt files and delete previous files
    for g in cmd :
        if os.path.exists(g):
            dirlist= open(g,"rb")
            data = dirlist.read()
            enc_data = Encrypt.encrypt(data)
            new_file = open(g+ ".snoopy" , "wb")       
            new_file.write(enc_data)
            new_file.close()
            dirlist.close()
            os.remove(g)
            print(Fore.LIGHTGREEN_EX+g+" --------------->" "+" "{Encrypted}")
        else : print(Fore.RED+"file not exist")

    print(Fore.LIGHTYELLOW_EX+"Back to menu : 1 \nexit: 2")
elif intro == 2 :
    print(Fore.CYAN+"Please enter youre file adress \nExample: e: && cd deadpool && cd scan && dir /S /B *.snoopy\n",end='')
    adr_file_dec= str(input("enter youre file adress: "))
    print(Fore.CYAN+"Please enter youre key for decrypting \nExample: '4yA2Qvjdwz3mRySc1QX4AFoBahsqxnsNHo8pb8MVdRo='\n ",end='')
    dec_key=str(input("enter youre key: "))
    dencrypt = Fernet(dec_key)
    cmd = check_output(adr_file_dec, shell = True ).decode().split()
    for g in cmd :
        if os.path.exists(g):
            dirlist= open(g,"rb")
            data = dirlist.read()
            enc_data = dencrypt.decrypt(data)
            new_file = open(g+ ".txt" , "wb")       
            new_file.write(enc_data)
            new_file.close()
            dirlist.close()
            os.remove(g)
            print(Fore.LIGHTGREEN_EX+g+" --------------->" "+" "{Dencrypted}")
        else:  
         print(Fore.RED+"file not exist!")
    print(Fore.LIGHTYELLOW_EX+"Back to menu : 1 \nexit: 2")

else : print(Fore.LIGHTRED_EX+"Wrong number!!")

