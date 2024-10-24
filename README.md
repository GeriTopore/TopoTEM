# TopoTEM
TopoTEM is a Python tool for analysing, quantifying and visualising atomic displacements and polarisation in atomic-resolution Scanning Transmission Microscopy (STEM) images.

## Installation
As TopoTEM is still in development, first clone this repository on your personal device in a location of your choice using Git:

```bash
git clone https://github.com/GeriTopore/TopoTEM.git
```
Make sure that conda is up to date in your `base` environment:
```bash
conda update conda
```
Create a new conda environment for TopoTEM with Python 3.12:
```bash
conda create -n topotem_dev python=3.12
conda activate topotem_dev
```

Then through a terminal, change to the TopoTEM directory and use `pip` to install the package as follows:

```bash
pip install -e .
```

## Getting Started
Under `TopoTEM/test_notebooks` the Jupyter notebook `polarisation_vectors_tutorial.ipynb` provides a good starting point and showcases the different visualisations available within TopoTEM. For more information, for now please refer to the documentation available in the TEMUL website [here](https://temul-toolkit.readthedocs.io/en/latest/polarisation_vectors_tutorial.html#).
