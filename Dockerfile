FROM python:3.9-slim

ENV PYTHONPATH=/test_paysend
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /test_paysend/
COPY . /test_paysend/
CMD ["python", "app/main.py"]