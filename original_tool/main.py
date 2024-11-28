"""
CLI Example how to use:
python main.py --Fasta ./data/selected.fasta --Model ./weights.DATA --Output ./prediction.txt

Auto create model:
python main.py --Fasta ./data/selected.fasta --Output ./prediction.txt
"""

import getopt, sys

from train_model import save_model, train_model, load_model
from load_seq_data import load_database_seq, load_fasta
from predict import model_predict, save_prediction

DATABASE_FILE_PATH = "./data/F_4_Uniprot_functionDATABASE.DAT"

argumentList = sys.argv[1:]
options = "hmo:" # Options
long_options = ["Model=", "Output=", "Fasta="] # Long options

# Values from CLI
model_file_path = ""
output_file_path = "./prediction.txt"
input_fasta_file_path = ""

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
    
    # checking each argument
    for current_argument, current_value in arguments:        
        if current_argument in ("--Model"):
            model_file_path = current_value
            print(current_value)

        elif current_argument in ("--Output"):
            output_file_path = current_value

        elif current_argument in ("--Fasta"):
            input_fasta_file_path = current_value

except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
    sys.exit(1)

if model_file_path == "":
    print("Creating model and saving to file: ./weights.DATA")
    database = load_database_seq(DATABASE_FILE_PATH)
    model = train_model(database)
    save_model(model)
else:
    print("Loading model from file: " + model_file_path)
    model = load_model(model_file_path)

print("Predicting functions for fasta file: " + input_fasta_file_path)
target_sequence = load_fasta(input_fasta_file_path)

print("Saving predictions to file: " + output_file_path)
for sequence in target_sequence:
    predicted_result = model_predict(sequence['seq'], model)
    save_prediction(sequence['name'], predicted_result[:1], output_file_path)


