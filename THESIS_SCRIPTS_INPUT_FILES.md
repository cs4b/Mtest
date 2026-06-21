# Input Files Required for Thesis Scripts

This document lists all input files required to run the scripts in `thesis/scripts/`. Each file is marked with its source and whether it's already available in the repository.

## ⚡ Quick Setup (Before Running Scripts)

**All required files are already in the repository.** To prepare for running RNN scripts:

```bash
cd diverse-hits/optimizers/drugex/

# Create symlinks for SMILES CSV files (required by RNN scripts)
ln -s drdsmiles.txt drd2_smiles.csv
ln -s gsksmiles.txt gsk3_smiles.csv
ln -s jnksmiles.txt jnk3_smiles.csv

# Verify setup
echo "Setup complete. Run verification with:"
echo "  python ~/thesis/scripts/verify_setup.py"
```

**All other files are ready to use immediately.** See sections below for detailed file list and locations.

---

## Overview

Scripts use three main categories of input files:
1. **Pre-trained Models** - Pretrained neural networks for DrugEx
2. **Fragment Bases** - SMILES data for molecular generation
3. **Scoring Functions** - Trained classifiers for target proteins (drd2, gsk3, jnk3)
4. **Training Data** - SMILES or fragment files for training

---

## Pre-trained Models (Required for All Scripts)

These files are needed for model initialization and are located in `diverse-hits/optimizers/drugex/`

### Graph Transformer Models (for fragmentation-based approaches)

