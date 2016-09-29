'''
Created on Jan 22, 2015

@author: Ivory
'''
import random

def hair_ZigZag():
    a2 = r"/\/\/\/\/\/\/\/"  #This function returns hair that is a Zig Zags |>*<|  |>*<|
    return a2

def hair_pointy():
#This function returns hair that has boxes with points on top.
    b2 = r"][][][][][][][]"
    b3 = r"^^^^^^^^^^^^^^^"
    return b3 + "\n" + b2
    
def hair_grass():
    c1 = r"WWWWWWWWWWWWWWW" #This function returns hair that looks like grass
    return c1 + "\n" + c1

def hair_BantuKnots():
    d1 = r"@@@@@@@@@@@@@@@" #This function returns hair that looks like Bantu Knots
    return d1

#HERE STARTS MY EYE FUNCTIONS

def eyes_Creepy():
    e1 = r" ____     ____ "
    e2 = r" \ O \   / O / "
    e3 = r" /___/   \___\ "     # This function makes creepy slanted eyes.
    return e1 +"\n" + e2 + "\n" + e3

def eyes_BugEyes():
    f1 = r" _   _     _  _"
    f2 = r" \(*)/    \(*)/"      #This function makes eyes that look like bug eyes
    f3 = r"   \/       \/ "
    return f1 +"\n" + f2 + "\n" + f3
def eyes_Broke():
    g1 = r" ____     ____ "
    g2 = r"] $0 [   ] $0 ["       #This function makes eyes with 0 dollars in them.
    g3 = r" ----     ---- "
    return g1 + "\n" + g2 + "\n" + g3

#HERE STARTS MY NOSE FUNCTIONS

def nose_BigNostrils():
    h1 = r"|   ()  ()    |"    #This function makes regular circle nostrils
    h2 = r"|             |"
    return h1 + "\n" + h2
def nose_diamond():
    i1 = r"|    /\  /\   |"
    i2 = r"|    \/  \/   |"     #This function makes large diamond nostrils
    i3 = r"|             |"
    return i1 +"\n" + i2 +"\n" + i3
def nose_Booger():
    j1 = r"|  (* ) (  )  |"    #This function makes big oval nostrils with a booger in one
    j2 = r"|             |"
    return j1 + "\n" + j2

#HERE STARTS MY MOUTH FUNCTIONS

def mouth_BigKisses():
    k1 = r"|    /\_/\    |"   #This function returns a mouth that looks like kissy lips
    k2 = r"|    -----    |"
    k3 = r"|    \___/    |"
    return k1 + "\n" + k2 + "\n" + k3
def mouth_straight():
    l1 = r"|  _________  |"   #This function returns a straight, serious-looking mouth
    return l1
def mouth_LittleCircle():
    m1 = r"|     ()      |"   #This function returns a little, disproportionate circle mouth
    return m1
    
#HERE STARTS MY CHIN FUNCTIONS
    
def chin_PointyBeard():
    n2 = r" \____________/"
    n3 = r"     \^^^/     "     #This function returns a chin with a pointy beard
    n4 = r"      \^/      "
    n5 = r"       v       "
    return n2 + "\n" + n3 + "\n" + n4 + "\n" + n5
def chin_CurlyBeard():
    o2 = r" \____________/"
    o3 = r"  @@@@@@@@@@@@ "     #This function returns a chin with a curly beard
    return o2 +"\n" + o3
def chin_spiked():
    p1 = r" \____________/"     #This returns a chin with a spikey beard
    p2 = r"  VVVVVVVVVVVV "
    return p1 +"\n" + p2

#HERE STARTS MY BOWTIE FUNCTIONS

def bowtie_star():
    q1 = r"     |\^/|     "
    q2 = r"     |/v\|     "    #This function returns a jagged-edge bowtie
    return q1 + "\n" + q2
def bowtie_Butterfly():
    r1 = r"     (\./)     "    #This on returns a butterfly bowtie
    r2 = r"     (/*\)     "
    return r1 + "\n" + r2
def bowtie_Strange():
    r1 = r"    /\\//\     "    #This one returns a bowtie with strange lines
    r2 = r"    \//\\/     "
    return r1 +"\n" + r2
def bowtie_Normal():
    s1 = r"     |\ /|     "  #This returns A FAIRLY NORMAL BOW TIE
    s2 = r"     |/*\|     "
    return s1 + "\n" + s2

def Head3():
    print hair_BantuKnots()
    print eyes_Creepy()
    print nose_Booger()      #This function compiles all the traits that make head 3
    print mouth_BigKisses()
    print chin_PointyBeard()
def Head1():
    print hair_ZigZag()
    print eyes_BugEyes()
    print nose_diamond()     #This function compiles all the traits that make head 1
    print mouth_LittleCircle()
    print chin_CurlyBeard()
    print bowtie_Butterfly()
    
def Head2():
    print hair_grass()
    print eyes_Broke()
    print nose_BigNostrils()   #This function compiles all the traits that make head 2
    print mouth_straight()
    print chin_spiked()
    print bowtie_Strange()
    
def totem():
    Head1()
    Head2()          #This function calls head 1, 2 and 3 for my (not random) totem pole
    Head3()
    
def random_hair():
    choice = random.randint(1,4)
    if choice == 1:
        print hair_ZigZag()
    elif choice == 2:
        print hair_pointy()
    elif choice == 3:          #This one chooses hair at random
        print hair_BantuKnots()
    else:
        print hair_grass()
def random_eyes():
    choice = random.randint(1,3)
    if choice==1:
        print eyes_Broke()     #This one chooses a set of eyes at random
    elif choice==2:
        print eyes_BugEyes()
    else:
        print eyes_Creepy()
def random_nose():
    choice= random.randint(1,3)
    if choice== 1:
        print nose_BigNostrils()  #This one chooses a nose at random
    elif choice ==2:
        print nose_Booger()
    else:
        print nose_diamond()
def random_mouth():
    choice= random.randint(1,3)
    if choice==1:
        print mouth_BigKisses()
    elif choice==2:               #This one chooses a mouth at random
        print mouth_LittleCircle()
    else:
        print mouth_straight()
def random_chin():
    choice = random.randint(1,3)
    if choice==1:
        print chin_CurlyBeard()    #This function chooses a beard (chin) at random
    if choice==2:
        print chin_PointyBeard()
    else:
        print chin_spiked()
    
def random_BowtieorNah():
    choice= random.randint(1,2)
    if choice== 1:
        choice = random.randint(1,4)
        if choice==1:
            print bowtie_Butterfly()    #This function only prints a bow tie if the random #
        elif choice==2:                 #is 1 and then prints a random bow tie if so.
            print bowtie_Normal()
        elif choice==3:
            print bowtie_star()
        else:
            print bowtie_Strange()
    else:
        print
def randompole():
    random_hair()
    random_eyes()
    random_nose()
    random_mouth()
    random_chin()
    random_BowtieorNah()    #This function calls all of the random functions three times
    random_hair()            #to make my random totem pole
    random_eyes()
    random_nose()
    random_mouth()
    random_chin()
    random_BowtieorNah()
    random_hair()
    random_eyes()
    random_nose()
    random_mouth()
    random_chin()
    random_BowtieorNah()
    
if __name__ == "__main__":
    # main function to print a totem pole with three heads followed by
    #   a random totem pole
    print "My totem pole"
    print
    totem()
    print
    print
    print "My random totem pole"
    print
    randompole()
    

    


