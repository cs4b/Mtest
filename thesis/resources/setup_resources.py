#!/usr/bin/env python3
"""
Setup script to install resources from thesis/resources/ to their correct locations.

This script:
1. Copies small files (vocabularies, fragment bases, SMILES data) to correct locations
2. Creates symlinks for CSV filenames
3. Checks for large files and provides download instructions
4. Verifies all setup is complete

Run this after git clone to set up all resource files.
"""

import os
import sys
import shutil
from pathlib import Path

# Color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))

# File mappings: (source_in_resources, destination, description)
FILE_MAPPINGS = [
    # Vocabulary files
    ('models/Papyrus05.5_graph_trans_PT.vocab', 
     'diverse-hits/optimizers/drugex/Papyrus05.5_graph_trans_PT.vocab',
     'Graph Transformer vocabulary'),
    ('models/Papyrus05.5_smiles_rnn_PT.vocab',
     'diverse-hits/optimizers/drugex/Papyrus05.5_smiles_rnn_PT.vocab',
     'RNN vocabulary'),
    
    # Fragment bases
    ('fragbases/drd2_fragbase.txt',
     'diverse-hits/optimizers/drugex/drd2_fragbase.txt',
     'DRD2 fragment base'),
    ('fragbases/gsk3_fragbase.txt',
     'diverse-hits/optimizers/drugex/gsk3_fragbase.txt',
     'GSK3 fragment base'),
    ('fragbases/jnk3_fragbase.txt',
     'diverse-hits/optimizers/drugex/jnk3_fragbase.txt',
     'JNK3 fragment base'),
    
    # SMILES data
    ('smiles_data/drdsmiles.txt',
     'diverse-hits/optimizers/drugex/drdsmiles.txt',
     'DRD2 SMILES data'),
    ('smiles_data/gsksmiles.txt',
     'diverse-hits/optimizers/drugex/gsksmiles.txt',
     'GSK3 SMILES data'),
    ('smiles_data/jnksmiles.txt',
     'diverse-hits/optimizers/drugex/jnksmiles.txt',
     'JNK3 SMILES data'),
    
    # GuacaMol configs
    ('scoring_functions/guacamol_known_bits.json',
     'diverse-hits/data/scoring_functions/guacamol_known_bits.json',
     'GuacaMol known bits'),
    ('scoring_functions/guacamol_thresholds.json',
     'diverse-hits/data/scoring_functions/guacamol_thresholds.json',
     'GuacaMol thresholds'),
]

# Large files that need to be obtained separately
LARGE_FILES = {
    'diverse-hits/optimizers/drugex/Papyrus05.5_graph_trans_PT.pkg': {
        'size': '153 MB',
        'description': 'Graph Transformer pre-trained model',
        'source': 'Papyrus database or diverse-hits release'
    },
    'diverse-hits/optimizers/drugex/Papyrus05.5_smiles_rnn_PT.pkg': {
        'size': '29 MB',
        'description': 'RNN pre-trained model',
        'source': 'Papyrus database or diverse-hits release'
    },
    'diverse-hits/data/scoring_functions/drd2/classifier.pkl': {
        'size': '71 MB',
        'description': 'DRD2 activity classifier',
        'source': 'diverse-hits data package'
    },
    'diverse-hits/data/scoring_functions/gsk3/classifier.pkl': {
        'size': '78 MB',
        'description': 'GSK3 activity classifier',
        'source': 'diverse-hits data package'
    },
    'diverse-hits/data/scoring_functions/jnk3/classifier.pkl': {
        'size': '36 MB',
        'description': 'JNK3 activity classifier',
        'source': 'diverse-hits data package'
    },
}

# CSV symlinks to create
CSV_SYMLINKS = [
    ('diverse-hits/optimizers/drugex/drdsmiles.txt', 
     'diverse-hits/optimizers/drugex/drd2_smiles.csv',
     'DRD2 SMILES CSV symlink'),
    ('diverse-hits/optimizers/drugex/gsksmiles.txt',
     'diverse-hits/optimizers/drugex/gsk3_smiles.csv',
     'GSK3 SMILES CSV symlink'),
    ('diverse-hits/optimizers/drugex/jnksmiles.txt',
     'diverse-hits/optimizers/drugex/jnk3_smiles.csv',
     'JNK3 SMILES CSV symlink'),
]

def copy_file(src, dst, description):
    """Copy a file from source to destination."""
    src_path = os.path.join(SCRIPT_DIR, src)
    dst_path = os.path.join(PROJECT_ROOT, dst)
    
    if not os.path.exists(src_path):
        print(f"  {RED}✗{RESET} {description}: source not found ({src})")
        return False
    
    # Create destination directory if needed
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    
    try:
        shutil.copy2(src_path, dst_path)
        size = os.path.getsize(dst_path)
        size_str = f"{size/1024:.1f}K" if size < 1024*1024 else f"{size/(1024*1024):.1f}M"
        print(f"  {GREEN}✓{RESET} {description:40} ({size_str})")
        return True
    except Exception as e:
        print(f"  {RED}✗{RESET} {description}: {e}")
        return False

