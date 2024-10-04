<a name="ds-structuredatasetmetadatajson"> </a>

# StructureDataset CLDF dataset with data and supplements for Barlow 'Loss of colexification of ‘hand’ and ‘five’ in Austronesian languages'

**CLDF Metadata**: [StructureDataset-metadata.json](./StructureDataset-metadata.json)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF StructureDataset](http://cldf.clld.org/v1.0/terms.rdf#StructureDataset)
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/cldf-datasets/barlowhandandfive
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/cldf-datasets/barlowhandandfive/tree/13c236b">cldf-datasets/barlowhandandfive 13c236b</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v5.0">Glottolog v5.0</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.10.12</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | barlowhandandfive
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-valuescsv"></a>Table [values.csv](./values.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ValueTable](http://cldf.clld.org/v1.0/terms.rdf#ValueTable)
[dc:extent](http://purl.org/dc/terms/extent) | 4789


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [parameters.csv::ID](#table-parameterscsv)
[Value](http://cldf.clld.org/v1.0/terms.rdf#value) | `string` | 
[Code_ID](http://cldf.clld.org/v1.0/terms.rdf#codeReference) | `string` | References [codes.csv::ID](#table-codescsv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 

## <a name="table-formscsv"></a>Table [forms.csv](./forms.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF FormTable](http://cldf.clld.org/v1.0/terms.rdf#FormTable)
[dc:extent](http://purl.org/dc/terms/extent) | 2023


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | A reference to the language (or variety) to which the form belongs<br>References [languages.csv::ID](#table-languagescsv)
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | A reference to the meaning denoted by the form<br>References [parameters.csv::ID](#table-parameterscsv)
[Form](http://cldf.clld.org/v1.0/terms.rdf#form) | `string` | The written expression of the form. If possible, the transcription system used for the written form should be described in CLDF metadata (e.g., by adding a common property `dc:conformsTo` to the column description using concept URLs of the GOLD Ontology (such as [phonemicRep](http://linguistics-ontology.org/gold/2010/phonemicRep) or [phoneticRep](http://linguistics-ontology.org/gold/2010/phoneticRep)) as values).
[Segments](http://cldf.clld.org/v1.0/terms.rdf#segments) | list of `string` (separated by ` `) | 
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Contribution_ID](http://cldf.clld.org/v1.0/terms.rdf#contributionReference) | `string` | Key of lexical dataset from which the form was taken<br>References [contributions.csv::ID](#table-contributionscsv)
`Glottocode_in_dataset` | `string` | Glottocode assigned to the variety in the source dataset from which the form was selected
`Language_name_in_dataset` | `string` | Name of the variety in the source dataset from which the form was selected

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

This table lists each language-level languoid in Glottolog 5.0 classified as Austronesian. Languages are roughly sorted by genealogy and then geography, more or less reflecting the spread of Austronesian languages from Taiwan to Polynesia. This sorting is reflected by the numbers given in the “Number” column.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 1274


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal`<br>&ge; -90<br>&le; 90 | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal`<br>&ge; -180<br>&le; 180 | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string`<br>Regex: `[a-z0-9]{4}[1-9][0-9]{3}` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string`<br>Regex: `[a-z]{3}` | 
`Number` | `integer` | 

## <a name="table-contributionscsv"></a>Table [contributions.csv](./contributions.csv)

Forms for this study (i.e., words for the concepts 'five' and 'hand' in Austronesian languages) were taken from the four datasets listed in this table.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ContributionTable](http://cldf.clld.org/v1.0/terms.rdf#ContributionTable)
[dc:extent](http://purl.org/dc/terms/extent) | 4


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Contributor](http://cldf.clld.org/v1.0/terms.rdf#contributor) | `string` | 
[Citation](http://cldf.clld.org/v1.0/terms.rdf#citation) | `string` | 

## <a name="table-parameterscsv"></a>Table [parameters.csv](./parameters.csv)

This dataset provides two kinds of parameters: 1) The two concepts 'hand' and 'five', with the corresponding forms listed in FormTable, and 2) six parameters analyzing the colexification status for these two concepts in Austronesian languages, with values listed in ValueTable.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable)
[dc:extent](http://purl.org/dc/terms/extent) | 8


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[ColumnSpec](http://cldf.clld.org/v1.0/terms.rdf#columnSpec) | `json` | 

## <a name="table-codescsv"></a>Table [codes.csv](./codes.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF CodeTable](http://cldf.clld.org/v1.0/terms.rdf#CodeTable)
[dc:extent](http://purl.org/dc/terms/extent) | 24


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | The parameter or variable to which the code belongs<br>References [parameters.csv::ID](#table-parameterscsv)
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
`color` | `string` | 

## <a name="table-replacementscsv"></a>Table [replacements.csv](./replacements.csv)

This table lists coding decisions for “replacement events” for the words for 'hand' or 'five' in subgroups or single languages of the Austronesian family.
For the concept 'hand', a row represents a probable loss of the inherited Proto-Austronesian form *qalima ‘hand’, whether in the individual history of a single language or in a protolanguage ancestral to multiple languages.
For the concept 'five', a row represents a probable loss of the inherited Proto-Austronesian form *lima ‘five’.

Replacement events are considered taking a relatively conservative approach—that is, a replacement event is reconstructed to a protolanguage only if there is strong evidence for it and no apparent exceptions (such as a reflex of *qalima ‘hand’ found in one or more member languages of the given group).

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 189


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
`Replacement_Group` | `string` | Replacement events can also be considered taking a more liberal approach—that is, replacement events can, in some cases, be reconstructed to higher-order protolanguages or to multiple protolanguages in an area, either when the apparent exceptions seem to be possibly due to subsequent borrowing or when the “replacement event” could be viewed as a single areal spread across multiple languages or language groups. The “conservative” replacement events listed here are grouped into “liberal” events via matching values for the `Replacement_Group` column. If there is no discrepancy between the more conservative and the more liberal approaches, an event will be in a replacement group of its own.
`Subgroup` | `string` | 
`Comment` | `string` | 
`Source` | `string` | 
[Concept](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [parameters.csv::ID](#table-parameterscsv)
[Language_IDs](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | list of `string` (separated by ` `) | References [languages.csv::ID](#table-languagescsv)

