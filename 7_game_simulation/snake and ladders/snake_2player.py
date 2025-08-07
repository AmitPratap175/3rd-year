import random as ran
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
player1 = 0
player2 = 0


#print ("Snakes and Ladders game")



def ladders_(x):#1,4,8,28,21,50,80,71
    if x == 1:
        return 38
    elif x == 4:
        return 14
    elif x == 8:
        return 30
    elif x == 28:
        return 76
    elif x == 21:
        return 42
    elif x == 50:
        return 67
    elif x == 80:
        return 99
    elif x == 71:
        return 92
    else:
        return x


# Snake Check
def snakes_(x):#32,36,48,62,88,95,97
    if x == 32:
        return 10
    elif x == 36:
        return 6
    elif x == 48:
        return 26
    elif x == 62:
        return 18
    elif x == 88:
        return 24
    elif x == 95:
        return 56
    elif x == 97:
        return 78
    else:
        return x


def check_for_snakes_and_ladders(n):
	"""This method checks for the presence of snakes or ladders in the board"""
	ladders = {1,4,8,28,21,50,80,71}
	snakes = {32,36,48,62,88,95,97}
	if n in ladders:
		#print ("Its a ladder,Climb up")
		n = ladders_(n)
	elif n in snakes:
		#print ("Its a snake!!,Come down")
		n = snakes_(n)
	return n


def roll_dice(r):
            """This method takes input from each of the players, prints the current position of the players and checks for the
            winner of the game"""
            d = ran.randint(1,6)
            if r+d<=100:
                        d = r + d
            else:
                        d=r
            return d,d-r

def position(player1):
            if player1==1:
                pos1=0.5
                pos2=0.5
            elif player1%10==1 and (player1//10)%2!=0:
                pos1=9.5
                pos2=player1//10+0.5
            elif player1%10==1 and (player1//10)%2==0:
                pos1=(player1%10)-0.5
                pos2=player1//10+0.5
            elif player1%10==0 and (player1//10)%2!=0:
                pos1=9.5
                pos2=player1//10-0.5
            elif player1%10==0 and (player1//10)%2==0:
                pos1=0.5
                pos2=player1//10-0.5
            elif (player1//10)%2!=0:
                pos1=10.5-(player1%10)
                pos2=player1//10+0.5
            elif (player1//10)%2==0:
                pos1=(player1%10)-0.5
                pos2=player1//10+0.5
            return pos1,pos2

def getchar_(i):
    if i>snakes_(i):
        return 'It is a snake!!! climb down'
    elif i<ladders_(i):
        return 'It is a ladder!!! climb up'
    else:
        return  ''

pos1=0
pos2=0
pos2_1=0
pos2_2=0
p1=0
p2=0

img= plt.imread("board.png")
figure, axes = plt.subplots()
axes.set(xlim=(0, 10), ylim = (0, 10))
x_left, x_right = axes.get_xlim()
y_low, y_high = axes.get_ylim()
axes.set_aspect(abs((x_right-x_left)/(y_low-y_high)))
plt.grid()
axes.imshow(img, extent=[0,10,0,10])


#17 54 62 64 87 93 95 98 


while player1 < 100 or player2 < 100:
            #print ("Its turn of player1\n")
            player1,p1 = roll_dice(player1)
            
            player1 = check_for_snakes_and_ladders(player1)
            #print ("Current status of Player1:",player1,"and Player2:",player2)

            pos1,pos2=position(player1)

            pos2_1,pos2_2=position(player2)

            if(pos1==pos2_1 and pos2==pos2_2):
                pos1-=0.05
                pos2_1+=0.05
                pos2-=0.05
                pos2_2+=0.05
            
            Drawing_colored_circle1 = plt.Circle(( pos1, pos2 ), 0.35 )
            Drawing_colored_circle2 = plt.Circle((pos2_1 , pos2_2  ), 0.35 ,color='g')
            axes.add_artist( Drawing_colored_circle1 )
            axes.add_artist( Drawing_colored_circle2 )
            plt.grid()
            for i in range(1,101):#1 4 9 28 21 51 80 72
                if i!=snakes_(i):
                    plt.plot([position(i)],[position(snakes_(i))],'r--')
            
            for i in range(1,10):
                plt.axhline(y = i, color = 'black', linestyle = '--',lw=0.5)
                plt.axvline(x = i, color = 'black', linestyle = '--',lw=0.5)
            plt.draw()
            plt.xticks([])
            plt.yticks([])
            plt.title('blue='+str(player1)+"  green="+str(player2)+"   Blue gets "+str(p1)+getchar_(player1))
            #plt.text(10,10,getchar_(player1))
            #getchar_(player1)
            plt.pause(1.5)
            Drawing_colored_circle1.remove()
            Drawing_colored_circle2.remove()

            if player1 == 100:
                    print ("Winner of the game is player1")
                    plt.title("Blue player is the winner!!!!!!!!!!!!!!")
                    break

            #print ("Its turn of player2\n")
            player2,p2 = roll_dice(player2)
            
            player2 = check_for_snakes_and_ladders(player2)
            #print ("Current status of Player1:",player1," and Player2:",player2)
            pos1,pos2=position(player1)

            pos2_1,pos2_2=position(player2)
            if(pos1==pos2_1 and pos2==pos2_2):
                pos1-=0.05
                pos2_1+=0.05
                pos2-=0.05
                pos2_2+=0.05

            Drawing_colored_circle1 = plt.Circle(( pos1, pos2 ), 0.35 )
            Drawing_colored_circle2 = plt.Circle((pos2_1 , pos2_2  ), 0.35 ,color='g')
            axes.add_artist( Drawing_colored_circle1 )
            axes.add_artist( Drawing_colored_circle2 )
            plt.grid()
            plt.draw()
            plt.xticks([])
            plt.yticks([])
            plt.title('blue='+str(player1)+"  green="+str(player2)+"   Green gets "+str(p2))
            #plt.text(1,-1,getchar_(player2))
            plt.pause(1.5)
            Drawing_colored_circle1.remove()
            Drawing_colored_circle2.remove()
            if player2 ==100:
                    print ("Winner of the game is player2")
                    plt.title("Green player is the winner!!!!!!!!!!!!!!")
                    break
plt.show()
