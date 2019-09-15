#!/usr/bin/python3

import stanfordnlp
from stanfordnlp.pipeline.doc import Sentence
from typing import List, Optional

stanfordnlp.download('en')   # This downloads the English models for the neural pipeline
nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English

class SentenceParsingResults(object):
    """Represents the results of sentence parsing."""

    def __init__(self, verb: str = None, verb_object: str = None, noun2: str = None, verb2: str = None, preposition: str = None, adjective: str = None):
        self.verb = verb
        self.verb_object = verb_object
        self.noun2 = noun2
        self.verb2 = verb2
        self.preposition = preposition,
        self.adjective = adjective

def Parse(text: str) -> SentenceParsingResults:
    """Parses the provided text."""
    sentences = __parse_sentences_from_text(text)
    return __parse_sentence(sentences[0])

def __get_verb(sentence: Sentence) -> Optional[str]:
    """
    Returns the verb in the provided sentence as a string, or None if there is no verb.
    """
    sentence.print_tokens()
    for token in sentence.tokens:
        for word in token.words:
            if word.pos.startswith('V'):
                return word.text
    return None

def __parse_sentence(sentence: Sentence) -> SentenceParsingResults:
    """Parses parts of speech from the provided Sentence."""
    verb = verb_object = noun2 = verb2 = preposition = adjective = None
    verb = __get_verb(sentence)
    if verb:
        # TODO
    
    return SentenceParsingResults(verb, verb_object, noun2, verb2, preposition, adjective)

def __parse_sentences_from_text(text: str) -> List[Sentence]:
    """Parses sentences from the provided text."""
    doc = nlp(text)
    return doc.sentences

if __name__ == "__main__":
    Parse("This is a sample sentence.")