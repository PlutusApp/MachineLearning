import numpy
import sys
import json
import ast

def main():
    #users = sys.argv[2];
    json_data = "[[0,100,2],[23,120,56],[35,90,10],[11,50,150],[33,140,4],[45,115,15],[67,80,10],[56,87,43],[87,95,40],[12,125,21]]"
    #users = json_data.split(' , ')
    users = eval(json_data)
    """MI = argv[3];
    userinfo = argv[2];
    users = argv[4];"""

    MI0 = sys.argv[2]
    MI = float(MI)
    userinfo0 = sys.argv[1]
    userinfo = float(userinfo0)
    j_data = sys.argv[3]
    users = eval(j_data)

    """"for a in range(0,2):
    users.remove(users[0])
    MI = 10000
    userinfo = 2
    print(users)"""
    """users = {
        'user1' : [0,100,2],
        'user2' : [23,120,56],
        'user3' : [35,90,10],
        'user4' : [11,50,150],
        'user5' : [33,140,4],
        'user6' : [45,115,15],
        'user7' : [67,80,10],
        'user8' : [56,87,43],
        'user9' : [87,95,40],
        'user10' : [12,125,21]
    }"""

    """users = [[0,100,2],[23,120,56],[35,90,10],[11,50,150],[33,140,4],[45,115,15],[67,80,10],[56,87,43],[87,95,40],[12,125,21]]"""



    """users.remove(users[2])
    print(users)"""


    for i in range(0,10):
        for j in range(0,10):
            #if users["user"+str(j)][2]
            if users[j][2] > users[i][2]:
                temp = users[j]
                users[j] = users[i]
                users[i] = temp

    for k in range(0,10):
        users[k][2] = k+1
        rate = users[k][2] * (users[k][1]/MI);
        users[k].append(rate);

    for i in range(0,10):
        for j in range(0,10):
            #if users["user"+str(j)][2]
            if users[j][3] > users[i][3]:
                temp = users[j]
                users[j] = users[i]
                users[i] = temp

    print([users[0][0],users[1][0],users[2][0],users[3][0],users[4][0]])

main()
