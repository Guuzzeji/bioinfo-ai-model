from load_frag import FRAG_TABLE

def load_fasta(filename: str) -> dict:
    file_data = open(filename, "r", encoding="utf-8")
    fasta_data = []
    
    is_fasta_seq_data = False
    temp_seq_data = ""

    lines = file_data.readlines()
    for i, line in enumerate(lines):
        if (line.startswith(">") or i == len(lines) - 1) and is_fasta_seq_data:
            if line != "" and line != "\n" and (line.find(">") == -1):
                temp_seq_data += line.strip()

            fasta_data[-1]["seq"] = temp_seq_data
            fasta_data[-1]["seq_frag"] = parse_seq(temp_seq_data)
            temp_seq_data = ""
            is_fasta_seq_data = False

        if line.startswith(">"):
            fasta_seq = {}
            fasta_seq["name"] = line.strip().split(" ")[0].replace(">", "")
            fasta_data.append(fasta_seq)
            is_fasta_seq_data = True

        elif is_fasta_seq_data:
            temp_seq_data += line.strip()

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


