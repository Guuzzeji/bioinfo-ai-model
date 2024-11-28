from load_frag import load_frag

FRAG_TABLE = load_frag("./data/New_Balanced_FragDATABASE_34567_top2000.txt")


def load_database_seq(filename: str) -> list[dict]:
    file_data = open(filename, "r", encoding="utf-8")
    seq_data = []

    for line in file_data:
        line = line.strip().split("|")

        seq_data.append({
            "seq": parse_seq(line[0]),
            "go_tag": line[1].split(" "),
        })

    return seq_data


def load_fasta(filename: str) -> dict:
    file_data = open(filename, "r", encoding="utf-8")
    fasta_data = []

    for line in file_data:
        if line.startswith(">"):
            fasta_seq = {}
            fasta_seq["name"] = line.strip().replace(">", "")
            fasta_data.append(fasta_seq)
        else:
            fasta_data[-1]["seq"] = parse_seq(line)

    return fasta_data

def parse_seq(seq: str) -> list[str]:
    frag_list_from_seq = []
    seq = seq[1:]

    i = 0
    while True:
        if i >= len(seq):
            break

        frag = seq[i:i+3]
        if frag in FRAG_TABLE:
            frag_list_from_seq.append(frag)
            seq = seq[i + len(frag):]
            i = 0
        else:
            i += 1

    return frag_list_from_seq

