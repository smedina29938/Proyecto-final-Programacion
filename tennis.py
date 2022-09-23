import pygame
class pelota_de_tenis: # aqui creamos un objeto el cual sera la pelota...
    def __init__(formapelota, ventana,x,y): # iniciamos algunos parametros y definimos x y "y" mas vx y vy el cual sera la velocidad
        formapelota.ventana =ventana
        formapelota.x =x
        formapelota.y =y
        formapelota.vx =x
        formapelota.vy =y
    def dibujar(dibujarpelota): #dibuja la pelota  y le agregamos el color que queramos mas las posiciones en las que iniciara
        pygame.draw.rect(dibujarpelota.ventana, (0,255,0), (dibujarpelota.x,dibujarpelota.y,10,10))
    def movimiento(movimiento): # aqui le añadimos las propiedades de velocidad y movimietno, para que siempre que se mueva mantenga una velocidad constante y las p
        movimiento.x += movimiento.vx
        movimiento.y += movimiento.vy 
class tenista1: # este crea el objeto de la raqueta...
    def __init__(formaraqueta, ventana): #igual este inicia el objeto tenista
        formaraqueta.tamaño = 80 # aqui definimos el ancho de la misma
        formaraqueta.x= 800/2-formaraqueta.tamaño/2 # aqui le definimos el lugar donde aparecera
        formaraqueta.y =580  # aqui igual solo que en lo alto para que aparezca cerca del suelo
        formaraqueta.ventana = ventana # aqui hacemos que aparezca en la ventana-imagen-pestaña
        formaraqueta.izq = False #aqui damos valores boleanos a estos para utilizarlos en su movimiento con las teclas
        formaraqueta.der = False #aqui damos valores boleanos a estos para utilizarlos en su movimiento con las teclas
    def dibujar(dibujoraqueta): # dibujamos la raqueta
        pygame.draw.rect(dibujoraqueta.ventana, (0,255,255), (dibujoraqueta.x,dibujoraqueta.y, dibujoraqueta.tamaño,10))
        
    def movimiento(movimientoraqueta): # aqui le damos valores al los movimientos que realizra en la pantalla
        if movimientoraqueta.izq: movimientoraqueta.x -=10 #para que valla a la izquierda
        if movimientoraqueta.der: movimientoraqueta.x +=10 #para que valla a la derecha 10 pts por cada vez que estemos presionando
        movimientoraqueta.x =0 if movimientoraqueta.x <0 else 800 - movimientoraqueta .tamaño if movimientoraqueta.x+ movimientoraqueta.tamaño > 800 else movimientoraqueta.x # este lo usamos para que no se salga de la pantalla

def refrescar(tablero): # este sera el que genere nuestra ventana o el juego como tal- es muy necesario ya que en esta iniciamos los objetos y los dibujamos
    tablero.fill((0,0,50)) # iniciamos pantalla
    pelotaa.dibujar() # iniciamos la pelota
    text = fuente.render(str(rebote1), True, ((255,255,255))) #generamos el texto, para mostrar la puntuacion
    text_rect =text.get_rect() # generamos una variable para usar el texto
    text_rect.centerx=400 # centramos este mismo
    raqueta1.dibujar() #dibujamos la raqueta
    tablero.blit(text, text_rect) #añadimos el texto al tablero
def juego(): #funcion para iniciar el juego
    global pelotaa, rebote1, fuente, raqueta1 #iniciamos variables globales, estos son para poder usarlos donde queramos y no nos generen fallos fuera de las funciones
    tablero= pygame.display.set_mode((800,600)) #definimos el tamaño de la pantalla
    pelotaa = pelota_de_tenis(tablero,50,100)# aca iniciamos la pelota en el juego, tablero: donde iniciamos este mismo :  50,100 es la posicione en la que esta se disparara
    pelotaa.vx=3 # esta es la velocidad que tendra en x 
    pelotaa.vy=3 # esta es la velocidad que tendra en y 
    rebote1= 0 #aca iniciamos el contador para el puntaje que se tendra
    reloj=pygame.time.Clock() # aca añadimos una variable de tiempo
    raqueta1=tenista1(tablero) # añadimos al tenista
    pygame.font.init()# iniciamos las letras o el puntaje 
    fuente = pygame.font.SysFont("Arial", 40) #definimos que tipo de letra queremos y su tamaño
    init =True # iniciamos un boleano para el while
    while init: # hacemos el bucle
        for raa in pygame.event.get(): # generamos un evento del juego tal sera el cierre del juego 
            if raa.type == pygame.QUIT:# cerramos en caso de...
                init=False
            if raa.type == pygame.KEYDOWN: #aca de damos los valores a a las teclas para generar movimiento izq y der
                if raa.key == pygame.K_LEFT:
                    raqueta1.izq = True
                if raa.key == pygame.K_RIGHT:
                    raqueta1.der = True
            if raa.type == pygame.KEYUP:
                if raa.key == pygame.K_LEFT:
                    raqueta1.izq = False
                if raa.key == pygame.K_RIGHT:
                    raqueta1.der = False
        pelotaa.movimiento() # añadimos la propiedad anterior de su respectivo movimiento
        raqueta1.movimiento() # añadimos la propiedad anterior de su respectivo movimiento
        if pelotaa.x >=790: #aca le damos valores a las paredes del juego esto para que la pelota rebote 
            pelotaa.vx *=-1
            pelotaa.x=790            
        if pelotaa.x <=0: #aca le damos valores a las paredes del juego esto para que la pelota rebote 
            pelotaa.vx *=-1
            pelotaa.x=0
        if pelotaa.y +10 > raqueta1.y: # aca hacemos que rebote en nuestra raqueta
            if (raqueta1.x<pelotaa.x<raqueta1.x + raqueta1.tamaño) and (raqueta1.x<pelotaa.x +10<raqueta1.x + raqueta1.tamaño):
                pelotaa.vy *=-1.05
                pelotaa.vx *=1.02
                pelotaa.y=raqueta1.y-10
                rebote1 +=1000
        if pelotaa.y <=0: #aca le damos valores a las paredes del juego esto para que la pelota rebote 
            pelotaa.vy *=-1
            pelotaa.y=0
        if pelotaa.y >=600: # aca decimos que si pasa del suelo sin tocar la raqueta se perdera y le decimos su respectivo puntaje
            print("acabas de perder:\nTu puntaje fue de:",rebote1, "pts")
            return False
        refrescar(tablero) #aca mostramos los elementos del tablero
        reloj.tick(60) #añadimos nuetra variable de tiempo
        pygame.display.update( ) # actualizamos nuestra pantalla para que muestre los elementos
if __name__=="__main__": #iniciamos nuestro juego 
    juego()