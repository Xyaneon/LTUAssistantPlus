#!/usr/bin/python3

import stanfordnlp
from stanfordnlp.pipeline.doc import Sentence
from typing import List, Optional
from nlp.universal_dependencies import ParsedUniversalDependencies

stanfordnlp.download('en')   # This downloads the English models for the neural pipeline
nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English

def Parse(text: str) -> ParsedUniversalDependencies:
    """Parses the provided text."""
    sentences = __parse_sentences_from_text(text)
    return __parse_sentence(sentences[0])

def __get_word_by_ud_pos(sentence: Sentence, upos: str) -> Optional[str]:
    """Gets the requested word from the sentence as a string by its Universal
    Dependencies part-of-speech tag if present, or None if not found."""
    upos_upper = upos.upper()
    for token in sentence.tokens:
        for word in token.words:
            if word.upos.upper() == upos_upper:
                return word.text
    return None

def __parse_sentence(sentence: Sentence) -> ParsedUniversalDependencies:
    """Parses parts of speech from the provided Sentence."""
    sentence.print_tokens()
    adj = __get_word_by_ud_pos(sentence, "ADJ")
    adp = __get_word_by_ud_pos(sentence, "ADP")
    adv = __get_word_by_ud_pos(sentence, "ADV")
    aux = __get_word_by_ud_pos(sentence, "AUX")
    verb = __get_word_by_ud_pos(sentence, "VERB")
    cconj = __get_word_by_ud_pos(sentence, "CCONJ")
    det = __get_word_by_ud_pos(sentence, "DET")
    intj = __get_word_by_ud_pos(sentence, "INTJ")
    noun = __get_word_by_ud_pos(sentence, "NOUN")
    num = __get_word_by_ud_pos(sentence, "NUM")
    part = __get_word_by_ud_pos(sentence, "PART")
    pron = __get_word_by_ud_pos(sentence, "PRON")
    propn = __get_word_by_ud_pos(sentence, "PROPN")
    punct = __get_word_by_ud_pos(sentence, "PUNCT")
    sconj = __get_word_by_ud_pos(sentence, "SCONJ")
    sym = __get_word_by_ud_pos(sentence, "SYM")
    verb = __get_word_by_ud_pos(sentence, "VERB")
    x = __get_word_by_ud_pos(sentence, "X")
    return ParsedUniversalDependencies(
        adj = adj,
        adp = adp,
        adv = adv,
        aux = aux,
        cconj = cconj,
        det = det,
        intj = intj,
        noun = noun,
        num = num,
        part = part,
        pron = pron,
        propn = propn,
        punct = punct,
        sconj = sconj,
        sym = sym,
        verb = verb,
        x = x)

def __parse_sentences_from_text(text: str) -> List[Sentence]:
    """Parses sentences from the provided text."""
    doc = nlp(text)
    return doc.sentences

if __name__ == "__main__":
    parsing_results = Parse("This is a sample sentence.")
    print(parsing_results.__repr__())