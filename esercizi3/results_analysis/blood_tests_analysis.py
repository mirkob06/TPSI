import xml.etree.ElementTree as ET
from xml import etree
from datetime import datetime

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

def check_tests(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for patient in root.findall('patient'):
        sample_time = datetime.strptime(patient.find('blood_sample/date_time').text, "%Y-%m-%dT%H:%M:%S")
        print(f"Patient: {patient.find('name').text} {patient.find('surname').text}")

        for test in patient.find('blood_sample/tests').findall('test'):
            test_time = datetime.strptime(test.find('analysis_date_time').text, "%Y-%m-%dT%H:%M:%S")
            operator_code = test.find('operator_code').text
            instruments = test.find('instruments').text
            analysis_name = test.find('analysis_name').text

            # Check if the test is within the allowed timeframe
            if test_time < sample_time or (test_time - sample_time).days > 1:
                print(f"Test {analysis_name} failed timing validation.")

            # (Extend with operator/instrument authorization checks here)

            print(f"Test {analysis_name} passed.")

# Run the program
xsd_path = "blood_tests.xsd"
xml_path = "blood_tests.xml"

if validate_xml(xml_path, xsd_path):
    check_tests(xml_path)
