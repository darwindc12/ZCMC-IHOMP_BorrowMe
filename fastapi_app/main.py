from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Base, engine
from ihomp_borrowme_app.models import Borrow, Department, Peripheral, Category, Status  # Import your models

# Create the FastAPI app
app = FastAPI()

# Ensure tables are created in the database
Base.metadata.create_all(bind=engine)


@app.get("/borrows/")
def get_all_borrows(db: Session = Depends(get_db)):
    borrows = db.query(Borrow).all()
    return borrows


@app.get("/borrows/{borrow_id}")
def get_borrow(borrow_id: int, db: Session = Depends(get_db)):
    borrow = db.query(Borrow).filter(Borrow.borrow_id == borrow_id).first()
    if not borrow:
        raise HTTPException(status_code=404, detail="Borrow not found")
    return borrow
