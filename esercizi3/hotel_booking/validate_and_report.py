import xml.etree.ElementTree as ET

def generate_summary_report(xml_file, output_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    summary = ET.Element('SummaryReport')

    for prenotazione in root.findall('.//Prenotazione'):
        cliente = prenotazione.find('NomeCliente').text + " " + prenotazione.find('CognomeCliente').text
        camera = prenotazione.find('NumeroCamera').text
        data_inizio = prenotazione.find('DataInizio').text
        data_fine = prenotazione.find('DataFine').text
        costo_totale = prenotazione.find('CostoTotale').text

        cliente_elem = ET.SubElement(summary, 'Cliente')
        ET.SubElement(cliente_elem, 'Nome').text = cliente
        ET.SubElement(cliente_elem, 'NumeroCamera').text = camera
        ET.SubElement(cliente_elem, 'DataInizio').text = data_inizio
        ET.SubElement(cliente_elem, 'DataFine').text = data_fine
        ET.SubElement(cliente_elem, 'CostoTotale').text = costo_totale

    tree = ET.ElementTree(summary)
    tree.write(output_file)

generate_summary_report('hotel_reservations.xml', 'summary_report.xml')
