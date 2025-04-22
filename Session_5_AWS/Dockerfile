# install the alphine-os with python 3.10
FROM python:3.10-slim

# creating the folder in the container
WORKDIR /flask_24

# copy the requirements.txt file to the container
COPY artefacts/requirements.txt .

# install the requirements
RUN pip install -r requirements.txt

# copy the rest of the files to the container
COPY . /flask_24/

CMD ["python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0", "--port=8000"]
