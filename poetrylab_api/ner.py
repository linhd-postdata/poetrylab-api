#!/usr/bin/python
import spacy

from spacy.tokens import Doc


def get_ner(poem):
    """
    Perform spacy's named entities recognition function to a poem.
    :param poem: String with the text of the poem
    :return: A list of detected named entities dicts
    """
    if isinstance(poem, Doc):
        doc = poem
    else:
        nlp = spacy.load('es_core_news_md')
        doc = nlp(poem)
    entities = [{"start": entity.start_char, "end": entity.end_char,
                 "text": entity.text,
                 "label": entity.label_, "desc": spacy.explain(entity.label_)}
                for entity in doc.ents if entity.label_ != "MISC"]
    return entities
