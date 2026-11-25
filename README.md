# AI Platform Gateway

**AI Platform Gateway** is a tiny Python web API created as a beginner-friendly FastAPI learning project. It receives requests in your browser or terminal and sends back JSON responses.

This project is an introduction to the idea of an AI platform gateway: a central API that could later receive requests for many AI models and providers.

> **For beginners:** JSON is just a simple text format for data. It looks like a Python dictionary and is easy for both people and programs to read.

## Table of Contents

1. [What This Project Does](#what-this-project-does)
2. [The Request and Response Flow](#the-request-and-response-flow)
3. [Project Structure](#project-structure)
4. [Requirements](#requirements)
5. [Setup and Run](#setup-and-run)
6. [Try the API](#try-the-api)
7. [Code Explained](#code-explained)
8. [Key Python and FastAPI Terms](#key-python-and-fastapi-terms)
9. [Common Problems](#common-problems)
10. [Learning Exercises](#learning-exercises)

## What This Project Does

The gateway currently provides five small endpoints:

| Method | Address | What it does |
|---|---|---|
| `GET` | `/` | Returns a welcome message and running status |
| `GET` | `/health` | Reports whether the service is healthy |
| `GET` | `/about` | Shows application and framework information |
| `GET` | `/models/{model_id}` | Accepts a model ID in the URL |
| `GET` | `/search` | Accepts an optional provider name |

The endpoints demonstrate:

- Starting a FastAPI application
- Creating URL routes
- Reading values from the URL
- Reading query parameters
- Returning JSON responses
- Automatic API documentation

There is no database and no real AI model connection yet. The project is a foundation for one.

## The Request and Response Flow

Imagine sending a message to a receptionist:

```text
Browser or terminal
        |
        |  GET /health
        v
FastAPI server
        |
        |  Find the /health route
        v
health_check() function
        |
        |  Return Python dictionary
        v
FastAPI converts it to JSON
        |
        v
Browser or terminal receives the response
```

Example response:

```json
{
  "status": "healthy",
  "service": "AI Platform Gateway"
}
```

## Project Structure

```text
AIPlatformGateway/
|-- main.py             The running FastAPI application and routes
|-- requirements.txt    Python package dependencies
|-- api/
|   |-- __init__.py     API package marker
|   `-- endpoints.py    Reserved for future endpoint organization
|-- services/
|   |-- __init__.py     Services package marker
|   `-- model_service.py Reserved for model-related business logic
|-- config/
|   `-- __init__.py     Reserved for configuration
|-- schemas/
|   `-- __init__.py     Reserved for request and response data models
`-- README.md           Project guide
```

The folders currently marked as reserved show how a project can grow. As the app becomes larger, routes can move into `api`, provider logic can move into `services`, and configuration can move into `config`.

## Requirements

- Python 3.9 or newer
- Windows PowerShell
- `pip`, included with standard Python installations

The project dependency is FastAPI with standard extras:

```text
fastapi[standard]
```

This installs FastAPI and common tools used to run and document a web API.

## Setup and Run

Open PowerShell inside the project folder, then run:

```powershell
# Create a virtual environment
py -m venv .venv

# Allow this terminal to activate it
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Activate the virtual environment
.venv\Scripts\Activate.ps1

# Install dependencies
python -m pip install -r requirements.txt

# Start the development server
python -m uvicorn main:app --reload
```

If activation is successful, your prompt will begin with `(.venv)`.

The server usually starts at:

```text
http://127.0.0.1:8000
```

Keep the terminal running while you test the API. Press `Ctrl+C` in that terminal to stop it.

## Try the API

Open these addresses in a browser:

- Welcome: http://127.0.0.1:8000/
- Health: http://127.0.0.1:8000/health
- About: http://127.0.0.1:8000/about
- Model 42: http://127.0.0.1:8000/models/42
- OpenAI search: http://127.0.0.1:8000/search
- Google search: http://127.0.0.1:8000/search?provider=Google

You can also use PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
Invoke-RestMethod http://127.0.0.1:8000/models/42
Invoke-RestMethod "http://127.0.0.1:8000/search?provider=Google"
```

### Interactive API Documentation

FastAPI creates documentation automatically.

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Swagger UI lets you test routes by entering values and pressing **Execute**. It is useful because you do not need to write a separate client first.

## Code Explained

### 1. Create the app

In `main.py`:

```python
app = FastAPI(
    title="AI Platform Gateway",
    description="Backend API for managing AI models and requests",
    version="1.0.0"
)
```

This creates the FastAPI application. The text is used in the automatically generated API documentation.

### 2. Create a route

```python
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Platform Gateway"
    }
```

- `@app.get("/health")` tells FastAPI to accept a `GET` request at `/health`.
- `health_check` is the Python function that handles the request.
- The function returns a dictionary.
- FastAPI converts that dictionary to JSON.

### 3. Read a path parameter

```python
@app.get("/models/{model_id}")
def get_model(model_id: int):
    return {
        "model_id": model_id,
        "message": "Model details retrieved successfully"
    }
```

In `/models/42`, `{model_id}` gets the value `42`.

The `: int` part means the value must be an integer. FastAPI can automatically reject a non-number such as `/models/hello`.

### 4. Read a query parameter

```python
@app.get("/search")
def search_models(provider: str = "OpenAI"):
    return {
        "provider": provider,
        "message": "Searching AI models"
    }
```

This route reads `provider` after `?`:

```text
/search?provider=Google
```

`"OpenAI"` is the default value. It is used when no provider is supplied.

## Key Python and FastAPI Terms

| Term | Meaning |
|---|---|
| API | A set of addresses and rules that allows programs to communicate |
| FastAPI | A Python framework for building web APIs |
| Route or endpoint | One address such as `/health` |
| `GET` | A request that asks to receive information |
| HTTP | The protocol used for web communication |
| JSON | A text format used to send structured data |
| Dictionary | A Python collection of key-and-value pairs |
| Function | A reusable block of code |
| Decorator | Text beginning with `@` that adds behavior to a function |
| Path parameter | A variable included inside the URL path |
| Query parameter | A variable added after `?` in the URL |
| Virtual environment | An isolated Python setup for one project |
| `uvicorn` | A server program that runs the FastAPI application |

## Common Problems

### The server will not start

Make sure you are inside the project folder and the virtual environment is active.

```powershell
cd "E:\AIDSML\ChtGpt\Day-09\Projects\AIPlatformGateway"
.venv\Scripts\Activate.ps1
```

### A package is missing

Reinstall the dependencies:

```powershell
python -m pip install -r requirements.txt
```

### Port 8000 is already in use

Run the app on another port:

```powershell
python -m uvicorn main:app --reload --port 8001
```

Then replace `8000` with `8001` in the example addresses.

### I see `422 Unprocessable Entity`

FastAPI could not validate the request. For example, `/models/hello` supplies text where an integer is required.

### I see `404 Not Found`

Check the address and confirm that the route you requested exists.

## Learning Exercises

Try these changes to understand how FastAPI works:

1. Change the welcome message in `main.py`.
2. Add a `/status` route that returns `"status": "online"`.
3. Add a `/greet/{name}` route that accepts a name and returns a greeting.
4. Give `/search` a second query parameter called `limit`, with a default of `10`.
5. Make the model route reject model IDs below `1`.
6. Open `/docs` after each change and find the new route.

Example exercise:

```python
@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello, {name}!"
    }
```

The `f` in `f"Hello, {name}!"` creates a formatted string. Python replaces `{name}` with the function's name value.

## Next Learning Step

After understanding this project, the next useful topics are:

- Pydantic schemas for validating request bodies
- `POST` requests for sending JSON to the API
- Layering endpoints, services, and configuration
- Real AI provider SDKs
- API keys stored safely in environment variables
- Unit tests
- Docker and cloud deployment

> Never place API keys directly in `main.py` or commit them to source control.
