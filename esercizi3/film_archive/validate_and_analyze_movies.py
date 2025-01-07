import xmlschema
import xml.etree.ElementTree as ET
import sys

def validate_xml(xsd_path, xml_path):
    schema = xmlschema.XMLSchema(xsd_path)
    return schema.is_valid(xml_path)

def analyze_movies(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for movie in root.findall('movie'):
        title = movie.find('title').text
        directors = [f"{d.find('firstName').text} {d.find('lastName').text}" 
                     for d in movie.find('directors').findall('director')]
        actors = [f"{a.find('firstName').text} {a.find('lastName').text} as {a.find('role').text}" 
                  for a in movie.find('actors').findall('actor')]
        reviews = [int(r.find('rating').text) for r in movie.find('reviews').findall('review')]
        avg_rating = sum(reviews) / len(reviews)
        
        if avg_rating > 8:
            print(f"Movie: {title}")
            print(f"  Directors: {', '.join(directors)}")
            print(f"  Main Actors: {', '.join(actors)}")
            print(f"  Average Rating: {avg_rating:.2f}\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python validate_and_analyze_movies.py <xsd_path> <xml_path>")
        sys.exit(1)
    
    xsd_path = sys.argv[1]
    xml_path = sys.argv[2]
    
    if validate_xml(xsd_path, xml_path):
        print("XML is valid.")
        analyze_movies(xml_path)
    else:
        print("XML is not valid.")
