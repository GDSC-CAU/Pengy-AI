# Pengy AI trainning

## Overview
This project is focused on training a model for object detection using datasets from Roboflow and COCO. The process is divided into three main Jupyter Notebooks, executed on Google Colab for efficient use of resources and easy access to GPUs.

### Notebooks:
1. `import_dataset.ipynb`
2. `setting_dataset.ipynb`
3. `train_model.ipynb`

## 1. Importing the Dataset (`import_dataset.ipynb`)
The first step in our project involves preparing our dataset for training. In `import_dataset.ipynb`, we:
- Mount Google Drive to access datasets stored in Google Drive.
- Import datasets from Roboflow and COCO. This step is crucial for gathering the diverse data needed for effective model training.

## 2. Setting up the Dataset (`setting_dataset.ipynb`)
Once the datasets are imported, `setting_dataset.ipynb` is used to prepare the data for training:
- Extract labels from the datasets.
- Merge datasets from different sources to increase the diversity and quantity of the training data.
- Check the class numbers to ensure all labels are within the expected range of values.
- Adjust class numbers if necessary to align with our model's expected input. This ensures consistency and prevents errors during model training.

## 3. Training the Model (`train_model.ipynb`)
With the dataset ready, `train_model.ipynb` focuses on the training process:
- Libraries necessary for training the object detection model are imported.
- The model is trained using the prepared dataset. This notebook captures the core of our project, utilizing Google Colab's computational resources to efficiently train our model.

## Execution Environment
All notebooks are designed to be run on Google Colab, leveraging its powerful GPUs and easy-to-use platform for machine learning projects. This choice ensures that anyone with access to Google Colab can reproduce our results without needing a powerful local setup.

## Getting Started
To get started with this project:
1. Clone this repository to your Google Drive.
2. Open each notebook in Google Colab and follow the instructions contained within.

## Prerequisites
- A Google Drive account with enough storage.
- Access to Google Colab.

## Acknowledgments
- Thanks to Roboflow and COCO for providing the datasets used in this project.
