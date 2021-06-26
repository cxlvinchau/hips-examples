from hips import load_problem
from hips.heuristics import RENS

# Load a problem
mip = load_problem("gen-ip054")
# Instantiate heuristic with MIP
rens = RENS(mip)
# Start the computation
rens.compute(max_iter=100)
# Print the objective value
print(rens.get_objective_value())
# Print the solution
print({var: rens.variable_solution(var) for var in mip.get_variables()})
