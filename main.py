from fastapi import FastAPI, HTTPException, Query, Path
from bson import ObjectId
from db import students_collection

app = FastAPI()

# Define endpoint definitions here...

@app.post("/students", status_code=201)
async def create_student(student_data: dict):

    #Checking if all required fields are there in request body
    required_fields = ['name', 'age', 'address']
    missing_fields = [field for field in required_fields if field not in student_data]
    if missing_fields:
        raise HTTPException(status_code=400, detail=f"Missing required fields: {missing_fields}")
    
    #Inserting in MongoDB database
    result = students_collection.insert_one(student_data)
    
    # returning the ID of the newly created student record
    return {"id": str(result.inserted_id)}

@app.get("/students", response_model=dict)
async def list_students(country: str = Query(None, description="Filter by country"), age: int = Query(None, description="Filter by age")):
    
    filters = {}
    if country:
        filters['address.country'] = country
    if age is not None:
        filters['age'] = {'$gte': age}
    
    # Fetch students from the database based on filters
    students = list(students_collection.find(filters, {'_id': 0}))
    
    # Return the list of students
    return {"data": students}

@app.get("/students/{id}", response_model=dict)
async def get_student(id: str = Path(..., description="The ID of the student previously created")):

    # Fetch the student from the database by ID
    student = students_collection.find_one({"_id": ObjectId(id)}, {'_id': 0})
    
    # Check if the student exists
    if student:
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@app.patch("/students/{id}", status_code=204)
async def update_student(id: str = Path(..., description="The ID of the student previously created"), student_data: dict = None):
    # Check if student exists
    existing_student = students_collection.find_one({"_id": ObjectId(id)})
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Update student data
    update_data = {key: value for key, value in student_data.items() if value is not None} if student_data else {}
    if update_data:
        students_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})

    return {}

@app.delete("/students/{id}", status_code=200)
async def delete_student(id: str = Path(..., description="The ID of the student previously created")):
    # Check if student exists
    existing_student = students_collection.find_one({"_id": ObjectId(id)})
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Delete the student from the database
    students_collection.delete_one({"_id": ObjectId(id)})
    
    return {}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

