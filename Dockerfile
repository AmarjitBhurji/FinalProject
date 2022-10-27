FROM python:3.8
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 4000
RUN python3 create.py
ENTRYPOINT ["python3", "app.py"]
