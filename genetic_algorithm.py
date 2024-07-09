import math, random
import itertools

def math_func(x):
    return x * math.sin(10 * math.pi * x) + 1 


population = {}

# Generate Population
for _ in range(20):
    number = random.uniform(0,1)
    population[number] = math_func(number)

# Sort & select top 25%
population = dict(sorted(population.items(), key=lambda item: item[1], reverse=True))
selected = round(len(population) * 0.25) + 1

new_population = dict(itertools.islice(population.items(), selected))


for _ in range(50):
    crossover = {}
    max_k = list(new_population.keys())[0]
    max_n = new_population[max_k]
    for key1, key2 in itertools.combinations(new_population.keys(), 2):
        #Crossover between key values
        new_key = (key1 + key2) / 2
        
        #Mutation of highest value nth decimal
        choice = random.choice([0,1,2])
        if choice == 1:
            new_key += 0.005
        elif choice == 2:
            new_key -= 0.005
            
        new_value = math_func(new_key)
        
        crossover[new_key] = new_value
    
    population = dict(sorted(crossover.items(), key=lambda item: item[1], reverse=True))
    selected = round(len(crossover) * 0.25) + 1
    new_population_1 = dict(itertools.islice(population.items(), selected))
    if next(iter(new_population_1.values())) >= max_n:
        new_population = new_population_1
        max_k = list(new_population.keys())[0]
        max_n = new_population[max_k]
        
print(f"El máximo encontrado es: f({max_k}) = {max_n}. \n")
    


