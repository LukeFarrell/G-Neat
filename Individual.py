'''
Created on Feb 5, 2017

@author: Jake
'''
from Neuron import Neuron
from Gene import Gene
from Connection import Connection
class Individual(object):
	IDGeneDict  = {}
	inputsNodes = []
	outputNodes = []
	neuronSet   = set()
	fitness     = None
	
	def addGene(g): 
		self.IDGeneDict[g.uniqueID] = g

	def mutateAddConnect():
		pass

	def mutateAddNeuron():
		pass

	def calcOut():
		pass

	def breedGene(g1,g2):
		pass

if __name__ == '__main__':
	n0=Neuron(0)
	n1=Neuron(1)
	n2=Neuron(2)
	n3=Neuron(3)
	n4=Neuron(4)

	n0.neuronType="input"
	n1.neuronType="input"
	n2.neuronType="hidden"
	n3.neuronType="hidden"
	n4.neuronType="output"

	c0=Connection(n0,n2,.9,True)
	c1=Connection(n0,n3,.3,True)
	c2=Connection(n1,n2,-.5,True)
	c3=Connection(n1,n3,.7,True)
	c4=Connection(n2,n4,-.1,True)
	c5=Connection(n3,n4,.8,True)

	n0.outCons.append(c0)
	n0.outCons.append(c1)
	n1.outCons.append(c2)
	n1.outCons.append(c3)
	n2.outCons.append(c4)
	n3.outCons.append(c4)

	n2.inCons.append(c0)
	n2.inCons.append(c1)
	n3.inCons.append(c0)
	n3.inCons.append(c1)
	n4.inCons.append(c2)
	n4.inCons.append(c3)

	n0.value=.0007
	n1.value=.0003

	print n4.neuralNet()


