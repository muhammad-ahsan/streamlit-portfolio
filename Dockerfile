FROM python:3.9-slim

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
COPY lib .

COPY .streamlit .
COPY Summary.py .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health


RUN pipenv install --system --deploy --ignore-pipfile
ENTRYPOINT ["streamlit", "run", "Summary.py", "--server.port=8501", "--server.address=0.0.0.0"]