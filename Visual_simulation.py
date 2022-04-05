
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import os
Vmax = 4

class people():
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
        self.vx = (random.random()-0.5)*Vmax
        self.vy = (random.random()-0.5)*Vmax
        self.type = "normal"
    def changetype(self, new_type):
        self.type = new_type

beta = 0.3
alpha = 0.05
gamma = 0.05

s_width = 10
s_height = 10
dt = 0.1
t_length = 50

def iscontact(person1, person2):
    if math.sqrt((person1.x-person2.x)**2+(person1.y-person2.y)**2) < 0.6:
        return True
    else:
        return False

def main(P, I):
    peoplelist = []
    currenttype = []
    for i in range(P):
        peoplelist.append(people(random.random()*s_width, random.random()*s_height))
        currenttype.append("normal")
    for i in range(I):
        peoplelist[i].changetype("infectious")
        currenttype[i] = "infectious"

    # Set up the time range
    t = np.arange(0, t_length, dt)
    N = []
    I = []
    R = []
    for i in range(len(t)):
        for person in peoplelist:
            person.x = person.x + person.vx*dt
            if person.x > s_width:
                person.x = 2*s_width-person.x
                person.vx = -person.vx
            elif person.x < 0:
                person.x = -person.x
                person.vx = -person.vx

            person.y = person.y + person.vy*dt
            if person.y > s_height:
                person.y = 2*s_height-person.y
                person.vy = -person.vy
            elif person.y < 0:
                person.y = -person.y
                person.vy = -person.vy


        for j in range(len(peoplelist)):
            if peoplelist[j].type == "infectious":
                for k in range(len(peoplelist)):
                    if iscontact(peoplelist[j], peoplelist[k]):
                        if peoplelist[k].type == "normal":
                            if random.random() < beta:
                                currenttype[k] = "infectious"
                        elif peoplelist[k].type == "recovered":
                            if random.random() < alpha:
                                currenttype[k] = "infectious"
                if random.random() < gamma:
                    currenttype[j] = "recovered"

        for j in range(len(peoplelist)):
            peoplelist[j].type = currenttype[j]

        for j in range(len(peoplelist)):
            if peoplelist[j].type == "normal":
                color = "y"
            elif peoplelist[j].type == "infectious":
                color = "r"
            else:
                color = "b"
            plt.scatter(peoplelist[j].x, peoplelist[j].y, s = 20, c = color)
        plt.title(f"Simulation at t = %02f"%(t[i]))
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.xlim([0, 10])
        plt.ylim([0, 10])
        plt.savefig("%04d.png"%(i))
        plt.cla()
        plt.clf()

        numN = 0
        numI = 0
        numR = 0
        for j in range(len(peoplelist)):
            if peoplelist[j].type == "normal":
                numN += 1
            elif peoplelist[j].type == "infectious":
                numI += 1
            else:
                numR += 1

        N.append(numN)
        I.append(numI)
        R.append(numR)

    plt.plot(t, N, "y-", label = "Normal")
    plt.plot(t, I, "r-", label = "Infectious")
    plt.plot(t, R, "b-", label = "Recovered")
    plt.title("Type of people change over time")
    plt.xlabel("Time")
    plt.ylabel("Number of people")
    plt.grid()
    plt.legend()
    plt.savefig("pandemic.png")


    os.system("ffmpeg -framerate 20 -y -i ./%04d.png ./simulation.mp4")

main(100, 1)







