#!/usr/bin/env bash
set -e  # Stop the script if any command fails

# ---------- Create and Setup Environment ----------
echo "=== Creating sciworld conda environment ==="
conda create -n sciworld python=3.10 -y

# ---------- Install ScienceWorld Dependencies ----------
echo "=== Installing ScienceWorld dependencies ==="
sudo apt-get update
sudo apt install -y openjdk-18-jdk

conda run -n sciworld pip install scienceworld omegaconf numpy gym gymnasium sentence_transformers

echo "✅ sciworld environment has been successfully set up!"
