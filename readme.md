# [Bioinformatics] AI-Assisted Protein Function Prediction using a Hybrid of DeepGO and a Custom Probability Model

> [!NOTE] 
> This codebase is bad, but I don't get enough sleep to care and it works, so idk.

Combining a multiple protein function prediction tools and a simple AI model to predict protein functions.

**Tools used:**
* DeepGO
* Custom made tool (Under `./original_tool`, a simple probability model)

**Notes**

You can download all the training data and other important data via this repository releases page. You will need this data to train and use the models.

There are two models that are found in the data folder once unzipped and place in the repository root folder.

* `model_10.pki` - Trained with 10 sequences found in the `train_sequences.fasta` file
* `model_100.pki` - Trained with 100 sequences found in the `train_sequences.fasta` file
* This models are small due to the time it takes to train them, about 2 hours for 100 sequences and about 45 minutes for 10 sequences.
* `Weights.DATA` - is used for the probability model (the custom tool created), this uses the `New_Balanced_FragDATABASE_34567_top2000.txt` file for training

All other files in the data folder are data used to train and test the models to see if it works

In the future we should convert this code to work via Tensorflow or PyTorch, so we can use GPU to train the models.

## Setup

1. Install Python3.12 (or higher) and pip
2. Open your terminal and clone this repo, then go to the project directory
3. Run `python3 -m venv venv`
4. Run `source venv/bin/activate` (on linux/mac) or `venv\Scripts\activate` (on windows)
5. Run `pip install -r requirements.txt`
6. Download `data.zip` folder from GitHub repository and save it to the project's root directory as `./data` folder

## Run / Usage

**Train model**

```bash
python train.py
```

**Run prediction**

```bash
python predict.py
```

make sure to have a `.fasta` file ready to be inputted when asked.

Feel free to open up these files and change them as you see fit, you can increase the training data from the default 100 to something higher and you can change the models you want to use in the `predict.py` file.

