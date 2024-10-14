from rdflib import Literal
from rdflib.namespace import RDF
from ontologies import Ontologies

def create_triples(g, file_number, name):
    ex_fn = Literal(file_number)
    ex_name = Literal(name)
    ex_subj = Ontologies.IL_LLCS[f'LLC_{str(ex_fn)}']

    g.add((ex_subj, RDF.type, Ontologies.get_llc_iri()))
    g.add((ex_subj, Ontologies.VCARD.name, ex_name))
    g.add((ex_subj, Ontologies.get_entity_id_iri(), ex_fn))

    return g