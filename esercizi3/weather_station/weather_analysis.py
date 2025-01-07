import xml.etree.ElementTree as ET
from xml import etree

def validate_xml(xml_file, xsd_file):
    with open(xsd_file, 'r') as schema_file:
        schema_root = etree.XML(schema_file.read())
        schema = etree.XMLSchema(schema_root)
        parser = etree.XMLParser(schema=schema)

        try:
            with open(xml_file, 'r') as file:
                etree.fromstring(file.read(), parser)
                print("XML is valid.")
        except etree.XMLSyntaxError as e:
            print(f"XML is invalid: {e}")
            return False
    return True

def calculate_averages(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    readings = root.find('station/readings')
    totals = {"temperature": 0, "humidity": 0, "pressure": 0, "wind_speed": 0, "wind_direction": 0, "rainfall": 0}
    count = 0

    for reading in readings.findall('reading'):
        totals["temperature"] += float(reading.find('temperature').text)
        totals["humidity"] += int(reading.find('humidity').text)
        totals["pressure"] += int(reading.find('pressure').text)
        totals["wind_speed"] += int(reading.find('wind_speed').text)
        totals["wind_direction"] += int(reading.find('wind_direction').text)
        totals["rainfall"] += float(reading.find('rainfall').text)
        count += 1

    averages = {key: totals[key] / count for key in totals}
    print("Daily Averages:", averages)

# Run the program
xsd_path = "weather_station.xsd"
xml_path = "weather_data.xml"

if validate_xml(xml_path, xsd_path):
    calculate_averages(xml_path)
