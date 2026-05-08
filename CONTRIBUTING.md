# CONTRIBUTING

## How to run the Dockerfile locally

Add more information about how to build the image.

```
docker run -dp 5000:5000 -w /app -v "%cd%:/app" IMAGE_NAME sh -c "flask db upgrade && flask run --host 0.0.0.0"
```

Add more information about how to run the image.