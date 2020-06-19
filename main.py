import ConfigParser
import pygame

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([800,600])
    archivo=ConfigParser.ConfigParser()
    archivo.read('mapa.map')
    #informacion del mapa
    img_textura = archivo.get('info','texturas')
    textura = pygame.image.load(img_textura)
    #recortar imagen
    m=[]
    for fila in range(12):
        fila_sp=[]
        for c in range(32):
            cuadro = textura.subsurface(32*c,32*fila,32,32)
            fila_sp.append(cuadro)
        m.append(fila_sp)

    cad_mapa = archivo.get('info','mapa')
    mapa = cad_mapa.split('\n')
    cf = 0
    for fila in mapa:
        cc=0
        for c in fila:
            print c,32*cf,32*cc
            pf= int(archivo.get(c,'tf'))
            pc=int(archivo.get(c,'tc'))
            col=int(archivo.get(c,'colision'))
            if col > 0:
                ventana.blit(m[pf][pc],[32*cc,32*cf])
            cc+=1
        cf+=1
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
        pygame.display.flip()