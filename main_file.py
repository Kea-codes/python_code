#if __name__ == __main__ : => THIS SCRIPT CAN BE IMPORTED OR RUN STANDALONE
#FUNCTIONS AND CLASSES IN THIS MODULE CAN BE REUSED WITHOUT THE MAIN BLOCK OF CODE EXECUTING
#----------------ADVANTAGES OF THIS------------------
# 1) GOOD PRACTICE
# 2) CODE IS MODULER
# 3) LEAVES NO GLOBAL VARIABLES
# 4) AVOID UNINTENDED EXECUTION

import main_file2 as mf2



def fav_food(food):
    print(f"YOUR FAVORITE FOOD IS: {food}")


def main():
    #your program goes here
    fav_food("PIZZA")
    mf2.fav_drink("COCA COLA")


if __name__ == '__main__' :
    main()