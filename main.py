from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient

# Initialize FastAPI app
app = FastAPI()

# Initialize MongoDB client
client = MongoClient("mongodb://localhost:27017/")
db = client["blog_db"]


# Define Pydantic models
class Post(BaseModel):
    title: str
    content: str
    author: str


class Comment(BaseModel):
    content: str
    author: str


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# Define routes for CRUD operations on blog posts
@app.post("/posts/")
def create_post(post: Post):
    post_id = db.posts.insert_one(post.dict()).inserted_id
    return {"message": "Post created successfully", "post_id": str(post_id)}


@app.get("/posts/{post_id}")
def read_post(post_id: str):
    post = db.posts.find_one({"_id": post_id})
    if post:
        return post
    raise HTTPException(status_code=404, detail="Post not found")


# Update a Blog Post
@app.put("/posts/{post_id}")
def update_post(post_id: str, updated_post: Post):
    result = db.posts.update_one({"_id": post_id}, {"$set": updated_post.dict()})
    if result.modified_count == 1:
        return {"message": "Post updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")


# Delete a Blog Post
@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    result = db.posts.delete_one({"_id": post_id})
    if result.deleted_count == 1:
        return {"message": "Post deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")


# Define routes for comments
@app.post("/posts/{post_id}/comments/")
def create_comment(post_id: str, comment: Comment):
    db.posts.update_one({"_id": post_id}, {"$push": {"comments": comment.dict()}})
    return {"message": "Comment added successfully"}


# Define routes for liking/disliking posts
@app.post("/posts/{post_id}/like/")
def like_post(post_id: str):
    db.posts.update_one({"_id": post_id}, {"$inc": {"likes": 1}})
    return {"message": "Post liked successfully"}


@app.post("/posts/{post_id}/dislike/")
def dislike_post(post_id: str):
    db.posts.update_one({"_id": post_id}, {"$inc": {"dislikes": 1}})
    return {"message": "Post disliked successfully"}
