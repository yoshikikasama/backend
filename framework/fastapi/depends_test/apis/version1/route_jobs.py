from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.session import get_db
from db.models.users import User
from schemas.jobs import JobCreate, ShowJob
from db.repository.jobs import (create_new_job,
                                retreive_job)
from apis.version1.route_login import get_current_user_from_token


router = APIRouter()


@router.post("/create-job", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    owner_id = current_user.id
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job


@router.get("/get/{id}", response_model=ShowJob)
def retreive_job_by_id(id: int, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    print(job)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does not exist")
    return job
