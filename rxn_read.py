#!/usr/bin/env python

import os, sys, glob, commands
import numpy
import Gnuplot


def plot_result(rxn_sum):
    g = Gnuplot.Gnuplot()
    g.plot(rxn_sum)
    raw_input('Please press return to continue...\n')
   
def write_result(rxn_sum):
    outputFile = open('rxn.dat','w')
    for i in range(len(rxn_sum)):
        outputFile.write(str(rxn_sum[i][0])+' '+str(rxn_sum[i][1])+'\n')
    outputFile.close()

def read_rxn(nwindow=50):
    get_rxn_tmp = commands.getoutput('grep "=>" findmolecules.x??? > rxn.tmp')
    inputFile = open('rxn.tmp','r')

    rxn_sum = numpy.zeros((nwindow,2),dtype=float)
    for i in range(nwindow):  
        rxn_sum[i][0] = i

    for line in inputFile.readlines():

       timestamp = line.split()[0].replace('findmolecules.x','').replace(':','')
       timestamp = int(timestamp)
       rxn_sum[timestamp][1] += int(line.split()[1])

    inputFile.close()
    get_rxn_tmp = commands.getoutput('rm rxn.tmp')
    return rxn_sum

def main():
    """
    This is the main function.
    """
    try:
        prog = sys.argv[0]
        #a = float(sys.argv[1])
        #b = float(sys.argv[2])
    except IndexError:
        # Tell the user what they need to give
        print '\nusage: '+prog+' a b    (where a & b are numbers)\n'
        # Exit the program cleanly
        sys.exit(0)

    nwindow = 100

    rxn_sum = read_rxn(nwindow)
    plot_result(rxn_sum)
    write_result(rxn_sum)
    

# This executes main() only if executed from shell
if __name__ == '__main__':
    main()
