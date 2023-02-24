#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import math



if __name__ == "__main__":
    # file = 'locateGravity1.txt'
    # result=[]
    # with open(file,"r") as f:
    #     for line in f.readlines():
    #         split_line = line.split(' ')
    #         if (len(split_line) < 58): break
    #         result.append([float(split_line[i]) for i in [15, 22, 29, 36, 43, 50, 57]])

    # df = pd.DataFrame(result)
    # df.plot()
    # plt.show()
    gacc = 9.81
    l = [0.0555, 0.264, 0.297]
    gear = [80.0/18, 80.0/26, 80.0/26]
    tor_50deg = [0.15, 0.27, 1.15]
    tor_90deg = [0.2, 0.40, 2.0]
    joint_tor50 = [tor_50deg[i]*2*gear[i] for i in range(3)]
    joint_tor90 = [tor_90deg[i]*2*gear[i] for i in range(3)]
    mass = [0.13, 2.0, 3.5]
    w = [mass[i]*gacc for i in range(3)]
    dx = []
    dy = []
    c,s = math.cos(50*math.pi/180), math.sin(50*math.pi/180)

    dx.append(joint_tor90[0]/w[0])
    dy.append((joint_tor50[0] - w[0]*s*dx[0])/(-w[0]*c))
    print("Calculated end_effector dx, dy:", dx[-1], dy[-1])

    dx[0] = l[0]/2
    dy[0] = 0
    ww = joint_tor90[0]/dx[0]
    print("If end_effector mass is at center, mass:" ,ww/gacc)
    w[1] += w[0]
    w[0] = 0

    lenDx = (dx[0]+l[1])
    print(lenDx, lenDx*w[0])
    dx.append((joint_tor90[1] - lenDx*w[0])/w[1])
    dy.append((joint_tor50[1] - w[0]*s*lenDx + w[0]*c*dy[0] - w[1]*s*dx[1] )/(-w[1]*c))

    lenDx = (dx[0]+l[1]+l[2])
    lenCx = (dx[1]+l[2])
    print(lenCx, lenCx*w[1])
    dx.append((joint_tor90[2] - lenDx*w[0] - lenCx*w[1])/w[2])
    dy.append((joint_tor50[2] - w[0]*s*lenDx + w[0]*c*dy[0] - w[1]*s*lenCx + w[1]*c*dy[1] - w[2]*s*dx[2])/(-w[2]*c))

    print("joint_tor50: ", joint_tor50)
    print("joint_tor90: ", joint_tor90)
    print("dx(end_effector,D,C): ", dx)
    print("dy(end_effector,D,C): ", dy)


