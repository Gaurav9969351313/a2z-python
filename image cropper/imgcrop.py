from PIL import Image
img = Image.open("5.jpg")
img2 = img.crop((0, 0, 100, 100))
img2.save("img2.jpg")
