# main.py
from utils.srt_loader import load_subtitles, write_srt
from utils.lang_detector import detect_language
from utils.translator import get_translator, translate_lines
import time

def main():
    start_time = time.time()  # 🔽 START TIMER
    srt_path = "examples/sample.srt"
    output_path = "output/sample_translated.es.srt"

    # Load subtitles
    subs = load_subtitles(srt_path)
    lines = [text for _, _, _, text in subs]

    # Detect language
    src_lang = detect_language(lines)
    print(f"Detected language: {src_lang}")

    # Translate
    tokenizer, model = get_translator(src_lang, "es")
    translated_lines = translate_lines(lines, tokenizer, model)

    # Write translated subtitles
    write_srt(subs, translated_lines, output_path)
    print(f"Translated subtitles written to: {output_path}")
    elapsed_time = time.time() - start_time  # 🔼 END TIMER
    print(f"\n⏱️ Total time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
