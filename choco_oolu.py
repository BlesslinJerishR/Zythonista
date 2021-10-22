import math

choco_rs = 1
choco_for_wrappers = 3
rupees = 15

def chocos(choc, wrapper):
    if(choc < wrapper):
        return 0;
    chocolates = choc / wrapper;
    return chocolates + chocos(chocolates + choc % wrapper, wrapper)

def total_chocos(money , price, wrapper):
    choc = money / price;
    return math.floor(choc + chocos(choc, wrapper));

# Drivers
print(f"Total Chocolates that can be bought with rupees "+ str(rupees) +" is "+ str(total_chocos(rupees, choco_rs,choco_for_wrappers)) +".")