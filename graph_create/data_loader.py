'''This code takes structured data in csv or parquet format,
and returns a struct.'''

#Note for refactoring/code development: Enforce data types!

import polars as pl

def load_multiple_data(files: list[str]) -> tuple[pl.struct, ...]:
    return tuple(load_data(file) for file in files)

def load_data(file): 
    lf = create_lf(file)
    struct = create_struct(lf)

    return struct

def create_lf(file):
    lf = pl.scan_csv(file)

    return lf

def create_struct(lf: pl.LazyFrame):

    struct = lf.collect().select(pl.struct(pl.all()))

    return struct

if __name__ == "__main__":
    files = [
        '../data/samples/llc_mst_sample.csv',
        '../data/samples/llc_name_sample.csv',
        '../data/samples/llc_agt_sample.csv'
    ]
    structs = load_multiple_data(files)
    print(structs)