@app.get("/cities/")
def list_cities(db: Session = Depends(get_db)):
    return crud.get_cities(db)

@app.get("/cities/{city_id}")
def get_city(city_id: int, db: Session = Depends(get_db)):
    return crud.get_city(db, city_id)

@app.post("/cities/")
def add_city(city: dict, db: Session = Depends(get_db)):
    return crud.create_city(db, city)

@app.put("/cities/{city_id}")
def update_city(city_id: int, city: dict, db: Session = Depends(get_db)):
    return crud.update_city(db, city_id, city)

@app.delete("/cities/{city_id}")
def delete_city(city_id: int, db: Session = Depends(get_db)):
    return crud.delete_city(db, city_id)
