# Use an official Python runtime as a parent image
FROM python:3.12.1

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /app/

#Expose the container port to the host machine
EXPOSE 8000 

#Run app
CMD [“python”, “manage.py”, “runserver”, “0.0.0.0:8000”]  