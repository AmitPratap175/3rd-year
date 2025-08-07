import random as ran
import matplotlib.pyplot as plt
import numpy as np
import math

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
            d = np.random.randint(1,6)
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
        return "   It is a snake!!! At "+str(i)+", climb down"
    elif i<ladders_(i):
        return "   It is a ladder!!! At "+str(i)+", climb up"
    else:
        return  ""

pos1=0
pos2=0
pos2_1=0
pos2_2=0
p1=0
p2=0
plt.style.use("dark_background")
img= plt.imread("board.png")
figure, axes = plt.subplots()
axes.set(xlim=(0, 10), ylim = (0, 10))
x_left, x_right = axes.get_xlim()
y_low, y_high = axes.get_ylim()
axes.set_aspect(abs((x_right-x_left)/(y_low-y_high)))
plt.grid()
axes.imshow(img, extent=[0,10,0,10])

def animate(player1,pos1,pos2,p1,a):
            Drawing_colored_circle1 = plt.Circle(( pos1, pos2 ), 0.35 ,color='g')
            axes.add_artist( Drawing_colored_circle1 )
            plt.grid()
            for i in range(1,10):
                plt.axhline(y = i, color = 'black', linestyle = '--',lw=0.5)
                plt.axvline(x = i, color = 'black', linestyle = '--',lw=0.5)
            plt.draw()
            plt.xticks([])
            plt.yticks([])
            #plt.title('blue='+str(player1)+"   Blue gets "+str(p1))
            plt.title(" Dice gets "+str(p1)+a)
            
            #plt.pause(0.1)
            plt.pause(1.5)
            Drawing_colored_circle1.remove()

#17 54 62 64 87 93 95 98 

def snake_and_ladders(player1,i):
    n=0
    while player1 < 100 :
            #print ("Its turn of player1\n")
            player1,p1 = roll_dice(player1)
            a=getchar_(player1)
            
            
            #print ("Current status of Player1:",player1,"and Player2:",player2)
            ladders = {1,4,8,28,21,50,80,71}
            snakes = {32,36,48,62,88,95,97}
            pos1,pos2=position(player1)
            if i==1 and player1 in ladders :
                animate(player1,pos1,pos2,p1,a)
                
                player1 = check_for_snakes_and_ladders(player1)
                pos1,pos2=position(player1)
                plt.pause(0.25)
                animate(player1,pos1,pos2,p1,a)
            elif i==1 and player1 in snakes :
                animate(player1,pos1,pos2,p1,a)
                
                player1 = check_for_snakes_and_ladders(player1)
                pos1,pos2=position(player1)
                plt.pause(0.25)
                animate(player1,pos1,pos2,p1,a)
            elif i==1:
                player1 = check_for_snakes_and_ladders(player1)
                pos1,pos2=position(player1)
                animate(player1,pos1,pos2,p1,a)
            else:
                player1 = check_for_snakes_and_ladders(player1)
            n+=1
            if player1 == 100:
                    #print ("The end of game "+str(i+1))
                    plt.title("The game ends with "+str(n)+" moves")
                    break
    if i==1:
        plt.show()
    return n
number=[]
for i in range(10000):
    player1 = 0
    number.append(snake_and_ladders(player1,i+1))
w=1
number=np.array(number)
n_ = math.ceil((np.max(number) - np.min(number))/w)
plt.hist(number,bins=n_)
plt.title("The distribution of number of steps it takes to win a game")
plt.ylabel("Frequecy")
plt.xlabel("No. of moves")
plt.show()
