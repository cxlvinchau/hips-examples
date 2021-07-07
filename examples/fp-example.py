from hips import GurobiSolver
from hips.loader import load_mps
from hips.heuristics import LineSearchDiving, FeasibilityPump
from hips.models import MIPModel

mip_model = MIPModel(GurobiSolver())
load_mps(mip_model, "mps_files/pure-binary/22433.mps")
mip_model.summary()

diver = FeasibilityPump(mip_model)
# Deactivate trivial rounding
diver._round_trivially = lambda : False
diver.compute()

print(f"Status: {diver.get_status()}")
print(f"Found solution: {diver.get_objective_value()}")
print(f"With Variable values: { {var: diver.variable_solution(var) for var in mip_model.get_variables()} }")