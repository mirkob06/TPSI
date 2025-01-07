import xmlschema
import xml.etree.ElementTree as ET
import sys

def validate_xml(xsd_path, xml_path):
    schema = xmlschema.XMLSchema(xsd_path)
    if schema.is_valid(xml_path):
        print("XML is valid.")
    else:
        print("XML is not valid.")
        for error in schema.iter_errors(xml_path):
            print(error)
        sys.exit(1)

def analyze_inventory(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    print("\nCategory-wise Product Values:")
    for category in root.find('categories').findall('category'):
        category_name = category.find('name').text
        total_value = 0
        print(f"\nCategory: {category_name}")
        
        for product in category.find('products').findall('product'):
            code = product.find('code').text
            price = float(product.find('price').text)
            quantity = int(product.find('quantity').text)
            value = price * quantity
            total_value += value
            print(f"  Product: {code}, Value: {value:.2f}")
        
        print(f"  Total Value for {category_name}: {total_value:.2f}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python validate_and_analyze_inventory.py <xsd_path> <xml_path>")
        sys.exit(1)
    
    xsd_path = sys.argv[1]
    xml_path = sys.argv[2]
    
    validate_xml(xsd_path, xml_path)
    analyze_inventory(xml_path)
