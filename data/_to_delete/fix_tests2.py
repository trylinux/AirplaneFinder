p='tests/test_research_builder.py'
s=open(p).read()

s=s.replace('''Research passes are told to emit 13 pipe-separated fields and mostly do, but a
few lines per batch come back short or long. Counting pipes cannot tell you
*which* field went missing, so the builder locates the three controlled-
vocabulary columns by value and rebuilds the row around them.''',
'''Research passes are told to emit 14 pipe-separated fields and mostly do, but a
few lines per batch come back short or long. Counting pipes cannot tell you
*which* field went missing, so the builder locates the three controlled-
vocabulary columns by value and rebuilds the row around them.

The 14th field is `description`, added September 2026. Before it existed
everything after year_built was swept into `aliases`, which is how research
prose ended up in the search-indexed aliases table and had to be migrated back
out. The description/aliases split is tested here for that reason.''')

# GOOD gains the description field
s=s.replace('''GOOD = ("North American|F-100|D|55-2888|Super Sabre||fixed_wing|monoplane|"
        "military|fighter|1955|Thunderbirds|on_display")''',
'''GOOD = ("North American|F-100|D|55-2888|Super Sabre||fixed_wing|monoplane|"
        "military|fighter|1955|Flown by the Thunderbirds|Thunderbirds|"
        "on_display")''')

s=s.replace('''    def test_all_thirteen_fields_map_correctly(self):''',
            '''    def test_all_fourteen_fields_map_correctly(self):''')

s=s.replace('''        assert row["year_built"] == "1955"
        assert row["aliases"] == "Thunderbirds"''',
'''        assert row["year_built"] == "1955"
        assert row["description"] == "Flown by the Thunderbirds"
        # Aliases keep what the research gave, plus the dashless designation
        # variants a visitor searching "F100D" needs.
        assert row["aliases"] == "Thunderbirds; F100D; F100"''')

s=s.replace('''    def test_prose_in_the_year_column_goes_to_aliases(self):
        line = ("Northrop|B-2|||Spirit||fixed_wing|monoplane|military|bomber|"
                "structural test airframe||on_display")
        row, _ = one(line)
        assert row["year_built"] == ""
        assert "structural test airframe" in row["aliases"]''',
'''    def test_prose_in_the_year_column_goes_to_description(self):
        """Prose where a year belongs must not become a year, and must not
        become an alias either — aliases are alternative names."""
        line = ("Northrop|B-2|||Spirit||fixed_wing|monoplane|military|bomber|"
                "structural test airframe||on_display")
        row, _ = one(line)
        assert row["year_built"] == ""
        assert "structural test airframe" in row["description"]
        assert "structural test airframe" not in row["aliases"]

    def test_description_and_aliases_stay_separate(self):
        line = ("Republic|F-105|D|61-0073|Thunderchief||fixed_wing|monoplane|"
                "military|ground_attack|1962|Delivered 29 January 1962 per the "
                "park marker|F105D|on_display")
        row, _ = one(line)
        assert row["description"].startswith("Delivered 29 January 1962")
        assert "Delivered" not in row["aliases"]
        assert "F105D" in row["aliases"]

    def test_a_single_trailing_field_is_read_by_shape(self):
        """One field where two belong: a short semicolon list is aliases,
        a sentence is a description."""
        short_list = ("Bell|UH-1|H|64-13644|Iroquois||rotary_wing||military|"
                      "utility||Huey; UH1H|on_display")
        row, _ = one(short_list)
        assert row["description"] == ""
        assert "Huey" in row["aliases"]

        sentence = ("Bell|UH-1|H|64-13645|Iroquois||rotary_wing||military|"
                    "utility||Served with the 174th Assault Helicopter Company "
                    "in Vietnam|on_display")
        row, _ = one(sentence)
        assert "174th Assault Helicopter Company" in row["description"]''')
open(p,'w').write(s)
print('patched',p)
