import os
import random
import pandas as pd
from scienceworld import ScienceWorldEnv


OUTPUT_ROOT = "agl_envs/simulation/task_data/scienceworld/single_data"

NUM_TRAIN_VARS = 5
NUM_TEST_VARS = 20
TRAIN_REPEAT = 64
TEST_REPEAT = 4
SEED = 42

SIMPLIFICATION = "easy"
ENV_STEP_LIMIT = 100
JAR_PATH = None

random.seed(SEED)

TOTAL_TASK_LIST = [
    "boil",
    "change-the-state-of-matter-of",
    "chemistry-mix",
    "chemistry-mix-paint-secondary-color",
    "chemistry-mix-paint-tertiary-color",
    "find-animal",
    "find-living-thing",
    "find-non-living-thing",
    "find-plant",
    "freeze",
    "grow-fruit",
    "grow-plant",
    "identify-life-stages-1",
    "identify-life-stages-2",
    "inclined-plane-determine-angle",
    "inclined-plane-friction-named-surfaces",
    "inclined-plane-friction-unnamed-surfaces",
    "lifespan-longest-lived",
    "lifespan-longest-lived-then-shortest-lived",
    "lifespan-shortest-lived",
    "measure-melting-point-known-substance",
    "measure-melting-point-unknown-substance",
    "melt",
    "mendelian-genetics-known-plant",
    "mendelian-genetics-unknown-plant",
    "power-component",
    "power-component-renewable-vs-nonrenewable-energy",
    "test-conductivity",
    "test-conductivity-of-unknown-substances",
    "use-thermometer",
]

env = ScienceWorldEnv(
    "",
    serverPath=JAR_PATH,
    envStepLimit=ENV_STEP_LIMIT,
)


for task_idx, task_name in enumerate(TOTAL_TASK_LIST):
    print(f"\n=== Task {task_idx}: {task_name} ===")

    try:
        env.load(task_name, 0, SIMPLIFICATION)
        train_variations = env.get_variations_train()
        test_variations = env.get_variations_test()
    except Exception as e:
        print(f"⚠️ Failed to load {task_name}: {e}")
        continue

    if not train_variations or not test_variations:
        print(f"⚠️ No variations for {task_name}")
        continue

    train_vars = train_variations[:NUM_TRAIN_VARS]
    test_vars = test_variations[:NUM_TEST_VARS]

    out_dir = os.path.join(OUTPUT_ROOT, str(task_idx))
    os.makedirs(out_dir, exist_ok=True)

    # Train parquet
    train_df = pd.DataFrame(
        [[task_name, v] for v in train_vars] * TRAIN_REPEAT,
        columns=["sub_task_name", "variation_idx"],
    )
    train_df.to_parquet(
        os.path.join(out_dir, "train.parquet"),
        index=False,
    )

    # Test parquet
    test_df = pd.DataFrame(
        [[task_name, v] for v in test_vars] * TEST_REPEAT,
        columns=["sub_task_name", "variation_idx"],
    )
    test_df.to_parquet(
        os.path.join(out_dir, "test.parquet"),
        index=False,
    )

    print(f"✔ {task_name} done")