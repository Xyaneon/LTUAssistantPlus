#!/usr/bin/python3

import stanfordnlp
from stanfordnlp.pipeline.doc import Sentence
from typing import List

stanfordnlp.download('en')   # This downloads the English models for the neural pipeline
nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English

def Parse(text):
    """Parses the provided text."""
    sentences = __parse_sentences_from_text(text)
    verb = noun = new_noun = new_verb = prep = adjective = None
    for sentence in sentences:
        print(sentence)
        verb = __get_verb(sentence)
        if verb:
            #print("Verb found: " + verb)
            print(__get_words(sentence, verb))

            # Support some fancier sentences.
            new_verb = __confirm_verb(sentence, verb)
            if new_verb:
                verb = new_verb
                print("Changing verb to %s" % __get_words(sentence, verb))
            
            copula = __get_copula(sentence, verb)

            noun = __get_subject(sentence, copula or verb)
            if noun:
                print(__get_words(sentence, noun))
                adjective = __get_adjective(sentence, noun)
            else:
                print("Could not find the subject")
            
            new_noun, new_verb, prep = __get_extra(sentence, copula or verb)
            if new_noun:
                print("New Noun: " + __get_words(sentence, new_noun))
            if new_verb:
                print("New Verb: " + __get_words(sentence, new_verb))
            if prep:
                print("Prep: " + __get_words(sentence, prep))
            
            # Probably contains useful info.
            if copula and not new_noun and not new_verb and not prep:
                new_noun = copula
        else:
            print("Could not find any verbs")
        
        # Just return the first sentence only for now.
        print("\n")
        
        final_verb = __get_words(sentence, verb)
        return final_verb, __get_words(sentence, noun), __get_words(sentence, new_noun), __get_words(sentence, new_verb), __get_words(sentence, prep), __get_words(sentence, adjective)

def __confirm_verb(sentence: Sentence, verb):
    """
    Support sentences such as "Tell me where room S202 is".
    Previously would find "Tell" as verb and "me" as subject, and not see
    anything else at all. The tell me isn't relevant here though.
    Searches for a ccomp to hopefully find the real verb.
    """
    new_verb = __find_dependency(sentence, verb, "ccomp")
    if new_verb and new_verb.pos.startswith('V'):
        return new_verb
    return None

def __find_dependency(sentence: Sentence, pos, dep_type, reverse = False):
    """
    Searches the dependencies of the parsed sentence to find relationships
    between words.
    The positions of the words that the relationship is on is passed in,
    and it then searches for any dependencies of the type we want on those
    words.
    """
    for dependency in sentence.dependencies:
        if dependency[0] == dep_type:
            to_check = pos if reverse else dependency[1:]
            if to_check[0] in range(pos[0, pos[1]]):
                return (to_check[1], to_check[1] + 1)

def __get_adjective(sentence: Sentence, noun_pos):
    """Gets the adjective."""
    return __find_dependency(sentence, noun_pos, "amod")

def __get_copula(sentence: Sentence, verb_pos):
    """Gets the copula (for example, in "My name is Jacob", "Jacob" is the copula)."""
    return __find_dependency(sentence, verb_pos, "cop", reverse=True)

def __get_verb(sentence: Sentence) -> str:
    """
    Looks for the first word in the sentence with a part of speech starting in "V".
    Returns that verb, and also the word before that if it is an adverb / determiner.
    """
    sentence.print_tokens()
    for token in sentence.tokens:
        print("Token index: " + token.index)
        for word in token.words:
            print("Word: " + word.__repr__())
            if word.pos.startswith('V'):
                return word.text
    return None

def __get_words(sentence: Sentence, wordPositions) -> str:
    """Helper function to get/parse something found."""
    if not wordPositions:
        return ""
    return " ".join(sentence.tokens[wordPositions[0]:wordPositions[1]])

def __parse_sentences_from_text(text: str) -> List[Sentence]:
    """Parses sentences from the provided text."""
    doc = nlp(text)
    return doc.sentences

if __name__ == "__main__":
    Parse("This is a sample sentence.")