FROM python:3.9
LABEL maintainer="Lisa.L.Crowell@gmail.com"
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . code
WORKDIR /code
EXPOSE 8000
CMD ["./startup.sh"]