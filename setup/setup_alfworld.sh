#!/usr/bin/env bash
set -e  # Stop the script if any command fails

# ---------- Create and Setup Environment ----------
echo "=== Creating alfworld conda environment ==="
conda create -n alfworld python=3.10 -y

# ---------- Install ALFWorld Dependencies ----------
echo "=== Installing ALFWorld dependencies ==="
conda run -n alfworld pip install gymnasium==0.29.1 stable-baselines3==2.6.0
conda run -n alfworld pip install alfworld pandas pyarrow omegaconf

# ---------- Download ALFWorld Source ----------
echo "=== Downloading ALFWorld source ==="
conda run -n alfworld python agl_envs/alfworld/download_alfworld_source.py

echo "✅ alfworld environment has been successfully set up!"
