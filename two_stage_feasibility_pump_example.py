import numpy as np
from hips import ProblemSense
from hips.heuristics import TwoStageFeasibilityPump, FeasibilityPump
from hips.loader import load_mps
from hips.models import MIPModel
from hips.solver import GurobiSolver, ClpSolver
import copy

model = MIPModel(ClpSolver())
load_mps(model, "examples/mps_files/10teams.mps")
model.set_mip_sense(ProblemSense.MIN)
model.summary()

import sys
sys.exit(0)

variables = copy.deepcopy(model.variables)

fp = FeasibilityPump(model, t=15, seed=0)

fp.compute(max_iter=1000)

sol = {var: fp.variable_solution(var) for var in model.variables}

print(sol)
print(model.is_feasible(sol))
print([(var, np.min(sol[var].array), np.max(sol[var].array)) for var in sol])

fp.tracker.plot("feasibility objective")