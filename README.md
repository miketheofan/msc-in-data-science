## Salinas Hyperspectral Image Analysis

This project implements spectral unmixing and classification techniques on the Salinas hyperspectral image dataset.

### Dataset

The project uses the following data files:

- `Salinas_cube.mat` - The hyperspectral image cube (220x120x204 dimensions)
- `Salinas_endmembers.mat` - Matrix of 7 endmember spectral signatures (204x7)
- `Salinas_gt.mat` - Ground truth labels
- `classification_labels_Salinas.mat` - Training, test and operational set labels

### Features

#### Spectral Unmixing

Multiple unmixing algorithms are implemented:

- Least Squares
- Sum-to-One constrained
- Non-Negative Least Squares
- Non-Negative Sum-to-One constrained
- Lasso regression

#### Visualization

The notebook provides several visualization functions:

- Plot abundance maps for each material
- Plot sum of abundance coefficients
- Compare results across different unmixing methods
- Display reconstruction errors

### Materials Analyzed

Seven different materials are analyzed:

- Grapes
- Broccoli
- Fallow 1
- Fallow 2
- Fallow 3
- Stubble
- Celery

### Requirements

The code requires the following Python libraries:

- numpy
- scipy
- matplotlib
- scikit-learn
- jupyter

### Usage

Run the Jupyter notebook `Project_AUEB.ipynb` to perform the analysis. The notebook contains step-by-step implementation of the unmixing algorithms and visualization of results.

**Note:** All data files must be in the same directory as the notebook for proper execution.
