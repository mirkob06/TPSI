from sqlalchemy.orm import Session
import models, schemas

def get_cities(db: Session):
    return db.query(models.City).all()

def get_city(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.id == city_id).first()

def create_city(db: Session, city: schemas.CityCreate):
    db_city = models.City(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def update_city(db: Session, city_id: int, city: schemas.CityUpdate):
    db_city = get_city(db, city_id)
    if db_city:
        for field, value in city.dict().items():
            setattr(db_city, field, value)
        db.commit()
        db.refresh(db_city)
    return db_city

def delete_city(db: Session, city_id: int):
    db_city = get_city(db, city_id)
    if db_city:
        db.delete(db_city)
        db.commit()
    return db_city

def filter_by_population(db: Session, min_pop: int, max_pop: int):
    return db.query(models.City).filter(models.City.population.between(min_pop, max_pop)).all()

def filter_by_area(db: Session, min_area: float, max_area: float):
    return db.query(models.City).filter(models.City.area.between(min_area, max_area)).all()
