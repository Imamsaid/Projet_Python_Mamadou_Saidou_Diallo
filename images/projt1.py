import duckdb

conn = duckdb.connect(database=':memory:', read_only=False)
