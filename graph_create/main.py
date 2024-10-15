from rdflib import Graph
from data_loader import load_data
from triple_generator import create_triples

def main():
    
    master, names, agents = load_data()

    g = Graph()

    ex_fn = names.struct.field('file_number')[0]
    ex_name = names.struct.field('name')[0]

    g = create_triples(g, ex_fn, ex_name)

    return g

if __name__ == "__main__":
    print(main().serialize())

''' master = pl.scan_csv('../data/samples/llc_mst_sample.csv')
    names = pl.scan_csv('../data/samples/llc_name_sample.csv')
    agents = pl.scan_csv('../data/samples/llc_agt_sample.csv')'''