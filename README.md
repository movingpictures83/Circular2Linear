# Circular2Linear
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: FASTA
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that takes a circular DNA sequence and linearizes it.

The plugin accepts as input a TXT file of tab-delimited keyword-value pairs.

Keywords:
fasta: Input sequence (FASTA format)
start: Position of starting nucleotide

Plugin outputs a FASTA file, of the same sequence beginning with "start", and wrapped around into a linear structure.

