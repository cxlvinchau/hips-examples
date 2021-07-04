from hips.solver import ClpSolver
from hips.models import MIPModel
from hips import ProblemSense, VarTypes

# Create solver
solver = ClpSolver()
# Create MIP model
model = MIPModel(solver)
# Create variables with lower bound 0
x_1 = model.add_variable("x_1", lb=0, ub=20, var_type=VarTypes.INTEGER)
x_2 = model.add_variable("x_2", lb=0)
# Set sense
model.set_mip_sense(ProblemSense.MAX)
# Set objective
model.set_objective(2 * x_1 + 4 * x_2)
# Add constraints
model.add_constraint(x_1 + 2 * x_2 <= 20)
model.add_constraint(3 * x_1 - x_2 <= 10)

from hips.solver import BranchAndBound

bb = BranchAndBound(model)
bb.optimize()

# Print solution
bb.get_incumbent()

# Print objective value
bb.get_incumbent_val()