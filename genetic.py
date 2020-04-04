import random
from random import randint
from statistics import variance as var, mean


random.seed(40)
def generate_population(number, size): # generates encoded form of each chromosome for whole population
    pop = [[randint(1, 3) for i in range(size)] for j in range(number)]
    return pop

def perform_crossover(par_A, par_B): #perform single point crossover at random point

    crossover_pt = randint(1, len(par_A) - 1)
    child_A = par_A[:crossover_pt] + par_B[crossover_pt:]
    child_B = par_B[:crossover_pt] + par_A[crossover_pt:]
    return child_A, child_B


def mutate(chromosome):
    mut_ind = randint(0, len(chromosome) - 1)
    chromosome[mut_ind] = randint(1, 3)
    return chromosome

def get_weights(size, start=50, end=100): #generates random weights of students
    weights = [randint(start, end) for i in range(size)]
    return weights


def get_fitness_val(encoded_chromo, weights): 
    #returns fitness value
    #mean of the variance is considered as fitness function

    gp_1, gp_2, gp_3 = [],[],[]
    for i in range(len(encoded_chromo)):
        if encoded_chromo[i] == 1:
            gp_1.append(weights[i])
        elif encoded_chromo[i] == 2:
            gp_2.append(weights[i])
        else:
            gp_3.append(weights[i])

    var1 = var(gp_1) if len(gp_1) > 1 else 0
    var2 = var(gp_2) if len(gp_2) > 1 else 0
    var3 = var(gp_3) if len(gp_3) > 1 else 0
    fitness = 1 / mean([var1, var2, var3])

    return fitness


def genetic(chromosomes, weights):

    best_chr = chromosomes[0]
    initial_fitness = get_fitness_val(best_chr, weights)
    final_fitness = initial_fitness

    for i in range(len(chromosomes)):
        for j in range(i + 1, len(chromosomes)):
            chr_A, chr_B = perform_crossover(chromosomes[i], chromosomes[j])
            prob = randint(0, 1)
            if prob:
                chr_A = mutate(chr_A)
                chr_B = mutate(chr_B)
            if get_fitness_val(chr_A, weights) > final_fitness:
                final_fitness = get_fitness_val(chr_A, weights)
                best_chr = chr_A
            if get_fitness_val(chr_B, weights) > final_fitness:
                final_fitness = get_fitness_val(chr_B, weights)
                best_chr = chr_B

    return best_chr, final_fitness, initial_fitness


size, pop_size = 20, 100 
#size = number of genes in each chromosome (total number of students in class)
#pop_size = number of chromosomes in a population
weights = get_weights(size)
chromosomes = generate_population(pop_size, size)

best_chr, final_fitness, initial_fitness = genetic(chromosomes, weights)

print("weights = " + str(weights))

print("initial fitness = " + str(initial_fitness))
print("final fitness = " + str(final_fitness))

print("initial chromosome = " + str(chromosomes[0]))
print("best chromosome = " + str(best_chr))