| File | Location | Status | Size | Purpose | Source |
|------|----------|--------|------|---------|--------|
| `Papyrus05.5_graph_trans_PT.pkg` | `diverse-hits/optimizers/drugex/` | ✅ **Available** | Large | Graph Transformer pre-trained weights | Papyrus database ([Download Link](https://doi.org/10.1038/s41597-020-00556-7)) |
| `Papyrus05.5_graph_trans_PT.vocab` | `diverse-hits/optimizers/drugex/` | ✅ **Available** | ~5KB | Fragment vocabulary for Graph Transformer | Same source |

### Sequence RNN Models (for SMILES sequence-based approaches)

| File | Location | Status | Size | Purpose | Source |
|------|----------|--------|------|---------|--------|
| `Papyrus05.5_smiles_rnn_PT.pkg` | `diverse-hits/optimizers/drugex/` | ✅ **Available** | Large | Sequence RNN pre-trained weights | Papyrus database ([Download Link](https://doi.org/10.1038/s41597-020-00556-7)) |
| `Papyrus05.5_smiles_rnn_PT.vocab` | `diverse-hits/optimizers/drugex/` | ✅ **Available** | ~5KB | SMILES vocabulary for Sequence RNN | Same source |

---

## Fragment Base Files (SMILES Data)

Located in `diverse-hits/optimizers/drugex/`. These are seed molecules for each target.

| File | Target | Status | Purpose | Source |
|------|--------|--------|---------|--------|
| `drd2_fragbase.txt` | DRD2 | ✅ **Available** | Fragment base (SMILES) for DRD2 target | Papyrus database / diverse-hits package |
| `gsk3_fragbase.txt` | GSK3 | ✅ **Available** | Fragment base (SMILES) for GSK3 target | Papyrus database / diverse-hits package |
| `jnk3_fragbase.txt` | JNK3 | ✅ **Available** | Fragment base (SMILES) for JNK3 target | Papyrus database / diverse-hits package |

**Note:** For RNN-based approaches:

| File | Target | Status | Purpose | Source |
|------|--------|--------|---------|--------|
| `drd2_smiles.csv` | DRD2 | ⚠️ **RENAME NEEDED** | SMILES data for RNN training (DRD2) | Currently named `drdsmiles.txt` in `dataset_preparation/` or root dir |
| `gsk3_smiles.csv` | GSK3 | ⚠️ **RENAME NEEDED** | SMILES data for RNN training (GSK3) | Currently named `gsksmiles.txt` in root dir |
| `jnk3_smiles.csv` | JNK3 | ⚠️ **RENAME NEEDED** | SMILES data for RNN training (JNK3) | Currently named `jnksmiles.txt` in root dir |

**IMPORTANT:** The scripts expect `.csv` extensions but actual files are `.txt`. Before running RNN scripts, rename or symlink:
```bash
cd diverse-hits/optimizers/drugex/
ln -s drdsmiles.txt drd2_smiles.csv  # or: cp drdsmiles.txt drd2_smiles.csv
ln -s gsksmiles.txt gsk3_smiles.csv
ln -s jnksmiles.txt jnk3_smiles.csv
```

---

## Scoring Functions (Required for Training)

These files enable molecular property evaluation for each target. Located in `diverse-hits/data/scoring_functions/{target}/`

### DRD2 Scoring Function Files

| File | Status | Purpose |
|------|--------|---------|
| `diverse-hits/data/scoring_functions/drd2/classifier.pkl` | ✅ **Available** | Pre-trained classifier for DRD2 activity prediction |
| `diverse-hits/data/scoring_functions/drd2/drd2_frags.tsv` | ✅ **Available** | Fragment data for DRD2 scoring |
| `diverse-hits/data/scoring_functions/drd2/drd2_frags.tsv.vocab` | ✅ **Available** | Vocabulary for fragment scoring |
| `diverse-hits/data/scoring_functions/drd2/all.txt` | ✅ **Available** | Complete molecule list for DRD2 |
| `diverse-hits/data/scoring_functions/drd2/splits.csv` | ✅ **Available** | Train/test split information |
| `diverse-hits/data/scoring_functions/drd2/stats.json` | ✅ **Available** | Statistics for DRD2 dataset |

### GSK3 Scoring Function Files

| File | Status | Purpose |
|------|--------|---------|
| `diverse-hits/data/scoring_functions/gsk3/classifier.pkl` | ✅ **Available** | Pre-trained classifier for GSK3 activity prediction |
| `diverse-hits/data/scoring_functions/gsk3/gsk3_frags.tsv` | ✅ **Available** | Fragment data for GSK3 scoring |
| `diverse-hits/data/scoring_functions/gsk3/gsk3_frags.tsv.vocab` | ✅ **Available** | Vocabulary for fragment scoring |
| `diverse-hits/data/scoring_functions/gsk3/all.txt` | ✅ **Available** | Complete molecule list for GSK3 |
| `diverse-hits/data/scoring_functions/gsk3/splits.csv` | ✅ **Available** | Train/test split information |
| `diverse-hits/data/scoring_functions/gsk3/stats.json` | ✅ **Available** | Statistics for GSK3 dataset |

### JNK3 Scoring Function Files

| File | Status | Purpose |
|------|--------|---------|
| `diverse-hits/data/scoring_functions/jnk3/classifier.pkl` | ✅ **Available** | Pre-trained classifier for JNK3 activity prediction |
| `diverse-hits/data/scoring_functions/jnk3/jnk3_frags.tsv` | ✅ **Available** | Fragment data for JNK3 scoring |
| `diverse-hits/data/scoring_functions/jnk3/jnk3_frags.tsv.vocab` | ✅ **Available** | Vocabulary for fragment scoring |
| `diverse-hits/data/scoring_functions/jnk3/all.txt` | ✅ **Available** | Complete molecule list for JNK3 |
| `diverse-hits/data/scoring_functions/jnk3/splits.csv` | ✅ **Available** | Train/test split information |
| `diverse-hits/data/scoring_functions/jnk3/stats.json` | ✅ **Available** | Statistics for JNK3 dataset |

### Shared Scoring Files

| File | Status | Purpose |
|------|--------|---------|
| `diverse-hits/data/scoring_functions/guacamol_known_bits.json` | ✅ **Available** | Known active bits for GuacaMol-based scoring |
| `diverse-hits/data/scoring_functions/guacamol_thresholds.json` | ✅ **Available** | Activity thresholds for multi-objective optimization |

---

## Scripts and Their Input File Requirements

### 1. **train.py** (Basic Graph Transformer Training)

**Purpose:** Single-target training demo with DRD2

**Input Files Required:**
- ✅ `diverse-hits/optimizers/drugex/drd2_fragbase.txt` - Fragment base molecules
- ✅ `diverse-hits/optimizers/drugex/Papyrus05.5_graph_trans_PT.pkg` - Pre-trained model
- ✅ `diverse-hits/optimizers/drugex/Papyrus05.5_graph_trans_PT.vocab` - Fragment vocabulary
- ✅ `diverse-hits/data/scoring_functions/drd2/*` - DRD2 scoring function (all files)

**Output:** Trained model in `diverse-hits/optimizers/drugex/` directories

---

### 2. **seq.py** (Sequence RNN Training)

**Purpose:** SMILES sequence-based training for drd2, gsk3, jnk3

**Input Files Required:**

For each target (drd2, gsk3, jnk3):
- ✅ `diverse-hits/optimizers/drugex/{target}_smiles.csv` - SMILES training data
- ✅ `diverse-hits/optimizers/drugex/Papyrus05.5_smiles_rnn_PT.pkg` - Pre-trained RNN model
- ✅ `diverse-hits/optimizers/drugex/Papyrus05.5_smiles_rnn_PT.vocab` - SMILES vocabulary
- ✅ `diverse-hits/data/scoring_functions/{target}/*` - Scoring function for target

**Note:** If `*_smiles.csv` files don't exist, they may need to be generated from `*_fragbase.txt` files or created separately.

---

### 3. **DE_dist_samp_gt.py** (Graph Transformer with Distribution & Sampling)

**Purpose:** Distributed sampling with Graph Transformer; main experimental script

**Input Files Required:**

For each target (drd2, gsk3, jnk3):
- ✅ `diverse-hits/optimizers/drugex/{target}_fragbase.txt` - Fragment base molecules
- ✅ `diverse-hits/optimizers/drugex/Papyrus05.5_graph_trans_PT.pkg` - Pre-trained Graph Transformer
- ✅ `diverse-hits/optimizers/drugex/Papyrus05.5_graph_trans_PT.vocab` - Fragment vocabulary
- ✅ `diverse-hits/data/scoring_functions/{target}/*` - Scoring function (all files)

**Configuration:** 
- `N_TRIALS_PER_COMBO = 15` - Hyperparameter search trials
- `N_REPEATS_BEST = 5` - Repeats of best configuration
- `CONSTRAINTS` - Sample-limited (10k) and time-limited (600s) budgets

**Output:** Results in `thesis/results/` with metrics and generated molecules

---

### 4. **DE_dist_samp_RNN_Final.py** (RNN with Distribution & Sampling)

**Purpose:** Distributed sampling with Sequence RNN; main experimental script

**Input Files Required:**

For each target (drd2, gsk3, jnk3):
- ✅ `diverse-hits/optimizers/drugex/{target}_smiles.csv` - SMILES training data (or generate from fragbase)
- ✅ `diverse-hits/optimizers/drugex/Papyrus05.5_smiles_rnn_PT.pkg` - Pre-trained RNN
- ✅ `diverse-hits/optimizers/drugex/Papyrus05.5_smiles_rnn_PT.vocab` - SMILES vocabulary
- ✅ `diverse-hits/data/scoring_functions/{target}/*` - Scoring function (all files)

**Configuration:** Same as Graph Transformer version

**Output:** Results in `thesis/results/rnn/` with metrics and generated molecules

---

### 5. **hyperparam.py** (Hyperparameter Search - Graph Transformer)

**Purpose:** Systematic hyperparameter optimization for Graph Transformer

**Input Files Required:** Same as `DE_dist_samp_gt.py`

**Outputs:** Hyperparameter search results in `thesis/results/{target}/hyperparameter_search/`

---

### 6. **seqtest_hp_circles.py** (Hyperparameter Search - RNN with Diversity)

**Purpose:** Hyperparameter optimization for RNN with diversity-aware selection

**Input Files Required:** Same as `DE_dist_samp_RNN_Final.py`

**Outputs:** RNN HP results with circular sampling in `thesis/results/rnn_hp_circles/`

---

### 7. **reseeding.py** (Reseeding Experiments)

**Purpose:** Dynamic reseeding during optimization based on high-scoring molecules

**Input Files Required:**

For each target:
- ✅ `diverse-hits/optimizers/drugex/{target}_fragbase.txt` - Initial fragment base
- ✅ `diverse-hits/optimizers/drugex/Papyrus05.5_graph_trans_PT.pkg` - Pre-trained model
- ✅ `diverse-hits/optimizers/drugex/Papyrus05.5_graph_trans_PT.vocab` - Vocabulary
- ✅ `diverse-hits/data/scoring_functions/{target}/*` - Scoring functions

**Also requires:** Training log file (auto-generated): `rs_training_molecules.csv` from previous runs

**Outputs:** Reseeding results in `thesis/results/reseed/`

---

### 8. **reseeding_from_base.py** (Reseeding from Fragment Base)

**Purpose:** Reseeding that starts from fragment base molecules

**Input Files Required:** Same as `reseeding.py`

**Key Files to Pre-generate:** Fragbase encoding with seeds.smi registry

---

### 9. **Analysis Scripts** (Various)

| Script | Input Requirements |
|--------|-------------------|
| `extract_metrics.py` | CSV/JSON files from results directories |
| `analyze_reward_distributions.py` | Training logs with reward data |
| `check_molecules_per_epoch.py` | Generated molecule files from training runs |
| `compare_training_approaches.py` | Multiple run directories (GT vs RNN) |
| `diagnose_reseeding.py` | Reseeding trial directories |
| `verify_hyperparameter_sampling.py` | Hyperparameter search results |

These scripts mostly read from outputs of training scripts; no external files needed.

---

## File Dependency Tree

```
diverse-hits/optimizers/drugex/
├── [MODELS - Pre-trained]
│   ├── Papyrus05.5_graph_trans_PT.pkg
│   ├── Papyrus05.5_graph_trans_PT.vocab
│   ├── Papyrus05.5_smiles_rnn_PT.pkg
│   └── Papyrus05.5_smiles_rnn_PT.vocab
├── [FRAGMENT BASES]
│   ├── drd2_fragbase.txt
│   ├── gsk3_fragbase.txt
│   ├── jnk3_fragbase.txt
│   └── [SMILES CSV files - may need generation]
│       ├── drd2_smiles.csv
│       ├── gsk3_smiles.csv
│       └── jnk3_smiles.csv
│
└── diverse-hits/data/scoring_functions/
    ├── drd2/
    │   ├── classifier.pkl
    │   ├── drd2_frags.tsv
    │   ├── drd2_frags.tsv.vocab
    │   ├── all.txt
    │   ├── splits.csv
    │   └── stats.json
    ├── gsk3/ [same structure]
    ├── jnk3/ [same structure]
    ├── guacamol_known_bits.json
    └── guacamol_thresholds.json
```

---

## Installation & Data Acquisition Checklist

### Pre-check: Verify Existing Files

```bash
# Check pre-trained models
ls diverse-hits/optimizers/drugex/Papyrus05.5_*.{pkg,vocab}

# Check fragment bases
ls diverse-hits/optimizers/drugex/*_fragbase.txt

# Check scoring functions
ls diverse-hits/data/scoring_functions/{drd2,gsk3,jnk3}/classifier.pkl
```

### If Files Are Missing

**For pre-trained models & scoring functions:**
1. Clone the diverse-hits repository: https://github.com/aspuru-guzik-group/absolute_potency_ge
2. Download the required data files from Zenodo or the repository release
3. Place in appropriate directories

**For SMILES CSV files (if missing):**
- Can be generated from fragment base files or copied/symlinked from existing `.txt` files:
  ```python
  import pandas as pd
  df = pd.read_csv('drdsmiles.txt', header=None)
  df.to_csv('drd2_smiles.csv', index=False, header=False)
  ```
- Or simply create symlinks (faster):
  ```bash
  ln -s drdsmiles.txt drd2_smiles.csv
  ln -s gsksmiles.txt gsk3_smiles.csv
  ln -s jnksmiles.txt jnk3_smiles.csv
  ```

---

## Quick Start: Verifying Setup

Run this to check if all critical files exist:

```bash
#!/bin/bash
echo "Checking critical input files..."

# Models
for file in Papyrus05.5_graph_trans_PT.{pkg,vocab} Papyrus05.5_smiles_rnn_PT.{pkg,vocab}; do
    if [ -f "diverse-hits/optimizers/drugex/$file" ]; then
        echo "✓ $file"
    else
        echo "✗ $file MISSING"
    fi
done

# Fragment bases
for target in drd2 gsk3 jnk3; do
    if [ -f "diverse-hits/optimizers/drugex/${target}_fragbase.txt" ]; then
        echo "✓ ${target}_fragbase.txt"
    else
        echo "✗ ${target}_fragbase.txt MISSING"
    fi
done

# Scoring functions
for target in drd2 gsk3 jnk3; do
    if [ -f "diverse-hits/data/scoring_functions/$target/classifier.pkl" ]; then
        echo "✓ $target scoring function"
    else
        echo "✗ $target scoring function MISSING"
    fi
done
```

---

## Summary Table

| Category | Status | Priority | Action If Missing |
|----------|--------|----------|-------------------|
| Pre-trained Models (Graph) | ✅ Available | **CRITICAL** | Already in repository |
| Pre-trained Models (RNN) | ✅ Available | **CRITICAL** | Already in repository |
| Fragment Bases (all targets) | ✅ Available | **CRITICAL** | Already in diverse-hits package |
| Scoring Functions (all targets) | ✅ Available | **CRITICAL** | Already in diverse-hits package |
| SMILES TXT files | ✅ Available | Important | Exist as `.txt`; need symlink to `.csv` |

**Status Summary:** ✅ **All critical files are available.** Only action needed: create symlinks for SMILES CSV files (see instructions above) before running RNN-based scripts.

