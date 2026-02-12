from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.contact import ContactMessage
from ..schemas.contact import ContactCreate, ContactResponse

router = APIRouter()

@router.post("/contact", response_model=ContactResponse)
def submit_contact_form(contact: ContactCreate, db: Session = Depends(get_db)):
    try:
        new_message = ContactMessage(
            name=contact.name,
            email=contact.email,
            message=contact.message
        )
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        return {"message": "Message sent successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
