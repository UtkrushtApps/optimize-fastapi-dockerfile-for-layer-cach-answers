# Solution Steps

1. 1. Create a new `Dockerfile`. Set the base image to `python:3.11-slim`.

2. 2. Add `WORKDIR /app` to set a working directory inside the image where all files are managed.

3. 3. To leverage Docker layer caching, copy only `requirements.txt` to the image first using `COPY requirements.txt ./`.

4. 4. Install dependencies with `RUN pip install --no-cache-dir -r requirements.txt`. By copying only `requirements.txt` before, this layer is cached unless dependencies change.

5. 5. Copy the rest of the app source code into the container using `COPY . .`.

6. 6. Expose port 8000 with `EXPOSE 8000`, so FastAPI can be accessed externally.

7. 7. Add the container start command: `CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]`.

8. 8. Create `requirements.txt` with FastAPI and Uvicorn as dependencies.

9. 9. Create `main.py` with a functional FastAPI notes API: endpoints for creating, listing, retrieving, and deleting notes.

10. 10. Build the Docker image the first time: `docker build -t fastapi-notes .`. It should install dependencies freshly.

11. 11. Build the Docker image a second time (without changing requirements): `docker build -t fastapi-notes .`. This time the `pip install` step should use the cache, making the build much faster.

12. 12. Start a container: `docker run -p 8000:8000 fastapi-notes`.

13. 13. Test the API (e.g., via curl or http client), and ensure FastAPI endpoints are accessible at `localhost:8000` and logs print as expected.

