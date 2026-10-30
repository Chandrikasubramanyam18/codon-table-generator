import sys

print("Welcome to Codon Table Generator")

sequence_type = input("Enter sequence type (DNA/RNA): ").upper()

if sequence_type != "DNA" and sequence_type != "RNA":
    print("Invalid sequence type.")
    sys.exit()

dna_sequence = input("Enter the sequence: ")
dna_sequence = dna_sequence.upper().replace(" ", "")

if dna_sequence == "":
    print("Sequence cannot be empty.")
    sys.exit()

if sequence_type == "RNA":
    dna_sequence = dna_sequence.replace("U", "T")

print("DNA sequence:", dna_sequence)

valid_bases = "ATGC"

for base in dna_sequence:
    if base not in valid_bases:
        print("Invalid DNA sequence. Please enter only A, T, G and C.")
        sys.exit()

codons = []
incomplete_codon = ""

for i in range(0, len(dna_sequence), 3):
    codon = dna_sequence[i:i+3]

    if len(codon) == 3:
        codons.append(codon)
    else:
        incomplete_codon = codon

if incomplete_codon:
    print("Incomplete codon:", incomplete_codon)

print("Codons:", codons)

codon_table = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",
    "TCT": "Serine", "TCC": "Serine",
    "TCA": "Serine", "TCG": "Serine",
    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",
    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",
    "CTT": "Leucine", "CTC": "Leucine",
    "CTA": "Leucine", "CTG": "Leucine",
    "CCT": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",
    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGT": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",
    "ATT": "Isoleucine", "ATC": "Isoleucine",
    "ATA": "Isoleucine", "ATG": "Methionine",
    "ACT": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",
    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "AGT": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",
    "GTT": "Valine", "GTC": "Valine",
    "GTA": "Valine", "GTG": "Valine",
    "GCT": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",
    "GAT": "Aspartic Acid", "GAC": "Aspartic Acid",
    "GAA": "Glutamic Acid", "GAG": "Glutamic Acid",
    "GGT": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}
amino_acids = []

for codon in codons:
    amino_acid = codon_table[codon]
    amino_acids.append(amino_acid)

print("Amino acids:", amino_acids)
print("\nTranslation Result")

for codon, amino_acid in zip(codons, amino_acids):
    print(codon, ":", amino_acid)

start_codons = []
stop_codons = ["TAA", "TAG", "TGA"]
found_stop_codons = []

for codon in codons:
    if codon == "ATG":
        start_codons.append(codon)

    if codon in stop_codons:
        found_stop_codons.append(codon)

print("Start codons:", start_codons)
print("Stop codons:", found_stop_codons)





