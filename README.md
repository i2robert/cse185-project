# segno (CSE 185 project)

`segno` is a fastq read trimming tool similar to `sickle` or `scythe` that filters and trims FASTQ reads based on their quality scores.

# Dependencies

Usage requires the `fastq` and `miniFasta` libraries to be installed. You can install these with `pip`:

```
pip install fastq
pip install miniFasta
```

# Basic Usage

For now, the tool must be run as a python script. The basic usage of `segno` is:

```
python segno.py [options] input.fq
```

To run `segno` on the sample test example (using files in this repo):

```
python segno.py sample_fastq.fq
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

The only require input to the script is a FASTQ file. Users may use the options below:

* `-o FILE`, `--out FILE` : Write output to file. Default: `stdout`
* `-q QUALITY_SCORE`, `--quality-threshold QUALITY_SCORE`: Threshold for trimming basedon average quality for a window. Default 20.
* `-l READ_LENGTH`, `--length-threshold READ_LENGTH`: Threshold to keep a read basedon length after trimming. Default 20.
* `-x`, `--no-fiveprime`: Don't do five-prime trimming.
* `-n`, `--trunc-n`: Truncate read at first instance of N.

# File Format

The input file must be in FASTQ format. If the output file option is specified, then the output file will also be in FASTQ format.