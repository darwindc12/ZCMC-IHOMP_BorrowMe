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


@app.post("/borrows/")
def create_borrow(
    borrower_name: str,
    department_id: int,
    category_id: int,
    peripheral_id: int,
    unique_number: str,
    db: Session = Depends(get_db),
):
    # Fetch related records
    department = db.query(Department).filter(Department.department_id == department_id).first()
    category = db.query(Category).filter(Category.category_id == category_id).first()
    peripheral = db.query(Peripheral).filter(Peripheral.peripheral_id == peripheral_id).first()

    if not department or not category or not peripheral:
        raise HTTPException(status_code=400, detail="Invalid references provided")

    # Create the new Borrow record
    new_borrow = Borrow(
        borrower_name=borrower_name,
        department=department,
        category=category,
        peripheral=peripheral,
        unique_number=unique_number,
    )
    db.add(new_borrow)
    db.commit()
    db.refresh(new_borrow)
    return new_borrow


@app.put("/borrows/{borrow_id}")
def update_borrow(
    borrow_id: int,
    borrower_name: str = None,
    status_id: int = None,
    db: Session = Depends(get_db),
):
    borrow = db.query(Borrow).filter(Borrow.borrow_id == borrow_id).first()
    if not borrow:
        raise HTTPException(status_code=404, detail="Borrow not found")

    if borrower_name:
        borrow.borrower_name = borrower_name
    if status_id:
        borrow.status_id = status_id

    db.commit()
    db.refresh(borrow)
    return borrow


@app.delete("/borrows/{borrow_id}")
def delete_borrow(borrow_id: int, db: Session = Depends(get_db)):
    borrow = db.query(Borrow).filter(Borrow.borrow_id == borrow_id).first()
    if not borrow:
        raise HTTPException(status_code=404, detail="Borrow not found")

    db.delete(borrow)
    db.commit()
    return {"detail": "Borrow deleted successfully"}
