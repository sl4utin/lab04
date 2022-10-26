import random as rnd

def fill_list(min,max,amount,list):
    for i in range(amount):
        list.append(rnd.randint(min,max))

def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1
