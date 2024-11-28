def load_frag(filename: str) -> list[str]:
    file_data =  open(filename, "r", encoding="utf-8")
    frag_table = []

    for line in file_data:
        frag_table.append(line.strip())

    return frag_table

FRAG_TABLE = load_frag("./data/New_Balanced_FragDATABASE_34567_top2000.txt")
