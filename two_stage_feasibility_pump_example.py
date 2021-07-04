from hips import load_problem
from hips.heuristics import TwoStageFeasibilityPump

mip = load_problem("bppc8-02")
fp = TwoStageFeasibilityPump(mip)
fp.compute(max_iter=100)

# Print objective value
print(fp.get_objective_value())

# Print solution
print({var: fp.variable_solution(var) for var in mip.get_variables()})