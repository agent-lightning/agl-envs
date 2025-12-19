# Simulation Environments for Agent Lightning

## 1. Overview

This directory contains simulation environments and training datasets for reinforcement learning (RL) experiments.

### Supported Environments

- **ALFWorld**  
  An embodied instruction-following environment built on top of ALFRED, focusing on language-guided household tasks.  
  https://github.com/alfworld/alfworld

- **ScienceWorld**  
  A text-based scientific reasoning environment designed for training and evaluating agents on procedural and commonsense science tasks.  
  https://github.com/allenai/ScienceWorld

---

&nbsp;

## 2. Setup

Set up the required environments and dependencies for each environment using the provided scripts.

### ALFWorld

```bash
# The setup script performs the following:
# - Creates a new conda environment named 'alfworld'
# - Installs all required ALFWorld dependencies

bash setup/setup_alfworld.sh
```

### ScienceWorld

```bash
# The setup script performs the following:
# - Creates a new conda environment named 'sciworld'
# - Installs all required ScienceWorld dependencies

bash setup/setup_sciworld.sh
```
---

&nbsp;

## 3. Preparing the Dataset

You can either use the **provided datasets** or create **custom datasets** by modifying the dataset generation scripts.  
All datasets are located under the `task_data/` directory.


### ALFWorld

#### Using the Provided Dataset
- Training set: `task_data/alfworld/train.parquet`
- Test set: `task_data/alfworld/test.parquet`

#### Creating a Custom Dataset
- Modify the following script: `task_data/alfworld/make_alfworld_dataset.py`

---


### ScienceWorld

We provide two types of datasets for ScienceWorld: **single-task** and **multi-task**.

#### 1. Single-Task Dataset

Each task has its own dataset. To identify which task corresponds to a given task_num, please refer to `task_data/scienceworld/split_Sets/id2taskname.json.`

#### Using the Provided Dataset
- Training set: `task_data/scienceworld/single_data/{task_num}/train.parquet`
- Test set: `task_data/scienceworld/single_data/{task_num}/test.parquet`

#### Creating a Custom Dataset
- Modify the following script: `task_data/scienceworld/make_single_sciworld_dataset.py`

&nbsp;

#### 2. Multi-Task Dataset

This dataset combines multiple ScienceWorld tasks into a single dataset.

#### Using the Provided Dataset
- Training set: `task_data/scienceworld/multi_data/train.parquet`
- Test set: `task_data/scienceworld/multi_data/test.parquet`

#### Creating a Custom Dataset
- Modify the following script: `task_data/scienceworld/make_multi_sciworld_dataset.py`