#tic tac toe
#This game is played by 2 players
#who gets first 15 win
#Author:Habiba Alaa Mohamed Ali El-Behairy
#Date:10-3-2022
#version:1.0
import pygame

BUTTONS_SIZE = 75
evennumbers=[0,2,4,6,8]
oddnumbers=[1,3,5,7,9]
pygame.init()
global SCREEN
SCREEN = pygame.display.set_mode((900, 600)) #done
COLOR_INACTIVE = pygame.Color('black') #colors
COLOR_ACTIVE = pygame.Color('red')
FONT = pygame.font.Font(None,200) #font 
board = [100,100,100,100,100,100,100,100,100]
global turn
turn=1

#function for write text
def write(text, z, y, color, s):
    global SCREEN
    myfont = pygame.font.SysFont("comicsans", s)
    draw_text = myfont.render(text,1, color)
    SCREEN.blit(draw_text, (z, y))



def pb():
    print ('|' ,board[0],'|',board[1] ,'|', board[2],'|')
    print ('--------------------')
    print ('|' ,board[3],'|',board[4] ,'|', board[5],'|')
    print ('--------------------')
    print ('|' ,board[6],'|',board[7] ,'|', board[8],'|')

   
def horizontalwinning():#check for horizontal win
            #print("horz",board)
            if board[0]+board[1]+board[2]==15 or board[3]+board[4]+ board[5]==15 or board[6]+board[7]+ board[8]==15 :
                return True
            
def verticalwinning():#check for vertival win
            #print("ver",board)
            if board[0]+board[3]+ board[6]==15 or board[1]+board[4]+ board[7]==15 or board[2]+board[5]+ board[8]==15 :
                return True

def diagonalwinning():#check for diagonal win
     #print("diag",board)
     if board[2]+board [4]+board[6]==15 or board[0]+board [4]+board[8]==15 :
            return True
   
def gamedraw ():

    if (board[0]+board[1]+board[2]!=15 and board[0]+board [3]+board[6]!=15 and board[1]+board [4]+board[7]!=15 and board[3]+board [4]+board[5]!=15 and board[2]+board [5]+board[8]!=15 and board[6]+board [7]+board[8]!=15 and board[2]+board [4]+board[6]!=15 and board[0]+board [4]+board[8]!=15 and board[0]!= 100   and board [1]!= 100  and board [2]!= 100 and board [3]!= 100  and board [4]!= 100  and board [5]!= 100  and board [6]!= 100  and board [7]!= 100  and board [8]!= 100 ):
       return True
    else:
        return False

def checkwinner():
    global turn
    if horizontalwinning() or  verticalwinning() or diagonalwinning():
        print ("CONGRATULATIONS")
        return True

