# XXM_backend_task
 XXM Backend Task which involves API Endpoints to execute CRUD operations for Pallet
 
Tech Stack:
- Programming Language: Python 3.7.7
- API Framework: FastAPI
- Database: MongoDB 4.4
- API Documentation: Swagger Editor (https://editor.swagger.io/)

Steps:
1. Run virtual env using Python 3.7
2. Install relevant packages like mongodb
3. Start python app using uvicorn index:app --reload
4. Go to http://localhost:8000/docs#/ to test the endpoints

Issues:
1. Python 3.7.7
- Install python 3.7 using ibrew (Source: https://diewland.medium.com/how-to-install-python-3-7-on-macbook-m1-87c5b0fcb3b5)
- Create python venv (Source: https://stackoverflow.com/questions/52816156/how-to-create-virtual-environment-for-python-3-7-0)

2. pymongo BSON encode object
- Use json dumps & loads (Source: https://stackoverflow.com/questions/7963762/what-is-the-most-economical-way-to-convert-nested-python-objects-to-dictionaries)

3. MongoDB Cluster Accessible IP Address (Security -> Network Access -> Add IP Address)

References:
1. FastAPI MongoDB REST API in Python | CRUD Operations | Swagger | PyMongo by Mahesh Kariya https://www.youtube.com/watch?v=G7hZlOLhhMY
2. FastAPI Tutorial - Building RESTful APIs with Python by Amigoscode https://www.youtube.com/watch?v=GN6ICac3OXY
