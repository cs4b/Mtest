#!/usr/bin/env python3
"""
Verify that all required input files for thesis scripts are present and accessible.
This script checks for pre-trained models, fragment bases, scoring functions, and data files.
"""

import os
import sys
from pathlib import Path

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def check_file(path: str, description: str = None) -> bool:
    """Check if a file exists and print status."""
    exists = os.path.exists(path)
    status = f"{GREEN}✓{RESET}" if exists else f"{RED}✗{RESET}"
    
    display_path = path.replace(os.getcwd() + '/', '')
    if description:
        print(f"  {status} {display_path:50} ({description})")
    else:
        print(f"  {status} {display_path}")
    
    return exists

def check_directory(path: str, description: str = None) -> bool:
    """Check if a directory exists and print status."""
    exists = os.path.isdir(path)
    status = f"{GREEN}✓{RESET}" if exists else f"{RED}✗{RESET}"
    
    display_path = path.replace(os.getcwd() + '/', '')
    if description:
        print(f"  {status} {display_path:50} ({description})")
    else:
        print(f"  {status} {display_path}")
    
    return exists

def main():
    print(f"\n{BLUE}═══════════════════════════════════════════════════════════════{RESET}")
    print(f"{BLUE}  Thesis Scripts Input Files Verification{RESET}")
    print(f"{BLUE}═══════════════════════════════════════════════════════════════{RESET}\n")
    
    all_good = True
    
    # Check pre-trained models
    print(f"{BLUE}Pre-trained Models (Graph Transformer){RESET}")
    all_good &= check_file('diverse-hits/optimizers/drugex/Papyrus05.5_graph_trans_PT.pkg', 'Required for GT scripts')
    all_good &= check_file('diverse-hits/optimizers/drugex/Papyrus05.5_graph_trans_PT.vocab', 'Fragment vocab')
    
    print(f"\n{BLUE}Pre-trained Models (Sequence RNN){RESET}")
    all_good &= check_file('diverse-hits/optimizers/drugex/Papyrus05.5_smiles_rnn_PT.pkg', 'Required for RNN scripts')
    all_good &= check_file('diverse-hits/optimizers/drugex/Papyrus05.5_smiles_rnn_PT.vocab', 'SMILES vocab')
    
    # Check fragment bases
    print(f"\n{BLUE}Fragment Base Files{RESET}")
    all_good &= check_file('diverse-hits/optimizers/drugex/drd2_fragbase.txt', 'DRD2 fragments')
    all_good &= check_file('diverse-hits/optimizers/drugex/gsk3_fragbase.txt', 'GSK3 fragments')
    all_good &= check_file('diverse-hits/optimizers/drugex/jnk3_fragbase.txt', 'JNK3 fragments')
    
    # Check SMILES data files
    print(f"\n{BLUE}SMILES Data Files (for RNN){RESET}")
    
    drd2_check = check_file('diverse-hits/optimizers/drugex/drd2_smiles.csv', 'DRD2 SMILES (CSV)')
    if not drd2_check:
        # Check for .txt version
        if check_file('diverse-hits/optimizers/drugex/drdsmiles.txt', '✓ Source exists (needs symlink)'):
            print(f"      {YELLOW}→ Create symlink: ln -s drdsmiles.txt drd2_smiles.csv{RESET}")
        all_good = False
    
    gsk3_check = check_file('diverse-hits/optimizers/drugex/gsk3_smiles.csv', 'GSK3 SMILES (CSV)')
    if not gsk3_check:
        if check_file('diverse-hits/optimizers/drugex/gsksmiles.txt', '✓ Source exists (needs symlink)'):
            print(f"      {YELLOW}→ Create symlink: ln -s gsksmiles.txt gsk3_smiles.csv{RESET}")
        all_good = False
    
    jnk3_check = check_file('diverse-hits/optimizers/drugex/jnk3_smiles.csv', 'JNK3 SMILES (CSV)')
    if not jnk3_check:
        if check_file('diverse-hits/optimizers/drugex/jnksmiles.txt', '✓ Source exists (needs symlink)'):
            print(f"      {YELLOW}→ Create symlink: ln -s jnksmiles.txt jnk3_smiles.csv{RESET}")
        all_good = False
    
    # Check scoring functions
    print(f"\n{BLUE}Scoring Functions (DRD2){RESET}")
    drd2_dir = 'diverse-hits/data/scoring_functions/drd2'
    all_good &= check_directory(drd2_dir, 'DRD2 scoring directory')
    all_good &= check_file(f'{drd2_dir}/classifier.pkl', 'DRD2 classifier')
    all_good &= check_file(f'{drd2_dir}/all.txt', 'DRD2 molecules')
    all_good &= check_file(f'{drd2_dir}/splits.csv', 'DRD2 splits')
    
    print(f"\n{BLUE}Scoring Functions (GSK3){RESET}")
    gsk3_dir = 'diverse-hits/data/scoring_functions/gsk3'
    all_good &= check_directory(gsk3_dir, 'GSK3 scoring directory')
    all_good &= check_file(f'{gsk3_dir}/classifier.pkl', 'GSK3 classifier')
    all_good &= check_file(f'{gsk3_dir}/all.txt', 'GSK3 molecules')
    all_good &= check_file(f'{gsk3_dir}/splits.csv', 'GSK3 splits')
    
    print(f"\n{BLUE}Scoring Functions (JNK3){RESET}")
    jnk3_dir = 'diverse-hits/data/scoring_functions/jnk3'
    all_good &= check_directory(jnk3_dir, 'JNK3 scoring directory')
    all_good &= check_file(f'{jnk3_dir}/classifier.pkl', 'JNK3 classifier')
    all_good &= check_file(f'{jnk3_dir}/all.txt', 'JNK3 molecules')
    all_good &= check_file(f'{jnk3_dir}/splits.csv', 'JNK3 splits')
    
    print(f"\n{BLUE}Shared Scoring Resources{RESET}")
    all_good &= check_file('diverse-hits/data/scoring_functions/guacamol_known_bits.json', 'GuacaMol config')
    all_good &= check_file('diverse-hits/data/scoring_functions/guacamol_thresholds.json', 'GuacaMol thresholds')
    
    # Summary
    print(f"\n{BLUE}═══════════════════════════════════════════════════════════════{RESET}")
    
    if all_good or (drd2_check and gsk3_check and jnk3_check):
        print(f"{GREEN}✓ All required files are present!{RESET}")
        if not (drd2_check and gsk3_check and jnk3_check):
            print(f"\n{YELLOW}⚠ Action required: Create CSV symlinks for RNN scripts{RESET}")
            print(f"  Run in {BLUE}diverse-hits/optimizers/drugex/{RESET}:")
            print(f"    {YELLOW}ln -s drdsmiles.txt drd2_smiles.csv{RESET}")
            print(f"    {YELLOW}ln -s gsksmiles.txt gsk3_smiles.csv{RESET}")
            print(f"    {YELLOW}ln -s jnksmiles.txt jnk3_smiles.csv{RESET}")
        print(f"\n{GREEN}Status: READY TO RUN{RESET}\n")
        return 0
    else:
        print(f"{RED}✗ Some files are missing or inaccessible!{RESET}")
        print(f"\n{YELLOW}Please check THESIS_SCRIPTS_INPUT_FILES.md for details.{RESET}\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())
