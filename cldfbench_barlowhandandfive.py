import pathlib
import collections

from clldutils.misc import slug
from clldutils.markup import add_markdown_text
from cldfbench import Dataset as BaseDataset, CLDFSpec

NOTES = """

### Forms

Counterparts for 'five' and 'hand' in Austronesian languages have been collected from four datasets
described in the [ContributionTable](cldf/contributions.csv). Since forms were aggregated on language
level (with forms for dialects taken as forms for the parent language) and across datasets, often more
than one word per language and concept was attested.
If multiple forms were attested, one was chosen trying to "maximize potential for colexification".
I.e. the pair of forms picked for a language is the one closest to exhibiting (partial) 
colexification. The is done to minimize "false negatives": i.e., cases where there could appear to 
be *no* colexification of the two concepts, but only because there are, e.g., two synonyms for 
'hand' and the particular dataset chose the "wrong" one.


### Features

Based on the words for 'five' and 'hand' collected in the [FormTable](cldf/forms.csv) and inferred
replacement events (described below), six features have been coded, with values reported in the 
[ValueTable](cldf/values.csv). The distribution of values for these features can be investigated 
using [geographical maps](maps/README.md).


### Replacement events

Replacement events, i.e. rows in the [replacements table](cldf/replacements.csv), represent a probable loss of the 
inherited form ‘hand’ or ‘five’, whether in the individual history of a single language or in a protolanguage ancestral
to multiple languages, with Glottolog languoids (i.e. language subgroups or individual languages in Glottolog 5.0's 
classification of Austronesian) serving as proxies. While the replacements table lists name and Glottocode of this
languoid, the individual languages in our sample which fall into this subgroup are linked via the Glottocodes in the
`Language_IDs` column.

Looking up related data from different tables of the dataset is best done by exploiting the fact that 
[any CLDF dataset can be converted to a SQLite database](https://github.com/cldf/pycldf?tab=readme-ov-file#converting-a-cldf-dataset-to-an-sqlite-database).
The schema of this database here is described below. So if we wanted to see whether the language Lenkau appears in any
replacement events, we could run the following query:
```sql
sqlite> select distinct r.subgroup from languagetable as l, "replacements.csv_languagetable" as rl, "replacements.csv" as r where l.cldf_id == rl.languagetable_cldf_id and rl."replacemen
ts.csv_cldf_id" = r.cldf_id and l.cldf_name = 'Lenkau';
South-East Admiralty
```
and if we wanted to see which other languages are subsumed under "South-East Admiralty", we could run
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
exhibit the replacement of *qalima ‘hand’; however, their sister language (in Glottolog 5.0's classification) 
[Yabem](https://glottolog.org/resource/languoid/id/yabe1254) does not, so such a replacement cannot be reconstructed 
to the immediate ancestor of the three languages, [North Huon Gulf linkage](https://glottolog.org/resource/languoid/id/nort2858). 
However, even though they are not subgrouped together within North Huon Gulf linkage (which has a flat—i.e., 
ternary-branching—structure in Glottolog 5.0) excluding Yabem, the two languages may nevertheless have shared 
in the replacement of *qalima ‘hand’. This view is reflected the replacements table by assigning the same `Replacement_Group`
value `hand-43` to the two (conservative) replacement events:
```shell
$ csvgrep -c Replacement_Group -m"hand-43" cldf/replacements.csv | csvcut -c Subgroup,Comment
Subgroup,Comment
Bugawac,possibly shared change between Bugawac/Kela
Kela (Papua New Guinea),possibly shared change between Bugawac/Kela
```
"""
PARAMETERS = {
    (
        'five',
        "What is the word for 'five'?",
        ""
    ): {},
    (
        'hand',
        "What is the word for 'hand'?",
        ""
    ): {},
    (
        'colex',
        'Is_there_colexification?',
        ""
    ): {
        'lexically distinct': (
            'black', 'The concepts ‘hand’ and ‘five’ are lexically distinct in the language.'),
        'unknown': (
            'gray',
            'The relationship between ‘hand’ and ‘five’ is unknown in the language due to '
            'insufficient data.'),
        'full colexification': ('red', '‘hand’ and ‘five’ are fully colexified.'),
        'partial colexification': ('orange', '‘hand’ and ‘five’ are partially colexified.'),
    },
    (
        'dist',
        'Is_distinctness_due_to_lexical_replacement_or_phonological_change?',
        "For those languages that lack colexification, i.e. languages with value ‘lexically "
        "distinct’ for parameter ‘Is there colexification?’, values for this parameter are "
        "‘lexical replacement’ or ‘phonological change’. However, some languages exhibit both "
        "lexical replacement and (partial) colexification; this is possible when there has been "
        "replacement of both ‘hand’ and ‘five’ such that the new forms are (partially) colexified: "
        "these cases are indicated by rows in ValueTable with an empty value and a comment "
        "“(recolexification)”."
    ): {
        'lexical replacement': (
            'black',
            'The concepts ‘hand’ and ‘five’ are lexically distinct in the language due to '
            'lexical replacement.'),
        'phonological change': (
            'yellow', '‘hand’ and ‘five’ are distinct due to phonological change.'),
    },
    (
        'repl_hand',
        'Was_there_lexical_replacement_of_hand?',
        ""
    ): {
        'no': ('white', 'The word for the concept ‘hand’ has not been replaced.'),
        'yes': ('red', ' The word for the concept ‘hand’ has been replaced.'),
        'unknown': (
            'gray',
            'It is unknown whether or not the word for the concept ‘hand’ has been replaced.'),
    },
    (
        'repl_five',
        'Was_there_lexical_replacement_of_five?',
        ""
    ): {
        'no': ('white', 'The word for the concept ‘five’ has not been replaced.'),
        'yes': ('red', 'The word for the concept ‘five’ has been replaced.'),
        'unknown': (
            'gray',
            'It is unknown whether or not the word for the concept ‘five’ has been replaced.'),
    },
    (
        'hand_replacement',
        'What_replaced_hand?',
        "Values for this parameter are descriptions of the most likely etymology (traced as far "
        "back as possible in the Austronesian family) given for the word in the language that "
        "came to mean ‘hand’; values followed by ‘?’ are somewhat uncertain; and those followed "
        "by ‘??’ are even more uncertain; when no likely etymology has been posited, then the "
        "value is given simply as ‘unclear’ (with no preceding etymology). Values are batched into "
        "five different categories, referenced by the `Code_ID` column."
    ): {
        '“hand” word other than *qalima': (
            'black',
            '‘hand’ derives from a word meaning ‘hand’ or ‘arm’ other than *qalima, whether '
            '[PAn *kamay ‘hand’](https://acd.clld.org/cognatesets/26632), '
            '[PMP *baRa ‘hand, arm’](https://acd.clld.org/cognatesets/25155), or '
            'POc *minV- ‘hand’.'),
        'part of the arm': (
            'red',
            '‘hand’ derives from a word referring to part of the arm, whether '
            '[PAn *qabaRa ‘shoulder’](https://acd.clld.org/cognatesets/25155), '
            '[PAn *kuSkuS ‘claw, talon, fingernail’](https://acd.clld.org/cognatesets/30315), '
            'Proto-Tsouic *ramuCu ‘finger’ (?), '
            '[PMP *taŋan ‘finger, toe’](https://acd.clld.org/cognatesets/25155), '
            '[PMP *leŋen ‘forearm, lower arm’](https://acd.clld.org/cognatesets/30521), '
            '[PPh *dalukap ‘palm of the hand, sole of the foot’](https://acd.clld.org/cognatesets/34040), or '
            'PNCV *bisu ‘finger, toe, nail’'),
        'wing': (
            'yellow',
            '‘hand’ derives from a word referring to the wing (of an animal), whether '
            '[PAn *paNij ‘wing’](https://acd.clld.org/cognatesets/27294), '
            '[PMP *kapak ‘wings; flutter’](https://acd.clld.org/cognatesets/31811), or '
            'PWOc *baqe ‘wing, (?) hand’'),
        '‘hold onto’': ('blue', '‘hand’ derives from ‘hold onto, cling to’'),
        'unclear': (
            'gray', '‘hand’ derives from a form other than *qalima, but its etymology is unclear.'),
    },
    (
        'five_replacement',
        'What_replaced_five?',
        "The same conventions apply here as for the parameter “What replaced_hand?” except that "
        "here most entries are given a language-internal etymology. Values are batched into "
        "seven different categories, referenced by the `Code_ID` column."
    ): {
        '“hand” word other than *qalima': (
            'black',
            'The word for ‘five’ derives from a hand-related word unrelated to *qalima (in '
            'some cases ultimately derived from ‘finger’ or ‘wing’)'),
        'addition with 2': ('yellow', '‘five’ derives from a formulation like ‘2+2+1’.'),
        'tally word': (
            'red',
            '‘five’ derives from an expression apparently referring to a physical tallying '
            'practice, including words like ‘finished’, ‘on top’, or ‘make/take’.'),
        '‘count’': ('purple', '‘five’ derives from ‘count’.'),
        'addition with 4': ('orange', '‘five’ derives from a formulation like ‘4+1’.'),
        '‘part’': ('blue', '‘five’ derives from ‘part’.'),
        'unclear': (
            'gray', '‘five’ derives from a form other than *lima, but its etymology is unclear.'),
    },
}


