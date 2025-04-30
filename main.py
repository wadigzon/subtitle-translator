# main.py
from utils.srt_loader import load_subtitles, write_srt
from utils.lang_detector import detect_language
from utils.translator import get_translator, translate_lines
import time

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Translate subtitle (.srt) files using GPU.")
    parser.add_argument("--input", required=True, help="Path to input .srt file")
    parser.add_argument("--target-lang", required=True, help="Target language (e.g., 'es', 'fr', 'en')")
    parser.add_argument("--output", help="Path to save the translated .srt file (optional)")
    parser.add_argument("--batch-size", type=int, default=20, help="Batch size for translation (default: 20)")

    args = parser.parse_args()

    start_time = time.time()  # 🔽 START TIMER

    srt_path = args.input
    tgt_lang = args.target_lang
    output_path = args.output or srt_path.replace(".srt", f".translated.{tgt_lang}.srt")

    # Load and prepare
    subs = load_subtitles(srt_path)
    lines = [text for _, _, _, text in subs]

    # Detect source language
    src_lang = detect_language(lines)
    print(f"Detected source language: {src_lang}")

    # Translate
    tokenizer, model = get_translator(src_lang, tgt_lang)
    translated_lines = translate_lines(lines, tokenizer, model, batch_size=args.batch_size)

    # Save
    write_srt(subs, translated_lines, output_path)
    print(f"Translated subtitles saved to: {output_path}")

    elapsed_time = time.time() - start_time  # 🔼 END TIMER
    print(f"\n⏱️ Total time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()

# sample call:
# $ python main.py --input ./examples/sample.srt --target-lang es --output translated.es.srt
