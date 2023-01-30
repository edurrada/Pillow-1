from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def cortar(img, w, h):
    width, height = img.size
    newWidth = (height/(h/100))*(w/100)
    box = ((width-newWidth)/2, 0, (width+newWidth)/2, height)
    img = img.crop(box)
    img = img.resize((w,h))
    return img

def concatenar(img1, img2):
    result = Image.new("RGB", (2*width, height), "white")
    result.paste(img1, (0, 0))
    result.paste(img2, (500, 0))
    return result

def texto(img, frase1, frase2):
    draw = ImageDraw.Draw(img)
    draw.text((150,28), frase1, font=fonte)
    draw.text((600,28), frase2, font=fonte)
    return img

imagem1 = Image.open('laptop.jpg')
imagem2 = Image.open('paisagem.jpg')

width, height = 500, 700

frase1 = 'Turn this...'
frase2 = '...Into that!!!'

fonte = ImageFont.truetype("arial.ttf", 50)

img1 = cortar(imagem1, width, height)
img2 = cortar(imagem2, width, height)
result = concatenar(img1, img2)
result = texto(result, frase1, frase2)

result.save('result.jpg')