from fastapi import FastAPI, JSONSchema

app = FastAPI()

# Define a schema for the root endpoint
root_schema = JSONSchema(
    type="object",
    properties={
        "name": {"type": "string"},
        "age": {"type": "integer"}
    }
)

@app.get("/")
async def read_root():
    return root_schema.to_dict()