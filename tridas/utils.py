from lxml import etree, objectify


def make_validated_parser(schemafile):
    """Create a validated XML parser from input schema file/URL"""
    xml_schema = etree.XMLSchema(file = schemafile)
    xml_parser = objectify.makeparser(schema = xml_schema)
    return xml_parser