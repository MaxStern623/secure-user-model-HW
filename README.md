# Calculator-command-line-100--test

Minimal user model example with SQLAlchemy, Pydantic, hashing, tests, and CI.

Running tests locally

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run tests:

```bash
pytest -q
```

Docker Hub

Docker image will be pushed to Docker Hub via CI. Add your Docker Hub repo link here after pushing:

https://hub.docker.com/repository/docker/YOUR_USERNAME/calculator
