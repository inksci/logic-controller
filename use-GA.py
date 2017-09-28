from pyevolve import G1DList

from pyevolve import GSimpleGA

from pyevolve import DBAdapters


# This function is the evaluation function, we want

# to give high score to more zero'ed chromosomes
ink = 0
def eval_func(chromosome):

    global ink

    score = 0.0

#     print "@#$%^", ink

    ink += 1
    

    # iterate over the chromosome elements (items)

    A = []

    for value in chromosome:

        A.append(value)

        if value==0:

            score += 1.0

#     print "A: ", A

    return score+1000000

# Genome instance

genome = G1DList.G1DList(5)


genome.setParams(rangemin=0, rangemax=31)


# The evaluator function (objective function)

genome.evaluator.set(eval_func)


ga = GSimpleGA.GSimpleGA(genome)

ga.setDBAdapter( DBAdapters.DBSQLite( identify="ex1" ) )

ga.setGenerations(9)

ga.setPopulationSize(50)

# Do the evolution, with stats dump

# frequency of 10 generations

ga.evolve(freq_stats=10)


# Best individual
print ga.bestIndividual()
