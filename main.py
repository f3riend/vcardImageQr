from qrcode_artistic import write_artistic
from tkinter import filedialog
from segno import helpers
from PIL import Image
import random
import string



def generate(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string





def createWindow(name,surname,phone,title,imagePath):
    fullName = name + " " + surname
    qrCode = helpers.make_vcard(
        name=f"{fullName}",
        displayname=f"{fullName}",
        phone=f"{phone}",
        title=f"{title}"
    )



    fileName = generate()

    
    if imagePath.endswith("gif"):
        write_artistic(qrCode,background=imagePath,target=f"{fileName}.gif",scale=5,border=1)
    else:
        write_artistic(qrCode,background=imagePath,target=f"{fileName}.png",scale=5,border=1)

    







name = input("Name: ")
surname = input("Surname: ")
phone = input("Phone: ") # should be country code for example +901234567890
title = input("Title: ")
imagePath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])


createWindow(name,surname,phone,title,imagePath)