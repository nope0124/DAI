import sys
import pandas as pd
#import time


def init():
    
    for i in range(len(names)):
        name = names["dai"][i]
        if name not in dict:
            dict[name] = []
            dict[name].append(i)
        else:
            dict[name].append(i)

def main():

    name = sys.argv[1].lower()
    
    if name in dict:
            for ind in dict[name]:
                print(names["chinese"][ind] + ": " + names["japanese"][ind])
    else:
        print("Last name was not found")

if __name__ == "__main__":
#    start = time.time()

    if len(sys.argv) <= 1: #例外処理
        print("No arguments")
        exit(0)
    
    dict = {}
    names = pd.read_csv("names.csv")
    init()
    main()
    
#    elapsed_time = time.time() - start
#    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
