# Bioinfo Final Project AI Proteins Prediction

Combining a multiple protein function prediction tools and a simple AI model to predict protein functions.

**Tools used:**
* DeepGO
* Custom made tool (Under `./original_tool`, a simple probability model)

>[!NOTE] This codebase is bad, but I don't get enough sleep to care and it works, so idk.

## Setup

1. Install Python3.12 (or higher) and pip
2. Open your terminal and go to this directory
3. Run `python3 -m venv venv`
4. Run `source venv/bin/activate` (on linux/mac) or `venv\Scripts\activate` (on windows)
5. Run `pip install -r requirements.txt`
6. Download data zip folder from repository

## Run

Train model

```bash
python train.py
```

Run prediction

```bash
python predict.py
```

make sure to have a .fasta file ready to be inputed when asked
