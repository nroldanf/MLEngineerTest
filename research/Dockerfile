FROM python:3.7

LABEL author="Nicolás Roldán"

# Create a working directory
RUN mkdir /ml_app
WORKDIR /ml_app

# Install Python requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Map a port
EXPOSE 8888
CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]