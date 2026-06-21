# Thesis Resources

This directory contains essential input files for thesis scripts. Files are organized by category:

- **models/** - Pre-trained model vocabularies (small files)
- **fragbases/** - Fragment base SMILES for molecular generation
- **smiles_data/** - SMILES sequences for RNN training
- **scoring_functions/** - Scoring function configs (small files)

## Large Files (Not Included - Download Required)

The following files are **too large for Git** but required for scripts:

### Pre-trained Model Files (182 MB total)
- `Papyrus05.5_graph_trans_PT.pkg` - 153 MB (Graph Transformer model)
- `Papyrus05.5_smiles_rnn_PT.pkg` - 29 MB (RNN model)

**Status:** Must be downloaded or obtained from:
- Original source: Papyrus database https://papyrus.readthedocs.io/
- Or from diverse-hits release on GitHub

**Location after download:** Place in `diverse-hits/optimizers/drugex/`

### Scoring Function Classifier Files (185 MB total)
- `drd2/classifier.pkl` - DRD2 activity predictor
- `gsk3/classifier.pkl` - GSK3 activity predictor
- `jnk3/classifier.pkl` - JNK3 activity predictor

Plus supporting files (frags.tsv, splits.csv, stats.json) for each target.

**Status:** Must be downloaded or obtained from diverse-hits package

**Location after download:** Place in `diverse-hits/data/scoring_functions/{target}/`

## Setup Instructions

### 1. Run Resource Setup (Copies small files)

```bash
cd /path/to/thesis/
python setup_resources.py
```

This automatically:
- ✅ Copies vocabulary files to `diverse-hits/optimizers/drugex/`
- ✅ Copies fragment base files
- ✅ Copies SMILES data files
- ✅ Creates symlinks for CSV filenames
- ✅ Copies scoring function configs
- ⚠️ Warns if large files are missing

### 2. Download Large Files (If Needed)

If large model files are missing, the script will provide download instructions.

```bash
# After running setup_resources.py, download and place:
# - Papyrus05.5_graph_trans_PT.pkg → diverse-hits/optimizers/drugex/
# - Papyrus05.5_smiles_rnn_PT.pkg → diverse-hits/optimizers/drugex/
# - Scoring function classifiers → diverse-hits/data/scoring_functions/
```

## File Inventory

### Small Files (Git-friendly) ✅

| File | Size | Location |
|------|------|----------|
| Papyrus05.5_graph_trans_PT.vocab | 522 B | models/ |
| Papyrus05.5_smiles_rnn_PT.vocab | 393 B | models/ |
| drd2_fragbase.txt | 135 KB | fragbases/ |
| gsk3_fragbase.txt | 155 KB | fragbases/ |
| jnk3_fragbase.txt | 45 KB | fragbases/ |
| drdsmiles.txt | 138 KB | smiles_data/ |
| gsksmiles.txt | 155 KB | smiles_data/ |
| jnksmiles.txt | 45 KB | smiles_data/ |
| guacamol_known_bits.json | 5.8 MB | scoring_functions/ |
| guacamol_thresholds.json | 160 B | scoring_functions/ |

**Total:** ~8 MB (manageable for Git)

### Large Files (Not Included) ⚠️

| File | Size | Status | Needed By |
|------|------|--------|-----------|
| Papyrus05.5_graph_trans_PT.pkg | 153 MB | ❌ Download | Graph Transformer scripts |
| Papyrus05.5_smiles_rnn_PT.pkg | 29 MB | ❌ Download | RNN scripts |
| drd2/classifier.pkl | 71 MB | ❌ Download | DRD2 experiments |
| gsk3/classifier.pkl | 78 MB | ❌ Download | GSK3 experiments |
| jnk3/classifier.pkl | 36 MB | ❌ Download | JNK3 experiments |
| Supporting scoring files | ~25 MB | ❌ Download | All experiments |

**Total Large Files:** ~372 MB (must be obtained separately)

## Quick Reference

```bash
# Copy all small files to their locations
python setup_resources.py

# Verify setup
python ../verify_input_files.py
```

---

## Notes

- Small files are tracked in Git and automatically deployed with `git clone`
- Large files must be obtained from original sources (see setup script output for links)
- After copying small files, run `verify_input_files.py` to check status
- The `setup_resources.py` script provides download instructions for missing large files
