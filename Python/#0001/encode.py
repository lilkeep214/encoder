import random
import string

def spam_files():

    generate_number = input("[>")

    result_gen = int(generate_number)

    for i in range(result_gen):
        file_name = "" + "".join(random.choices(string.ascii_letters + string.digits, k=100))
        file_message = "" + "".join(random.choices(string.ascii_letters + string.digits + string.punctuation + string.whitespace + string.hexdigits + string.octdigits + string.printable, k=1000000))

        with open(f"{file_name}.txt", "a") as file:
            file.write(f"{file_message}")
            file.close