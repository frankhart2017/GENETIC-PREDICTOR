import random

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)

def get_fitness(target, guess):
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)

def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)

def display(target, guess):
    fitness = get_fitness(target, guess)
    return (guess, fitness)

def predict(target):
    random.seed()
    bestParent = generate_parent(len(target))
    bestFitness = get_fitness(target, bestParent)
    v = []
    vals = display(target, bestParent)
    v.append(vals)

    while True:
        child = mutate(bestParent)
        childFitness = get_fitness(target, child)

        if bestFitness >= childFitness:
            continue
        vals = display(target, child)
        v.append(vals)
        if childFitness >= len(bestParent):
            break
        bestFitness = childFitness
        bestParent = child

    return v
