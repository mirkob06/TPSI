import xmlschema
import xml.etree.ElementTree as ET
import sys

def validate_xml(xsd_path, xml_path):
    """
    Validates an XML file against an XSD schema.
    """
    try:
        schema = xmlschema.XMLSchema(xsd_path)
        schema.validate(xml_path)
        print(f"The XML file '{xml_path}' is valid according to the XSD schema '{xsd_path}'.")
        return True
    except xmlschema.exceptions.XMLSchemaValidationError as e:
        print(f"XML validation error: {e}")
        return False


def find_hybrid_cars(xml_path, car_class):
    """
    Finds agencies renting hybrid cars of a specified class.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    agencies = []
    for car in root.findall("car"):
        car_fuel = car.find("fuel_type").text
        car_class_value = car.find("class").text
        if car_fuel == "hybrid" and car_class_value == car_class:
            for agency in car.findall("agencies"):
                agency_name = agency.attrib.get("name", "Unknown")
                agency_city = agency.attrib.get("city", "Unknown")
                agencies.append((agency_name, agency_city))

    return agencies


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <schema.xsd> <file.xml> <car_class>")
        sys.exit(1)

    xsd_file = sys.argv[1]
    xml_file = sys.argv[2]
    car_class = sys.argv[3]

    if validate_xml(xsd_file, xml_file):
        hybrid_agencies = find_hybrid_cars(xml_file, car_class)
        if hybrid_agencies:
            print(f"Agencies for hybrid cars of class {car_class}:")
            for agency in hybrid_agencies:
                print(f" - {agency[0]}, {agency[1]}")
        else:
            print(f"No agencies found for hybrid cars of class {car_class}.")