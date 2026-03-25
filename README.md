# FastAPI

 FastAPI Project

This is a simple FastAPI-based backend project built to understand API development, routing, and data handling using Python.

📌 Features

- REST API using FastAPI
- CRUD operations (Create, Read, Update, Delete)
- Pydantic models for data validation
- Simple product management system
- Clean and structured code

 🛠️ Tech Stack

- Python 🐍
- FastAPI ⚡
- Pydantic
- Uvicorn (ASGI server)

📂 Project Structure

FastAPI/
│── main.py          # Main application file
│── models.py        # Pydantic models
│── requirements.txt # Dependencies
│── README.md        # Project documentation

````

⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/harshh-m/FastAPI.git
cd FastAPI
````

2. Create virtual environment:

```bash
python -m venv venv
```

3. Activate virtual environment:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

▶️ Run the Server

```bash
uvicorn main:app --reload
```

Server will run on:

```
http://127.0.0.1:8000
```

📖 API Docs

FastAPI provides automatic documentation:

* Swagger UI:
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* ReDoc:
  [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

📌 Example Endpoints

* `GET /` → Welcome message
* `GET /products` → Get all products
* `POST /products` → Add new product
* `PUT /products/{id}` → Update product
* `DELETE /products/{id}` → Delete product

🎯 Learning Outcome

* Learned how APIs work
* Understood request/response handling
* Practiced backend development basics
* Got hands-on experience with FastAPI

📌 Future Improvements

* Database integration (PostgreSQL / MongoDB)
* Authentication (JWT)
* Better error handling
* Frontend integration

🤝 Contributing

Feel free to fork this repo and improve it.

📜 License

This project is open-source and free to use.



