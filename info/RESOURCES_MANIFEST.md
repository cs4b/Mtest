# Thesis Resources Manifest

Generated: June 21, 2026

This manifest documents all input files required for thesis scripts and their distribution:
- **Included in Git** (small files)
- **Too Large for Git** (must be obtained separately)

## File Inventory

### ✅ Included in Git (Automatically Deployed)

**Total Size: ~8 MB**

#### Vocabularies (models/)
| File | Size | Purpose |
|------|------|---------|
| `Papyrus05.5_graph_trans_PT.vocab` | 522 B | Graph Transformer vocabulary |
| `Papyrus05.5_smiles_rnn_PT.vocab` | 393 B | RNN vocabulary |

#### Fragment Bases (fragbases/)
| File | Size | Purpose |
|------|------|---------|
| `drd2_fragbase.txt` | 135 KB | DRD2 seed molecules |
| `gsk3_fragbase.txt` | 155 KB | GSK3 seed molecules |
| `jnk3_fragbase.txt` | 45 KB | JNK3 seed molecules |

#### SMILES Data (smiles_data/)
| File | Size | Purpose |
|------|------|---------|
| `drdsmiles.txt` | 138 KB | DRD2 SMILES sequences |
| `gsksmiles.txt` | 155 KB | GSK3 SMILES sequences |
| `jnksmiles.txt` | 45 KB | JNK3 SMILES sequences |

#### Scoring Configs (scoring_functions/)
| File | Size | Purpose |
|------|------|---------|
| `guacamol_known_bits.json` | 5.8 MB | Known active bits |
| `guacamol_thresholds.json` | 160 B | Multi-objective thresholds |

### ⚠️ Not Included - Too Large (Must Download)

**Total Size: ~372 MB**

#### Pre-trained Models (~182 MB)
| File | Size | Location | Status | Source |
|------|------|----------|--------|--------|
| `Papyrus05.5_graph_trans_PT.pkg` | 153 MB | `diverse-hits/optimizers/drugex/` | ❌ Missing | Papyrus or diverse-hits |
| `Papyrus05.5_smiles_rnn_PT.pkg` | 29 MB | `diverse-hits/optimizers/drugex/` | ❌ Missing | Papyrus or diverse-hits |

**Why excluded:** Too large for Git LFS consideration; must be obtained from original source

**How to get:**
1. Visit https://papyrus.readthedocs.io/ 
2. Or download from diverse-hits GitHub releases
3. Place in `diverse-hits/optimizers/drugex/`

#### Scoring Function Classifiers (~190 MB)
| File | Size | Location | Status | Needed For |
|------|------|----------|--------|------------|
| `drd2/classifier.pkl` | 71 MB | `diverse-hits/data/scoring_functions/drd2/` | ❌ Missing | DRD2 experiments |
| `gsk3/classifier.pkl` | 78 MB | `diverse-hits/data/scoring_functions/gsk3/` | ❌ Missing | GSK3 experiments |
| `jnk3/classifier.pkl` | 36 MB | `diverse-hits/data/scoring_functions/jnk3/` | ❌ Missing | JNK3 experiments |

Plus supporting files per target (~25 MB):
- `{target}/frags.tsv` - Fragment vocabulary
- `{target}/frags.tsv.vocab` - Fragment vocab index
- `{target}/all.txt` - Complete molecule list
- `{target}/splits.csv` - Train/test split
- `{target}/stats.json` - Dataset statistics

**Why excluded:** Too large; part of diverse-hits data package

**How to get:**
1. Clone diverse-hits: https://github.com/aspuru-guzik-group/absolute_potency_ge
2. Or obtain from diverse-hits releases
3. Place in `diverse-hits/data/scoring_functions/{target}/`

## Setup Workflow

### After `git clone`:

```bash
# 1. Navigate to resources directory
cd thesis/resources/

# 2. Run setup script (copies all small files)
python setup_resources.py

# 3. Script will report missing large files
# 4. Download large files from indicated sources
# 5. Place in indicated locations
# 6. Re-run setup script to verify
```

### Typical Output Flow:

```
1. First run (before downloading large files):
   ✓ Small files copied: 13
   ⚠ Large files: 0 present, 5 missing
   
2. Download large files and run again:
   ✓ Small files copied: 13
   ✓ Large files: 5 present, 0 missing
   ✓ Setup complete!
```

## Size Summary

| Category | Size | Status |
|----------|------|--------|
| Vocabularies | ~1 KB | ✅ In Git |
| Fragment Bases | ~335 KB | ✅ In Git |
| SMILES Data | ~338 KB | ✅ In Git |
| Scoring Configs | ~5.8 MB | ✅ In Git |
| **Small Files Total** | **~6.5 MB** | **✅ Included** |
| Pre-trained Models | ~182 MB | ⚠️ Not in Git |
| Scoring Classifiers | ~190 MB | ⚠️ Not in Git |
| **Large Files Total** | **~372 MB** | **❌ Not Included** |
| **Grand Total** | **~378.5 MB** | Mixed |

## Verification

After setup, verify all files are in place:

```bash
# From repository root:
python verify_input_files.py

# Expected output:
✓ All required files are present!
Status: READY TO RUN
```

## Notes for Repository Maintainers

- Small files are Git-tracked and deployed with `git clone`
- Large files require separate distribution (email, cloud storage, or release)
- The `setup_resources.py` script is designed to work standalone
- Manifest is auto-updated when resources are added
- Use `du -sh thesis/resources/*` to check local size

## Alternative: Git LFS

If you want to include large files in Git:

```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track 'diverse-hits/optimizers/drugex/*.pkg'
git lfs track 'diverse-hits/data/scoring_functions/*/*.pkl'

# Commit and push
git add .gitattributes
git commit -m "Add LFS tracking for large model files"
git push
```

This requires all users to have Git LFS installed but makes deployment automatic.

---

**Last Updated:** June 21, 2026  
**Manifest Version:** 1.0
