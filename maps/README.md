# Maps

The maps below have been created using the `cldfviz.map` command from the [`cldfviz` package](https://pypi.org/project/cldfviz/).


## Is there colexification?



&nbsp; | Value | Count | Description
--- | --- | ---:| ---
$${\color{black}⏺}$$ | lexically distinct | 465 | The concepts ‘hand’ and ‘five’ are lexically distinct in the language.
$${\color{red}⏺}$$ | full colexification | 194 | The concepts ‘hand’ and ‘five’ are fully colexified in the language.
$${\color{orange}⏺}$$ | partial colexification | 153 | The concepts ‘hand’ and ‘five’ are partially colexified in the language.
$${\color{gray}⏺}$$ | unknown | 462 | The relationship between ‘hand’ and ‘five’ is unknown in the language due to insufficient data.
&nbsp; | &nbsp; | **1274** | &nbsp;

![colex](colex.svg)

View [interactive map](https://cldf-datasets.github.io/barlowhandandfive/maps/colex.html).

## Is distinctness due to lexical replacement or phonological change?

For those languages that lack colexification (i.e., languages with the value “lexically distinct” for the parameter “Is there colexification?”), the values for this parameter are “lexical replacement” or “phonological change”. However, some languages exhibit both lexical replacement and (partial) colexification; this is possible when there has been replacement of both ‘hand’ and ‘five’ such that the new forms are (partially) colexified: these cases are indicated by rows in the ValueTable with an empty value and a comment “(recolexification)”.

&nbsp; | Value | Count | Description
--- | --- | ---:| ---
$${\color{black}⏺}$$ | lexical replacement | 380 | The concepts ‘hand’ and ‘five’ are distinct in the language due to lexical replacement.
$${\color{yellow}⏺}$$ | phonological change | 85 | The concepts ‘hand’ and ‘five’ are distinct in the language due to phonological change.
&nbsp; | &nbsp; | **465** | &nbsp;

![dist](dist.svg)

View [interactive map](https://cldf-datasets.github.io/barlowhandandfive/maps/dist.html).

## Was there lexical replacement of ‘hand’?



&nbsp; | Value | Count | Description
--- | --- | ---:| ---
$${\color{white}⏺}$$ | no | 428 | The word for the concept ‘hand’ has not been replaced.
$${\color{red}⏺}$$ | yes | 390 |  The word for the concept ‘hand’ has been replaced.
$${\color{gray}⏺}$$ | unknown | 456 | It is unknown whether or not the word for the concept ‘hand’ has been replaced.
&nbsp; | &nbsp; | **1274** | &nbsp;

![repl_hand](repl_hand.svg)

View [interactive map](https://cldf-datasets.github.io/barlowhandandfive/maps/repl_hand.html).

## Was there lexical replacement of ‘five’?



&nbsp; | Value | Count | Description
--- | --- | ---:| ---
$${\color{white}⏺}$$ | no | 1121 | The word for the concept ‘five’ has not been replaced.
$${\color{red}⏺}$$ | yes | 84 | The word for the concept ‘five’ has been replaced.
$${\color{gray}⏺}$$ | unknown | 69 | It is unknown whether or not the word for the concept ‘five’ has been replaced.
&nbsp; | &nbsp; | **1274** | &nbsp;

![repl_five](repl_five.svg)

View [interactive map](https://cldf-datasets.github.io/barlowhandandfive/maps/repl_five.html).

## What replaced ‘hand’?

Values for this parameter are descriptions of the most likely etymology (traced as far back as possible in the Austronesian family) given for the word in the language that came to mean ‘hand’; values followed by “?” are somewhat uncertain; and those followed by “??” are even more uncertain; when no likely etymology has been posited, then the value is given simply as “unclear” (with no preceding etymology). Values are batched into five different categories, referenced by the `Code_ID` column.

&nbsp; | Value | Count | Description
--- | --- | ---:| ---
$${\color{black}⏺}$$ | “hand” word other than *qalima | 139 | The word for ‘hand’ derives from a word meaning ‘hand’ or ‘arm’ other than *qalima, whether [PAn *kamay ‘hand’](https://acd.clld.org/cognatesets/26632), [PMP *baRa ‘hand, arm’](https://acd.clld.org/cognatesets/25155), or POc *minV- ‘hand’.
$${\color{red}⏺}$$ | part of the arm | 109 | The word for ‘hand’ derives from a word referring to part of the arm, whether [PAn *qabaRa ‘shoulder’](https://acd.clld.org/cognatesets/27538), [PAn *kuSkuS ‘claw, talon, fingernail’](https://acd.clld.org/cognatesets/30315), Proto-Tsouic *ramuCu ‘finger’ (?), [PMP *taŋan ‘finger, toe’](https://acd.clld.org/cognatesets/28404), [PMP *leŋen ‘forearm, lower arm’](https://acd.clld.org/cognatesets/30521), [PPh *dalukap ‘palm of the hand, sole of the foot’](https://acd.clld.org/cognatesets/34040), or PNCV *bisu ‘finger, toe, nail’
$${\color{yellow}⏺}$$ | wing | 69 | The word for ‘hand’ derives from a word referring to the wing (of an animal), whether [PAn *paNij ‘wing’](https://acd.clld.org/cognatesets/27294), [PMP *kapak ‘wings; flutter’](https://acd.clld.org/cognatesets/31811), or PWOc *baqe ‘wing, (?) hand’
$${\color{blue}⏺}$$ | ‘hold onto’ | 1 | The word for ‘hand’ derives from ‘hold onto, cling to’
$${\color{gray}⏺}$$ | unclear | 72 | The word for ‘hand’ derives from a form other than *qalima, but its etymology is unclear.
&nbsp; | &nbsp; | **390** | &nbsp;

![hand_replacement](hand_replacement.svg)

View [interactive map](https://cldf-datasets.github.io/barlowhandandfive/maps/hand_replacement.html).

## What replaced ‘five’?

The same conventions apply here as for the parameter “What replaced hand?” except that here most entries are given a language-internal etymology. Values are batched into seven different categories, referenced by the `Code_ID` column.

&nbsp; | Value | Count | Description
--- | --- | ---:| ---
$${\color{black}⏺}$$ | “hand” word other than *qalima | 45 | The word for ‘five’ derives from a hand-related word unrelated to *qalima (in some cases ultimately derived from ‘finger’ or ‘wing’)
$${\color{yellow}⏺}$$ | addition with 2 | 8 | The word for ‘five’ derives from a formulation like ‘2+2+1’.
$${\color{red}⏺}$$ | tally word | 6 | The word for ‘five’ derives from an expression apparently referring to a physical tallying practice, including words like ‘finished’, ‘on top’, or ‘make/take’.
$${\color{purple}⏺}$$ | ‘count’ | 2 | The word for ‘five’ derives from ‘count’.
$${\color{orange}⏺}$$ | addition with 4 | 2 | The word for ‘five’ derives from a formulation like ‘4+1’.
$${\color{blue}⏺}$$ | ‘part’ | 1 | The word for ‘five’ derives from ‘part’.
$${\color{gray}⏺}$$ | unclear | 20 | The word for ‘five’ derives from a form other than *lima, but its etymology is unclear.
&nbsp; | &nbsp; | **84** | &nbsp;

![five_replacement](five_replacement.svg)

View [interactive map](https://cldf-datasets.github.io/barlowhandandfive/maps/five_replacement.html).

## What is the numeral system?

The values for this parameter are taken from Barlow (2023) “Papuan-Austronesian contact and the spread of numeral systems in Melanesia”, updated here to reflect changes between Glottolog 4.6 and Glottolog 5.0: (1) badu1237 is removed (subsumed within sund1252); (2) bali1287 is added (with numeral system “unknown”); (3) dalk1234 is added (with numeral system “unknown”); (4) mori1267 is added (split from maor1246: both with numeral system “decimal proper”); and (5) ngga1239 is added (with numeral system “unknown”).

&nbsp; | Value | Count | Description
--- | --- | ---:| ---
$${\color{red}⏺}$$ | decimal proper | 632 | A decimal system with atomic numerals ‘one’ through ‘nine’.
$${\color{orange}⏺}$$ | decimal modified | 228 | A decimal system with one or more derived numerals lower than ‘ten’.
$${\color{yellow}⏺}$$ | quinary | 290 | A system that constructs numerals based on the number 5.
$${\color{blue}⏺}$$ | binary proper | 22 | A system that constructs the numerals ‘three’ and ‘four’ based on the number 2.
$${\color{purple}⏺}$$ | binary+3 | 14 | A system that constructs the numeral ‘four’ based on the number 2 but has an atomic ‘three’.
$${\color{black}⏺}$$ | quaternary | 5 | A system that constructs numerals based on the number 4.
$${\color{gray}⏺}$$ | unknown | 83 | An unknown numeral system.
&nbsp; | &nbsp; | **1274** | &nbsp;

&nbsp; | Value | Count | Description
---:| --- | ---:| ---
⏺| in Melanesia | 514 | 
▼| not in Melanesia | 760 | 

![num_syst](num_syst.svg)

View [interactive map](https://cldf-datasets.github.io/barlowhandandfive/maps/num_syst.html).
