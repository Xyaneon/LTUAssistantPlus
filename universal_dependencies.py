#!/usr/bin/python3

class ParsedUniversalDependencies(object):
    """Represents the parsed Universal Dependencies information from a sentence.

    For more infomration on Universal Dependencies parts-of-speech (POS) tags, see
    https://universaldependencies.org/u/pos/index.html .
    """

    def __init__(self,
        adj: str = None,
        adp: str = None,
        adv: str = None,
        aux: str = None,
        cconj: str = None,
        det: str = None,
        intj: str = None,
        noun: str = None,
        num: str = None,
        part: str = None,
        pron: str = None,
        propn: str = None,
        punct: str = None,
        sconj: str = None,
        sym: str = None,
        verb: str = None,
        x: str = None):
        """Initializes a new instance of the ParsedUniversalDependencies class."""
        self.adj = adj
        """The ADJ (adjective) tag associated with the parsed sentence."""
        self.adp = adp
        """The ADP (adposition) tag associated with the parsed sentence."""
        self.adv = adv
        """The ADV (adverb) tag associated with the parsed sentence."""
        self.aux = aux
        """The AUX (auxiliary) tag associated with the parsed sentence."""
        self.cconj = cconj
        """The CCONJ (coordinating conjunction) tag associated with the parsed sentence."""
        self.det = det
        """The DET (determiner) tag associated with the parsed sentence."""
        self.intj = intj
        """The INTJ (interjection) tag associated with the parsed sentence."""
        self.noun = noun
        """The NOUN (noun) tag associated with the parsed sentence."""
        self.num = num
        """The NUM (numeral) tag associated with the parsed sentence."""
        self.part = part
        """The PART (particle) tag associated with the parsed sentence."""
        self.pron = pron
        """The PRON (pronoun) tag associated with the parsed sentence."""
        self.propn = propn
        """The PROPN (proper noun) tag associated with the parsed sentence."""
        self.punct = punct
        """The PUNCT (punctuation) tag associated with the parsed sentence."""
        self.sconj = sconj
        """The SCONJ (subordinating conjunction) tag associated with the parsed sentence."""
        self.sym = sym
        """The SYM (symbol) tag associated with the parsed sentence."""
        self.verb = verb
        """The VERB (verb) tag associated with the parsed sentence."""
        self.x = x
        """The X (other) tag associated with the parsed sentence."""
    
    def __repr__(self) -> str:
        """Returns a string representation of this object."""
        attributes = ["adj", "adp", "adv", "aux", "cconj", "det", "intj", "noun", "num", "part", "pron", "propn", "punct", "sconj", "sym", "verb", "x"]
        attributes_str = ";".join(["{}={}".format(attribute, getattr(self, attribute)) for attribute in attributes if getattr(self, attribute) is not None])
        return f"<{self.__class__.__name__} {attributes_str}>"