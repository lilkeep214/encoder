import random
import string
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def spam_filees():

    generatef_number = input("[>")

    resultf_gen = int(generatef_number)

    for i in range(resultf_gen):
        file_fmessage = "" + "".join(random.choices(string.ascii_letters + string.digits + string.whitespace + string.hexdigits + string.octdigits + string.printable, k=1000000))
        with open("Encoded.txt", "a") as file:
            file.write(f"{file_fmessage}")
        print(f"Name : {Fore.LIGHTGREEN_EX}{file_fmessage}")



    input("")