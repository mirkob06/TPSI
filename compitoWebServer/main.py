from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, models, schemas
from database import get_db, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/cities/", response_model=list[schemas.CityResponse])
def list_cities(db: Session = Depends(get_db)):
    return crud.get_cities(db)

@app.get("/cities/{city_id}", response_model=schemas.CityResponse)
def get_city(city_id: int, db: Session = Depends(get_db)):
    return crud.get_city(db, city_id)

@app.post("/cities/", response_model=schemas.CityResponse)
def add_city(city: schemas.CityCreate, db: Session = Depends(get_db)):
    return crud.create_city(db, city)

@app.put("/cities/{city_id}", response_model=schemas.CityResponse)
def update_city(city_id: int, city: schemas.CityUpdate, db: Session = Depends(get_db)):
    return crud.update_city(db, city_id, city)

@app.delete("/cities/{city_id}")
def delete_city(city_id: int, db: Session = Depends(get_db)):
    return crud.delete_city(db, city_id)

@app.get("/cities/statistics/population", response_model=list[schemas.CityResponse])
def stats_population(minPopulation: int, maxPopulation: int, db: Session = Depends(get_db)):
    return crud.filter_by_population(db, minPopulation, maxPopulation)

@app.get("/cities/statistics/area", response_model=list[schemas.CityResponse])
def stats_area(minArea: float, maxArea: float, db: Session = Depends(get_db)):
    return crud.filter_by_area(db, minArea, maxArea)
