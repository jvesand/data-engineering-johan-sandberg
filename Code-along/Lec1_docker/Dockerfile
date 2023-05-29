FROM python:3.11

# changes pwd in container
WORKDIR /app

# ADD main.py .

# copy main.py (in the current folder) to the pwd
# copy is more commonly used than ADD
COPY requirements.txt main.py .

# RUN pip install plotly_express dash
RUN pip install -r requirements.txt

# informs Docker that container listens to this port at runtime
EXPOSE 8050

CMD ["python3", "./main.py"]
