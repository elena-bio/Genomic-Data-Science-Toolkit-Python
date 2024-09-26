## Retrieve Data from Dictionaries with Command Line Arguments

This script retrieves data from a FASTA file and builds a dictionary containing sequences that exceed a specified length. It is designed to be run from the command line, making it a useful tool for bioinformatics applications where FASTA data is prevalent.

## Features

- Reads a FASTA file.
- Filters sequences based on a specified minimum length.
- Supports command line arguments for easy usage.

## Usage

```bash
processfasta.py [-h] [-1 <length>] <filename>
```

### Arguments

- `-h`              Print the help message.
- `-1 <length>`     Filter out sequences with a length smaller than `<length>` (default `<length>=0`).
- `<filename>`      The FASTA file to be processed.
  

### Example

To retrieve sequences from a FASTA file named `myfile.txt`, use the following command:

```bash
processfasta.py -1 50 myfile.txt
```
### Requirements

- Python 3.x
- `sys` and `getopt` modules (both are included in the standard library)