class InputBox:

    def __init__(self, x, y, w, h, text='',player =True):
        self.rect = pygame.Rect(x, y, w, h) #diem.
        self.color = COLOR_INACTIVE
        self.text = text #text
        self.txt_surface = FONT.render(text, True, self.color) #text color
        self.active = False
        self.player = player



    def handle_event(self, event,index,input_boxes):
        global turn 

        if event.type == pygame.MOUSEBUTTONDOWN: #touching mouse
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:

            if self.active:

                if event.key == pygame.K_RETURN:
                    
                    print(self.text)
                    print(index)
                    pb()
                   
                    if int(self.text) in evennumbers and turn==1:
                        x= int(self.text)
                        if (board[index]==100):
                            board[index]=x
                            evennumbers.remove(x)
                            pb()
                            self.player= False
                            print( self.player)
                            turn=2
                            #print("here even",turn)
                            checkwinner()
                            return board[index]
                            
                    elif int(self.text) in oddnumbers and turn==2:
                        y = int(self.text)
                        if(board[index]==100):
                            board[index]=y
                            oddnumbers.remove(y)
                            pb()
                            self.player= True
                            turn=1
                            #print("here odd",turn)
                            checkwinner()
                            return board[index]
                    else:
                        self.text = ''
                    
                elif event.key == pygame.K_BACKSPACE:
                   self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
               
                


    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

   

    def draw(self ):
        global SCREEN
        # Blit the text.
        SCREEN.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(SCREEN, self.color, self.rect, 2)

        write("Player1", 10, 10, (0, 0, 0), 35)
        write("Player2", 760, 10, (0, 0, 0), 35)

        
        
        write("Player 1 start and choose square and write number from side list then press enter",112,550,(255, 0, 0),18)
        #Side numbers
        f=pygame.Rect(788, 100, BUTTONS_SIZE, BUTTONS_SIZE)
        button_1 = pygame.draw.rect(SCREEN, (0, 0, 0), f)
        write("1", 811, 100, (255, 255, 255), 45)

        g=pygame.Rect(788, 200, BUTTONS_SIZE, BUTTONS_SIZE)
        button_3 = pygame.draw.rect(SCREEN, (0, 0, 0),g )
        write("3", 811, 200, (255, 255, 255), 45)

        h=pygame.Rect(788, 300, BUTTONS_SIZE, BUTTONS_SIZE)
        button_5 = pygame.draw.rect(SCREEN, (0, 0, 0),h)
        write("5", 811, 300, (255, 255, 255), 45)

        i=pygame.Rect(788, 400, BUTTONS_SIZE, BUTTONS_SIZE)
        button_7 = pygame.draw.rect(SCREEN, (0, 0, 0),i)
        write("7", 811, 400, (255, 255, 255), 45)

        j=pygame.Rect(788, 500, BUTTONS_SIZE, BUTTONS_SIZE)
        button_9 = pygame.draw.rect(SCREEN, (0, 0, 0),j)
        write("9", 811, 500, (255, 255, 255), 45)
        oddlist=[f,g,h,i,j]

        a=pygame.Rect(37, 100, BUTTONS_SIZE, BUTTONS_SIZE)
        button_0 = pygame.draw.rect(SCREEN, (0, 0, 0),a )
        write("0", 60, 100, (255, 255, 255), 45)

        b=pygame.Rect(37, 200, BUTTONS_SIZE, BUTTONS_SIZE)
        button_2 = pygame.draw.rect(SCREEN, (0, 0, 0),b)
        write("2", 60, 200, (255, 255, 255), 45)

        c=pygame.Rect(37, 300, BUTTONS_SIZE, BUTTONS_SIZE)
        button_4 = pygame.draw.rect(SCREEN, (0, 0, 0),c)
        write("4", 60, 300, (255, 255, 255), 45)

        d=pygame.Rect(37, 400, BUTTONS_SIZE, BUTTONS_SIZE)
        button_6 = pygame.draw.rect(SCREEN, (0, 0, 0),d)
        write("6", 60, 400, (255, 255, 255), 45)

        e=pygame.Rect(37, 500, BUTTONS_SIZE, BUTTONS_SIZE)
        button_8 = pygame.draw.rect(SCREEN, (0, 0, 0),e)
        write("8", 60, 500, (255, 255, 255), 45)
        evenlist=[a,b,c,d,e]

#the main function
def main():
    global turn
    clock = pygame.time.Clock()
    #board squares 
    input_box3=InputBox(548, 38, 150, 135) #the place of the boxes
    input_box2=InputBox(345, 38, 190, 135)
    input_box1=InputBox(140, 38, 145, 135)
    input_box6=InputBox(548, 188, 150, 135)
    input_box5=InputBox(345, 188, 190, 135)
    input_box4=InputBox(140, 188, 145, 135)
    input_box9=InputBox(548, 338, 150, 150)
    input_box8=InputBox(345, 338, 190, 150)
    input_box7=InputBox(140, 338, 145, 150)
    input_boxes=[input_box1,input_box2,input_box3,input_box4,input_box5,input_box6,input_box7,input_box8,input_box9]
    done = False

    #game while loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                index= input_boxes.index(box)
                box.handle_event(event,index,input_boxes)
                
                
        for box in input_boxes:
            box.update()
           

        SCREEN.fill((255,255, 255)) #color
        for box in input_boxes:
            box.draw()
            
        #check if there is a winner
        if checkwinner():
            write("CONGRATULATIONS!" , 200, 150, (255, 100, 0), 45)
            write("YOU'RE THE WINNER" , 200, 200, (255, 100, 0), 45)
        
        pygame.display.flip()
        pygame.display.update()
        #frame rate
        clock.tick(30)
        if gamedraw():
            write("GAME DRAW!" , 250, 200, (255, 100, 0), 45)
        pygame.display.flip()
        pygame.display.update()
        #frame rate
        clock.tick(30)

if __name__ == '__main__':
    main()
    pygame.quit()