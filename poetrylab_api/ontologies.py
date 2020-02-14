import io
import uuid

from owlready2 import get_ontology
from rdflib import Graph


ONTOLOGY_URL_TEMPLATE = ("https://raw.githubusercontent.com/linhd-postdata/"
                         "{onto}-ontology/master/postdata-{onto}.owl")
ONTOLOGIES = {
    "core":       ONTOLOGY_URL_TEMPLATE.format(onto="core"),
    "structural": ONTOLOGY_URL_TEMPLATE.format(onto="structuralElements"),
    "prosodic":   ONTOLOGY_URL_TEMPLATE.format(onto="prosodicElements"),
    "literary":   ONTOLOGY_URL_TEMPLATE.format(onto="literaryAnalysis"),
}


def get_scansion_graph(scansion):
    structural_onto = get_ontology(ONTOLOGIES["structural"]).load()
    onto = add_structural_individuals(scansion, structural_onto)
    return onto_to_graph(onto)


def onto_to_graph(onto):
    with io.BytesIO() as file:
        onto.save(file=file, format="rdfxml", filter=filter_individuals)
        rdf = file.getvalue().decode("utf8")
        return Graph().parse(data=rdf)


def filter_individuals(graph, s, *args):
    # Let's just keep the individuals of the classes we are interested in
    classes = [graph.onto.Line, graph.onto.Word, graph.onto.Syllable]
    return s >= 0 and any(isinstance(graph.onto.world._get_by_storid(s), cls)
                          for cls in classes)


def add_structural_individuals(scansion, onto):
    for line in scansion:
        if "tokens" not in line:
            continue
        o_line = onto.Line(
            f"{onto.Line.name}/{uuid.uuid4()}",
            content=[join_tokens(line["tokens"])],
        )
        o_line.has_words = []
        for token in line["tokens"]:
            o_word = onto.Word(
                f"{onto.Word.name}/{uuid.uuid4()}",
                content=[join_syllables(token)],
                belongsToLine=[o_line],
            )
            o_word.has_syllables = []
            if "word" not in token:
                continue
            for syllable in token["word"]:
                o_syllable = onto.Syllable(
                    f"{onto.Syllable.name}/{uuid.uuid4()}",
                    content=[syllable["syllable"]],
                    belongsToWord=[o_word],
                )
                o_word.has_syllables += [o_syllable]
            o_line.has_words += [o_word]
    return onto


def join_tokens(tokens):
    output = []
    for token in tokens:
        item = join_syllables(token)
        output.append(item)
    return " ".join(output)


def join_syllables(token):
    if "symbol" in token:
        return token["symbol"]
    else:
        return "".join([syll["syllable"] for syll in token["word"]])
