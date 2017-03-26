usertype = 2
price = 900
MI = 10000
rating = 2


def main():
        if usertype == 0 or usertype == 2:
            if (price <= 0.1*MI):
                if (rating <= 2):
                    sentence = "This is a product of fair price and good quality which is suitable for your saving habit."
                    return;
                else:
                    sentence = "This is a product of fair price but the quality cannot be guaranteed."
                    return;
            elif price > 0.1*MI and price < 0.4*MI:
                if rating >= 3:
                    sentence = "The item is not fully encouraged to buy. The suggestion is to look for other products or save for later and better use."
                    return;
                else:
                    sentence = "This is a good product but you are encouraged to consider if you really need it."
                    return;
            else:
                sentence = "You should reconsider about your saving habit. If the item is not essential, there might be a better way you can use the money."
                return;
        elif usertype == 1:
            if (price < 0.3*MI):
                if (rating <= 3):
                    sentence = "This is a product of fair price and good quality which is suitable for your saving habit."
                    return;
                else:
                    sentence = "This is a product of fair price but the quality cannot be guaranteed."
                    return;
            elif price >= 0.3*MI and price <= 0.6*MI:
                if rating >= 3:
                    sentence = "The item is not fully encouraged to buy. The suggestion is to look for other products or save for later and better use."
                    return;
                else:
                    sentence = "This is a good product but you are encouraged to consider if you really need it."
                    return;
            else:
                if rating == 1:
                    sentence = "If this is a good investment for you, think deeply about it."
                    return;
                else:
                    sentence = "The cost and quality is not in good proposition. The suggestion is to look for other products or save for later and better use."
                    return;
        else:
            if price <= 0.2*MI:
                if rating <=3:
                    sentence = "This is a product of fair price and good quality which is suitable for your saving habit."
                    return;
                else:
                    sentence = "This is a product of fair price but the quality cannot be guaranteed."
                    return;
            elif price > 0.2*MI and price <= 0.6*MI:
                if rating >= 3:
                    sentence = "The item is not fully encouraged to buy. The suggestion is to look for other products or save for later and better use."
                    return;
                else:
                    sentence = "This is a good product but you are encouraged to consider if you really need it."
                    return;
            else:
                sentence = "You should reconsider about your saving habit. If the item is not essential, there might be a better way you can use the money."
                return;


main()
