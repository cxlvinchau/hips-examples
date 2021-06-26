import hips
from hips import *
from hips.heuristics._feasibility_pump import FeasibilityPump

def build_model(solver=None):
    if solver is None or solver == "gurobi":
        mip_model = hips.load_problem_gurobi("10teams")
        return mip_model
    elif solver == "clp":
        mip_model = hips.load_problem_clp("10teams")
        return mip_model

# Test with Gurobi
mip_model = build_model("gurobi")
mip_model.set_mip_sense(ProblemSense.MIN)
heur = FeasibilityPump(mip_model, t=15)
heur.compute(max_iter=1000)
print("Status: {}".format(heur.get_status()))
print("Found solution: {}".format(heur.get_objective_value()))
heur.tracker.plot("feasibility objective")


# Test with CLP
mip_model = build_model("clp")
mip_model.set_mip_sense(ProblemSense.MIN)
heur = FeasibilityPump(mip_model, t=15)
heur.compute(max_iter=1000)
print("Status: {}".format(heur.get_status()))
print("Found solution: {}".format(heur.get_objective_value()))
heur.tracker.plot("feasibility objective")