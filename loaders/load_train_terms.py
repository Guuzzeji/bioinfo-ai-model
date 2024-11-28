def load_train_terms():
    file_data =  open("./data/train_terms.tsv", "r", encoding="utf-8")
    go_table = []

    for line in file_data:
        chunk_data = line.strip().split("\t")

        if chunk_data[2] == "MFO":
            go_table.append({
                "EntryID": chunk_data[0],
                "term": chunk_data[1]
            })

    return go_table