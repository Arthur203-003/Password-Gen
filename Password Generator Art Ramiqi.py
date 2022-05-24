import string
import random

karakteret = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def gjenero_password_te_rendomte():
    length = int(input("Shkruaj sa karaktere deshiron te kete passwordi juaj: "))
    while length <= 0:
        length = int(input("Numer jovalid!! Ju lutem provoni perseri: "))

    random.shuffle(karakteret)

    password = []
    for i in range(length):
        password.append(random.choice(karakteret))

    random.shuffle(password)

    print("".join(password))

gjenero_password_te_rendomte()