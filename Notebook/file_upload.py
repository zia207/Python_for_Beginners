
!pip install nbformat

import nbformat
import os
for file in os.listdir('.'):
    if file.endswith('.ipynb'):
        with open(file) as f:
            nb = nbformat.read(f, as_version=4)
            print(f"Loaded notebook: {file}")