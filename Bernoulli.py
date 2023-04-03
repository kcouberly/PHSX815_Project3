import sys
import numpy as np

sys.path.append(".")

def CoinToss(weight):
    R = np.random.rand()
    if R < weight:
        a = 1
    else:
        a = 0
    return(a)

# main function
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-Ntoss number] [-weight number] % sys.argv[0]")
        print ("Outputs file to 'output.txt' ")
        sys.exit(1)
        
    #default settings
    #number of tosses
    n_toss = 100
    #bernoulli parameter
    weight = 0.6
    if '-Ntoss' in sys.argv:
        p = sys.argv.index('-Ntoss')
        Ns = int(sys.argv[p+1])
        if Ns > 0:
            n_toss = Ns            
    if '-weight' in sys.argv:
        p = sys.argv.index('-weight')
        w = float(sys.argv[p+1])
        if w > 0:
            weight = w
               
    output = open('output.txt','w')
    for i in range(0,n_toss):
        a = CoinToss(weight)
        #print(a)
        output.write(str(a)+"\n")
    output.close()
               
               