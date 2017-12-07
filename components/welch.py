from components.systemSimulation import SystemSimulation
import random
import numpy as np

class WelchAlgorithm :
	def __init__(self, simulation_nb, window, time):
		#Window is the window parameter for our welch algorithm
		self.window = window

		#simulation_nb is the number of simulation that we will run in order to calculate our mean for each observation.
		self.simulation_nb = simulation_nb

		#time define the total simulation time for each of them.
		self.time = time

	def launch(self, arrival_rate, nb_customers, service_rate, no_of_servers, capacity):
		total_measure = []
		meanMeasure = []
		welchMeasure = []
		for i in range(self.simulation_nb):
			#Launch a simulation for each index
			simulation = SystemSimulation(arrival_rate, nb_customers, service_rate, no_of_servers, capacity)
			customers, measures = simulation.main_simulation_loop(self.time, measure = True)
			total_measure.append([measures[time].system_length for time in [measure for measure in measures]])
		#Mean of each replication of the system  
		meanMeasure = [float(sum(arr))/len(arr) for arr in zip(*total_measure)]

		#Depending on the index of our observation we will apply the specific measure as seen in class.
		for i in range(0, len(meanMeasure)):
			if (i <= self.window):
				welchMeasure.append(float(sum(meanMeasure[0 : i+(self.window)])) / max(len(meanMeasure[0 : i+(self.window)]), 1))
			elif (i + self.window <= len(meanMeasure)):
				welchMeasure.append(float(sum(meanMeasure[i-self.window : i+self.window])) / max(len(meanMeasure[i-self.window : i+self.window]), 1))
			else :
				welchMeasure.append(float(sum(meanMeasure[i-self.window : len(meanMeasure)])) / max(len(meanMeasure[i-self.window : len(meanMeasure)]), 1))
		return meanMeasure, welchMeasure