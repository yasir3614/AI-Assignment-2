#BEFORE RUNNING THE CODE DO THE FOLLOWING
#USE PYTHON 3.8.x
# FOR GRAPHS
# run this in your terminal => python -m pip install -U matplotlib



import random
import copy
import matplotlib.pyplot as plt
import time
from math import log
# Population
# Fitness Calculation

# selection
# crossover -> Single Point Crossover = Same array index par.
# mutation


def get_fitness_cost(chromosome,length):
    value = ""
    for gene in chromosome:
        value += str(gene)
    power_value = 2.0**(length)-1
    #print("POWER: " , power_value)
    return int(((int(value, 2))/power_value) * 100)


def apply_crossover(chromosome1, chromosome2,length):
    temp1 = (chromosome1[int(length/2):])
    temp2 = (chromosome2[int(length/2):])
    chromosome1[int(length/2):] = (temp2)
    chromosome2[int(length/2):] = (temp1)
    return chromosome1, chromosome2


def mutate_population(selected_population,length):
    rand_bit_index = random.randint(0, length-1)
    for chromosome in selected_population:
        if (chromosome[rand_bit_index] == 0):
            chromosome[rand_bit_index] = int(not chromosome[rand_bit_index])

    return selected_population


def main():
    
    
    #Change these to check for performance

    print("Please Enter Chromosome Length: ")
    CHROMOSOME_LENGTH = int(input())
    print("Please enter Population Size")
    POPULATION_SIZE = int(input())

    print("Using Single Point Crossover and Mutation in every generation")
    print("Finding Solution ~Please wait while the solution is being found ~")


    #Computes Itself , increments each iteration until all the chromosomes become '1'
    GENERATION_SIZE = 0 
    
    chromosomes = []
 
    #Random Chromosome generation on the basis of population size and length of chromose
    for i in range(0, POPULATION_SIZE):
        chromosomes.append([random.randint(0, 1) for value in range(0, CHROMOSOME_LENGTH)])

    cost_and_population_Pair = []
    for chromosome in chromosomes:
        cost_and_population_Pair.append((get_fitness_cost(chromosome,CHROMOSOME_LENGTH), chromosome))
    cost_and_population_Pair.sort(key=lambda fitness_cost: fitness_cost[0], reverse=True)

  
    #SELECTION 
    selected_population = [chromosome[1]
                           for chromosome in cost_and_population_Pair]
    selected_population = selected_population[:][0:POPULATION_SIZE - 1]
    

    # X AND Y FOR GRAPH 
    X_axis_generation = []
    Y_axis_fitness = []

    #BOOLEAN TO CHECK IF SOLUTION IS FOUND
    solution_found = False


    start_time=time.time()
    #LOOP FOR GENERATIONS

    while solution_found==False:
        
        # APPLYING CROSSOVER ON SELECTION
        for i in range(0,POPULATION_SIZE-2):
            selected_population[i], selected_population[i+1] = apply_crossover(selected_population[i], selected_population[i+1],CHROMOSOME_LENGTH)
        selected_population[0], new_population = apply_crossover(selected_population[0], copy.deepcopy(selected_population[POPULATION_SIZE - 2]),CHROMOSOME_LENGTH)
        

            
        selected_population.append(new_population)
       
        #MUTATING PROCESS
        selected_population = mutate_population(selected_population,CHROMOSOME_LENGTH)
 
        #CHECKING FITNESS OF POPULATION and CHOOSING THE BEST  POPULATION_SIZE - 1 FOR NEXT ITERATION
        fitness_costs = []
        for chromosome in selected_population:
            fitness_costs.append(get_fitness_cost(chromosome,CHROMOSOME_LENGTH))

            #UNCOMMENT THE BELOW LINE TO CHEK FITNESS VALUE FOR EACH ARRAY 

            #print(get_fitness_cost(chromosome,CHROMOSOME_LENGTH),chromosome)
            if get_fitness_cost(chromosome,CHROMOSOME_LENGTH) == int(100):
                print("Solution Found: ", chromosome)
                solution_found = True
                break

        GENERATION_SIZE += 1
        Y_axis_fitness.append(sum(fitness_costs)/len(fitness_costs))
        X_axis_generation.append(GENERATION_SIZE)
      

    print("Chromosome Length " , CHROMOSOME_LENGTH)
    print("Population Size: ", POPULATION_SIZE)    
    print("Total Generations: " , GENERATION_SIZE)
    print("Time Required to find solution: %s seconds " % (time.time() - start_time))
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.plot(X_axis_generation, Y_axis_fitness)
    plt.show()

    
if __name__ == "__main__":
    main()
