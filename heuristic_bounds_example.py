from hips import *
from hips.heuristics._bounds import HeuristicBounds, BoundDirection
from hips.models import *
from hips.solver import GurobiSolver, ClpSolver


def build_model(mip_model):
    x = mip_model.add_variable("x", VarTypes.INTEGER, lb=0, ub=2, dim=2)
    constr1 = HIPSArray([1,2/3])*x <= 2
    constr2 = HIPSArray([1,3])*x <= 3
    mip_model.add_constraint(constr1)
    mip_model.add_constraint(constr2)
    obj_func = HIPSArray([1,1])*x
    mip_model.set_objective(obj_func)
    mip_model.lp_model.set_lp_sense(ProblemSense.MAX)

# Test with Gurobi
print("#----------Gurobi-----------#")
# Test lower bound (LOWER) -> x = [0,0]
mip_model = MIPModel(GurobiSolver())
build_model(mip_model)
heur = HeuristicBounds(mip_model, BoundDirection.LOWER)
heur.compute()
print("Status: {}".format(heur.get_status()))
print("Found solution: {}".format(heur.get_objective_value()))
print("With Variable values: {}".format({var: heur.variable_solution(var).to_numpy() for var in mip_model.get_variables()}))
print("#---------------------------#")

#Test upper bound (UPPER) -> Infeasible
mip_model = MIPModel(GurobiSolver())
build_model(mip_model)
heur = HeuristicBounds(mip_model, BoundDirection.UPPER)
heur.compute()
print("Status: {}".format(heur.get_status()))
print("#---------------------------#")

#Test closest bound (CLOSEST) -> [2,0]
mip_model = MIPModel(GurobiSolver())
build_model(mip_model)
heur = HeuristicBounds(mip_model, BoundDirection.CLOSEST)
heur.compute()
print("Status: {}".format(heur.get_status()))
print("Found solution: {}".format(heur.get_objective_value()))
print("With Variable values: {}".format({var: heur.variable_solution(var).to_numpy() for var in mip_model.get_variables()}))
print("#---------------------------#")

# Test with CLP
print("#------------CLP------------#")
# Test lower bound (LOWER) -> x = [0,0]
mip_model = MIPModel(ClpSolver())
build_model(mip_model)
heur = HeuristicBounds(mip_model, BoundDirection.LOWER)
heur.compute()
print("Status: {}".format(heur.get_status()))
print("Found solution: {}".format(heur.get_objective_value()))
print("With Variable values: {}".format({var: heur.variable_solution(var).to_numpy() for var in mip_model.get_variables()}))
print("#---------------------------#")

#Test upper bound (UPPER) -> Infeasible
mip_model = MIPModel(ClpSolver())
build_model(mip_model)
heur = HeuristicBounds(mip_model, BoundDirection.UPPER)
heur.compute()
print("Status: {}".format(heur.get_status()))
print("#---------------------------#")

#Test closest bound (CLOSEST) -> [2,0]
mip_model = MIPModel(ClpSolver())
build_model(mip_model)
heur = HeuristicBounds(mip_model, BoundDirection.CLOSEST)
heur.compute()
print("Status: {}".format(heur.get_status()))
print("Found solution: {}".format(heur.get_objective_value()))
print("With Variable values: {}".format({var: heur.variable_solution(var).to_numpy() for var in mip_model.get_variables()}))
print("#---------------------------#")