from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def cortar(img, w, h):
    width, height = img.size
    newWidth = (height/(h/100))*(w/100)
    box = ((width-newWidth)/2, 0, (width+newWidth)/2, height)
    img = img.crop(box)
    img = img.resize((w,h))
    # img.save('teste.jpg')
    return img

def concatenar(img1, img2, width, height):
    result = Image.new("RGB", (2*width, height), "white")
    result.paste(img1, (0, 0))
    result.paste(img2, (width, 0))
    return result

def texto(img, frase1, frase2):
    draw = ImageDraw.Draw(img)
    draw.text((150,28), frase1, font=fonte)
    draw.text((600,28), frase2, font=fonte)
    return img

imagem1 = Image.open('laptop.jpg')
imagem2 = Image.open('paisagem.jpg')

IMAGE_WIDTH = 500
IMAGE_HEIGHT = 700

text_left = 'Turn this...'
text_right = '...Into that!!!'

FONT_SIZE = 50
FONT_PATH = "arial.ttf"

fonte = ImageFont.truetype(FONT_PATH, FONT_SIZE)

img1 = cortar(imagem1, IMAGE_WIDTH, IMAGE_HEIGHT)
img2 = cortar(imagem2, IMAGE_WIDTH, IMAGE_HEIGHT)
result = concatenar(img1, img2, IMAGE_WIDTH, IMAGE_HEIGHT)
result = texto(result, text_left, text_right)

result.save('result.jpg')