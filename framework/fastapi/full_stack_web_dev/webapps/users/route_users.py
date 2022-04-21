from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/register/")
def register(request: Request):
    return templates.TemplateResponse("users/register.html", {"request": request})