CONTRIBUTIONS = {  # ID, Name, Citation
    #- the Austronesian basic vocabulary database (ABVD) (Greenhill, Blust, and Gray 2008),
    'abvd': (
        'The Austronesian basic vocabulary database',
        'Greenhill, Simon J., Robert Blust, and Russell D. Gray. 2008. The Austronesian basic vocabulary database: '
        'From bioinformatics to lexomics. Evolutionary Bioinformatics 4:271–83. doi: 10.4137/EBO.S893. '
        'https://abvd.eva.mpg.de. Data from: CLDF dataset derived from Greenhill et al.’s '
        '“Austronesian Basic Vocabulary Database” (v2020). https://github.com/lexibank/abvd.'),
    #- LexiRumah (Kaiping, Edwards, and Klamer 2019),
    'lexirumah': (
        'LexiRumah',
        'Kaiping, Gereon A., Owen Edwards, and Marian Klamer. 2019. LexiRumah 3.0.0. '
        'Leiden: Leiden University Centre for Linguistics. '
        'doi: 10.5281/zenodo.3537977. https://lexirumah.model-ling.eu.'
    ),
    #- Numeral systems of the world’s languages (Chan et al. 2019), and
    'chan2019': (
        'Numeral systems of the world’s languages',
        'Chan, Eugene, Hans-Jörg Bibiko, Christoph Rzymski, Simon J Greenhill, and Robert Forkel. 2019. '
        'channumerals (v1.0). doi: 10.5281/zenodo.3475912. Derived from Eugene Chan’s '
        '“Numeral systems of the world’s languages” (accessed 30 September 2019). '
        'https://lingweb.eva.mpg.de/channumerals.'
    ),
    #- Numerals of the Pacific (Barlow 2024).
    'barlowpacific': (
        'Numerals of the Pacific: A collection of numeral terms in Austronesian and Papuan languages',
        'Barlow, Russell. 2024. Numerals of the Pacific: '
        'A collection of numeral terms in Austronesian and Papuan languages (v1.6). '
        'doi: 10.5281/zenodo.13766733.'
    ),
}


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "barlowhandandfive"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return CLDFSpec(module='StructureDataset', dir=self.cldf_dir)

    def iterrows(self, name):
        for row in self.raw_dir.read_csv('{}.tsv'.format(name), delimiter='\t', dicts=True):
            yield {k: (v or '').strip() for k, v in row.items()}

    def cmd_readme(self, args):
        return add_markdown_text(
            BaseDataset.cmd_readme(self, args), NOTES, 'Description')

    def cmd_makecldf(self, args):
        args.writer.cldf.add_component(
            'FormTable',
            {
                'name': 'Contribution_ID',
                'dc:description': 'Key of lexical dataset from which the form was taken.',
                'propertyUrl': 'http://cldf.clld.org/v1.0/terms.rdf#contributionReference',
            },
            {
                'name': 'Glottocode_in_dataset',
                'dc:description':
                    'Glottocode assigned to the variety in the source dataset from which the form '
                    'was picked',
            },
            {
                'name': 'Language_name_in_dataset',
                'dc:description':
                    'Name of the variety in the source dataset from which the form was picked',
            },
        )
        args.writer.cldf.remove_columns('FormTable', 'Source')
        args.writer.cldf.remove_columns('ValueTable', 'Source')
        t = args.writer.cldf.add_component(
            'LanguageTable', {'name': 'Number', 'datatype': 'integer'})
        t.common_props['dc:description'] = \
            ('This table lists each language-level languoid in Glottolog 5.0 classified as '
             'Austronesian. Languages are roughly sorted by genealogy and then geography, more or '
             'less reflecting the spread of Austronesian languages from Taiwan to Polynesia. This '
             'sorting is reflected by the numbers given in the “Number” column.')
        t = args.writer.cldf.add_component('ContributionTable')
        t.common_props['dc:description'] = \
            ("Forms for this study, i.e. counterparts of 'five' and 'hand' in Austronesian languages, were taken from "
             "the four datasets listed in this table.")
        t = args.writer.cldf.add_component('ParameterTable')
        t.common_props['dc:description'] = \
            ("This dataset provides two kinds of parameters: 1) The two concepts 'hand' and 'five', with the "
             "corresponding counterparts listed in FormTable, and 2) six parameters analyzing the colexification "
             "status for these two concepts in Austronesian languages, with values listed in ValueTable.")
        args.writer.cldf.add_component('CodeTable', 'color')
        t = args.writer.cldf.add_table(
            'replacements.csv',
            {
                'name': 'ID',
                'propertyUrl': 'http://cldf.clld.org/v1.0/terms.rdf#id',
            },
            {
                'name': 'Replacement_Group',
                'dc:description':
                    "Replacement events can also be considered taking a more liberal approach: that is, replacement "
                    "events can, in some cases, be reconstructed to higher-order protolanguages or to multiple "
                    "protolanguages in an area, either when the apparent exceptions seem to be possibly due to "
                    "subsequent borrowing or when the “replacement event” could be viewed as a single areal spread "
                    "across multiple languages or language groups. The “conservative” replacement events listed here "
                    "are grouped into “liberal” events via matching values for the `Replacement_Group` column.\n"
                    "If there is no discrepancy between the more conservative and the more liberal approaches, an "
                    "event will be in a replacement group of its own.",
            },
            'Subgroup',
            'Comment',
            'Source',
            {
                'name': 'Concept',
                'propertyUrl': 'http://cldf.clld.org/v1.0/terms.rdf#parameterReference',
            },
            {
                'name': 'Language_IDs',
                'propertyUrl': 'http://cldf.clld.org/v1.0/terms.rdf#languageReference',
                'separator': ' ',
            }
        )
        t.common_props['dc:description'] = \
            ("This table lists coding decisions for “replacement events” for the words for 'hand' or 'five' in "
             "sub-groups or single languages of the Austronesian family.\n"
             "For concept 'hand', a row represents a probable loss of the inherited Proto-Austronesian form "
             "*qalima ‘hand’, whether in the individual history of a single language or in a protolanguage ancestral "
             "to multiple languages.\n"
             "For concept 'five', a row represents a probable loss of the inherited Proto-Austronesian *lima ‘five’.\n"
             "\n"
             "Replacement events are considered taking a relatively conservative approach: that is, a replacement "
             "event is reconstructed to a protolanguage only if there is strong evidence for it and no apparent "
             "exceptions (i.e., a reflex of *qalima ‘hand’ found in one or more member languages of the given group).")

        aust, lineages = {}, {}
        for lg in args.glottolog.api.languoids():
            if lg.lineage and lg.lineage[0][1] == 'aust1307':
                if lg.level == args.glottolog.api.languoid_levels.language:
                    lineages[lg.id] = {gc for _, gc, _ in lg.lineage}
                aust[lg.id] = lg
                if lg.id == 'amba1266':  # Amba (Solomon Islands)
                    aust['Amba'] = lg
                aust[lg.name] = lg

        what_replaced = {'hand': {}, 'five': {}}
        for row in self.raw_dir.read_csv('values.csv', dicts=True):
            if row['Parameter_ID'].startswith('Source_of_'):
                what_replaced[row['Parameter_ID'].partition('_of_')[-1][1:-1]][row['Language_ID']] = row['Value']

        forms = collections.defaultdict(lambda: collections.defaultdict(set))
        for row in self.iterrows('Forms_of_hand_and_five_in_Austronesian_languages'):
            if (not row['Glottocode']) and row['Language_level_glottocode']:
                row['Glottocode'] = row['Language_level_glottocode']
            if row['Glottocode']:
                assert row['Glottocode'] in aust, row['Glottocode']
                forms[row['Language_level_glottocode']][(row['Dataset'], row['Glottocode'], row['Language_name'])].add((row['Form'], row['Parameter_ID']))

        for cid, (name, citation) in CONTRIBUTIONS.items():
            args.writer.objects['ContributionTable'].append(
                dict(ID=cid, Name=name, Citation=citation))

        for (pid, pname, desc), codes in PARAMETERS.items():
            args.writer.objects['ParameterTable'].append(dict(ID=pid, Name=pname, Description=desc))
            for code, (color, desc) in codes.items():
                args.writer.objects['CodeTable'].append(dict(
                    ID='{}-{}'.format(pid, slug(code)),
                    Parameter_ID=pid,
                    Name=code,
                    Description=desc,
                    color=color,
                ))

        for row in self.iterrows('Colexification_of_hand_and_five_in_Austronesian_languages'):
            # Language_number	Glottocode	Language_name	Latitude	Longitude
            # hand	five -> forms
            row = {k: None if v == '_' else v for k, v in row.items()}
            args.writer.objects['LanguageTable'].append(dict(
                ID=row['Glottocode'],
                Glottocode=row['Glottocode'],
                Name=row['Language_name'],
                Latitude=aust[row['Glottocode']].latitude,
                Longitude=aust[row['Glottocode']].longitude,
                Number=int(row['Language_number']),
            ))

            for col in ['five', 'hand']:
                form = row[col]
                if form:
                    datasets = {}
                    for k, v in forms[row['Glottocode']].items():
                        if form in {f for f, c in v if c == col}:
                            datasets[k[0]] = (k[1], k[2])
                    assert row['Dataset_for_{}'.format(col)] in datasets
                    ds_gc, ds_name = datasets[row['Dataset_for_{}'.format(col)]]
                    args.writer.objects['FormTable'].append(dict(
                        ID='{}-{}'.format(row['Glottocode'], col),
                        Language_ID=row['Glottocode'],
                        Parameter_ID=col,
                        Value=row[col],
                        Form=row[col],
                        Contribution_ID=row['Dataset_for_' + col],
                        Glottocode_in_dataset=ds_gc,
                        Language_name_in_dataset=ds_name,
                    ))

            for (pid, pname, _), codes in PARAMETERS.items():
                if row.get(pname):
                    if row[pname] == '(recolexification)':
                        cid = None
                    elif pid.endswith('_replacement'):
                        cid = '{}-{}'.format(pid, slug(what_replaced[pid.split('_')[0]][row['Glottocode']]))
                    elif codes:
                        cid = '{}-{}'.format(pid, slug(row[pname]))
                    else:
                        cid = None

                    if pid.endswith('replacement') and row[pname] == '?':
                        row[pname] = 'unclear'
                    args.writer.objects['ValueTable'].append(dict(
                        ID='{}-{}'.format(pid, row['Glottocode']),
                        Language_ID=row['Glottocode'],
                        Parameter_ID=pid,
                        Value=None if row[pname] == '(recolexification)' else row[pname],
                        Code_ID=cid,
                        Comment=row[pname] if row[pname] == '(recolexification)' else None,
                    ))

            if row['hand'] and row['hand'] == row['five']:
                assert row['Is_there_colexification?'] == 'full colexification', row
            elif row['hand'] and row['five'] and (row['hand'] in row['five'] or row['five'] in row['hand']):
                if row['Is_there_colexification?'] not in {'full colexification', 'partial colexification'}:
                    assert (row['five'].startswith('lim')) and (row['hand'].startswith('im'))

        for concept in ['five', 'hand']:
            for row in self.iterrows('Replacements_of_{}_in_Austronesian'.format(concept)):
                gl = aust[row['Subgroup']]
                args.writer.objects['replacements.csv'].append(dict(
                    ID='{}-{}'.format(concept, row['Higher_count']),
                    Concept=concept,
                    Replacement_Group='{}-{}'.format(concept, row['Lower_count'][:-1]),
                    Subgroup=row['Subgroup'],
                    Comment=row['Comment'],
                    Source=row['Sources_of_‘{}’'.format(concept)],
                    Language_IDs=[k for k, v in lineages.items() if gl.id in v] if gl.id not in lineages else [gl.id],
                ))
