from brise_plandok.constants import AttributesNames


def make_markdown_table(array):
    """Input: Python lists with rows of table as lists
               First element as header.
        Output: String to put into a .md file

    Ex Input:
        [["Name", "Age", "Height"],
         ["Jake", 20, 5'10],
         ["Mary", 21, 5'7]]

    Source: https://gist.github.com/m0neysha/219bad4b02d2008e0154
    """

    markdown = "\n" + str("| ")

    for e in array[0]:
        to_add = " " + str(e) + str(" |")
        markdown += to_add
    markdown += "\n"

    markdown += "|"
    for i in range(len(array[0])):
        markdown += str("-------------- | ")
    markdown += "\n"

    for entry in array[1:]:
        markdown += str("| ")
        for e in entry:
            if type(e) == int:
                e = str(e)
            elif type(e) == float:
                e = f"{e:.3f}"
            to_add = e + str(" | ")
            markdown += to_add
        markdown += "\n"

    return markdown + "\n"


def convert_back_post_processed(gold_attrs):
    if AttributesNames.Widmung in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.Widmung}) | {"WidmungUndZweckbestimmung"}
    if AttributesNames.Nutzungsart in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.Nutzungsart}) | {"WidmungUndZweckbestimmung"}
    if AttributesNames.BebauteFlaecheMax in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.BebauteFlaecheMax}) | {"Flaechen"}
    if AttributesNames.BebauteFlaecheMin in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.BebauteFlaecheMin}) | {"Flaechen"}
    if AttributesNames.BebauteFlaecheMaxProzentual in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.BebauteFlaecheMaxProzentual}) | {"Flaechen"}
    if AttributesNames.BebauteFlaecheMaxNebengebaeude in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.BebauteFlaecheMaxNebengebaeude}) | {"Flaechen"}
    if AttributesNames.GesamtePlangebiet in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.GesamtePlangebiet}) | {"PlangebietAllgemein"}
    if AttributesNames.GebaeudeHoeheMaxWN in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.GebaeudeHoeheMaxWN}) | {"GebaeudeHoeheMax"}
    if AttributesNames.GebaeudeHoeheMaxAbsolut in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.GebaeudeHoeheMaxAbsolut}) | {
            "GebaeudeHoeheMax"
        }
    return gold_attrs
