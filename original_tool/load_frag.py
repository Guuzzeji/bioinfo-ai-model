def load_frag(filename: str) -> list[str]:
    file_data =  open(filename, "r", encoding="utf-8")
    frag_table = []

    for line in file_data:
        frag_table.append(line.strip())

    return frag_table