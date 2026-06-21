#!/bin/bash

set -e  # Exit on error

echo "=========================================="
echo "Setting up thesis script environment"
echo "=========================================="
echo ""

# Configuration
CONDA_ENV_NAME="thesis-env"
PYTHON_VERSION="3.11"

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "❌ ERROR: Conda is not installed or not in PATH"
    echo "Please install Miniconda or Anaconda first"
    exit 1
fi

echo "Step 1: Creating Conda environment..."
# Create or update conda environment
if conda env list | grep -q "^$CONDA_ENV_NAME "; then
    echo "  → Environment '$CONDA_ENV_NAME' already exists, updating..."
    conda env update -n "$CONDA_ENV_NAME" -f environment.yml --prune
else
    echo "  → Creating new environment '$CONDA_ENV_NAME'..."
    conda env create -n "$CONDA_ENV_NAME" -f environment.yml
fi

# Activate the environment
echo ""
echo "Step 2: Activating environment and installing packages..."
source activate "$CONDA_ENV_NAME"

# Install local packages in editable mode
echo "  → Installing DrugEx package..."
pip install -e ./DrugEx

echo "  → Installing divopt (diverse-hits) package..."
pip install -e ./diverse-hits

echo ""
echo "Step 3: Creating necessary directories..."
# Create directories that scripts expect to exist
mkdir -p diverse-hits/optimizers/drugex/encoded/graph
mkdir -p diverse-hits/data/scoring_functions/drd2
mkdir -p thesis/results/rnn
mkdir -p thesis/results/graph

echo ""
echo "=========================================="
echo "✓ Setup complete!"
echo "=========================================="
echo ""
echo "To activate the environment, run:"
echo "  conda activate $CONDA_ENV_NAME"
echo ""
echo "To run a script, use:"
echo "  conda activate $CONDA_ENV_NAME"
echo "  python thesis/scripts/YOUR_SCRIPT.py"
echo ""
echo "IMPORTANT NOTES:"
echo "  - Pre-trained models (*.pkg, *.vocab) must be placed in:"
echo "    diverse-hits/optimizers/drugex/"
echo "  - Data files (*.tsv, *.smiles) must be placed in:"
echo "    diverse-hits/data/ and diverse-hits/data/scoring_functions/"
echo "  - See README.md for download instructions"
echo ""
