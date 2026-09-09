import re,sys
p=sys.argv[1]
s=open(p).read()

# 1. realign(): split description from aliases
old = '''    row["aliases"] = ";".join(
        a.strip() for a in ";".join(tail).split(";") if a.strip())
    return row, None'''
new = '''    # The contract's last two data fields are description then aliases.
    # Before the 14-field contract everything here was aliases, which is how
    # prose ended up in the search-indexed aliases table (see the September
    # 2026 alias migration). Split them.
    row["description"], alias_src = _split_desc_aliases(tail)
    row["aliases"] = ";".join(
        a.strip() for a in alias_src.split(";") if a.strip())
    return row, None'''
assert old in s; s=s.replace(old,new)

# 2. helper + dashless alias generation
helper = '''
_DIGITS = "0123456789"


def join_designation(model, variant):
    """Join model and variant the way the DB's generated column does."""
    model = (model or "").strip()
    variant = (variant or "").strip()
    if not variant:
        return model
    if variant[0] in _DIGITS:
        return f"{model}-{variant}"
    if model and model[-1] in _DIGITS:
        return f"{model}{variant}"
    return f"{model} {variant}"


_DESIG = re.compile(r"^([A-Za-z]{1,4})-(\\d{1,3}[A-Za-z]{0,3})$")


def dashless(s):
    """PT-22 -> PT22. Returns None if the string is not a designation."""
    m = _DESIG.match((s or "").strip())
    if not m:
        return None
    v = m.group(1) + m.group(2)
    return v if v != s.strip() else None


def _split_desc_aliases(tail):
    """Map the fields after year_built onto (description, aliases).

    A well-formed 14-field line leaves exactly two: description then aliases.
    One field means the research dropped one — an aliases list is short and
    semicolon-separated, a description is prose, so length decides. More than
    two means an unescaped pipe inside the description, so everything but the
    last field folds back into it.
    """
    tail = [t.strip() for t in tail]
    if not tail:
        return "", ""
    if len(tail) == 1:
        one = tail[0]
        if ";" in one or len(one.split()) <= 6:
            return "", one
        return one, ""
    return " ".join(t for t in tail[:-1] if t), tail[-1]

'''
anchor = '\ndef realign(parts):'
assert anchor in s; s=s.replace(anchor, helper+anchor, 1)

# 3. sanitise(): add the dashless designation variants
old2 = '''    if not row.get("manufacturer") or not row.get("model"):
        problems.append("missing manufacturer or model")'''
new2 = '''    # Dashless designation variants as aliases: a visitor searching "PT22"
    # must find the PT-22. Established September 2026; every imported state
    # from Ohio onward carries these.
    al = [a.strip() for a in row.get("aliases", "").split(";") if a.strip()]
    low = {a.lower() for a in al}
    for src in [row.get("model", ""),
                join_designation(row.get("model"), row.get("variant"))] + list(al):
        d = dashless(src)
        if d and d.lower() not in low:
            al.append(d)
            low.add(d.lower())
    row["aliases"] = "; ".join(al)

    # A comma anywhere in these two would need CSV quoting the importer's
    # splitter does not expect; the research contract forbids them.
    for f in ("description", "aliases"):
        if "," in row.get(f, ""):
            problems.append(f"comma in {f} — the contract forbids it")

    if not row.get("manufacturer") or not row.get("model"):
        problems.append("missing manufacturer or model")'''
assert old2 in s; s=s.replace(old2,new2)

# 4. docstring: 13 -> 14
s=s.replace('Research passes are told to emit exactly 13 pipe-separated fields.',
            'Research passes are told to emit exactly 14 pipe-separated fields.')
s=s.replace('so realign() sees the usual 13.','so realign() sees the usual 14.')
s=s.replace('''found by value rather than by index, and the rest realigned around them. A
line whose anchors cannot be located is reported, never guessed at.''',
'''found by value rather than by index, and the rest realigned around them. A
line whose anchors cannot be located is reported, never guessed at.

DESCRIPTION VS ALIASES
----------------------
The contract's last two data fields are description then aliases. Before the
14-field contract everything after year_built was treated as aliases, which is
how research prose ended up in the search-indexed aliases table and had to be
migrated back out in September 2026. _split_desc_aliases keeps them apart.''')
open(p,'w').write(s)
print('patched', len(s))
