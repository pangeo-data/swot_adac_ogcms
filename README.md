# swot_adac_ogcms

[![DOI](https://zenodo.org/badge/382082673.svg)](https://zenodo.org/badge/latestdoi/382082673)

Documentation and notebooks for the SWOT Adopt-a-Crossover Model Intercomparison.

In order to access the data on the Open Storage Network (OSN) from any arbitrary environment, copy and paste the [catalog.yml](https://github.com/pangeo-data/swot_adac_ogcms/blob/main/catalog.yaml) and [validate_catalog.py](https://github.com/pangeo-data/swot_adac_ogcms/blob/main/validate_catalog.py) to your directory where you'd like to execute your analyses and then see any Jupyter notebook in this directory for examples.
The egress charges to access the data from OSN are free.

Intermediate results which were computationally intense to produce were saved on our Google Cloud scratch bucket, and are not publicly available.
For example, the [potential densities](https://github.com/pangeo-data/swot_adac_ogcms/blob/main/Potential-density.ipynb) for each simulation, which are called in the Filter notebooks to compute the mixed-layer depths, are computed from the outputs on OSN and saved as a intermediate results on our bucket.

