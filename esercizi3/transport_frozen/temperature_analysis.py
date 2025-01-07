import xml.etree.ElementTree as ET
from datetime import datetime

def parse_xml(file_path, threshold):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for veicolo in root.findall('veicolo'):
        veicolo_id = veicolo.find('ID').text
        print(f"Veicolo ID: {veicolo_id}")

        all_below_threshold = True
        timestamps = []

        for misura in veicolo.findall('misura'):
            temperatura = float(misura.find('temperatura').text)
            data_ora = misura.find('data_ora').text

            # Convertire data_ora in timestamp
            timestamp = int(datetime.strptime(data_ora, "%Y-%m-%dT%H:%M:%S").timestamp())

            if temperatura > threshold:
                all_below_threshold = False
                timestamps.append(timestamp)

        print(f"Tutti i valori sotto la soglia? {all_below_threshold}")
        if timestamps:
            print(f"Timestamp delle temperature sopra la soglia: {timestamps}")

# Esegui la funzione
parse_xml("veicoli.xml", -30.0)