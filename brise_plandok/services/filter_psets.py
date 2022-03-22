from brise_plandok.constants import DocumentFields, SenFields, AttributeFields
from brise_plandok.services.psets import PSETJson, PSETS


def filter_psets(doc, full):
    response = {}
    _group_sections(doc, response)
    _add_psets(response, PSETJson.GOLD_PSETS, PSETJson.GOLD_ATTRIBUTES)
    _add_psets(response, PSETJson.PRED_PSETS, PSETJson.PRED_ATTRIBUTES)
    _flatten(response, PSETJson.GOLD_PSETS)
    _flatten(response, PSETJson.PRED_PSETS)
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
            section[pset_field][attr_name][AttributeFields.VALUE] = list(
                set(
                    section[pset_field][attr_name][AttributeFields.VALUE]
                    + attr[AttributeFields.VALUE]
                )
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


def _add_psets(response, pset_type, attr_type):
    for section_id, section in response.items():
        for pset_name, pset_attributes in PSETS.items():
            add = True
            for req_attr in pset_attributes[PSETJson.REQUIRED]:
                if req_attr[PSETJson.PROPERTY_NAME] not in section[attr_type]:
                    add = False
                    break
            if add:
                section[pset_type][pset_name] = {PSETJson.PROPERTIES: []}
                for attr in (
                    pset_attributes[PSETJson.REQUIRED] + pset_attributes[PSETJson.OPTIONAL]
                ):
                    _add_pset_attribute(attr, pset_name, section, pset_type, attr_type)


def _add_pset_attribute(pset_attr, pset_name, section, pset_type, pset_field):
    if pset_attr[PSETJson.PROPERTY_NAME] in section[pset_field]:
        section[pset_type][pset_name][PSETJson.PROPERTIES].append(
            {
                PSETJson.PROPERTY_NAME: pset_attr[PSETJson.PROPERTY_NAME],
                PSETJson.PROPERTY_VALUE: section[pset_field][pset_attr[PSETJson.PROPERTY_NAME]][
                    AttributeFields.VALUE
                ],
                PSETJson.PROPERTY_TYPE: pset_attr[PSETJson.PROPERTY_TYPE],
            }
        )
    else:
        section[pset_type][pset_name][PSETJson.PROPERTIES].append(
            {
                PSETJson.PROPERTY_NAME: pset_attr[PSETJson.PROPERTY_NAME],
                PSETJson.PROPERTY_VALUE: None,
                PSETJson.PROPERTY_TYPE: pset_attr[PSETJson.PROPERTY_TYPE],
            }
        )


def _flatten(response, pset_type):
    for section_id, section in response.items():
        psets_old = section[pset_type]
        pset_new = {}
        for pset_name, pset_attributes in psets_old.items():
            pset_new[pset_name] = []
            for pset_attr in pset_attributes[PSETJson.PROPERTIES]:
                if pset_attr[PSETJson.PROPERTY_VALUE] is not None:
                    if len(pset_attr[PSETJson.PROPERTY_VALUE]) == 1:
                        pset_new[pset_name].append(
                            {
                                PSETJson.PROPERTY_NAME: pset_attr[PSETJson.PROPERTY_NAME],
                                PSETJson.PROPERTY_VALUE: pset_attr[PSETJson.PROPERTY_VALUE][0],
                                PSETJson.PROPERTY_TYPE: pset_attr[PSETJson.PROPERTY_TYPE],
                            }
                        )
                    else:
                        for i, value in enumerate(pset_attr[PSETJson.PROPERTY_VALUE]):
                            pset_new[pset_name].append(
                                {
                                    PSETJson.PROPERTY_NAME: pset_attr[PSETJson.PROPERTY_NAME]
                                    + str(i + 1),
                                    PSETJson.PROPERTY_VALUE: value,
                                    PSETJson.PROPERTY_TYPE: pset_attr[PSETJson.PROPERTY_TYPE],
                                }
                            )
        section[pset_type] = pset_new


def _retain_minimal(response):
    for section_id, section in response.items():
        del section[PSETJson.GOLD_ATTRIBUTES]
        del section[PSETJson.PRED_ATTRIBUTES]
        del section[PSETJson.GOLD_PSETS]
