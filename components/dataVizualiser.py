#Antoine GARGOT - CS 555 - Project

import matplotlib.pyplot as plot


class DataVizualiser:
    
    def plot_expected_length_stay(self, snaps):

        times = [snap for snap in snaps]
        times.sort()

        sim_data = [[time for time in times],[snaps[time].average_wait for time in times]]
        theoretical_data = [[time for time in times],[1/(service_rate - arrival_rate) for time in times]]
        
        plot.plot(theoretical_data[0],theoretical_data[1], label = 'Expected Value')
        plot.plot(sim_data[0],sim_data[1], label = 'Simulation Data')
        plot.xlabel('Time')
        plot.legend()
        plot.ylabel('Average Cost per player')
        plot.show()

    def plot_varying_lambda(self, time, max_lmbda, service_rate, servers):
        #Function to plot the length of a queue over time

        sim_data = [[],[]]

        for lmbda in range(1, max_lmbda):
            a = SimulationModel(lmbda, service_rate, servers)
            players, snaps = a.main_simulation_loop(time, snap_shot = False)
            sim_data[0].append(lmbda)
            sim_data[1].append(sum(players[ID].wait for ID in players)/len(players))
            
                
        plot.plot(sim_data[0],sim_data[1])
        plot.xlabel('Demand')
        plot.ylabel('Average Cost per player')
        plot.show()

    def plot_length(self, snaps):
        #Function to plot the average wait per player in the queueing system
        times = [snap for snap in snaps]
        times.sort()

        sim_data = [[time for time in times],[snaps[time].queue_length for time in times]]
        
        plot.plot(sim_data[0],sim_data[1])
        plot.xlabel('Time')
        plot.xlim(0,time)
        plot.ylabel('Length of Queue')
        plot.show()