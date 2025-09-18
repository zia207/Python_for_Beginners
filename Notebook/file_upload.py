
import nbformat
from nbclient import NotebookClient

# Load notebook
with open('01_06_02_functional_programming_toolz_python.ipynb') as f:
    nb = nbformat.read(f, as_version=4)

# Execute it
client = NotebookClient(nb, timeout=600)
client.execute()

