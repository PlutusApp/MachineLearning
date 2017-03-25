import numpy
import json
import random

def product_rating():
    data = 0
    with open('./training_data/data.txt') as json_data:
        data = json.load(json_data)

    targets = 0
    with open('./training_data/targets.txt') as json_data:
        targets = json.load(json_data)

        rand = random.randint(1,1000000)



        """MI = data[rand][0];
        ME = data[rand][1];
        TI = data[rand][2];
        RCS = data[rand][3];
        Age = data[rand][4];
        TA = data[rand][5];
        price = 10000;
        tar = targets[rand];"""

        MI = 500
        ME = 350
        TI = 12000
        RCS = 0.1
        Age = 19
        TA = 8000
        price = 110
        tar = 1

        print("mi is %f" % MI);
        print("me is %f" % ME);
        print("ti is %f" % TI);
        print("rcs is %f" % RCS);
        print("Age is %f" % Age);
        print("ta is %f" % TA);
        print("target is %f" % tar);

    if(MI/ME <= 0.8):
        if(price < 0.1 * MI):
            return 5;

        else:
            return 6;


    else:
        if(TA <= 10 * ME):
            if(price < 0.4 * MI):
                if(price <= 0.1 * MI):
                    return 2;

                else:
                    return 3;


            else:
                return 4;


        else:
            if(price <= 0.1 * TA):
                if(price < 0.2 * MI):
                    print("2")
                    return 2;

                else:
                    return 4;


            else:
                if(RCS <= 0.3):
                    return 3;

                else:
                    return 1;



print(product_rating())
