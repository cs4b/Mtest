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

# Detect OS
OS_TYPE="$(uname -s)"
echo "Detected OS: $OS_TYPE"
echo ""

# Offer environment choice
echo "Step 1: Select environment type"
echo "  1) GPU (CUDA 11.8+) - Faster, requires NVIDIA GPU"
echo "  2) CPU-only - Works on Windows/Mac/Linux (slower)"
echo ""
read -p "Enter choice (1 or 2, default 2): " ENV_CHOICE
ENV_CHOICE=${ENV_CHOICE:-2}

case $ENV_CHOICE in
    1)
        ENV_FILE="environment.yml"
        ENV_TYPE="GPU"
        if [ "$OS_TYPE" == "MINGW64_NT"* ] || [ "$OS_TYPE" == "MSYS_NT"* ]; then
            echo ""
            echo "⚠️  WARNING: You selected GPU environment on Windows"
            echo "   CUDA support on Windows may be limited"
            echo "   Consider using CPU-only environment instead"
            echo ""
        fi
        ;;
    2)
        ENV_FILE="environment-cpu.yml"
        ENV_TYPE="CPU-only"
        ;;
    *)
        echo "Invalid choice. Using CPU-only"
        ENV_FILE="environment-cpu.yml"
        ENV_TYPE="CPU-only"
        ;;
esac

echo "Using $ENV_TYPE environment: $ENV_FILE"
echo ""

echo "Step 2: Creating Conda environment..."
# Create or update conda environment
if conda env list | grep -q "^$CONDA_ENV_NAME "; then
    echo "  → Environment '$CONDA_ENV_NAME' already exists, updating..."
    conda env update -n "$CONDA_ENV_NAME" -f "$ENV_FILE" --prune
else
    echo "  → Creating new environment '$CONDA_ENV_NAME'..."
    conda env create -n "$CONDA_ENV_NAME" -f "$ENV_FILE"
fi

# Activate the environment
echo ""
echo "Step 3: Activating environment and installing packages..."
source activate "$CONDA_ENV_NAME"

# Install local packages in editable mode
echo "  → Installing DrugEx package..."
#pip install -e ./DrugEx
SETUPTOOLS_SCM_PRETEND_VERSION_FOR_DRUGEX=3.4.5 python -m pip install -e ./DrugEx #troubleshoot

echo "  → Installing divopt (diverse-hits) package..."
pip install -e ./diverse-hits

echo ""
echo "Step 4: Creating necessary directories..."
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
