import requests

# Create a Blog Post:
post_data = {
    "title": "Sample Blog Post",
    "content": "This is a sample blog post content.",
    "author": "John Doe"
}

response = requests.post("http://localhost:8000/posts/", json=post_data)
print(response.json())

"""Read a Blog Post:
You can read a blog post by making a 
GET request to /posts/{post_id} where {post_id} is the ID of the post you want to read. For example:"""

response = requests.get("http://localhost:8000/posts/your_post_id_here")
print(response.json())

# Create a Comment on a Post:
comment_data = {
    "content": "Great post!",
    "author": "Jane Doe"
}

response = requests.post("http://localhost:8000/posts/your_post_id_here/comments/", json=comment_data)
print(response.json())

# Like a Post:
response = requests.post("http://localhost:8000/posts/your_post_id_here/like/")
print(response.json())

# Dislike a Post:
response = requests.post("http://localhost:8000/posts/your_post_id_here/dislike/")
print(response.json())

# Update a Blog Post
updated_post_data = {
    "title": "Updated Blog Post Title",
    "content": "This is the updated content of the blog post.",
    "author": "John Doe"
}

response = requests.put("http://localhost:8000/posts/your_post_id_here", json=updated_post_data)
print(response.json())

# Delete a Blog Post
response = requests.delete("http://localhost:8000/posts/your_post_id_here")
print(response.json())

# We need  to replace "your_post_id_here" with the actual ID of the post you want to interact with.
