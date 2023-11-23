import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def main():
    # n = int(input("Enter the number of nodes: "))
    n = 20
    # p = float(input("Enter the probability for edge creation (0.0 - 1.0): "))
    p = 0.2
    G = nx.fast_gnp_random_graph(n, p, directed=True)
    print("\n----Create Random Graph successfully.----\n")

    # SIR Model
    # S: Susceptible, I: Infected, R: Recovered

    # Initialize all node to Susceptible state
    nx.set_node_attributes(G, 'S', 'state')
    
    # Select a random node to be infected
    infected_num = random.randint(1, 5) 
    dict = {}
    for i in range (infected_num):
        infected_node = random.randint(0, n-1)
        dict[infected_node] = 'I' 
    print(dict)
    nx.set_node_attributes(G, dict, 'state')
    print(G.nodes.data())



if __name__ == '__main__':
    main()
