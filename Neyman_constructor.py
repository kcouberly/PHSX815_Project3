import sys
import numpy as np
import matplotlib.pyplot as plt


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
        print ("Usage: %s [-Ntoss number] [-Nexp number] % sys.argv[0]")
        print ("Outputs file to 'output.txt' ")
        sys.exit(1)
        
    #default settings
    #number of tosses
    n_toss = 100
    #number of experiments
    n_exp = 1000
    if '-Ntoss' in sys.argv:
        p = sys.argv.index('-Ntoss')
        Ns = int(sys.argv[p+1])
        if Ns > 0:
            n_toss = Ns            
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-weight')
        Ne = float(sys.argv[p+1])
        if w > 0:
            n_exp = Ne
    #true values of p for plotting
    p = np.linspace(0.05,0.95,50)
    #filling array of p true, p 'measured'
    true_meas = []
    true = []
    meas = []
    for i in range(len(p)):
        temp = []
        for x in range(n_exp):
            heads = 0
            for y in range(n_toss):
                a = CoinToss(p[i])
                heads += a
            tails = n_toss - heads
            value = heads/(heads+tails)
            true.append(p[i])
            meas.append(value)
            temp.append(value)
        true_meas.append(temp)
    #standard devation of 'measurements' at a value
    values = np.asarray(true_meas[24])
    std_dev = np.std(values)
    mean = np.mean(values)
    print('simulated measurement at true value',p[24])
    print('average measurement:',mean)
    print('standard deviation:',std_dev)
    
    #plotting
    plt.hist2d(true, meas, bins=(50, 50), cmap=plt.cm.BuPu)
    plt.colorbar()
    plt.xlabel('p true')
    plt.ylabel('p meas')
    plt.title(str(n_toss) + ' flips per experiment')
    plt.show()
            
            
        