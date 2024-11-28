import json
from decimal import Decimal 
from collections import defaultdict

def train_model(data: list[dict]) -> dict:
    sequence_count = defaultdict(int)
    joint_count = defaultdict(lambda: defaultdict(int))

    for seq_data in data:
        # Count each sequence word
        for seq_word in set(seq_data['seq']):
            sequence_count[seq_word] += 1
            
            for func_word in set(seq_data['go_tag']):
                joint_count[seq_word][func_word] += 1

    # Step 3: Calculate probabilities
    probabilities = {}
    for seq_word, func_dict in joint_count.items():
        probabilities[seq_word] = {}
        for func_word, joint_freq in func_dict.items():
            probabilities[seq_word][func_word] = joint_freq / sequence_count[seq_word]

    return probabilities

def save_model(model: dict) -> None:
    with open("./weights.DATA", 'w') as f:
        json.dump(model, f)

def load_model(file_path: str) -> dict:
    with open(file_path, 'r') as f:
        return json.load(f)