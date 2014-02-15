
import igraph
from igraph import Graph

	
def digraph():
	g = Graph()
	g = Graph.Read_Ncol("graph.txt")
	g2 = open('graph.txt').readlines()
	g2.reverse()
	g2 = ' '.join(g2)
	
	hello = open('graph.txt').read().split()
	hello = hello[::-1]
			
	g3 = Graph.Read_Ncol("graph.txt")
	g5 = [0]*80000
	g6 = [0]*80000
	count = 0
	a = 2
	for i in range(0, 77358):
		j = 0
		
		for j in range(0,77358):
			if (g3[i,j] == 1):
				count += 1
				g5[i+j] = 1
			elif (g3[i,j] == 0):
				j = 77777
		                g6[i] = count
	scc_length = max(g6)
	print(scc_length)
		

	
digraph()

