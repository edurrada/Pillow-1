from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def cortar(img, w, h):
    width, height = img.size
    newWidth = (height/(h/100))*(w/100) #dimensao final - 7:5
    box = ((width-newWidth)/2, 0, (width+newWidth)/2, height)
    img = img.crop(box)
    img = img.resize((w,h))
    img.save(f'imagem{i}.jpg')
    return img

def concatenar(img1, img2):
    saida.paste(img1, (0, 0))
    saida.paste(img2, (500, 0))
    saida.save('saida.jpg')

def texto(frase1,frase2):
    img = Image.open('saida.jpg')
    draw = ImageDraw.Draw(img)
    draw.text((150,28), frase1, font=fonte)
    draw.text((600,28), frase2, font=fonte)
    img.save('saida2.jpg')


imagem1= Image.open('laptop.jpg')
imagem2= Image.open('paisagem.jpg')

width, height = 500, 700

frase1 = 'Turn this...'
frase2 = '...Into that!!!'

fonte = ImageFont.truetype("arial.ttf", 50)

Imagens = [imagem1, imagem2]
for i, imagem in enumerate (Imagens):
    Imagens[i]=cortar(imagem, width, height)
saida = Image.new("RGB", (2*width, height), "white")
concatenar(Image.open('imagem0.jpg'),Image.open('imagem1.jpg'))
texto(frase1,frase2)

