from fastapi import APIRouter

router = APIRouter(prefix="/user")
USERS = []
@router.get("/"):
    
def get_all_users():
    return USERS

@router.get("/{username}")
def get_user(username : str): 
    return {"username" : username} 