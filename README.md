# Buffer Simulation
##Antoine GARGOT - CS 555 - Project

## *Buffer simulator for Analytic Models and Simulation of Computer Systems*

Simulation of a M/M/2/2+5 system (i.e. 2 servers with the common buffer of capacity 5) by means of discrete event simulation. Investigate the following two cases:
  * System A: arrival rate lambda=2, service rate of each server mu=1
  * System B: lambda=10, mu=1

Test your random number generator (RNG):
  * Does your RNG generate random numbers?
  * How do you initialize the seed of your RNG? 
  * Generate two sequences of 1000000 numbers each, for every sequence use a different seed. 
       Are these two sequences different? How do you know this?    

Eliminate the warm-up period separately for each of the following cases by applying 
   the Welch graphical procedure:
    * System A with the initial condition x(t=0)=0, i.e. the system is empty at t=0.
   	* System A with the initial condition x(t=0)=7, i.e. the system is full at t=0.
   	* System B with the initial condition x(t=0)=0, i.e. the system is empty at t=0.
  	* System B with the initial condition x(t=0)=4, i.e. there are 4 customers in the system at t=0.

Change the seed of your RNG if you run multiple simulations to investigate a nonstationary state.


For the stationary regions of the Systems A and B identified in item (2) find: 
   * Blocking probability.
   * Mean time a customer spends in the system.
   * Mean number of customers in the system.
   
Find the confidence intervals for (3.1), (3.2) and (3.3). Assume the 90% confidence level. 


