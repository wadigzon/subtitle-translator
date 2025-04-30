# utils/translator.py
from transformers import MarianMTModel, MarianTokenizer
import torch

def get_translator(src_lang, tgt_lang):
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name).to("cuda")
    return tokenizer, model

def translate_lines(lines, tokenizer, model, batch_size = 20):
    # legacy
    #batch = tokenizer.prepare_seq2seq_batch(lines, return_tensors="pt", padding=True).to("cuda")
    #translated = model.generate(**batch)
    # Use __call__ instead of deprecated method

    ## only works for small files (gives and out of memory)
    #model_inputs = tokenizer(lines, return_tensors="pt", padding=True, truncation=True).to("cuda")
    #translated = model.generate(**model_inputs)
    #return tokenizer.batch_decode(translated, skip_special_tokens=True)    
    all_translations = []
    for i in range(0, len(lines), batch_size):
        chunk = lines[i:i + batch_size]
        inputs = tokenizer(chunk, return_tensors="pt", padding=True, truncation=True).to("cuda")
        with torch.no_grad():  # Save memory
            outputs = model.generate(**inputs)
            translations = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        all_translations.extend(translations)
    return all_translations    