import pygame
pygame.init()

from vars import *

screen=pygame.display.set_mode((square_size*8,square_size*8))

from pieces import *
ss=square_size
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
                pygame.draw.rect(screen, BLACK, (j*2*square_size,i*square_size,square_size, square_size))
        else:
            for j in range(1,5):
                pygame.draw.rect(screen, BLACK, (j*2*square_size - square_size,i*square_size,square_size, square_size))

white_turn = True
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    drawBoard()
    for i in range(len(pieces)):
        if None != pieces[i]:
            pieces[i].highlight()
            pieces[i].click(pieces, white_turn)
            pieces[i].draw()
            if pieces[i].moved:
                    #print(pieces[i].moved)
                    #time.sleep(0.5)
                    if pieces[i].check(pieces)==False:
                        #print(k2.selected)
                        pieces[i].turn=False
                        pieces[i].rect.x=pieces[i].oldx
                        pieces[i].rect.y=pieces[i].oldy
                        pieces[i].draw()
                        for piece in pieces:
                            if piece !=None:
                                piece.draw()
                        break
                    pieces[i].moved=False
                    pieces[i].turn=True
            if pieces[i].turn:
                white_turn = not white_turn
                for x in range(len(pieces)):
                    if (i != x) and pieces[x] != None:
                        if (pieces[i].rect.y == pieces[x].rect.y) and (pieces[i].rect.x == pieces[x].rect.x):
                            pieces[x] = None
                            pieces[i].turn = False

    for index in range(len(pieces)):
        if pieces[index] != None:
            try:
                piece_name = (str(pieces[index]).strip('<').split()[0].split('.')[1])
            except IndexError:
                piece_name = None
            if piece_name == 'pawn':
                if (pieces[index].rect.y == square_size*7) or (pieces[index].rect.y == 0):
                    temp = pieces[index]
                    pieces[index] = queen(temp.rect.x, temp.rect.y, screen, temp.white,'queen')

    for i in range(len(pieces)):
        try:
            if pieces[i] != None:
                pieces[i].turn = False
            if pieces[i] == False:
                del pieces[i]
        except IndexError:
            continue
    

    pygame.display.update()
pygame.quit()