from rdflib import Graph, Literal, URIRef, BNode
from ontologies import Ontologies
from triple_generator import TripleElement

class LLC(TripleElement):
    file_number: URIRef
    name: URIRef

if __name__ == '__main__':
