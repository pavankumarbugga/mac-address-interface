FROM python:3.6.9

COPY * .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "./main.py"]

# If something to be set by default argument
#CMD [ "44:38:39:ff:ef:57" ]