import sys

sys.path.append('./loaders')
from load_seq_data import load_fasta
from load_go_probability import load_go_probability
from load_go_table import GO_TABLE

sys.path.append('./tooling')
from deepgo import deepgo_predict
from probability_model import probability_model

from sklearn import svm
from sklearn import datasets
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

def vector_to_goterm(vector: list[int]) -> (list, list):
    goterm_probs = load_go_probability()
    table = GO_TABLE
    goterms = []
    goterm_scores = {}

    for index, value in enumerate(table):
        if vector[index] == 1:
            goterms.append(table[index]["go_tag"])

    for terms in goterms:
        goterm_scores[terms] = goterm_probs[terms]

    return goterm_scores


# load
clf = joblib.load("./data/model_100.pkl")

path_to_fasta_input = input("Path to .fasta file: ")
target_sequence = load_fasta(path_to_fasta_input)

for sequence in target_sequence:
    deepgo_result = deepgo_predict(sequence['seq'])
    custom_result = probability_model(sequence["seq_frag"])
    label_deepgo = goterm_label_to_vector([x["goterm"] for x in deepgo_result[1:]])
    label_custom = goterm_label_to_vector([x[0] for x in custom_result[1:]])

    combine_vectors = label_deepgo + label_custom

    predict_result = clf.predict([[x[1] for x in combine_vectors]])
    to_goterm_predict = vector_to_goterm(predict_result[0])

    print(sequence['name'], to_goterm_predict)