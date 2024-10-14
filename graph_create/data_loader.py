import polars as pl

def load_data(): #Refactor - lazy frames and structs
    master = pl.read_csv('../data/samples/llc_mst_sample.csv')
    names = pl.read_csv('../data/samples/llc_name_sample.csv').to_struct()
    agents = pl.read_csv('../data/samples/llc_agt_sample.csv')

    return master, names, agents