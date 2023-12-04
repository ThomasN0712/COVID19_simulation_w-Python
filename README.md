# Network-Dynamic-Population-Model

*Part 1:*
This Python code implements a basic simulation of the Susceptible-Infected-Recovered (SIR) epidemic model on a random network using the NetworkX library. 
My approach is simple and can be divided into 4 main steps:
The first step is Graph Generation: I asked the user to provide the number of nodes (n), probability of edge creation (edge_p). The graph is generated using the built in fast_gnp_random_graph()function. 
Initially, all nodes are set to the 'S' (Susceptible) state. Then max of (n/5) random nodes will get infected. After the infected nodes are created. The graph will be drawn, the node colored blue for susceptible and red for infected.
The user is prompted to input a threshold value p (0.0 - 1.0) for the simulation. This threshold represents the likelihood of an uninfected node becoming infected based on the ratio of infected neighbors. In each iteration, susceptible nodes become infected if the ratio of infected neighbors exceeds the specified threshold. The simulation proceeds in a loop until no further infections occur (Using a flag variable to detect whether or not anything changes during an iteration). 
After the simulation completes, the final state of the graph is visualized.


*Part 2:*
