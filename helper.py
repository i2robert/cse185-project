import sys
import fastq as fq

def GetScore(c: str) -> int:
    quality_score = ord(c) - 33
    return quality_score

def GetQuality(score: int) -> str:
    quality_char = chr(score) + 33
    return quality_char

def ERROR(message: str):
    sys.stderr.write("[ERROR]: " + message)
    sys.exit(1)

def FormatFastqObject(fo: fq.fastq_object):
    output_str = f"{fo.getHead()}\n{fo.getSeq()}\n+\n{fo.getQual()}\n"
    return output_str