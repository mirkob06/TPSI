import datetime

url = f"http://www.smart-telepass.it/storico?id=1234&anno=2023"
response = requests.get(url)

if response.status_code != 200:
    print ("error in the request at the web server")
    return []

root = ET.fromstring(response.text)
transuction = []

for transuction in root.findall("traunsuction"):
    transuction.append(Transuction(
        code=int(transuction.find("code").text),
        enter=transuction.find("enter").text,
        timeIn=datetime.fromisformat(transuction.find("timeIn").text),
        exit=transuction.find("exit").text,
        timeOut=datetime.fromisformat(transuction.find("timeOut").text),
        amount=float(transuction.find("amount").text)
    ))
    
    return transuction
