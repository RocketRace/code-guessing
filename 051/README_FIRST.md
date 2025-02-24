# [Round 51](https://cg.esolangs.gay/51/): Do the impossible

[_Submitted entry_](https://cg.esolangs.gay/51/#)

_Relevant files:_ `length.py`, `README.md`, `cg.ipynb`

I used a Jupyter notebook to generate a regex that takes as input a bytes 
representing a utf-8 encoded string, and matches extended grapheme clusters 
within those bytes. The data is generated from Unicode Standard Annex #29 
[on cluster boundaries](https://www.unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries),
as well as the python `regex` library to collate character classes (that was 
the most convenient way to get that, trust me).

The final submission contains the compressed `length.py` as well as `README.md`
urging the reader to scroll through the script. I hid a little conversation inside!
