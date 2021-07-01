import intake
cat = intake.open_catalog('catalog.yaml')
for item in cat:
    print(item)
    ds = cat[item].to_dask()
    print(ds)