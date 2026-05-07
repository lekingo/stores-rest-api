FROM python:3.13
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["sh", "-c", "flask db upgrade && flask run --host 0.0.0.0"]