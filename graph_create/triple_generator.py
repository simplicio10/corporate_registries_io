from rdflib import Literal
from rdflib.namespace import RDF
from ontologies import Ontologies

def create_triples(g, file_number, name):
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

    return g