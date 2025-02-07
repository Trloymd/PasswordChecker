import random

klavye = "asdfghjklşiqwertyuıopğüzxcvbnmöçASDFGHJKLŞİQWERTYUIOPĞÜZXCVBNMÖÇ><.:,;*?-_|\}][{§½$#£>!'^+%&/()=ƒğæß∂ƒğ^∆¨¬´æ≈ç√∫~µ≤≥÷`|!'^+%&/()=1234567890é}]"

length = int(input("Şifre Kaç Haneli Olsun (8den fazla olmalı): "))

if length < 8:
    print("Şifre uzunluğu en az 8 olmalıdır!")
else:
    sifre = input("Şifreni yaz: ")

    while len(sifre) < length:
        sifre += random.choice(klavye)

    print("Oluşturulan Şifre:", sifre)
