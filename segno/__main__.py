import argparse
import sys
import os
import fastq as fq
from helper import *

version = "0.0.1"

def main():
    parser = argparse.ArgumentParser(
        prog="segno", 
        description="Commmand-line script to perform fastq read quality trimming"
    )

    # Input
    parser.add_argument("fastq", help="Single end fastq file")

    # Output
    parser.add_argument("-o", "--out", help="Write output to file. " \
		"Default: stdout", metavar="FILE", type=str, required=False)
    
    # Other options
    parser.add_argument("-q", "--quality-threshold", help="Threshold for trimming based" \
        "on average quality for a window. Default 20.", metavar="QUALITY_SCORE", type=int, \
        default=20, required=False)
    parser.add_argument("-l", "--length-threshold", help="Threshold to keep a read based" \
        "on length after trimming. Default 20.", metavar="READ_LENGTH", type=int, \
        default=20, required=False)
    parser.add_argument("-x", "--no-fiveprime", help="Don't do five-prime trimming.", \
        action='store_true')
    parser.add_argument("-n", "--trunc-n", help="Truncate read at first instance of N.", \
        action='store_true')
    parser.add_argument("--version", help="Print the version and quit.", \
        action='version', version = f"{version}")
    
    args = parser.parse_args()

    # Set up output file
    outfile = sys.stdout if args.out == None else open(args.out, 'w')

    # Load fastq file
    if not os.path.exists(args.fastq):
        ERROR(f"{args.fastq} does not exist")
    else: 
        f = open(args.fastq, 'r')

        header = f.readline().strip('\n')
        while header != "":
            seq = f.readline().strip('\n')
            spacer = f.readline().strip('\n')
            qual = f.readline().strip('\n')

            fo = fq.fastq_object(header, seq, qual)
            trimmed_fo = TrimRead(fo, args.no_fiveprime, args.quality_threshold, args.trunc_n)

            if len(trimmed_fo) > args.length_threshold:
                outfile.write(FormatFastqObject(trimmed_fo))

            header = f.readline().strip('\n')

    outfile.close()

if __name__ == "__main__":
    main()