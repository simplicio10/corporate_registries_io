import polars as pl

master = pl.read_csv('../data/samples/llc_mst_sample.csv')
names = pl.read_csv('../data/samples/llc_name_sample.csv')
agents = pl.read_csv('../data/samples/llc_agt_sample.csv')

print(master)