import datetime

def filter_transuction_for_year(transuction, year):
    return [t for t in transuction if t.timeIn.year == year]

def count_enter_Livorno(transuction):
    return sum(1 for t in transuction if t.enter == "Livorno")

def calculate_total_import(transuction):
    return sum(t.import for t in transuction)

def calculate_total_time(transuction):
    return sum(int((t.timeOut - t.timeIn).total.seconds()) for t in transuction)