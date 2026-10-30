# Codon Table Generator

## Introduction
This is a Python project that converts DNA and RNA sequences into their corresponding amino acids using the standard genetic code.

## Objectives
- Create a codon table using a Python dictionary.
- Accept DNA and RNA sequences from the user.
- Validate the input sequence.
- Divide the sequence into groups of three bases.
- Translate codons into amino acids.
- Identify start and stop codons.
- Handle incomplete codons.

## Features
1. Supports DNA and RNA sequences.
2. Converts lowercase input into uppercase.
3. Checks whether the input sequence is valid.
4. Splits sequences into codons.
5. Translates codons into amino acids.
6. Identifies start codon ATG.
7. Identifies stop codons TAA, TAG and TGA.
8. Displays the complete codon table.
9. Reports incomplete codons.

## Technologies Used
- Python 3
- Dictionaries
- Lists
- Loops
- Conditional statements
- String manipulation

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python3 main.py
```

5. Select DNA or RNA.
6. Enter your sequence.

## Sample Input

Sequence type: DNA

DNA sequence: ATGGCTTTTTAA

## Expected Output

Codons:
ATG, GCT, TTT, TAA

Amino acids:
Methionine, Alanine, Phenylalanine, Stop

Start codon: ATG

Stop codon: TAA

## Codon Table Reference

The project uses the standard genetic code.

Reference: NCBI Genetic Codes  
https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/taxonomy-processing/genetic-codes/

## Author
Python Assessment Project

## Comparison with an Existing GitHub Project

I compared my codon table with the Python project
[Genetic Codes by linsalrob](https://github.com/linsalrob/genetic_codes).

The reference project supports the NCBI standard genetic code
(translation table 1).

Both projects use the standard genetic code to translate codons.
My project displays the complete amino acid names, while the
reference project also supports one-letter and three-letter codes.

My project supports DNA and RNA input by converting RNA bases
(U) into DNA bases (T). The reference project can accept both
DNA and RNA codons directly.

The comparison shows that my codon table follows the standard
genetic code. The main difference is how the amino acids and
input sequences are represented.

Reference:
https://github.com/linsalrob/genetic_codes
