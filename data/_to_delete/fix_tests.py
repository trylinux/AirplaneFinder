import sys
p='tests/test_flagship_topup_files.py'
s=open(p).read()
old='''    def test_fixed_wing_always_has_a_wing_type(self, dataset):
        name, rows, _ = dataset
        bad = [f"{r['manufacturer']} {r['model']}" for r in rows
               if r["aircraft_type"] == "fixed_wing" and not r["wing_type"].strip()]
        assert not bad, f"{name}: fixed-wing rows missing wing_type: {bad}"'''
new='''    # Airframes that are fixed_wing only because the vocabulary has nowhere
    # else to put them, and that have no wing to describe. Both are recorded
    # with the reason in their own description field; filling in "monoplane"
    # would be a fabrication. Keep this list closed and argued.
    WINGLESS_BY_DESIGN = {
        # Q-designated, so fixed_wing by the drone convention - but a
        # ducted-fan lift vehicle with no wing at all.
        ("Honeywell", "RQ-16"),
        # Ground-effect machine (GEM-2X). Recorded fixed_wing for want of a
        # ground-effect category.
        ("Curtiss-Wright", "Model 2500"),
    }

    def test_fixed_wing_always_has_a_wing_type(self, dataset):
        name, rows, _ = dataset
        bad = [f"{r['manufacturer']} {r['model']}" for r in rows
               if r["aircraft_type"] == "fixed_wing"
               and not r["wing_type"].strip()
               and (r["manufacturer"], r["model"]) not in self.WINGLESS_BY_DESIGN]
        assert not bad, f"{name}: fixed-wing rows missing wing_type: {bad}"'''
assert old in s, "anchor not found"
open(p,'w').write(s.replace(old,new))
print('patched', p)
