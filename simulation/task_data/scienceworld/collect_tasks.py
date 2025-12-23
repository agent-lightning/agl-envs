import json
import os

from scienceworld import ScienceWorldEnv

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
    "use-thermometer"
]

SIMPLIFICATION = "easy"
ENV_STEP_LIMIT = 100
JAR_PATH = None

OUTPUT_PATH = "scienceworld_tasks.json"


def collect_tasks():
    env = ScienceWorldEnv(
        "",
        serverPath=JAR_PATH,
        envStepLimit=ENV_STEP_LIMIT,
    )

    results = []

    for task_idx, task_name in enumerate(TOTAL_TASK_LIST):
        print(f"\n=== Task {task_idx}: {task_name} ===")

        try:
            env.load(task_name, 0, SIMPLIFICATION)
            train_vars = env.get_variations_train()
        except Exception as e:
            print(f"⚠️ Failed to load {task_name}: {e}")
            continue

        task_entry = {
            "task": task_name,
            "train_variations": [],
        }

        for var in train_vars:
            try:
                env.load(task_name, var, SIMPLIFICATION)
                _, info = env.reset()
                task_entry["train_variations"].append({
                    "variation": var,
                    "description": info["taskDesc"],
                })
            except Exception as e:
                print(f"  ⚠️ Var {var} failed: {e}")

        results.append(task_entry)

    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    collect_tasks()