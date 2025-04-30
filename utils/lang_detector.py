# utils/lang_detector.py
from langdetect import detect

def detect_language(text_lines):
    combined_text = ' '.join(text_lines[:10])
    return detect(combined_text)
