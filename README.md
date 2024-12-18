# Library Management System API
A Flask-based API for managing books and members in a library system. The API supports CRUD operations for both entities and includes token-based authentication for secure access.

## Table of Contents
1. How to Run the Project
2. Design Choices
3. Assumptions and Limitations
4. API Endpoints

# How to Run the Project
## Prerequisites
1. Python 3.8 or higher installed.
2. A working internet connection for cloning the repository.
3. Basic knowledge of curl or Postman for testing API endpoints.

## Steps to Run
1. Clone the Repository
    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    cd library-management-system
2. Set Up the Environment
    ``` bash  
    pip install -r requirements.txt
3. Run the Application (Start the Flask server):
    ```bash
    python app.py
    
The API will be accessible at http://127.0.0.1:5000.

Test the Endpoints
Use curl, Postman, or your preferred API testing tool to interact with the endpoints. See API Endpoints for details.

# Design Choices
## Folder Structure
The project follows a modular structure for better maintainability and separation of concerns:

1. `models.py`: Contains the mock data for books and members.
2. `routes/`: Includes route files for books and members.
3. `utils/`: Contains utility files, including authentication.py for token-based authentication.
4. `tests/`: Holds automated test cases for endpoints.

## *Token-Based Authentication*
A lightweight custom token-based authentication was implemented without third-party libraries. The Authorization header is required for all requests.


# Assumptions and Limitations
## *Assumptions*
Authentication tokens are predefined in the code for simplicity.
The books and members data are stored in memory (as Python dictionaries) and will reset when the application restarts.
API users are expected to provide a valid Authorization header in the format:
Authorization: Bearer <token>
Predefined tokens include:
token123 (user1)
token456 (user2)

## *Limitations*
1. Persistence: No database is integrated; all data resets on server restart.
2. Security: The token-based authentication is simplistic and should not be used in production without enhancements.
3. Scalability: The current implementation is suitable for a small-scale demo but would require significant upgrades for large-scale use.
4. Validation: Minimal input validation is performed. Production-ready systems should include stricter validation.

# API Endpoints
## *Books*
1 .GET `/api/books`
Fetches a list of all books.

2. POST `/api/books`
Adds a new book.
    ```Body:
    json
    {
      "title": "Book Title",
      "author": "Author Name"
    }
3. PUT /api/books/<book_id>
Updates the availability of a book.
    ```Body:
    json
    Copy code
    {
      "available": true
    }

4. DELETE `/api/books/<book_id>`
Deletes a book.

## *Members*
1. GET /api/members
Fetches a list of all members.

2. POST /api/members
Adds a new member.
    ```Body:
    json
    Copy code
    {
      "name": "Member Name",
      "email": "email@example.com"
    }

3. PUT /api/members/<member_id>
Updates a member's details.
    ```Body:
    json
    Copy code
    {
      "name": "Updated Name",
      "email": "new_email@example.com"
    }

4. DELETE /api/members/<member_id>
Deletes a member.
