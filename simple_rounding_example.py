from hips import *
from hips.heuristics._simple_rounding import SimpleRounding
from hips.models import *
from hips.solver import GurobiSolver

def build_model(mip_model):
    x = mip_model.add_variable("x", VarTypes.INTEGER, lb=0, ub=float("inf"), dim=2)
    constr1 = HIPSArray([1,2/3])*x <= 2
    constr2 = HIPSArray([1,1.5])*x <= 3
    mip_model.add_constraint(constr1)
    mip_model.add_constraint(constr2)
    obj_func = HIPSArray([1,1])*x
    mip_model.set_objective(obj_func)
    mip_model.lp_model.set_lp_sense(ProblemSense.MAX)

# Test with Gurobi
mip_model = MIPModel(GurobiSolver())
build_model(mip_model)
heur = SimpleRounding(mip_model)
heur.compute()
print("Status: {}".format(heur.get_status()))
print("Found solution: {}".format(heur.get_objective_value()))
print("With Variable values: {}".format({var: heur.variable_solution(var) for var in mip_model.get_variables()}))


# Test with Clp
mip_model = MIPModel(ClpSolver())
build_model(mip_model)
heur = SimpleRounding(mip_model)
heur.compute()
print("Status: {}".format(heur.get_status()))
print("Found solution: {}".format(heur.get_objective_value()))
print("With Variable values: {}".format({var: heur.variable_solution(var) for var in mip_model.get_variables()}))
