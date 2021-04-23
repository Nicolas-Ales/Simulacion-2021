from PIL import Image
import math
import matplotlib.pyplot as plt


def grafRuido(lista,nombre):
    size = int(math.sqrt(len(lista)))
    img = Image.new('RGB', (size, size), "black")  # Create a new black image
    pixels = img.load()  # Create the pixel map
    pos = 0
    for i in range(img.size[0]):  # For every pixel:
        for j in range(img.size[1]):
            t = int(255*lista[pos])
            pos += 1
            pixels[i, j] = (t, t, t)  # Set the colour accordingly
    img.save(str(nombre+'.png'))
    img.show()

def grafPar(muestra,nombre):
    par = 0
    inpar = 0
    for m in muestra:
        if (math.floor(m * 10000) % 2) == 0:
            par += 1
        else:
            inpar += 1
    datos = [par,inpar]
    nombres = ['Pares','Impares']
    plt.pie(datos,labels=nombres, autopct='%1.1f%%', shadow=True)
    plt.title(str('Paridad para muestra del generador ' + nombre))
    plt.axis('equal')
    plt.savefig(str('Paridad '+nombre))
    plt.show()
    
def grafHist(muestra, nombre):
    plt.hist(muestra,bins=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
    plt.grid(True)
    plt.savefig(str('His'+nombre))
    plt.show()