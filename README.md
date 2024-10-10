# CLDF dataset with data and supplements for Barlow “Loss of colexification of ‘hand’ and ‘five’ in Austronesian languages”

[![CLDF validation](https://github.com/cldf-datasets/barlowhandandfive/workflows/CLDF-validation/badge.svg)](https://github.com/cldf-datasets/barlowhandandfive/actions?query=workflow%3ACLDF-validation)

## How to cite

If you use these data please cite
this dataset using the DOI of the [particular released version](../../releases/) you were using

## Description


This dataset is licensed under a CC-BY-4.0 license




### Forms

Words for the concepts ‘five’ and ‘hand’ in Austronesian languages have been collected from four datasets,
described in the [ContributionTable](cldf/contributions.csv). Since some entries in these datasets contain multiple forms for a single concept, and since forms were aggregated at the language
level (with forms for dialects taken as forms for the parent language) and across datasets, often more
than one form per concept in a given language was attested.
If multiple forms were attested, one was chosen so as to maximize the potential for finding colexification.
In other words, the pair of forms selected for a language is the one closest to exhibiting full 
colexification (or, failing that, partial colexification). The decision was made so as to minimize 
“false negatives” (i.e., cases where there could appear to be *no* colexification of the two concepts, 
but only because there are, e.g., two synonyms for ‘hand’ in a given language and the particular dataset chose the “wrong” one).


### Features

Based on the words for ‘five’ and ‘hand’ collected in the [FormTable](cldf/forms.csv), six features have been coded, with values reported in the 
[ValueTable](cldf/values.csv). A seventh feature details the types of numeral systems found in the languages in this dataset; it derives from Barlow (2023) “Papuan-Austronesian contact and the spread of numeral systems in Melanesia”, updated to reflect the changes in classifications between Glottolog versions 4.7 and 5.0. The distribution of values for these features can be investigated 
using [geographical maps](maps/README.md).


### Replacement events

Replacement events (i.e., rows in the [replacements table](cldf/replacements.csv)) represent a probable loss of the 
inherited form for ‘hand’ or ‘five’, whether in the individual history of a single language or in a protolanguage ancestral
to multiple languages, with Glottolog languoids (i.e., language subgroups or individual languages in the Glottolog 5.0 
classification of the Austronesian family) serving as proxies. While the replacements table lists the name and Glottocode of this
languoid, the individual languages in our sample that fall within this designation are linked via the Glottocodes in the
`Language_IDs` column.

Looking up related data from different tables of the dataset is best done by exploiting the fact that 
[any CLDF dataset can be converted to a SQLite database](https://github.com/cldf/pycldf?tab=readme-ov-file#converting-a-cldf-dataset-to-an-sqlite-database).
The schema of this database here is described below. If, for example, we wanted to see whether the language 
[Lenkau](https://glottolog.org/resource/languoid/id/lenk1247) appears in any
replacement events, we could run the following query:
```sql
sqlite> select distinct r.subgroup from languagetable as l, "replacements.csv_languagetable" as rl, "replacements.csv" as r where l.cldf_id == rl.languagetable_cldf_id and rl."replacemen
ts.csv_cldf_id" = r.cldf_id and l.cldf_name = 'Lenkau';
South-East Admiralty
```
and if we wanted to see which other languages are subsumed under “South-East Admiralty”, we could run
```
sqlite> select distinct l.cldf_name from languagetable as l, "replacements.csv_languagetable" as rl, "replacements.csv" as r where l.cldf_id == rl.languagetable_cldf_id and rl."replacements.csv_cldf_id" = r.cldf_id and r.subgroup = 'South-East Admiralty';
Lenkau
Nauna
Penchal
Lou
Paluai
```

As explained in the [cldf/README](cldf/README.md), replacement events can be reconstructed using a more conservative or
a more liberal approach. As an example of a discrepancy between the two approaches, consider the replacement of
*qalima ‘hand’ for [Bugawac](https://glottolog.org/resource/languoid/id/buga1250) and 
[Kela (Papua New Guinea)](https://glottolog.org/resource/languoid/id/kela1255). In this case, both Bugawac and Kela
exhibit the replacement of *qalima ‘hand’; however, their sister language (in the Glottolog 5.0 classification) 
[Yabem](https://glottolog.org/resource/languoid/id/yabe1254) does not, so such a replacement cannot be reconstructed 
to the immediate ancestor of the three languages, [North Huon Gulf linkage](https://glottolog.org/resource/languoid/id/nort2858). 
However, even though they are not subgrouped together within North Huon Gulf linkage (which has a flat—i.e., 
ternary-branching—structure in Glottolog 5.0) excluding Yabem, the two languages may nevertheless have shared 
in the replacement of *qalima ‘hand’. This view is reflected in the replacements table by assigning the same `Replacement_Group`
value `hand-43` to the two (conservative) replacement events:
```shell
$ csvgrep -c Replacement_Group -m"hand-43" cldf/replacements.csv | csvcut -c Subgroup,Comment
Subgroup,Comment
Bugawac,possibly shared change between Bugawac/Kela
Kela (Papua New Guinea),possibly shared change between Bugawac/Kela
```


## CLDF Datasets

The following CLDF datasets are available in [cldf](cldf):

- CLDF [StructureDataset](https://github.com/cldf/cldf/tree/master/modules/StructureDataset) at [cldf/StructureDataset-metadata.json](cldf/StructureDataset-metadata.json)
