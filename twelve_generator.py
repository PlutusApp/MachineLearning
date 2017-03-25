import random
import json


    data = 0
    with open('./training_data/data.txt') as json_data:
        data = json.load(json_data)

#2 rated people
MI = data[0][0];
ME = data[0][1];
TI = data[0][2];
RCS = data[0][3];
Age = data[0][4];
TA = data[0][5];
price = 10000;
tar = targets[0];
