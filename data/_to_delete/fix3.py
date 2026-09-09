p='scripts/build_from_research.py'
s=open(p).read()
old='''    # year_built is the next field if it looks like a year; anything else
    # there is prose that belongs in aliases.
    row["year_built"] = ""
    if tail and re.fullmatch(r"(1[89]|20)\\d{2}", tail[0]):
        row["year_built"] = tail[0]
        tail = tail[1:]'''
new='''    # The year_built slot is always consumed, whatever is sitting in it, so
    # that a blank year cannot shift the description/aliases split that
    # follows. A real year is kept; anything else there is prose, which is
    # moved to the front of the description rather than dropped or aliased.
    row["year_built"] = ""
    stray_year_prose = ""
    if tail:
        head, tail = tail[0], tail[1:]
        if re.fullmatch(r"(1[89]|20)\\d{2}", head):
            row["year_built"] = head
        elif head:
            stray_year_prose = head'''
assert old in s; s=s.replace(old,new)

old2='''    row["description"], alias_src = _split_desc_aliases(tail)'''
new2='''    row["description"], alias_src = _split_desc_aliases(tail)
    if stray_year_prose:
        row["description"] = (stray_year_prose + " " + row["description"]).strip()'''
assert old2 in s; s=s.replace(old2,new2)
open(p,'w').write(s); print('patched',p)

# and the two wrong assertions in my new tests
t='tests/test_research_builder.py'
u=open(t).read()
u=u.replace('assert row["aliases"] == "Thunderbirds; F100D; F100"',
            'assert row["aliases"] == "Thunderbirds; F100; F100D"')
u=u.replace('''        sentence = ("Bell|UH-1|H|64-13645|Iroquois||rotary_wing||military|"
                    "utility||Served with the 174th Assault Helicopter Company "
                    "in Vietnam|on_display")''',
            '''        sentence = ("Bell|UH-1|H|64-13645|Iroquois||rotary_wing||military|"
                    "utility|Served with the 174th Assault Helicopter Company "
                    "in Vietnam|on_display")''')
open(t,'w').write(u); print('patched',t)
