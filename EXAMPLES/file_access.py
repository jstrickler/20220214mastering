#!/usr/bin/env python

import sys
import os

if len(sys.argv) < 2:
    start_dir = "."
else:
    start_dir = sys.argv[1]

for base_name in os.listdir(start_dir):  # <1>
    file_path = os.path.join(start_dir, base_name)
    if os.access(file_path, os.W_OK):  # <2>
        print(f"{base_name:30s} is writable")
