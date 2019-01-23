from random import randint as rand
import copy
import time
timeF = 0
def truncate(n): #taken from https://realpython.com/python-rounding/
    return float(int(n*1000))/1000
def makeover(n):
    n = truncate(n)
    m = str(int(n//60))
    s = str(n%60)
    if len(str(int(n%60))) != 2:
        s = "0"+s
    while len(s) < 6:
        s += "0"
    m += ":"
    return m+s
class Scramble:
    def __init__(self,cube):
        self.cube = cube
        self.moves = [[["R2", "R'", "R"], ["L2", "L'", "L"], [["Rw2", "Rw'", "Rw"], ["2R2", "2R'", "2R"]], [["Lw2", "Lw'", "Lw"], ["2L2", "2L'", "2L"]], ["3R2", "3R'", "3R"], ["3L2", "3L'", "3L"]], 
                      [["U2", "U'", "U"], ["D2", "D'", "D"], [["Uw2", "Uw'", "Uw"], ["2U2", "2U'", "2U"]], [["Dw2", "Dw'", "Dw"], ["2D2", "2D'", "2D"]], ["3U2", "3U'", "3U"], ["3D2", "3D'", "3D"]], 
                      [["F2", "F'", "F"], ["B2", "B'", "B"], [["Fw2", "Fw'", "Fw"], ["2F2", "2F'", "2F"]], [["Bw2", "Bw'", "Bw"], ["2B2", "2B'", "2B"]], ["3F2", "3F'", "3F"], ["3B2", "3B'", "3B"]]]
        self.s = self.scramble()
        self.d = True
    def scramble(self):
        tmp = ""
        N = 2
        G = 3
        PG = 3
        LG = 3
        for x in range(20*(self.cube-2)+10*(not self.cube-2)):
            G = rand(0,2)
            while ((self.cube-2) and G == LG) or G == PG:
                G = rand(0,2)
            if G == PG:
                N = not N
            else:
                N = rand(0,self.cube-2)
            if self.cube >= 6 and (N == 2 or N == 3):
                tmp += self.moves[G][N][1][rand(0,6)%3] + " "
            elif self.cube >= 4 and (N == 2 or N == 3):
                tmp += self.moves[G][N][0][rand(0,6)%3] + " "
            else:
                tmp += self.moves[G][N][rand(0,6)%3] + " "
            if PG == G:
                LG = G
            else:
                PG = G
            if not (x+1)%10:
                tmp += "\n"
        print(tmp)
        return tmp
    def display(self):
        if self.d:
            lss = list(self.s)
            textSize(40//self.cube+self.cube)
            text(self.s,10,350-18*(self.cube-2))
    def __str__(self):
        return self.s
class Timer:
    def __init__(self):
        self.tf = 0
        self.time = 00.000
        self.ptime = 00.000
        self.ctime = 00.000
        self.mode = 0
    def update(self):
        if self.mode == 3:
            self.time = (time.time() - self.t)
            self.ptime = self.time
        elif self.mode == 1:
            if time.time() - self.tf >= 0.5:
                self.mode = 2
    def display(self):
        self.update()
        textSize(48)
        fill(255)
        if self.mode == 1:
            fill(255,0,0)
        elif self.mode == 2:
            fill(0,255,0)
        strTime = makeover(self.ptime)
        text(strTime,535 - 15*(len(strTime)), 360)
        fill(255)
class Time:
    def __init__(self,t,scramble):
        self.delete = 0
        self.s = t%60
        self.m = int(t//60)
        self.DNF = False
        self.p2 = False
        self.showS = False
        self.t = t
        self.v = t + 1000000000*self.DNF + 2*self.p2
        self.c = False
        self.S = scramble
        self.i = len(P.times[P.cube-2])+1
    def __int__(self):
        return self.v
    def __str__(self):
        self.i = P.times[P.cube-2].index(self)
        if len(str(int(self.s))) < 2:
            s = str(self.s)
            s = "0" + s
        else:
            s = str(self.s)
        while len(s) < 6:
            s += "0"
        s = str(self.m) + ":" + s
        if self.c:
            return "(" + s + ")"
        return s
    def update(self):
        self.i = P.times[P.cube-2].index(self)
        self.x1 = 70 + 100*(int(self.i//10))
        self.x2 = self.x1 + 54
        self.y1 = 491 + 20*(int(self.i%10))
        self.y2 = self.y1 + 10
        self.v = self.t + 1000000000*self.DNF + 2*self.p2
        if (
            len(P.ctimes) > 2 and  # no crosses if less than 2 solves
            (P.ctimes[0] == self.v or  # best time
            P.rtimes[0] == self.v) and # worst time
            (P.ctimes.count(self.v) == 1 or  # checks if there is more than one instance
            ((P.ttimes.index(self.v) == self.i) or # first instance
            (P.ctimes.count(self.v) == len(P.ctimes) and self.i == len(P.ctimes) - 1))) # last instance if all numbers are the same
            ):
            self.c = True
        else:
            self.c = False
    def display(self):
        fill(150*(self.DNF)-20*self.delete+54*self.c,54-10*self.delete-54*(self.DNF+self.p2)+54*self.c,108*(self.p2)-20*self.delete+54*self.c)
        rect(70 + 100*(int(self.i//10)),491 + 20*(int(self.i%10)),54,10)
        fill(255)
        textSize(10)
        if (not self.c and len(str(self)) > 8) or (self.c and len(str(self)) > 10):
                if self.c:
                    textSize(20 - len(str(self)))
                else:
                    textSize(18 - len(str(self)))
        if self.c:
            text(str(self),72 + 100*(int(self.i//10)),500 + 20*(int(self.i%10)))
        else:
            text(str(self),75 + 100*(int(self.i//10)),500 + 20*(int(self.i%10)))
        if self.showS and self.S:
            textSize(20//P.cube+P.cube)
            fill(205,147,234) 
            text(str(self.S), 10, 100)
            fill(255)
class Program:
    def __init__(self):
        #### DUMMIES ####
        self.CMo3 = False
        self.BMo3 = False
        self.CAo5 = False
        self.BAo5 = False
        self.CAo10 = False
        self.BAo10 = False
        self.AoS = False
        self.MoS = False
        #### DUMMIES ####
        self.S = Scramble(3)
        self.T = Timer()
        self.blind = False
        self.times = [[],[],[],[],[],[]]
        self.state = "main"
        self.timerT = ""
        self.keys = {"SPACE":False,"TAB":False}
        self.cube = 3
        self.ctimes = []
        self.rtimes = []
        self.ttimes = []
    def update(self):
        self.ttimes = []
        for i in self.times[self.cube-2]:
            self.ttimes.append(i.v)
        ttimes = self.ttimes
        self.ctimes = sorted(self.ttimes)
        self.rtimes = sorted(self.ttimes, reverse = True)
        ctimes = self.ctimes
        ###### BUGGED? ######
        for t in ttimes:
            if t//100000000:
                t = "DNF"
        for t in ctimes:
            if t//1000000000:
                t = "DNF"
        if len(ttimes) > 2:
            AoT = ctimes[1:len(ttimes)-1]
            DNF = 0
            for i in AoT:
                if i == "DNF":
                    DNF += 1
                    AoT.remove(i)
            if len(AoT) > 2 and DNF:
                self.AoS = makeover(sum(AoT)/(len(AoT))) + " DNF" + str(DNF)
            elif not len(AoT):
                self.AoS = "DNF" + str(DNF-1)
            elif not DNF:
                self.AoS = makeover(sum(AoT)/(len(AoT)))
        else:
            self.AoS = False
        if len(ttimes):
            MoT = ctimes[:len(ttimes)]
            DNF = 0
            for i in MoT:
                if i == "DNF":
                    DNF += 1
                    MoT.remove(i)
            if len(MoT) and DNF:
                self.MoS = makeover(sum(MoT)/(len(MoT))) + " DNF" + str(DNF)
            elif not len(MoT):
                self.MoS = "DNF" + str(DNF)
            elif not DNF:
                self.MoS = makeover(sum(MoT)/(len(MoT)))
        else:
            self.MoS = False
        if len(ttimes) > 9:
            self.CAo10 = makeover(sum(sorted(ttimes[:10])[1:9])/8)
            self.CAo5 = makeover(sum(sorted(ttimes[:5])[1:4])/3)
            self.CMo3 = makeover(sum(ttimes[:3])/3)
            self.BAo10 = makeover(sum(ctimes[1:9])/8)
            self.BAo5 = makeover(sum(ctimes[1:4])/3)
            self.BMo3 = makeover(sum(ctimes[:3])/3)
        elif len(ttimes) > 4:
            self.CAo5 = makeover(sum(sorted(ttimes[:5])[1:4])/3)
            self.CMo3 = makeover(sum(ttimes[:3])/3)
            self.BAo5 = makeover(sum(ctimes[1:4])/3)
            self.BMo3 = makeover(sum(ctimes[:3])/3)
        elif len(ttimes) > 2:
            self.CMo3 = makeover(sum(ttimes[:3])/3)
            self.BMo3 = makeover(sum(ctimes[:3])/3)
        for t in self.times[self.cube-2]:
            t.update()
    def display(self):
        if self.state == "main":
            if not self.blind or not self.T.mode:
                self.S.display()
                self.T.display()
                for t in self.times[self.cube-2]:
                    t.display()
                textSize(10)
                if not self.T.mode:
                    if self.times[self.cube-2]:
                        text("Session Mean: "+str(self.MoS),946,180)
                    if self.AoS:
                        text("Session Average: "+str(self.AoS),932,200)
                    if len(self.times[self.cube-2]) > 2:
                        text("Current Mo3: "+str(self.CMo3),950,220)
                        text("Best Mo3: "+str(self.BMo3),967,240)
                    if len(self.times[self.cube-2]) > 4:
                        text("Current Ao5: "+str(self.CAo5),952,260)
                        text("Best Ao5: "+str(self.BAo5),969,280)
                    if len(self.times[self.cube-2]) > 9:
                        text("Current Ao10: "+str(self.CAo10),946,300)
                        text("Best Ao10: "+str(self.BAo10),963,320)
                s = 50
                g = 24
                if self.blind:
                    fill(0)
                for i in range(self.cube):
                    for j in range(self.cube):
                        rect(10+j*((s/self.cube)+(g/(self.cube))),
                            10+i*((s/self.cube)+(g/(self.cube))),
                            (s/self.cube), 
                            (s/self.cube))
                fill(255)
            elif self.T.mode == 1:
                self.T.display()
                background(55,0,0)
            elif self.T.mode == 2:
                self.T.display()
                background(0,55,0)
            elif self.T.mode == 3:
                self.T.display()
                background(0)
        elif self.state == "insert":
            fill(255)
            textSize(50)
            text("Insert Time",390,150)
            textSize(30)
            text("(in seconds)",440,180)
            text(self.timerT, 540-10*len(self.timerT),330)
        elif self.state == "cube":
            fill(255)
            textSize(50)
            text("Insert Cube",390,150)
            textSize(30)
            text("(NxNxN only, insert N)",370,180)
    
P = Program()
def setup():
    size(1080,720)
    textSize(32)
    fill(255)
    stroke(255)
def draw():
    background(0)
    P.display()
def keyPressed():
    if P.state == "cube":
        if "2" <= key <= "7":
            P.cube = int(key)
            P.state = "main"
            P.update()
            P.T.__init__()
            P.S.__init__(P.cube)
    if P.state == "insert":
        if "0" <= key <= "9":
            if P.timerT.count(".") and len(P.timerT[P.timerT.index("."):len(P.timerT)]) > 3:
                pass
            else:
                P.timerT += key
        if key == BACKSPACE:
            P.timerT = P.timerT[0:len(P.timerT)-1]
        if key == "." and not P.timerT.count(".") and len(P.timerT):
            P.timerT += key
        if key == ENTER:
            if P.timerT:
                while P.timerT.count(".") and len(P.timerT[P.timerT.index("."):len(P.timerT)]) <= 3:
                    P.timerT += "0"
                if P.timerT.count("."):
                    P.timerT = P.timerT[:P.timerT.index(".")]+P.timerT[P.timerT.index(".")+1:]
                    timing = float(P.timerT)/1000
                else:
                    timing = float(P.timerT)
                P.times[P.cube-2].insert(0,Time(timing,False))
                while len(P.times[P.cube-2]) > 100:
                    del(P.times[P.cube-2][len(P.times[P.cube-2])-1])
                for t in P.times[P.cube-2]:
                    t.i = P.times[P.cube-2].index(t)
                    t.update()
                P.T.ptime = timing
                P.T.update()
                P.update()
                P.state = "main"
    if key == TAB and not P.T.mode and not P.keys["TAB"]:
        P.keys["TAB"] = True
        if P.state == "main":
            P.state = "insert"
            P.timerT = ""
        elif P.state == "insert":
            P.state = "main"
    # if key == "s" and not P.T.mode:
    #     P.state = "cube setter"
    if keyCode == 32 and not P.keys["SPACE"]:
        P.keys["SPACE"] = True
        if P.T.mode == 3:
            P.T.mode = 0
            P.times[P.cube-2].insert(0,Time(truncate(P.T.ptime),str(P.S)))
            P.S.__init__(P.cube)
            P.S.d = True
            while len(P.times[P.cube-2]) > 100:
                del(P.times[P.cube-2][len(P.times[P.cube-2])-1])
            for t in P.times[P.cube-2]:
                t.i = P.times[P.cube-2].index(t)
                t.update()
            P.update()
        elif not P.T.mode:
            global time
            P.T.mode = 1
            P.T.tf = time.time()
            P.S.d = False
    if P.state == "main" and not P.T.mode and key == BACKSPACE:
        x = mouseX
        y = mouseY
        if 10 <= x <= 80 and 10 <= y <= 80:
            P.blind = not P.blind
        for t in P.times[P.cube-2]:
            if t.x1 <= x <= t.x2 and t.y1 <= y <= t.y2:
                t.delete += 1
                if t.delete == 10:
                    P.times[P.cube-2].remove(t)
                    for q in P.times[P.cube-2]:
                        q.update()
                        P.update()
            else:
                t.delete = 0
    if P.state == "main" and not P.T.mode and key == ENTER:
        x = mouseX
        y = mouseY
        for t in P.times[P.cube-2]:
            if t.x1 <= x <= t.x2 and t.y1 <= y <= t.y2:
                t.showS = True
            else:
                t.showS = False
    print keyCode,key
def keyReleased():
    if key == BACKSPACE:
        for t in P.times[P.cube-2]:
            t.delete = 0
    if keyCode == 32:
        P.keys["SPACE"] = False
        if P.T.mode == 1:
            P.T.mode = 0
            P.S.d = True
        elif P.T.mode == 2:
            P.T.t = time.time()
            P.T.__init__()
            P.T.mode = 3 
    if key == TAB:
        print "hops"
        P.keys["TAB"] = False
    if key == ENTER:
        for t in P.times[P.cube-2]:
            t.showS = False
def mouseClicked():
    if P.state == "main" and not P.T.mode:
        x = mouseX
        y = mouseY
        if 10 <= x <= 80 and 10 <= y <= 80:
            P.state = "cube"
        for t in P.times[P.cube-2]:
            if t.x1 <= x <= t.x2 and t.y1 <= y <= t.y2:
                if not (t.DNF or t.p2):
                    t.p2 = True
                elif t.p2:
                    t.p2 = False
                    t.DNF = True
                elif t.DNF:
                    t.DNF = False
                t.update()
                P.update()
