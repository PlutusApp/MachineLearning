import numpy
import json

data = 0
with open('./training_data/data.txt') as json_data:
    data = json.load(json_data)

targets = 0
with open('./training_data/targets.txt') as json_data:
    targets = json.load(json_data)



TA = 100000;
MI = 10000;
ME = 5000;
price = 300;
RCS = 2;

if(MI/ME <=1){
    if(price < 0.1 * MI){
        return 5;
    }
    else{
        return 6;
    }
}
else{
    if(TA <= 8 * ME){
            if(price < 0.5 * MI){
                if(price <= 0.1 * MI){
                    return 2;
                }
                else{
                    return 3;
                }
            }
            else{
                return 4;
            }
    }
    else{
        if(price <= 0.7 * TA){
            if(price < 0.2 * MI){
                return 2;
            }
            else{
                return 4;
            }
        }
        else{
            if(RCS <= 0.3){
                return 3;
            }
            else{
                return 1;
            }
        }
    }
}
