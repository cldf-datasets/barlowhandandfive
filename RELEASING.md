# Releasing

Install required packages:
```shell
pip install -e .
```

Recreate the CLDF dataset:
```shell
cldfbench makecldf cldfbench_barlowhandandfive.py --glottolog-version v5.0
```

Run the consistency checks on the dataset:
```shell
pytest
```

Create the metadata for Zenodo:
```shell
cldfbench zenodo cldfbench_barlowhandandfive.py
```

```shell
cldfbench cldfreadme cldfbench_barlowhandandfive.py 
```

```shell
cldferd --format compact.svg cldf > erd.svg
```

```shell
cldfbench readme cldfbench_barlowhandandfive.py 
```

Recreate the maps:
```shell
cldfbench barlowhandandfive.maps
```
