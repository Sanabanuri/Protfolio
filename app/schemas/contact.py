from pydantic import BaseModel, EmailStr

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    message: str

class ContactResponse(BaseModel):
    message: str
