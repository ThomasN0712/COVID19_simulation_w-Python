# Cascade.py 
import networkx as nx
import matplotlib.pyplot as plt
import random
import math

def draw_graph(G, pos):
    # color node based on states
    node_color = []
    for node in G.nodes():
        if G.nodes[node]['state'] == 'S':
            node_color.append('royalblue')
        elif G.nodes[node]['state'] == 'I':
            node_color.append('firebrick')
        else:
            node_color.append('green')
    
    # draw the graph:
    nx.draw_networkx_edges(G, pos, alpha=0.7)
    nx.draw_networkx_nodes(G, pos, node_color=node_color)
    nx.draw_networkx_labels(G, pos, font_color='white')
    plt.title('Cascade in Random Graph')
    plt.show()

def plot_line_chart(x, y):
    plt.plot(x, y, color='green')
    plt.ylabel('Number of infected nodes')
    plt.xlabel('Time')
    plt.show()

def main():
    n = int(input("Enter the number of nodes: "))
    edge_p = float(input("Enter the probability for edge creation (0.0 - 1.0): "))
    G = nx.fast_gnp_random_graph(n, edge_p)
    pos = nx.spring_layout(G)

    # Initialize all node to Susceptible state
    nx.set_node_attributes(G, 'S', 'state')
    
    # Select a random nodes to be infected
    infected_num = random.randint(math.ceil(n/5), math.ceil(n/3)) 
    dict = {}
    for i in range (infected_num):
        infected_node = random.randint(0, n-1)
        dict[infected_node] = 'I' 
    nx.set_node_attributes(G, dict, 'state')

    # Ask user for a threshold q:
    p = float(input("Enter the threshold q (0.0 - 1.0): "))
    if p > 1.0:
        p = 1.0
    if p < 0.0:
        p = 0.0
    draw_graph(G, pos)

    # main loop
    flag = True
    x = []
    counter = 0 
    
    while flag == True:
        flag = False
        for node in G.nodes():
            if G.nodes[node]['state'] == 'S':
                # count the number of infected neighbors
                infected_neighbors_counter = 0
                for neighbor in G.neighbors(node):
                    if G.nodes[neighbor]['state'] == 'S':
                        infected_neighbors_counter += 1
                
                # Try catch for divide by zero
                try:
                    q = infected_neighbors_counter/len(list(G.neighbors(node)))
                except:
                    continue
                # infect if threshold is lower than infected neighbors ratio
                if p >= q:
                    G.nodes[node]['state'] = 'I'
                    flag = True
                x.append(len([node for node in G.nodes() if G.nodes[node]['state'] == 'I']))
                counter += 1
    
    draw_graph(G, pos)
    
    # plot the number of infected nodes over time
    y = list(range(0, counter)) 
    plot_line_chart(x, y)

if __name__ == '__main__':
    main()
