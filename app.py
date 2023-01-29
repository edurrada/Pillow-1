from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#Quais palavras sobrepor na imagem
palavra = "Turn this..."

imagem1= Image.open('laptop.jpg')
    #abrir a imagem

    # abrir para sobreposição
draw = ImageDraw.Draw(imagem1)
    #setar qual fonte usar
fonte = ImageFont.truetype("arial.ttf", 60)

    #escrever na imagem o texto
    ## coordenadas x,y; texto, fonte
draw.text((350,45), palavra, font=fonte)

#cortando
width, height = imagem1.size
newWidth = (height/7)*5 #dimensao final - 7:5
box = ((width-newWidth)/2, 0, (width+newWidth)/2, height)
imagem1 = imagem1.crop(box) 
#imagem1.save('img1.jpg')

#salvar


palavra = "..into that!!"
imagem2= Image.open('paisagem.jpg')
#abrir a imagem

    # abrir para sobreposição
draw = ImageDraw.Draw(imagem2)
    #setar qual fonte usar
fonte = ImageFont.truetype("arial.ttf", 60)

    #escrever na imagem o texto
    ## coordenadas x,y; texto, fonte
draw.text((250,45), palavra, font=fonte)



#------------CONCATENAÇÃO

#img1.size
w=500
h=700
img1_size = imagem1.resize((w,h)) #redimensionar
img2_size = imagem2.resize((w,h))

# creating a new image and pasting the images
img3 = Image.new("RGB", (2*w, h), "white")

# pasting the first image (image_name, (position))
img3.paste(img1_size, (0, 0))
  
# pasting the second image (image_name,(position))
img3.paste(img2_size, (w, 0))

img3.save(f'saida.jpg')



def cortar():
    width, height = imagem2.size
    newWidth = (height/7)*5 #dimensao final - 7:5
    box = ((width-newWidth)/2, 0, (width+newWidth)/2, height)
    imagem2 = imagem2.crop(box)
    return imagem2