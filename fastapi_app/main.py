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

