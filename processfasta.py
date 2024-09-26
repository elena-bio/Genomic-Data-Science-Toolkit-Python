#!/usr/bin/python3

import sys
import getopt

def usage(): 
    print ("""
    processfasta.py : reads a FASTA file and builds a 
    dictionary with all sequences bigger than a given length
    processfasta.py [-h][-1 <length> ] <filename>
    -h              print this message
    -1 <length>     filter all sequences with a length smaller than <length>
                    (default <length>=0)
    <filename>      the file has to be in FASTA format
    """)

# Get command line arguments
o, a = getopt.getopt(sys.argv[1:], "1:h")
opts = {}
seqlen = 0

for k, v in o:
    opts[k] = v

# Check for help option
if "-h" in opts.keys():
    usage()
    sys.exit()

# Check if file is provided
if len(a) < 1:
    usage()
    sys.exit("input fasta file is missing")

# Check for the sequence length option
if "-1" in opts.keys():
    if int(opts["-1"]) < 0:
        print("Length of sequence should be positive!")
        sys.exit(0)
    seqlen = int(opts["-1"])

# Get the filename
filename = a[0]

# Try to open the file
try:
    f = open(filename, "r")
except IOError:
    print(f"File {filename} does not exist!")
    sys.exit(1)

# Process the FASTA file and filter sequences by length
sequences = {}
current_header = None
current_sequence = ""

# Reading the file line by line
for line in f:
    line = line.strip()
    if line.startswith(">"):  # Header line (starts a new sequence)
        # If there's an existing sequence, store it if it's long enough
        if current_header and len(current_sequence) >= seqlen:
            sequences[current_header] = current_sequence
        # Start a new sequence
        current_header = line[1:]  # Remove '>'
        current_sequence = ""
    else:
        current_sequence += line

# Don't forget to check the last sequence after file read completes
if current_header and len(current_sequence) >= seqlen:
    sequences[current_header] = current_sequence

# Output the filtered sequences
if sequences:
    for header, sequence in sequences.items():
        print(f">{header}\n{sequence}")
else:
    print("No sequences found that meet the length criteria.")

f.close()

    

   

