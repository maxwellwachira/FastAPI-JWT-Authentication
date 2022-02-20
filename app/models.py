from pydantic import BaseModel, Field, EmailStr


#Field is used to add more validation in pydantic models
class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...) 
    content: str = Field(...)

    #config and schema_extra are used to declare request example data
    class Config:
        schema_extra = {
            "example": {
                "title" : "Securing FastAPI applications with JWT",
                "content": "Using PyJWT to sign, encode and decode JWT tokens"
            }
        }


class UserSchema (BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example" : {
                "fullname": "John Doe",
                "email": "maxwellwachira67@gmail.com",
                "password": "verystrongpassword"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example" : {
                "email": "maxwellwachira67@gmail.com",
                "password": "verystrongpassword"
            }
        }