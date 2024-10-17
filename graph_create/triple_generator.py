'''Goals for refactoring:

The generator should intiially create a triple, using the file number as subject,
for each relationship relating to that triple.

Ex: The subject is LLC_001 and it will automatically link the entity name and file number.

A triple will also be created for each entity that relates to the LLC,
e.g., members, managers, and registered agents.'''

from typing import Union, Optional
from pydantic import BaseModel, ConfigDict
from rdflib import Graph, Literal, URIRef, BNode
from rdflib.namespace import RDF
from rdflib.term import Node
from ontologies import Ontologies

class TripleElement(BaseModel):
    '''
    Creates a custom TripleElement datatype that can generate triples
    using RDFLib types
    '''
    model_config = ConfigDict(arbitrary_types_allowed=True) #Placeholder: Add more rigorous validation

    value: Union[str, int, float, bool, URIRef, Literal, BNode]
    datatype: Optional[URIRef] = None
    language: Optional[str] = None

    def to_rdf_term(self) -> Node:
        if isinstance(self.value, (URIRef, BNode)):
            return self.value
        return Literal(self.value, datatype=self.datatype, lang=self.language)

def add_triple(g: Graph, s: TripleElement, p: TripleElement, o: TripleElement) -> tuple:
    #Adds a triple to graph using TripleElement object
    g.add((
        s.to_rdf_term(),
        p.to_rdf_term(),
        o.to_rdf_term()
    ))

if __name__ == '__main__':
    g = Graph()

    ex_fn = Literal(10)
    ex_name = Literal('ABC, LLC')
    ex_subj = Ontologies.IL_LLCS[f'LLC_{str(ex_fn)}']

    llc_iri = TripleElement(value=Ontologies.get_llc_iri())
    entity_id = TripleElement(value=Ontologies.get_entity_id_iri())

    if llc_iri is None or entity_id is None:
        raise ValueError("LLC IRI or Entity ID is None")

    add_triple(g, ex_subj, RDF.type, llc_iri)
    add_triple(g, ex_subj, Ontologies.VCARD.name, ex_name)
    add_triple(g, ex_subj, entity_id, ex_fn)

    print(g.serialize())

'''def create_triples(g, file_number, name):
    ex_fn = Literal(file_number)
    ex_name = Literal(name)
    ex_subj = Ontologies.IL_LLCS[f'LLC_{str(ex_fn)}']

    llc_iri = Ontologies.get_llc_iri()
    entity_id = Ontologies.get_entity_id_iri()

    if llc_iri is None or entity_id is None:
        raise ValueError("LLC IRI or Entity ID is None")

    g.add((ex_subj, RDF.type, llc_iri))
    g.add((ex_subj, Ontologies.VCARD.name, ex_name))
    g.add((ex_subj, entity_id, ex_fn))

    return g'''