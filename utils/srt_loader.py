# utils/srt_loader.py
import pysrt

def load_subtitles(file_path):
    subs = pysrt.open(file_path)
    return [(sub.index, sub.start, sub.end, sub.text) for sub in subs]

def write_srt(indexed_subs, translated_lines, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for (idx, start, end, _), text in zip(indexed_subs, translated_lines):
            f.write(f"{idx}\n{start} --> {end}\n{text}\n\n")
