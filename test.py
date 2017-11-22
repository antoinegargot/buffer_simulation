#Antoine GARGOT - CS 555 - Project
from components.welch import WelchAlgorithm
from components.dataVizualiser import DataVizualiser
import matplotlib.pyplot as plot
#from components.systemSimulation import SystemSimulation

if __name__ == '__main__':
    #simulation_time = 100
    welch = WelchAlgorithm(300, 10, 80)
    measures, welchMeasure = welch.launch(2, 0, 1, 2, 5)
    #simulation = SystemSimulation(2, 7, 1, 2, 5)
    #customers, measures = simulation.main_simulation_loop(80, measure = True)
    #A1 = SystemSimulation(2, 0, 1, 2, 5)
    #customersA1, measuresA1 = A1.main_simulation_loop(simulation_time, measure = True)
    # measures = {}
    # for i in range (400) :
    #     A2 = SystemSimulation(2, 7, 1, 2, 5)
    #     customersA2, measuresA2 = A2.main_simulation_loop(simulation_time, measure = True)
    #     measures.update(measuresA2)   
    #B1 = SystemSimulation(2, 0, 1, 2, 5)
    #customersB1, measuresB1 = B1.main_simulation_loop(simulation_time, measure = True)
    
    #B2 = SystemSimulation(2, 0, 1, 2, 5)
    #customersB2, measuresB2 = B2.main_simulation_loop(simulation_time, measure = True)
    #Graph = DataVizualiser()
    #Graph.plot_length(measuresA1)
    plot.plot(welchMeasure)
    plot.xlabel('Time')
    plot.ylabel('Customers in the system')
    plot.show()
