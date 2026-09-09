p='data/METHODOLOGY.md'
s=open(p).read()
old='''Every research pass returns pipe-delimited lines, exactly 13 fields
(14 with an optional `display_status`):

    manufacturer|model|variant|tail_number|model_name|aircraft_name|
    aircraft_type|wing_type|military_civilian|role_type|year_built|
    description|aliases
'''
new='''Every research pass returns pipe-delimited lines, exactly 14 fields
(the 14th, `display_status`, defaults to `on_display` if omitted):

    manufacturer|model|variant|tail_number|model_name|aircraft_name|
    aircraft_type|wing_type|military_civilian|role_type|year_built|
    description|aliases|display_status

The canonical builder is `scripts/build_from_research.py`. Use it. It
locates the controlled-vocabulary columns by value rather than by index, so
a dropped or extra field cannot shift `monoplane` into `military_civilian`
and take down the whole atomic import; it splits `description` from
`aliases`; and it adds the dashless designation variants. Do not write a
per-state builder — six of those accumulated in `data/*/builder.py` during
the September 2026 sweep and had to be removed.
'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s); print('patched',p)
