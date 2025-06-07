def delete_format(images):

    img = [i.rsplit('.', 1)[0] for i in images]
    return img

images = ["a23.12.png", "b1.1.2.jpeg", "f2.1.png"]
result = delete_format(images)
print(result)
