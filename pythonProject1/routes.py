from fastapi import APIRouter, Depends
from schemas import TrainSchema, TrainSchemaPeople, TrainSchemaName
from models import User
from database import Session, get_db

api_router = APIRouter()


@api_router.post("/me")
def set_my_data(input_data: TrainSchemaPeople,
                db: Session = Depends(get_db)):
    if not (db.query(User).filter(User.surname == input_data.surname).first() and db.query(User).filter(User.name == input_data.name).first()):
        user = User()
        user.name = input_data.name
        user.surname = input_data.surname
        user.age = input_data.age
        db.add(user)
        db.commit()
        return{"добавленный пользователь ": user.name,
               "suename ": user.surname,
               "age": user.age}
    else:
        return {"message": "Пользователь с такими именем и фамилией уже существует"}

# @api_router.get("/me")
# def get_my_data(name: str,
#                 db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.name == name).first()
#     # user = db.query(User).filter(User.name == input_name.name).first()
#     # if user:
#     #     return {"name": user.name,
#     #         "surname": user.surname,
#     #         "age": user.age}
#     # else:
#     #     return {"message": "Пользователь с таким именем не найден"}
#     return {"name": name}


# @api_router.delete("/me")
# def delete_my_data(input_name: TrainSchemaName,
#                    db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.name == input_name.name).first()
#     if user:
#         db.delete(user)
#         db.commit()
#         return {"message ": "пользователь удален"}
#     else:
#         return {"message ": "пользователь не найден"}

















