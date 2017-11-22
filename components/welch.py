from components.systemSimulation import SystemSimulation
import random
import numpy as np

class WelchAlgorithm :
	def __init__(self, simulation_nb, window, time):
		self.window = window
		self.simulation_nb = simulation_nb
		self.time = time

	def launch(self, arrival_rate, nb_customers, service_rate, no_of_servers, capacity):
		total_measure = []
		meanMeasure = []
		for i in range(self.simulation_nb):
			simulation = SystemSimulation(arrival_rate, nb_customers, service_rate, no_of_servers, capacity)
			customers, measures = simulation.main_simulation_loop(self.time, measure = True)
			total_measure.append([measures[time].system_length for time in [measure for measure in measures]])
		#Mean of each replication of the system  
		meanMeasure = [float(sum(arr))/len(arr) for arr in zip(*total_measure)]

		welchMeasure = meanMeasure
		for i in range(0, len(meanMeasure)):
			if (i <= self.window):
				welchMeasure[i] = float(sum(meanMeasure[0 : i+(self.window)])) / max(len(meanMeasure[0 : i+(self.window)]), 1)
			elif (i + self.window <= len(meanMeasure)):
				welchMeasure[i] = float(sum(meanMeasure[i-self.window : i+self.window])) / max(len(meanMeasure[i-self.window : i+self.window]), 1)
			else :
				welchMeasure[i] = float(sum(meanMeasure[i-self.window : len(meanMeasure)])) / max(len(meanMeasure[i-self.window : len(meanMeasure)]), 1)
		return meanMeasure, welchMeasure