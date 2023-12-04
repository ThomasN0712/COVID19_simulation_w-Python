#COVID19_simulation.py
import networkx as nx
import matplotlib.pyplot as plt
import random
import math

def draw_graph(G, pos, iter, shelter_in_place, vaccine):
    # color node based on states
    node_color = []
    for node in G.nodes():
        if G.nodes[node]['state'] == 'S':
            node_color.append('royalblue')
        elif G.nodes[node]['state'] == 'I':
            node_color.append('firebrick')
        elif G.nodes[node]['state'] == 'R':
            node_color.append('darkorange')
        elif G.nodes[node]['state'] == 'V':
            node_color.append('forestgreen')
    
    # draw the graph:
    plt.figure(figsize=(10,7))
    nx.draw_networkx_edges(G, pos, alpha=0.7)
    nx.draw_networkx_nodes(G, pos, node_color=node_color)
    nx.draw_networkx_labels(G, pos, font_color='white')
    plt.title("COVID19 Simulation using SIR")

    # create legend
    legend_element = [plt.Line2D([0], [0], marker='o', color='w', label='Susceptible', markerfacecolor='royalblue', markersize=11),
                      plt.Line2D([0], [0], marker='o', color='w', label='Infected', markerfacecolor='firebrick', markersize=11),
                      plt.Line2D([0], [0], marker='o', color='w', label='Recovered', markerfacecolor='darkorange', markersize=11),
                      plt.Line2D([0], [0], marker='o', color='w', label='Vaccinated', markerfacecolor='forestgreen', markersize=11),
                      plt.Line2D([0], [0], marker='o', color='w', label='Iteration: ' + str(iter), markerfacecolor='white', markersize=11),
                      plt.Line2D([0], [0], marker='o', color='w', label='Shelter in place measures: ' + str(shelter_in_place), markerfacecolor='white', markersize=11),
                      plt.Line2D([0], [0], marker='o', color='w', label='Vaccine effect: ' + str(vaccine), markerfacecolor='white', markersize=11)]
    plt.legend(legend_element, ["Susceptible", "Infected", "Recovered", "Vaccinated", "Iteration: " + str(iter), "Shelter in place measures: " + str(shelter_in_place), "Vaccine effect: " + str(vaccine)], loc = "best")
    plt.show()

def main():
    shelter_in_place = False
    vaccine = False

    while True:
        # menu
        print("-----COVID19 Simulation using SIR-----\n1. Create new graph and set attributes \n2. Enable/disable shelter in place measures\n3. Enable/disable Vaccine effect\n4. Start simulation\n5. Exit")
        user_input = input("Enter your choice: ")

        # create new graph
        if user_input == '1':
            n = int(input("Enter the number of nodes: "))
            edge_p = float(input("Enter the probability for edge creation (0.0 - 1.0): "))
            G = nx.fast_gnp_random_graph(n, edge_p, directed=True)
            # Try to use planer layout if possible, otherwise use spring layout
            try:
                pos = nx.planar_layout(G)
            except:
                pos = nx.spring_layout(G)
            
            # SIR Model
            # S: Susceptible, I: Infected, R: Recovered

            # Initialize all node to Susceptible state
            nx.set_node_attributes(G, 'S', 'state')
            
            # Select a random nodes to be infected
            infected_num = random.randint(1, math.ceil(n/5)) 
            dict = {}
            for i in range (infected_num):
                infected_node = random.randint(0, n-1)
                dict[infected_node] = 'I' 
            nx.set_node_attributes(G, dict, 'state')

            # Ask user for a threshold q:
            p = float(input("Enter the probability of contagion (0.0 - 1.0): "))
            if p > 1.0:
                p = 1.0
            if p < 0.0:
                p = 0.0

            t = int(input("Enter the length of infection: "))
            nx.set_node_attributes(G, t, 'time')

        try:
            # enable/disable shelter in place measures
            if user_input == "2":
                '''
                If enabled, the probability of contagion is halved.
                '''
                # shelter in place
                if shelter_in_place == False:
                    print("\n----Shelter in place measures enabled----\n")
                    shelter_in_place = True
                    p = p/2
                elif shelter_in_place == True:
                    print("\n----Shelter in place measures disabled----\n")
                    shelter_in_place = False
                    p = p*2
            
            # enable/disable vaccine effect
            if user_input == "3":
                '''
                If enabled, random portion of the population will be vaccinated at random during the simulation.
                '''
                # vaccine
                if vaccine == False:
                    print("\n----Vaccine effect enabled----\n")
                    vaccine = True
                elif vaccine == True:
                    print("\n----Vaccine effect disabled----\n")
                    vaccine = False
            
            # start simulation
            if user_input == "4":
                flag = True
                iter = 0
                # main loop
                while flag == True:
                    iter += 1
                    flag = False

                    # if vaccine is enabled, randomly select up to 1/5 of the population to be vaccinated
                    if vaccine == True:
                        vaccinated_num = random.randint(1, math.ceil(n/5))
                        vaccinated = {}
                        for i in range (vaccinated_num):
                            vaccinated_node = random.randint(0, n-1)
                            vaccinated[vaccinated_node] = 'V'
                        nx.set_node_attributes(G, vaccinated, 'state')

                    for node in G.nodes():
                        # if node is infected, check if it is time to recover, if not, reduce counter attribute by one day
                        if G.nodes[node]['state'] == 'I':
                            if G.nodes[node]['time'] <= 0:
                                G.nodes[node]['state'] = 'R'
                            else:
                                G.nodes[node]['time'] -= 1
                            #check if surrounding nodes are susceptible, if yes, infect roll the dice and infect them
                            for neighbor in G.neighbors(node):
                                if G.nodes[neighbor]['state'] == 'S':
                                    if random.random() < p:
                                        G.nodes[neighbor]['state'] = 'I'
                            flag = True
                    draw_graph(G, pos, iter, shelter_in_place, vaccine)
        except:
            print("Please create a graph first.")
            
        # exit
        if user_input == "5":
            break

if __name__ == '__main__':
    main()
