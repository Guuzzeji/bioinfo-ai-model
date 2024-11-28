
def load_go_probability():
    file_data = open("./data/IA.txt", "r", encoding="utf-8")
    go_prob = {}

    for line in file_data:
        data = line.strip().split("\t")
        go_prob[data[0]] = float(data[1])

    return go_prob