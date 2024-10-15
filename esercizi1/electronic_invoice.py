class Invoice():
    def __init__(self, client, amount, date):
        self.client = client
        self.amount = amount
        self.date = date

    def display_invoice(self):
        print(f"Client: {self.client}, Amount: €{self.amount:.2f}, Date: {self.date}")

    @classmethod
    def create_today_invoice(cls, client, amount):
        from datetime import date
        today_date = date.today()
        return cls(client, amount, today_date)


invoice1 = Invoice("Mario Rossi", 250.50, "2024-10-12")
invoice2 = Invoice.create_today_invoice("Luca Bianchi", 150.75)

invoice1.display_invoice()
invoice2.display_invoice()
