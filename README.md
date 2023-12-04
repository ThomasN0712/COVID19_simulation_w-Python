# Network-Dynamic-Population-Model

### Part 1:
This Python code implements a basic simulation of the cascade effect on a random network using the NetworkX library. My approach is simple and can be divided into 4 main steps:

- The first step is Graph Generation: I asked the user to provide the number of nodes (n), probability of edge creation (edge_p). The graph is generated using the built in fast_gnp_random_graph()function. 

- Initially, all nodes are set to the 'S' (Susceptible) state. Then max of (n/5) random nodes will get infected. After the infected nodes are created. The graph will be drawn, the node colored blue for susceptible and red for infected.

- The user is prompted to input a threshold value p (0.0 - 1.0) for the simulation. This threshold represents the likelihood of an uninfected node becoming infected based on the ratio of infected neighbors. In each iteration, susceptible nodes become infected if the ratio of infected neighbors exceeds the specified threshold. The simulation proceeds in a loop until no further infections occur (Using a flag variable to detect whether or not anything changes during an iteration). 

- After the simulation completes, the final state of the graph is visualized.


### Part 2:
This program aims to explore the dynamics of COVID-19 spread through a simulation utilizing the SIR (Susceptible, Infected, Recovered) model. The simulation is conducted on a directed graph representing a population, where nodes represent individuals and edges denote potential transmission pathways.

*Approach:*
- *Graph Initialization:* A new graph is created with user-specified attributes, and the SIR model is applied. The initial infection is introduced randomly, mimicking the unpredictable nature of disease spread.
- *Parameter Control:* Users have the flexibility to modify parameters during the simulation, including enabling/disabling shelter-in-place measures and vaccine effects. These user-controlled variables add a dynamic element to the simulation, allowing for a more nuanced exploration of different scenarios.
- *Simulation Loop:* The simulation progresses through iterations, with the state of nodes evolving based on infection and recovery dynamics. The visual representation of the graph at each iteration provides a clear snapshot of the simulated epidemic.

*Analysis and Insights:*
Impact of Shelter-in-Place Measures:
Enabling shelter-in-place measures will halves the probability of contagion, which resulted in less infection rate, this resulted in less infected nodes due to nodes having more time to recover.

*Vaccine Effects:*
The simulation allows for the introduction of a vaccine, randomly affecting a portion of the population. The results illustrate the impact of vaccination on the overall progression of the epidemic, emphasizing the importance of widespread vaccine coverage.

*Conclusion:*
The simulation-based analysis provides valuable insights into the dynamics of COVID-19 spread under different conditions. The interactive nature of the script allows users to explore the impact of key variables, allowing a deeper understanding of epidemic control strategies.

