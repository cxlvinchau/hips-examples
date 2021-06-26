import os
import time
import numpy as np

import hips
from hips.constants import ProblemSense
from hips.loader import load_mps
from hips.models import MIPModel
from hips.solver import GurobiSolver
from hips.heuristics import FeasibilityPump


print("Start experiment")

feasible = []
times = []
test_number = 5
for i in range(test_number):
    mip_model = hips.load_problem_gurobi("10teams")

    mip_model.set_mip_sense(ProblemSense.MIN)
    start = time.time()

    fs = FeasibilityPump(mip_model, t=20)
    fs.compute(1000)

    end = time.time()

    sol = {var: fs.variable_solution(var) for var in mip_model.lp_model.vars}
    feasible.append(mip_model.is_feasible(sol))

    times.append(end-start)
    print("Model {} solved.".format(i))

print("#--------------------#")
print("Feasible solutions found in {} tests: {}".format(test_number, sum(feasible)))

print(times)
print("Average time consumed: {}s".format(sum(times)/len(times)))

feasible = np.array(feasible)
times = np.array(times)
feasible_times = times[feasible]
print("Average time consumed for feasible solutions: {}s".format(sum(feasible_times)/len(feasible_times)))