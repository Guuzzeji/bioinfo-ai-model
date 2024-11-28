def load_go_table(filename: str) -> list[dict]:
    file_data =  open(filename, "r", encoding="utf-8")
    go_table = []

    for line in file_data:
        # Store go label and sequence label
        chunk_data = line.strip().split("\t")
        go_table.append({
            "go_tag": chunk_data[0],
            "seq": chunk_data[1]
        })

    return go_table


GO_TABLE = load_go_table("./../data/F_3_GO_table.DAT")
