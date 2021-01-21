from PIL import Image

names = ["image1.jpg","image2.jpg","image3.png"]

images = []

converted_images = []

for name in names:
    image = Image.open(name)
    images.append(image)

for image in images:
    image_converted = image.convert("RGB")
    converted_images.append(image_converted)


convert_image_copy = converted_images.copy()
convert_image_copy.pop(0)

converted_images[0].save("images1.pdf", save_all = True, append_images = convert_image_copy)

