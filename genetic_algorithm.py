import math, random
import itertools

def math_func(x):
    return x * math.sin(10 * x) + 1 


population = {}

# Generate Population
for _ in range(1000):
    number = random.uniform(0,1)
    population[number] = math_func(number)

# Sort & select top 25%
population = dict(sorted(population.items(), key=lambda item: item[1], reverse=True))
selected = round(len(population) * 0.25) + 1

new_population = dict(itertools.islice(population.items(), selected))
position = 0


for _ in range(100):
    crossover = {}
    str_number = str(new_population.items()[0])
    for key1, key2 in itertools.combinations(new_population.keys(), 2):
        #Crossover between key values
        new_key = (key1 + key2) / 2
        new_value = math_func(new_key)
        
        #Mutation of highest value nth decimal
        new_value_str = str(new_value)
        dot_position = new_value_str.find('.')
        pos = dot_position + position
        new_value_str = new_value_str[:pos] + str_number + new_value_str[pos + 1:]
        mutated_value = float(new_value_str)
        
        position += 1
        crossover[new_key] = mutated_value
    
    population = dict(sorted(crossover.items(), key=lambda item: item[1], reverse=True))
    selected = round(len(crossover) * 0.25) + 1
    new_population = dict(itertools.islice(population.items(), selected))
    


