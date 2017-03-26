import sys

usertype0 = sys.argv[1]
usertype = int(usertype0)
price0 = sys.argv[2]
price = float(price0)
MI0 = sys.argv[3]
MI = float(MI0)
rating0 = sys.argv[4]
rating = float(rating0)


def main():
        if usertype == 0 or usertype == 2:
            if (rating <= 1):
                if (price <= 0.1*MI):
                    sentence = "This is a product of fair price and good quality which is suitable for your saving habit."
                    result = [sentence , "good-buy" , "done"]
                    print(result);
                    return;
                else:
                    sentence = "This is a product of fair price but the quality cannot be guaranteed."
                    result = [sentence , "good-buy" , "done"]
                    print(result);
                    return;
            elif rating > 1 and rating <= 2:
                if price > 0.1*MI and price < 0.4*MI:
                    sentence = "The item is not fully encouraged to buy. The suggestion is to look for other products or save for later and better use."
                    result = [sentence , "average-buy" , "warning"]
                    print(result);
                    return;
                else:
                    sentence = "This is a good product but you are encouraged to consider if you really need it."
                    result = [sentence , "average-buy" , "warning"]
                    print(result);
                    return;
            else:
                sentence = "You should reconsider about your saving habit. If the item is not essential, there might be a better way you can use the money."
                result = [sentence , "bad-buy" , "not_interested"]
                print(result);
                return;
        elif usertype == 1:
            if (rating <= 2):
                if (price < 0.3*MI):
                    sentence = "This is a product of fair price and good quality which is suitable for your saving habit."
                    result = [sentence , "good-buy" , "done"]
                    print(result);
                    return;
                else:
                    sentence = "This is a product of fair price but the quality cannot be guaranteed."
                    result = [sentence , "good-buy" , "done"]
                    print(result);
                    return;
            elif rating >= 2 and rating <=3:
                if price >= 0.3*MI and price <= 0.6*MI:
                    sentence = "The item is not fully encouraged to buy. The suggestion is to look for other products or save for later and better use."
                    result = [sentence , "average-buy" , "warning"]
                    print(result);
                    return;
                else:
                    sentence = "This is a good product but you are encouraged to consider if you really need it."
                    result = [sentence , "average-buy" , "warning"]
                    print(result);
                    return;
            else:
                if price < 0.6*MI:
                    sentence = "If this is a good investment for you, think deeply about it."
                    result = [sentence , "bad-buy" , "not_interested"]
                    print(result);
                    return;
                else:
                    sentence = "The cost and quality is not in good proposition. The suggestion is to look for other products or save for later and better use."
                    result = [sentence , "bad-buy" , "not_interested"]
                    print(result);
                    return;
        else:
            if rating <2:
                if price <= 0.2*MI:
                    sentence = "This is a product of fair price and good quality which is suitable for your saving habit."
                    result = [sentence , "good-buy" , "done"]
                    print(result);
                    return;
                else:
                    sentence = "This is a product of fair price but the quality cannot be guaranteed."
                    result = [sentence , "good-buy" , "done"]
                    print(result);
                    return;
            elif rating >= 2 and rating < 3:
                if price > 0.2*MI and price <= 0.6*MI:
                    sentence = "The item is not fully encouraged to buy. The suggestion is to look for other products or save for later and better use."
                    result = [sentence , "average-buy" , "warning"]
                    print(result);
                    return;
                else:
                    sentence = "This is a good product but you are encouraged to consider if you really need it."
                    result = [sentence , "average-buy" , "warning"]
                    print(result);
                    return;
            else:
                sentence = "You should reconsider about your saving habit. If the item is not essential, there might be a better way you can use the money."
                result = [sentence , "bad-buy" , "not_interested"]
                print(result);
                return;

main()
