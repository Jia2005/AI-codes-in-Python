#Genetics
import random
def fitness_function(x):
    return x * x

def generate_population(size, lower, upper):
    return [random.randint(lower, upper) for _ in range(size)]

def select_parents(population):
    return random.sample(population, 2)

def crossover(p1, p2):
    return (p1 + p2) // 2

def mutate(child, lower, upper, mutation_rate=0.1):
    if random.random() < mutation_rate:
        change = random.choice([-1, 1])
        child += change
        child = max(min(child, upper), lower)
    return child

def genetic_algorithm():
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))
    population_size = int(input("Enter population size: "))
    generations = int(input("Enter number of generations: "))
    
    population = generate_population(population_size, lower, upper)
    
    for _ in range(generations):
        population = sorted(population, key=fitness_function, reverse=True)
        new_population = population[:2]  
        
        while len(new_population) < population_size:
            p1, p2 = select_parents(population)
            child = crossover(p1, p2)
            child = mutate(child, lower, upper)
            new_population.append(child)
        
        population = new_population
    
    best = max(population, key=fitness_function)
    print(f"Best solution: {best} with fitness {fitness_function(best)}")

if __name__ == "__main__":
    genetic_algorithm()
