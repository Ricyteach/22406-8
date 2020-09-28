import itertools
from pathlib import Path

from app.common import *


PROB_NAME = "prob"
CANDE_FOLDER = Path(__file__).parents[2] / 'cande'
MSH_FILE = CANDE_FOLDER / f"{PROB_NAME}.msh"
CANDE_FILE = CANDE_FOLDER / f"{PROB_NAME}.cid._partial"

N_STRUCTS = 1
check_n_structs = len_checker(N_STRUCTS)

CONNECTIVITY = check_n_structs([
    Connectivity.noncontiguous,
])

KEEP_INDEXES = check_n_structs([
    [*range(1, 83)],
])

# user input
INTERF_STRUCT_NODES = check_n_structs([
    range(0),
])

N_BEAMS = check_n_structs([
    len(KEEP_INDEXES[0])-1,
])

STRUCT_STEPS = check_n_structs([1])
STRUCT_MATS = check_n_structs([1])

N_LL_STEPS = 0

N_SOILS = 3
check_n_soils = len_checker(N_SOILS)

# material boundaries
MAT_BOUNDS = check_n_soils({
    1: [(-548.0, -120.0), (548.0, -120.0), (548.0, 0.0), (-548.0, 0.0)],
    2: [(-548.0, 0.0), (548.0, 0.0), (548.0, 123.0), (-548.0, 123.0)],
    3: [(-187.5, 0.0), (187.0, 0.0), (187.5, 123.0), (-187.5, 123.0)]
})
# TODO: add visual sanity check for MAT_BOUNDS

N_DL_STEPS = 2
# step boundaries: {mat_num_range: {step_num: y_value}}
# anything each element with mat_num in the mat_num_range greater than y_value will be applied current step_num
DL_STEP_BOUNDS = {
    range(1,2): {1: -120.0},
    range(2,4): {2: -120.0},
}

# sanity check_n_steps
assert sorted({v for d in DL_STEP_BOUNDS.values() for v in d.keys()}) == list(range(1, N_DL_STEPS+1))

# sanity check_n_mats
assert sorted({mat for mat in itertools.chain(*DL_STEP_BOUNDS.keys())}) == list(range(1, N_SOILS + 1))
