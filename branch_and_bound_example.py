from hips import load_problem
from hips.solver import BranchAndBound

# Load a problem
mip = load_problem("flugpl")
# Instantiate branch and bound with mip
bb = BranchAndBound(mip)
# Start the computation
bb.optimize()
# Print the objective value
print(bb.incumbent_val)
# Print the solution
print({var: bb.incumbent[var] for var in mip.get_variables()})