def create_symlink(target, link, description):
    """Create a symlink from link to target."""
    link_path = os.path.join(PROJECT_ROOT, link)
    target_path = os.path.join(PROJECT_ROOT, target)
    
    # Check if target exists
    if not os.path.exists(target_path):
        print(f"  {RED}✗{RESET} {description}: target not found ({target})")
        return False
    
    # Create symlink if it doesn't exist
    if os.path.exists(link_path):
        if os.path.islink(link_path):
            print(f"  {GREEN}✓{RESET} {description:40} (already exists)")
            return True
        else:
            print(f"  {YELLOW}⚠{RESET} {description:40} (file exists, not symlink)")
            return False
    
    try:
        # Create relative symlink
        os.symlink(os.path.basename(target_path), link_path)
        print(f"  {GREEN}✓{RESET} {description:40} (symlink created)")
        return True
    except Exception as e:
        print(f"  {RED}✗{RESET} {description}: {e}")
        return False

def check_large_files():
    """Check for large files and report status."""
    missing = []
    present = []
    
    for file_path, info in LARGE_FILES.items():
        full_path = os.path.join(PROJECT_ROOT, file_path)
        if os.path.exists(full_path):
            present.append((file_path, info))
        else:
            missing.append((file_path, info))
    
    return present, missing

def main():
    print(f"\n{BLUE}═══════════════════════════════════════════════════════════════{RESET}")
    print(f"{BLUE}  Thesis Resources Setup{RESET}")
    print(f"{BLUE}═══════════════════════════════════════════════════════════════{RESET}\n")
    
    # Change to project root
    os.chdir(PROJECT_ROOT)
    
    success_count = 0
    
    # Copy small files
    print(f"{BLUE}Copying small resource files...{RESET}")
    for src, dst, desc in FILE_MAPPINGS:
        if copy_file(src, dst, desc):
            success_count += 1
    
    print(f"\n{BLUE}Creating CSV symlinks...{RESET}")
    for target, link, desc in CSV_SYMLINKS:
        if create_symlink(target, link, desc):
            success_count += 1
    
    # Check large files
    print(f"\n{BLUE}Checking large files...{RESET}")
    present, missing = check_large_files()
    
    if present:
        print(f"\n{BLUE}Large files present ({len(present)}){RESET}")
        for file_path, info in present:
            size = os.path.getsize(os.path.join(PROJECT_ROOT, file_path))
            size_str = f"{size/(1024*1024):.1f}M"
            rel_path = file_path.replace('diverse-hits/optimizers/drugex/', '').replace('diverse-hits/data/scoring_functions/', '')
            print(f"  {GREEN}✓{RESET} {rel_path:50} ({size_str})")
    
    if missing:
        print(f"\n{YELLOW}Large files missing ({len(missing)}) - Download required:{RESET}")
        print(f"\n{YELLOW}These files must be obtained from their sources:{RESET}\n")
        
        for file_path, info in missing:
            rel_path = file_path.replace('diverse-hits/optimizers/drugex/', '').replace('diverse-hits/data/scoring_functions/', '')
            print(f"  {YELLOW}•{RESET} {rel_path}")
            print(f"      Size: {info['size']}")
            print(f"      Desc: {info['description']}")
            print(f"      Source: {info['source']}")
            print(f"      Destination: {BLUE}{file_path}{RESET}")
            print()
        
        print(f"{YELLOW}Instructions:{RESET}")
        print(f"  1. Download model files from Papyrus database:")
        print(f"     → https://papyrus.readthedocs.io/")
        print(f"     → Or from diverse-hits GitHub releases")
        print(f"  2. Place in: diverse-hits/optimizers/drugex/")
        print(f"  3. Download scoring functions from diverse-hits package")
        print(f"  4. Place in: diverse-hits/data/scoring_functions/{{target}}/")
        print(f"  5. Re-run this script to verify")
    else:
        print(f"\n{GREEN}✓ All large files are present!{RESET}")
    
    # Summary
    print(f"\n{BLUE}═══════════════════════════════════════════════════════════════{RESET}")
    print(f"\n{BLUE}Summary:{RESET}")
    print(f"  {GREEN}✓{RESET} Small files copied: {success_count}")
    print(f"  {GREEN if not missing else YELLOW}✓{RESET if not missing else '⚠'} Large files: {len(present)} present, {len(missing)} missing")
    
    if not missing:
        print(f"\n{GREEN}✓ Setup complete! All resources ready.{RESET}")
        print(f"  Run 'python ../verify_input_files.py' to verify\n")
        return 0
    else:
        print(f"\n{YELLOW}⚠ Setup partial. Download large files and re-run this script.{RESET}\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())
