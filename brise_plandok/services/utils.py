from brise_plandok.constants import DocumentFields, SenFields, AttributeFields


def filter_json(doc):
    response = {}
    for sen_id, sen in doc[DocumentFields.SENS].items():
        response[sen_id] = {
            SenFields.TEXT: sen[SenFields.TEXT] if SenFields.TEXT in sen else None,
            SenFields.GOLD_MODALITY: sen[SenFields.GOLD_MODALITY] if SenFields.GOLD_MODALITY in sen else None,
            SenFields.GOLD_ATTRIBUTES: sen[SenFields.GOLD_ATTRIBUTES] if SenFields.GOLD_ATTRIBUTES in sen else None,
            SenFields.PREDICTED_ATTRIBUTES: sen[
                SenFields.PREDICTED_ATTRIBUTES] if SenFields.PREDICTED_ATTRIBUTES in sen else None,
        }
    return response


def json_to_html(response_json):
    response_html = "<html>"
    response_html += "<style>table, th, td {border:1px solid black;}</style>"
    for sen_id, sen in response_json.items():
        response_html += f"<h1>{sen_id}</h1>"
        response_html += f"<p>{sen[SenFields.TEXT]}</p>"
        response_html = _print_modality(response_html, sen)
        response_html = _print_attributes(response_html, sen)
    response_html += "</html>"
    return response_html


def _print_modality(response_html, sen):
    response_html += "<h3>Modality</h3>"
    modality = sen[SenFields.GOLD_MODALITY] if sen[SenFields.GOLD_MODALITY] is not None else "-"
    response_html += f"<p>{modality}</p>"
    return response_html


def _print_attributes(response_html, sen):
    response_html += "<h3>Attributes</h3>"
    response_html += '<table style="width:50%">'
    response_html += f"<tr><th>Name</th><th>value</th><th>Type</th></tr>"
    for attr_name, attr in sen[SenFields.GOLD_ATTRIBUTES].items():
        for i in range(len(attr[AttributeFields.VALUE])):
            response_html += "<tr>"
            response_html += f"<td>{attr[AttributeFields.NAME]}</td>"
            response_html += f"<td>{attr[AttributeFields.VALUE][i]}</td>"
            response_html += f"<td>{attr[AttributeFields.TYPE][i]}</td>"
            response_html += "</tr>"
    response_html += "</table>"
    return response_html
