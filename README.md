# Drug Discovery Optimization Benchmark

A comprehensive benchmarking framework for molecular generation and multi-objective optimization algorithms in drug discovery, with thesis scripts for training and evaluation.

## Overview

This repository contains:
- **DrugEx**: Deep learning-based molecular generation with reinforcement learning
- **divopt**: Scoring function framework with memory-efficient diversity tracking
- **Benchmarks**: GuacaMol standard benchmarks + custom drug discovery tasks
- **Thesis Scripts**: Training and analysis scripts for research reproducibility

## Quick Start

### Prerequisites

- **Conda** (Anaconda or Miniconda) - [Install here](https://docs.conda.io/projects/conda/latest/user-guide/install/index.html)
- **Python 3.11+**
- **GPU** (NVIDIA CUDA 11.8+) - Optional, CPU-only also supported
- **Disk Space**: ~50 GB (for models, data, and results)

### 1. Set Up Environment

From the repository root, run the setup script:

```bash
bash setup_environment.sh
```

The script will:
- Ask if you want GPU (CUDA 11.8+) or CPU-only environment
- Create a Conda environment with all dependencies
- Install local packages (`drugex` and `divopt`)
- Create necessary directories for scripts

**Environment Options:**
- **GPU** (faster): Requires NVIDIA GPU with CUDA 11.8+ (Linux/Mac only)
  - Uses `environment.yml`
- **CPU-only** (default, cross-platform): Works on Windows, Mac, Linux
  - Uses `environment-cpu.yml`

Then activate the environment:
```bash
conda activate thesis-env
```

**Manual setup (if needed):**
```bash
# For GPU (CUDA 11.8+, Linux/Mac):
conda env create -f environment.yml
conda activate thesis-env

# For CPU-only (Windows/Mac/Linux):
conda env create -f environment-cpu.yml
conda activate thesis-env

# Install packages
pip install -e DrugEx/
pip install -e diverse-hits/
```

### 2. Download Required Models & Data

Several scripts require pre-trained models and datasets. These are **not** included in the repository due to size constraints.

**Pre-trained Models Needed:**
- `Papyrus05.5_graph_trans_PT.pkg` - DrugEx graph transformer model
- `Papyrus05.5_graph_trans_PT.vocab` - Vocabulary for graph model
- `Papyrus05.5_smiles_rnn_PT.pkg` - DrugEx SMILES RNN model
- `Papyrus05.5_smiles_rnn_PT.vocab` - Vocabulary for RNN model

**Location:** Place these files in `diverse-hits/optimizers/drugex/`

**Data Files Needed:**
- `drd2_smiles.csv` - DRD2 SMILES data
- `drd2_fragbase.txt` - DRD2 fragments base
- Scoring functions in `diverse-hits/data/scoring_functions/drd2/`

**Location:** Place these files in `diverse-hits/data/` and `diverse-hits/data/scoring_functions/`

*Contact the repository maintainer for download links or instructions if needed.*

### 3. Verify Installation

```bash
conda activate thesis-env
python -c "import drugex; import divopt; print('✓ Setup successful')"
```

## Running Thesis Scripts

### Available Scripts

All scripts are in `thesis/scripts/`. Key scripts include:

| Script | Purpose |
|--------|---------|
| `train.py` | Train DrugEx with graph transformer |
| `seq.py` | Train DrugEx with SMILES RNN |
| `extract_metrics.py` | Extract metrics from results |
| `check_budget_constraints.py` | Verify optimization budgets |
| `analyze_reward_distributions.py` | Analyze reward signals |
| `ModelScorer.py` | Score molecules with custom functions |

### Running a Script

```bash
conda activate thesis-env
cd thesis/scripts/
python SCRIPT_NAME.py [options]
```

**Example: Train graph-based DrugEx**
```bash
conda activate thesis-env
cd thesis/scripts/
python train.py
```

**Example: Extract metrics from results**
```bash
conda activate thesis-env
cd thesis/scripts/
python extract_metrics.py
```

### Output

Scripts typically output results to `thesis/results/` directories.

## Repository Structure

```
.
├── diverse-hits/              # Benchmark framework
│   ├── divopt/                # Scoring & diversity framework
│   ├── optimizers/            # Molecular generation algorithms
│   │   └── drugex/            # DrugEx implementation
│   ├── data/                  # Datasets & configs
│   └── scripts/               # Benchmark scripts
│
├── DrugEx/                    # DrugEx library
│   ├── drugex/                # Core module
│   └── data/                  # (Pre-trained models go here)
│
├── thesis/                    # Thesis-specific work
│   ├── scripts/               # Training & analysis scripts
│   └── results/               # Output results
│
├── setup_environment.sh       # Environment setup script
├── environment.yml            # GPU environment (CUDA 11.8+)
├── environment-cpu.yml        # CPU-only environment
└── README.md                  # This file
```

## Environment Details

**GPU Version (environment.yml):**
- Python 3.11
- PyTorch with CUDA 11.8 support
- RDKit, DGL, scikit-learn, pandas, numpy, scipy
- For Linux/Mac with NVIDIA GPU

**CPU-Only Version (environment-cpu.yml):**
- Python 3.11
- PyTorch CPU-only
- Same dependencies as GPU version
- For Windows, Mac, or systems without NVIDIA GPU

For complete dependencies, see respective environment files.

## Troubleshooting

### CUDA/Environment Setup Issues

**Error: `unsupported request` / `pytorch-cuda` not found**

**Solution:** You're on Windows or don't have CUDA 11.8+ installed. Use CPU-only environment:
```bash
# Remove the GPU environment (if it exists)
conda env remove -n thesis-env

# Create CPU-only environment instead
conda env create -f environment-cpu.yml
conda activate thesis-env
pip install -e DrugEx/
pip install -e diverse-hits/
```

**For Windows users:**
- Always use `environment-cpu.yml` (GPU support on Windows is limited)
- Run setup script and select option 2 (CPU-only)

**For GPU troubleshooting:**
- Verify CUDA installation: `nvidia-smi`
- Check CUDA version compatibility (need 11.8+)
- If using older CUDA, manually edit environment.yml pytorch-cuda version

**Error: `UnavailableInvalidChannel` or `HTTP 404 Not Found for channel`**

This can happen with older conda or network issues. Try these solutions:

```bash
# Option 1: Update conda first
conda update -n base -c defaults conda

# Option 2: Clear conda cache and retry
conda clean --all
conda env create -f environment-cpu.yml

# Option 3: Use mamba (faster package resolver, often works better)
conda install -c conda-forge mamba
mamba env create -f environment-cpu.yml
```

If still failing, try installing PyTorch separately:
```bash
# For CPU-only
conda create -n thesis-env python=3.11
conda activate thesis-env
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt  # Other dependencies
pip install -e DrugEx/ -e diverse-hits/
```

### Model Files Not Found
**Error:** `FileNotFoundError: [Errno 2] No such file or directory: '...Papyrus05.5_graph_trans_PT.pkg'`

**Solution:** Download and place pre-trained models in `diverse-hits/optimizers/drugex/` as described in Step 2 of Quick Start.

### Import Errors
**Error:** `ModuleNotFoundError: No module named 'drugex'` or `'divopt'`

**Solution:** Ensure packages are installed in editable mode:
```bash
conda activate thesis-env
pip install -e DrugEx/
pip install -e diverse-hits/
```

### CUDA Out of Memory
**Error:** `RuntimeError: CUDA out of memory`

**Solutions:**
1. Reduce batch size in script parameters
2. Use CPU-only environment instead
3. Use a machine with more GPU memory

### Setup Script Issues on Windows

If `bash setup_environment.sh` fails on Windows:
1. Install Git Bash (comes with Git for Windows)
2. Run from Git Bash terminal instead of Command Prompt
3. Or manually run the environment creation (see Manual setup above)

### RDKit Import Errors

```bash
# Reinstall RDKit
conda remove rdkit
conda install -c conda-forge rdkit
```

## Testing

Run the test suite:

```bash
cd diverse-hits/
pytest test/ -v --tb=short

# Run specific test
pytest test/test_scoring_function.py -v
```

## Performance Notes

Typical performance on modern GPU (e.g., RTX 3090):
- **DrugEx**: 1,000 molecules/epoch (~5s/epoch)
- **CPU-only**: ~10-50x slower depending on the algorithm

## Citation

If you use this repository in research, please cite:
- DrugEx: [Link to publications]
- GuacaMol: [Link to publications]

## License

See individual package licenses in `DrugEx/LICENSE` and `diverse-hits/LICENSE`.

---

**Last Updated**: June 2026  
**Python Version**: 3.11  
**Primary Dependencies**: RDKit, DGL, scikit-learn, PyTorch
