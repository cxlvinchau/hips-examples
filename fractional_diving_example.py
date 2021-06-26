from hips import *
from hips.heuristics._fractional_diving import FractionalDiving
from hips.models import *
from hips.solver import GurobiSolver, ClpSolver

def build_model(mip_model):
    x = mip_model.add_variable("x", VarTypes.INTEGER, lb=0, ub=float("inf"), dim=2)
    constr1 = HIPSArray([-3,2])*x <= 2
    constr2 = HIPSArray([2,2])*x <= 7
    mip_model.add_constraint(constr1)
    mip_model.add_constraint(constr2)
    obj_func = HIPSArray([1,2])*x
    mip_model.set_objective(obj_func)

# Test with Gurobi
mip_model = MIPModel(GurobiSolver())
build_model(mip_model)
heur = FractionalDiving(mip_model)
heur.compute()
print("Status: {}".format(heur.get_status()))
print("Found solution: {}".format(heur.get_objective_value()))
print("With Variable values: {}".format({var: heur.variable_solution(var) for var in mip_model.get_variables()}))
heur.tracker.plot("objective value")


# Test with CLP
mip_model = MIPModel(ClpSolver())
build_model(mip_model)
heur = FractionalDiving(mip_model)
heur.compute()
print("Status: {}".format(heur.get_status()))
print("Found solution: {}".format(heur.get_objective_value()))
print("With Variable values: {}".format({var: heur.variable_solution(var) for var in mip_model.get_variables()}))
heur.tracker.plot("objective value")
