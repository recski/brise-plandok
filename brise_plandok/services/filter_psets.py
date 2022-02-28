from brise_plandok.constants import DocumentFields, SenFields, AttributeFields
from brise_plandok.services.psets import PSETJson, PSETS


def filter_psets(doc, full):
    response = {}
    _group_sections(doc, response)
    _add_psets(response)
    if not full:
        _retain_minimal(response)
    return response


def _group_sections(doc, response):
    for sen_id, sen in doc[DocumentFields.SENS].items():
        section_id = sen_id.split("_")[0] + "_" + sen_id.split("_")[1]
        if section_id not in response:
            _create_section_entry(response, section_id)
        section = response[section_id]
        section[PSETJson.SECTION_TEXT] += sen[SenFields.TEXT]
        _add_values(section, sen, SenFields.GOLD_ATTRIBUTES, PSETJson.GOLD_ATTRIBUTES)
        _add_values(section, sen, SenFields.PREDICTED_ATTRIBUTES, PSETJson.PRED_ATTRIBUTES)


def _add_values(section, sen, attribute_field, pset_field):
    for attr_name, attr in sen[attribute_field].items():
        if attr_name in section[pset_field]:
            section[pset_field][attr_name][AttributeFields.VALUE].append(
                attr[AttributeFields.VALUE]
            )
        else:
            section[pset_field][attr_name] = {
                AttributeFields.NAME: attr_name,
                AttributeFields.VALUE: attr[AttributeFields.VALUE],
            }


def _create_section_entry(response, section_id):
    response[section_id] = {
        PSETJson.SECTION_ID: section_id,
        PSETJson.SECTION_TEXT: "",
        PSETJson.GOLD_ATTRIBUTES: {},
        PSETJson.PRED_ATTRIBUTES: {},
        PSETJson.GOLD_PSETS: {},
        PSETJson.PRED_PSETS: {},
    }


def _add_psets(response):
    for section_id, section in response.items():
        for pset_name, pset_attributes in PSETS.items():
            section[PSETJson.GOLD_PSETS][pset_name] = {PSETJson.PROPERTIES: []}
            section[PSETJson.PRED_PSETS][pset_name] = {PSETJson.PROPERTIES: []}
            for pset_attr in pset_attributes:
                _add_pset_attribute(
                    pset_attr, pset_name, section, PSETJson.GOLD_PSETS, PSETJson.GOLD_ATTRIBUTES
                )
                _add_pset_attribute(
                    pset_attr, pset_name, section, PSETJson.PRED_PSETS, PSETJson.PRED_ATTRIBUTES
                )


def _add_pset_attribute(pset_attr, pset_name, section, pset_type, pset_field):
    if pset_attr in section[pset_field]:
        section[pset_type][pset_name][PSETJson.PROPERTIES].append(section[pset_field][pset_attr])
    else:
        section[pset_type][pset_name][PSETJson.PROPERTIES].append(
            {
                AttributeFields.NAME: pset_attr,
                AttributeFields.VALUE: None,
            }
        )


def _retain_minimal(response):
    for section_id, section in response.items():
        del section[PSETJson.GOLD_ATTRIBUTES]
        del section[PSETJson.PRED_ATTRIBUTES]
        del section[PSETJson.GOLD_PSETS]
        keys_to_delete = _get_psets_to_delete(section)
        _delete_psets(keys_to_delete, section)


def _get_psets_to_delete(section):
    keys_to_delete = []
    for pset_name, pset in section[PSETJson.PRED_PSETS].items():
        keep = False
        for prop in pset[PSETJson.PROPERTIES]:
            if prop[AttributeFields.VALUE] is not None:
                keep = True
                break
        if not keep:
            keys_to_delete.append(pset_name)
    return keys_to_delete


def _delete_psets(keys_to_delete, section):
    for key_to_delete in keys_to_delete:
        del section[PSETJson.PRED_PSETS][key_to_delete]
