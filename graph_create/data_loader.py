import polars as pl

def load_data(): #Refactor - lazy frames and structs
    master = pl.scan_csv('../data/samples/llc_mst_sample.csv')
    names = pl.scan_csv('../data/samples/llc_name_sample.csv')
    agents = pl.scan_csv('../data/samples/llc_agt_sample.csv')



    return master, names, agents

def create_structs(lf: pl.LazyFrame):

    struct = lf.collect().select(pl.struct(pl.all()))

    return struct

if __name__ == "__main__":
    master, names, agents = load_data()
    print(create_structs(names))