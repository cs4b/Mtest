# Thesis Repository Setup Guide

## Summary of Changes

Your repository has been cleaned up and prepared for upload to GitLab. Here's what was done:

### ✅ Completed Actions

1. **Removed Git History**
   - Fresh git repository (all old commits cleared)
   - Clean slate for new remote

2. **Created Setup Script** (`setup_environment.sh`)
   - Automated environment configuration
   - Installs all dependencies via conda
   - Installs DrugEx and divopt packages
   - Creates required directories
   - Run it with: `bash setup_environment.sh`

3. **Updated .gitignore**
   - Excludes all large model files (*.pkg, *.vocab, *.pth, etc.)
   - Excludes large data files (*.tsv, *.smiles, *.json model files)
   - Excludes results and checkpoint directories
   - Excludes duplicate thesis directories
   - Keeps all Python source code and configuration

4. **Rewrote README.md**
   - Focuses on running thesis scripts from `thesis/scripts/`
   - Clear setup instructions
   - Documents which models/data need to be downloaded separately
   - Troubleshooting guide for common issues

5. **Repository Size Reduced**
   - **Before**: 385.99 MB (with pre-committed large files)
   - **After**: 72.56 MB (clean, ready for upload)
   - **Reduction**: 81% smaller! 🎉

### 📦 What's Included

- ✅ DrugEx source code (`DrugEx/` directory)
- ✅ divopt framework (`diverse-hits/` directory)
- ✅ All thesis scripts (`thesis/scripts/`)
- ✅ Configuration files and documentation
- ✅ Scoring function configs (structure only, data files excluded)

### 🚫 What's Excluded (Not in Repository)

- ❌ Pre-trained models (*.pkg, *.vocab files)
- ❌ Large data files (SMILES, fragments, QSAR models)
- ❌ Optimization results and checkpoints
- ❌ Duplicate thesis directories
- ❌ Generated output files

## Next Steps: Push to GitLab

### 1. Create a New GitLab Repository

Go to GitLab and create a new empty repository (DO NOT initialize with README, .gitignore, or license).

### 2. Add Remote and Push

```bash
# Add your new remote (replace with your actual GitLab URL)
git remote add origin https://gitlab.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitLab
git push -u origin main
```

### 3. Verify Upload

Visit your GitLab repository page and confirm all files are there.

## User Instructions for Repository

Once uploaded, users will:

### 1. Clone the Repository
```bash
git clone https://gitlab.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Run Setup
```bash
bash setup_environment.sh
conda activate thesis-env
```

### 3. Download Required Models & Data

Users need to obtain and place the following files:

**Pre-trained Models:**
- Place in `diverse-hits/optimizers/drugex/`:
  - `Papyrus05.5_graph_trans_PT.pkg`
  - `Papyrus05.5_graph_trans_PT.vocab`
  - `Papyrus05.5_smiles_rnn_PT.pkg`
  - `Papyrus05.5_smiles_rnn_PT.vocab`

**Data Files:**
- Place in `diverse-hits/data/`:
  - `drd2_smiles.csv`
  - `drd2_fragbase.txt`
  - Scoring functions in `diverse-hits/data/scoring_functions/drd2/`

### 4. Run Scripts

```bash
conda activate thesis-env
cd thesis/scripts/
python train.py
```

## Repository Structure

```
.
├── diverse-hits/              # Benchmark framework
│   ├── divopt/                # Scoring & diversity logic
│   ├── optimizers/            # Molecular generation code
│   │   └── drugex/            # DrugEx implementation
│   ├── data/                  # Configs & empty data dirs
│   └── scripts/               # Benchmark execution scripts
│
├── DrugEx/                    # DrugEx library
│   ├── drugex/                # Source code
│   ├── data/                  # (Users place models here)
│   └── docs/                  # Documentation
│
├── thesis/                    # Research-specific
│   ├── scripts/               # Training & analysis scripts
│   │   ├── train.py           # Graph transformer training
│   │   ├── seq.py             # SMILES RNN training
│   │   ├── extract_metrics.py # Result analysis
│   │   └── ... 30+ scripts
│   └── results/               # (Generated during runs)
│
├── setup_environment.sh       # Automated setup
├── environment.yml            # Conda spec
├── README.md                  # User guide
└── .gitignore                 # Exclusion rules
```

## Files Modified

1. **setup_environment.sh** (NEW)
   - Automated environment creation
   - 50 lines, executable script

2. **.gitignore** (UPDATED)
   - Cleaned up and organized
   - Now excludes: large models, data, results, duplicates
   - Keeps all source code

3. **README.md** (COMPLETELY REWRITTEN)
   - Focus on thesis scripts execution
   - Clear setup and running instructions
   - Troubleshooting section
   - Model/data download notes

## Verification Checklist

- ✅ Repository is clean (72.56 MB)
- ✅ All 339 files properly tracked
- ✅ No large files included
- ✅ All thesis scripts included
- ✅ Setup script is functional
- ✅ README is clear and user-friendly
- ✅ Initial commit created
- ✅ Ready for GitLab upload

## Notes

- The repository uses relative paths (e.g., `diverse-hits/...`) so it works anywhere
- Scripts expect to be run from their directories or with proper path setup
- GPU support is configured via CUDA 11.8 in environment.yml
- CPU-only mode can be enabled by modifying environment.yml

## Support

If users encounter issues:
1. Check README.md Troubleshooting section
2. Ensure all models/data files are in correct locations
3. Verify conda environment is activated
4. Check CUDA/GPU setup for your system
