import pygame
pygame.init()
from vars import *
ss=square_size
screen=pygame.display.set_mode((ss*8,ss*8))

from pieces import *

BLACK=(0,0,0)
WHITE = (255,255,255)

r1=rook(0*ss,7*ss,screen,True,'rook')
r2=rook(7*ss,7*ss,screen,True,'rook')
r3=rook(0*ss,0*ss,screen,False,'rook')
r4=rook(7*ss,0*ss,screen,False,'rook')
q1=queen(3*ss,7*ss,screen,True,'queen')
q2=queen(3*ss,0*ss,screen,False,'queen')
k1=king(4*ss,0*ss,screen,False,'king')
k2=king(4*ss,7*ss,screen,True,'king')
n1=knight(1*ss,0*ss,screen,False,'knight')
n2=knight(1*ss,7*ss,screen,True,'knight')
n3=knight(6*ss,0*ss,screen,False,'knight')
n4=knight(6*ss,7*ss,screen,True,'knight')
b1=bishop(2*ss,7*ss,screen,True,'bishop')
b2=bishop(2*ss,0*ss,screen,False,'bishop')
b3=bishop(5*ss,7*ss,screen,True,'bishop')
b4=bishop(5*ss,0*ss,screen,False,'bishop')
p1=pawn(0*ss,6*ss,screen,True,'pawn')
p2=pawn(1*ss,6*ss,screen,True,'pawn')
p3=pawn(2*ss,6*ss,screen,True,'pawn')
p4=pawn(3*ss,6*ss,screen,True,'pawn')
p5=pawn(4*ss,6*ss,screen,True,'pawn')
p6=pawn(5*ss,6*ss,screen,True,'pawn')
p7=pawn(6*ss,6*ss,screen,True,'pawn')
p8=pawn(7*ss,6*ss,screen,True,'pawn')
pb1=pawn(0*ss,1*ss,screen,False,'pawn')
pb2=pawn(1*ss,1*ss,screen,False,'pawn')
pb3=pawn(2*ss,1*ss,screen,False,'pawn')
pb4=pawn(3*ss,1*ss,screen,False,'pawn')
pb5=pawn(4*ss,1*ss,screen,False,'pawn')
pb6=pawn(5*ss,1*ss,screen,False,'pawn')
pb7=pawn(6*ss,1*ss,screen,False,'pawn')
pb8=pawn(7*ss,1*ss,screen,False,'pawn')
dummy=pawn(10*ss,1*ss,screen,False,'pawn')



pieces = [dummy,r1,r2,r3,r4,q1,q2,k1,k2,n1,n2,n3,n4,b1,b2,b3,b4,p1,p2,p3,p4,p5,p6,p7,p8,pb1,pb2,pb3,pb4,pb5,pb6,pb7,pb8]
pawns=[p1,p2,p3,p4,p5,p6,p7,p8,pb1,pb2,pb3,pb4,pb5,pb6,pb7,pb8]
def drawBoard():
    screen.fill(WHITE)
    for i in range(8):
        if(i%2==1):
            for j in range(4):
                pygame.draw.rect(screen, BLACK, (j*2*ss,i*ss,ss, ss))
        else:
            for j in range(1,5):
                pygame.draw.rect(screen, BLACK, (j*2*ss - ss,i*ss,ss, ss))

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    drawBoard()
    for pawny in pawns:
        if pawny.__getattribute__('dragy')==10 and pawny.__getattribute__('type')=='pawn':
            pawny=queen(pawny.__getattribute__('dragx'),0,screen,False,'queen')
    
        if pawny.__getattribute__('dragy')==0 and pawny.__getattribute__('type')=='pawn':
            b=0
            for i in range(1,len(pieces)):
                if pieces[i]==pawny:
                    #pieces[i]=pawny
                    break
            for i in range(1,len(pawns)):
                if pawns[i]==pawny:
                    #pieces[i]=pawny
                    break
            pawny.dragy=10000
            pawny.draw()
            
            pawny=queen(pawny.__getattribute__('dragx'),0,screen,True,'queen')
            
            pieces[b]=pawny

            #pieces.append(pawny)
    for i in range(len(pieces)):
        if None != pieces[i]:
            pieces[i].highlight()
            pieces[i].click(pieces)
            pieces[i].draw()
            if pieces[i].turn:
                for x in range(len(pieces)):
                    if (i != x) and pieces[x] != None:
                        if (pieces[i].rect.y == pieces[x].rect.y) and (pieces[i].rect.x == pieces[x].rect.x):
                            pieces[x] = None
                            pieces[i].turn = False

    for i in pieces:
        if i != None:
            i.turn = False

    pygame.display.update()
pygame.quit()