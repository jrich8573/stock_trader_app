# TODO:  added comments 
# python version to use
FROM python:3.9

# env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# set working directory
WORKDIR /app

# copy requirements into working dir
COPY requirements.txt /app/

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# copy app code into working dir
COPY . /app/

# port to run app
EXPOSE 8000

# gunicorn to run the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "run:app"]