FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/* ./src/
CMD ["python", "src/QR_Generator2.py"] # sample file run



Dockerfile k8s-deployement.yaml k8s-service.yaml LICENSE README.md requirements.txt