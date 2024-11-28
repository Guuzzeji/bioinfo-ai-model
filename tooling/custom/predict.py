from decimal import Decimal, getcontext
from collections import defaultdict

from load_go_table import load_go_table

getcontext().prec = 50

GO_TABLE = load_go_table("./data/F_3_GO_table.DAT")

# Prediction function
def model_predict(sequence_words: list[str], model: dict) -> list[tuple[str, float]]:
    function_scores = defaultdict(float)
    
    # Calculate the score for each function word
    for func_word in set(f for func_dict in model.values() for f in func_dict):
        combined_probability = Decimal(1.0)
        
        # Multiply probabilities for each sequence word
        for seq_word in sequence_words:
            if seq_word in model and func_word in model[seq_word]:
                combined_probability *= Decimal(model[seq_word][func_word])
            else:
                combined_probability *= Decimal(1e-6)  # Small probability for unseen pairs
                
        function_scores[func_word] = combined_probability

    # Sort function words by their score in descending order
    sorted_functions = sorted(function_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Return the top function word(s) with highest probability
    return sorted_functions

def save_prediction(seq_name: str, data: list[tuple[str, float]], output_file: str) -> None:
    with open(output_file, 'a') as f:
        for func_word, probability in data:
            f.write(f"{seq_name},{func_word},{"".join([x["go_tag"] for x in GO_TABLE if func_word == x["seq"]])},{probability}\n")