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

def FormatFastqObject(fo: fq.fastq_object) -> str:
    output_str = f"{fo.getHead()}\n{fo.getSeq()}\n+\n{fo.getQual()}\n"
    return output_str

def TrimRead(fo: fq.fastq_object, no_fiveprime: bool, quality_threshold: int, trunc_n: bool):
    head = fo.getHead()
    seq = fo.getSeq()
    qual = fo.getQual()
    length = len(fo)

    trim_start = -1
    trim_end = length

    window_size = 5

    if not no_fiveprime:
        for i in range(length):
            window_start, window_end = GetWindow(i, window_size, length)
            window = qual[window_start: window_end]

            average_quality = AverageQualityFromWindow(window)

            if average_quality > quality_threshold:
                trim_start = i
                break
            
    for i in range(length - 1, -1, -1):
        window_start, window_end = GetWindow(i, window_size, length)
        window = qual[window_start: window_end]

        average_quality = AverageQualityFromWindow(window)

        if average_quality > quality_threshold:
            trim_end= i
            break
    
    if trunc_n:
        for i in range(trim_start, trim_end):
            if seq[i] == 'N':
                trim_end = i
                break

    trimmed_fo = fq.fastq_object(head, seq[trim_start: trim_end], qual[trim_start: trim_end])
    return trimmed_fo

def GetWindow(i: int, size: int, length: int) -> tuple[int, int]:
    start = max(0, i - (size//2))
    end = min(length, i + (size//2) + 1)
    return (start, end)

def AverageQualityFromWindow(window: str) -> float:
    total_window_score = 0

    for c in window:
        total_window_score += GetScore(c)

    return total_window_score / len(window)