from collections import defaultdict


def read_fasta(file_path):
    sequences = []
    current_sequence = ""
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith(">"):
                if current_sequence:
                    sequences.append(current_sequence)
                current_sequence = ""
            else:
                current_sequence += line.strip()
    if current_sequence:
        sequences.append(current_sequence)
    return sequences


def create_profile_matrix(sequences):
    n = len(sequences[0])
    profile = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}

    for seq in sequences:
        for i, nucleotide in enumerate(seq):
            profile[nucleotide][i] += 1

    return profile


def get_consensus_string(profile):
    consensus = []
    n = len(profile['A'])
    for i in range(n):
        max_count = -1
        max_nucleotide = 'A'
        for nucleotide in ['A', 'C', 'G', 'T']:
            if profile[nucleotide][i] > max_count:
                max_count = profile[nucleotide][i]
                max_nucleotide = nucleotide
        consensus.append(max_nucleotide)
    return ''.join(consensus)


def main(input_file, output_file):
    sequences = read_fasta(input_file)
    profile = create_profile_matrix(sequences)
    consensus = get_consensus_string(profile)

    with open(output_file, 'w') as out_file:
        out_file.write(consensus + "\n")
        for nucleotide in ['A', 'C', 'G', 'T']:
            out_file.write(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}\n")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        main(input_file, output_file)