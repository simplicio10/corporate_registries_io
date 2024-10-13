import polars as pl
from soli import SOLI
from rdflib import Graph, URIRef, Literal, BNode, Namespace
from rdflib.namespace import RDF

soli = SOLI()
il_llcs = Namespace("http://example.org/il_llcs/")

master = pl.read_csv('../data/samples/llc_mst_sample.csv')
names = pl.read_csv('../data/samples/llc_name_sample.csv').to_struct()
agents = pl.read_csv('../data/samples/llc_agt_sample.csv')

llc_class, score = soli.search_by_label("limited liability company")[0]

llc_iri = URIRef(llc_class.iri)

g = Graph()

ex_fn = names.struct.field('file_number')[0]
ex_name = names.struct.field('name')[0]

ex_subj = il_llcs[f'LLC_{str(ex_fn)}']

g.add((ex_subj, RDF.type, llc_iri))

print(g.serialize(format='turtle'))