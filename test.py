#Antoine GARGOT - CS 555 - Project
from components.systemSimulation import SystemSimulation
from components.dataVizualiser import DataVizualiser
import matplotlib.pyplot as plot

if __name__ == '__main__':
    simulation_time = 10
    A1 = SystemSimulation(1, 5, 1, 2, 5)
    customersA1, measuresA1 = A1.main_simulation_loop(simulation_time, measure = True)
    #Graph = DataVizualiser()
    #Graph.plot_length(measuresA1)
    plot.plot([measuresA1[time].queue_length for time in [measure for measure in measuresA1]])
    plot.xlabel('Time')
    plot.ylabel('Length of Queue')
    plot.show()