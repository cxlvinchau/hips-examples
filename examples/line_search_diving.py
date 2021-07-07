from hips import load_problem
from hips.heuristics import LineSearchDiving

mip_model = load_problem("gr4x6")
mip_model.summary()

diver = LineSearchDiving(mip_model)
# Deactivate trivial rounding
diver._round_trivially = lambda : False
diver.compute()

print(f"Status: {diver.get_status()}")
print(f"Found solution: {diver.get_objective_value()}")
print(f"With Variable values: { {var: diver.variable_solution(var) for var in mip_model.get_variables()} }")