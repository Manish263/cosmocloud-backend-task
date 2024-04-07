# Library Management System API

This is a FastAPI-based API for managing student data. It provides endpoints for creating, retrieving, updating, and deleting student records.

## Getting Started

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Manish263/cosmocloud-backend-task.git
   cd student-management-api

2. **Set up the environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate #onwindows
   source venv/bin/activate #onmac/linux

3. **Run the application:**
   ```bash
   uvicorn main:app --reload


## Endpoints

### 1. Create Student

- **Description:** Create a new student record in the system.
- **Method:** `POST`
- **Endpoint:** `/students`
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "age": 20,
    "address": {
      "city": "New York",
      "country": "USA"
    }
  }

- **Response:**
  ```json
  {
  "id": "1234567890"
  }

### 2. List Students

- **Description:** Retrieve a list of students with optional filters.
- **Method:** `GET  `
- **Endpoint:** `/students`
- **Query Parameters:** `country (optional): Filter by country.`
`age (optional): Filter by minimum age.`


- **Response:**
  ```json
   {
  "data": [
    {
      "name": "John Doe",
      "age": 20,
      "address": {
        "city": "New York",
        "country": "USA"
      }
    },
    {
      "name": "Jane Smith",
      "age": 22,
      "address": {
        "city": "Los Angeles",
        "country": "USA"
      }
    }
  ]
  }



### 3. Fetch Student

- **Description:**  Fetch details of a specific student.
- **Method:** `GET`
- **Endpoint:** `/students/{id}`
- **Path Parameter:** `id` ID of the student to fetch.

- **Response:**
  ```json
  {
  "name": "John Doe",
  "age": 20,
  "address": {
    "city": "New York",
    "country": "USA"
    }
  }


### 4. Update Student

- **Description:** Update properties of an existing student record.
- **Method:** `PATCH`
- **Endpoint:** `/students/{id}`
- **Path Parameter:** `id` ID of the student to fetch.

- **Response:** `204 No Content`

### 5. Delete Student

- **Description:** Delete an existing student record.
- **Method:** `DELETE`
- **Endpoint:** `/students/{id}`
- **Path Parameter:** `id` ID of the student to fetch.

- **Response:** `200 Ok`

## Live Website
-**Check out the live demo of this API at https://cosmocloud-backend-task.onrender.com/.**

## Access the API:
*Access the API:
Open your web browser and go to **https://cosmocloud-backend-task.onrender.com/**  to access the Swagger documentation and explore the available endpoints.*
