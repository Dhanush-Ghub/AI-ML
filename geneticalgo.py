import random

class Chromosome:
    def _init_(self, cities):
        self.cities = cities

    def fitness(self, distances):
        total_distance = 0
        for i in range(len(self.cities) - 1):
            total_distance += distances[self.cities[i]][self.cities[i + 1]]
        return total_distance

def generate_random_chromosome(num_cities):
    
    cities = list(range(num_cities))
    random.shuffle(cities)
    return Chromosome(cities)

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1.cities) - 2)
    child_cities = parent1.cities[:crossover_point] + parent2.cities[crossover_point:]
    return Chromosome(child_cities)

def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome.cities)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(chromosome.cities) - 1)
            chromosome.cities[i], chromosome.cities[j] = chromosome.cities[j], chromosome.cities[i]

def select_parents(population, selection_pressure):
    parents = random.sample(population, 2)
    return parents

def genetic_algorithm(num_cities, population_size, num_generations, mutation_rate, selection_pressure, distances):
    population = [generate_random_chromosome(num_cities) for _ in range(population_size)]
    best_chromosome = min(population, key=lambda x: x.fitness(distances))

    for generation in range(num_generations):
        new_population = []

        for _ in range(population_size):
            parents = select_parents(population, selection_pressure)
            child = crossover(parents[0], parents[1])
            mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population
        best_chromosome = min(population + [best_chromosome], key=lambda x: x.fitness(distances))

    return best_chromosome

# Example usage:

num_cities = 4
population_size = 10
num_generations = 10
mutation_rate = 0.01
selection_pressure = 2

# Define your distances matrix based on your problem
distances = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

best_chromosome = genetic_algorithm(num_cities, population_size, num_generations, mutation_rate, selection_pressure, distances)

print("Best chromosome:", best_chromosome.cities)
print("Best fitness:", best_chromosome.fitness(distances))