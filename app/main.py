from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, database

# create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Blog API",
    description="Simple CRUD API for blog posts",
    version="1.0.0"
)

# Dependency for DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---- CRUD Endpoints ----

@app.get("/posts/", response_model=list[schemas.PostResponse])
def read_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)

@app.get("/posts/{post_id}", response_model=schemas.PostResponse)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/posts/", response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)

@app.put("/posts/{post_id}", response_model=schemas.PostResponse)
def update_post(post_id: int, post_data: schemas.PostCreate, db: Session = Depends(get_db)):
    updated = crud.update_post(db, post_id, post_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    success = crud.delete_post(db, post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted successfully"}

@app.post("/posts/{post_id}/like", response_model=schemas.PostResponse)
def like_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post.likes += 1
    db.commit()
    db.refresh(post)
    return post
