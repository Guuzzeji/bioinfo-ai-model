import sys

sys.path.append('./loaders')
from load_go_table import load_go_table
from load_seq_data import load_fasta
from load_go_probability import load_go_probability
from load_go_table import GO_TABLE
from load_train_terms import load_train_terms

sys.path.append('./tooling')
from deepgo import deepgo_predict
from probability_model import probability_model

from sklearn.neural_network import MLPClassifier
import joblib

def goterm_label_to_vector(goterms: list[str]) -> (list, list):
    table = GO_TABLE
    vector = []

    for index, value in enumerate(table):
        if table[index]["go_tag"] in goterms:
            vector.append((table[index]["go_tag"], 1))
        else:
            vector.append((table[index]["go_tag"], 0))

    return vector

print("Loading training data...")
training_data = load_fasta("./data/train_sequences.fasta")[:100]
train_go_terms = load_train_terms()
print(f"{len(training_data)} training data loaded.")

print("Gather GO terms...")
data_set = []
for i, sequence in enumerate(training_data):
    print(f"Processing {sequence['name']} ({i+1}/{len(training_data)})")
    deepgo_result = deepgo_predict(sequence['seq'])
    custom_result = probability_model(sequence["seq_frag"])

    label_deepgo = goterm_label_to_vector([x["goterm"] for x in deepgo_result[1:]])
    label_custom = goterm_label_to_vector([x[0] for x in custom_result[1:]])

    combine_vectors = label_deepgo + label_custom
    label_output_data = goterm_label_to_vector([x["term"] for x in train_go_terms if x["EntryID"] == sequence["name"]])

    data_set.append({
        "input": combine_vectors,
        "output": label_output_data,
    })

print("Creating training model...")
input_data = [[x[1] for x in y["input"]] for y in data_set]
output_data = [[x[1] for x in y["output"]] for y in data_set]

print("Training model...")
clf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(100,), max_iter=50000)
clf.fit(input_data, output_data)

print("Saving model...")
joblib.dump(clf, "model.pkl") 

