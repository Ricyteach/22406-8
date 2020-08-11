import itertools
from pathlib import Path

from app.common import *


PROB_NAME = "prob2"
CANDE_FOLDER = Path(__file__).parents[2] / 'cande'
MSH_FILE = CANDE_FOLDER / f"{PROB_NAME}.msh"
CANDE_FILE = CANDE_FOLDER / f"{PROB_NAME}.cid._partial"

N_STRUCTS = 3
check_n_structs = len_checker(N_STRUCTS)

CONNECTIVITY = check_n_structs([
    Connectivity.contiguous,
    Connectivity.contiguous,
    Connectivity.contiguous,
])

KEEP_INDEXES = check_n_structs([
    [*range(1, 39), *range(0)],
    [*range(39, 77), *range(0)],
    [*range(77, 115), *range(0)],
])

# user input
INTERF_STRUCT_NODES = check_n_structs([
    range(0),
    range(0),
    range(0),
])

N_BEAMS = check_n_structs([
    len(KEEP_INDEXES[0]),
    len(KEEP_INDEXES[1]),
    len(KEEP_INDEXES[2]),
])

STRUCT_STEPS = check_n_structs([1, 1, 1])
STRUCT_MATS = check_n_structs([1, 2, 3])

N_LL_STEPS = 0

N_SOILS = 3
check_n_soils = len_checker(N_SOILS)

# material boundaries
MAT_BOUNDS = check_n_soils({
    1: [(-362.0, -69.0), (362.0, -69.0), (362.0, 62.0), (-362.0, 62.0)],
    2: [(-362.0, -4.7), (362.0, -4.7), (362.0, 62.0), (-362.0, 62.0)],
    3: [(-158.0, -4.7), (158.0, -4.7), (158.0, 62.0), (-158.0, 62.0)]
})
# TODO: add visual sanity check for MAT_BOUNDS

N_DL_STEPS = 2
# step boundaries: {mat_num_range: {step_num: y_value}}
# anything each element with mat_num in the mat_num_range greater than y_value will be applied current step_num
DL_STEP_BOUNDS = {
    range(1,2): {1: -69.0},
    range(1,4): {2: -4.7}
}
# sanity check_n_structs
assert sorted({v for d in DL_STEP_BOUNDS.values() for v in d.keys()}) == list(range(1, N_DL_STEPS+1))
assert sorted({mat for mat in itertools.chain(*DL_STEP_BOUNDS.keys())}) == list(range(1, N_SOILS + 1))
