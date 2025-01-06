import xml.etree.ElementTree as ET
from datetime import datetime

# Represents a single location in the shipment route
class Location:
    def __init__(self, place, timestamp, vehicle):
        self.place = place  # Place name
        self.timestamp = datetime.fromisoformat(timestamp)  # Timestamp in ISO 8601 format
        self.vehicle = vehicle  # Mode of transport

# Represents a complete shipment
class Shipment:
    def __init__(self):
        self.tracking_code = None  # Tracking code
        self.sender = None  # Sender
        self.recipient = None  # Recipient
        self.package = None  # Package
        self.route = []  # List of locations
        self.status = None  # Shipment status

    def read_from_xml(self, file_path):
        # Reads shipment data from XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        self.tracking_code = root.find('tracking_code').text
        self.read_shipment_details(root)

        for leg in root.find('route'):
            self.route.append(Location(leg.find('place').text,
                                      leg.find('timestamp').text,
                                      leg.find('vehicle').text))

    def read_shipment_details(self, root):
        # Reads shipment details (sender, recipient, etc.)
        self.sender = self._read_element(root, 'sender')
        self.recipient = self._read_element(root, 'recipient')
        self.package = self._read_element(root, 'package')
        self.status = self._read_element(root, 'status')

    def _read_element(self, element, tag):
        # Reads text from an XML element
        return element.find(tag).text

    def calculate_total_time(self):
        # Calculates the total shipment time
        if not self.route:
            return None
        return (self.route[-1].timestamp - self.route[0].timestamp).total_seconds()