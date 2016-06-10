

def geojson_format(data):
    poly = data['poly']
    obj = "POLYGON((" + data['poly'] + "))"
    data['poly'] = obj
    return data
