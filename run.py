from src.main.server.server import app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("run:app", host="localhost", port=8000, reload=True)
