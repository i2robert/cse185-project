# segno (CSE 185 project)

`segno` is a fastq read trimming tool similar to `sickle` or `scythe` that filters and trims FASTQ reads based on their quality scores.

# Dependencies

Usage requires the `fastq` and `miniFasta` libraries to be installed. You can install these with `pip`:

```
pip install fastq
pip install miniFasta
```

# Installation

In order to install `segno`, first make sure that the dependencies listed above have been installed. Once these libraries have been installed, `segno` can be installed with the command:

```
python setup.py install
```

Additionally, the tool can be installed locally if root access is unavailable:

```
python setup.py install --user
```

If the tool was installed correctly, then running `python segno --version` should print the current version of the tool.

# Basic Usage

Once the tool has been installed, it can be run as a python command from the command line. The basic usage of `segno` is:

```
python segno [options] input.fq
```

To run `segno` on the sample test example (using files in this repo):

```
python segno sample_fastq.fq
```

This should produce the output below:

```
@EAS20_8_6_1_2_768/1
CAGCACAGAGGATATCGCTGTTACAAAAA
+
HGHIHHHGHECHHHHHHHGGHHHHHHHHH
@EAS20_8_6_1_2_768/1
CAGCACAGAGGATATCGCTGTNAC
+
HGHIHHHGHECHHHHHHHGGHHHH
```

# segno Options

The only required input to the script is a FASTQ file. Users may use the options below:

* `-o FILE`, `--out FILE` : Write output to file. Default: `stdout`
* `-q QUALITY_SCORE`, `--quality-threshold QUALITY_SCORE`: Threshold for trimming basedon average quality for a window. Default 20.
* `-l READ_LENGTH`, `--length-threshold READ_LENGTH`: Threshold to keep a read basedon length after trimming. Default 20.
* `-x`, `--no-fiveprime`: Don't do five-prime trimming.
* `-n`, `--trunc-n`: Truncate read at first instance of N.

# File Format

The input file must be in FASTQ format. If the output file option is specified, then the output file will also be in FASTQ format.

# Contributions

This tool was developed by Isaac Roberts, based on the functionality of the tool `sickle`.

Code for the argument parser and the command line tool setup was heavily inspired by Melissa Gymrek's demo project: `https://github.com/gymreklab/cse185-demo-project/`.