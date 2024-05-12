MongoDB Installation and Setup:

Download and install MongoDB from the official MongoDB website.
Start MongoDB service locally.

Running the API:

Save the provided code in a file, e.g., main.py.
Open a terminal or command prompt.
Navigate to the directory containing main.py.
Run the FastAPI application using Uvicorn:
-->>uvicorn main:app --reload
This will start the FastAPI application, and you should see output indicating that the server is running.


Once the API is running locally, you can interact with it using HTTP requests.
Use tools like cURL, Postman, or Python requests library to make HTTP requests to the API endpoints.


Endpoints:

GET /: Returns a simple greeting message.
POST /posts/: Creates a new blog post. Requires a JSON payload with title, content, and author fields.
GET /posts/{post_id}: Retrieves a specific blog post by its ID.
PUT /posts/{post_id}: Updates an existing blog post. Requires the post ID in the URL and a JSON payload with updated post data.
DELETE /posts/{post_id}: Deletes a blog post by its ID.
POST /posts/{post_id}/comments/: Adds a comment to a blog post. Requires the post ID in the URL and a JSON payload with content and author fields.
POST /posts/{post_id}/like/: Increments the like count of a blog post.
POST /posts/{post_id}/dislike/: Increments the dislike count of a blog post.



Post Model:
title: Title of the blog post (string).
content: Content of the blog post (string).
author: Author of the blog post (string).
Comment Model:
content: Content of the comment (string).
author: Author of the comment (string).
Additional Notes:

Make sure MongoDB is running locally and accessible at localhost:27017.
Adjust MongoDB connection string ("mongodb://localhost:27017/") if your MongoDB instance is running on a different host or port.
Ensure that the necessary Python packages (fastapi, uvicorn, pymongo) are installed and up to date.

Configuration Files and Dependencies:

No additional configuration files are required.
Dependencies are managed using pip and specified in the code.
API Documentation:

Each endpoint is self-explanatory and follows RESTful conventions.
Input and output data formats are specified using Pydantic models.
Error handling is implemented using FastAPI's HTTPException.
Ensure that all requests are made using appropriate HTTP methods (GET, POST, PUT, DELETE) and include required parameters and payloads.



