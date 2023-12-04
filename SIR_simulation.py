import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def draw_graph(G, pos):
    # color node based on states
    node_color = []
    for node in G.nodes():
        if G.nodes[node]['state'] == 'S':
            node_color.append('blue')
        elif G.nodes[node]['state'] == 'I':
            node_color.append('red')
        else:
            node_color.append('green')
    

    # draw the graph:
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_nodes(G, pos, node_color=node_color)
    plt.show()


def main():
    
    # n = int(input("Enter the number of nodes: "))
    n = 8
    # p = float(input("Enter the probability for edge creation (0.0 - 1.0): "))
    p = 0.3
    G = nx.fast_gnp_random_graph(n, p, directed=True)
    pos = nx.spring_layout(G)
    print("\n----Create Random Graph successfully.----\n")

    # SIR Model
    # S: Susceptible, I: Infected, R: Recovered

    # Initialize all node to Susceptible state
    nx.set_node_attributes(G, 'S', 'state')
    
    # Select a random nodes to be infected
    infected_num = random.randint(1, 2) 
    dict = {}
    for i in range (infected_num):
        infected_node = random.randint(0, n-1)
        dict[infected_node] = 'I' 
    nx.set_node_attributes(G, dict, 'state')

    # Ask user for a threshold q:
    q = float(input("Enter the threshold q (0.0 - 1.0): "))

    # main loop
    flag = True
    while flag == True:
        flag = False
        for node in G.nodes():
            if G.nodes[node]['state'] == 'S':
                # count the number of infected neighbors
                infected_neighbors_counter = 0
                for neighbor in G.neighbors(node):
                    if G.nodes[neighbor]['state'] == 'S':
                        infected_neighbors_counter += 1

                q = infected_neighbors_counter/len(list(G.neighbors(node)))

                if q > p:
                    G.nodes[node]['state'] = 'I'
                    flag = True
            draw_graph(G, pos)
                 
    print(G.nodes.data('state'))

    
    

if __name__ == '__main__':
    main()
