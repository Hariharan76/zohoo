#DockerFile,image,container
FROM python:3.10
ADD main.py .

RUN pip install numpy pandas

CMD [ "python","./main.py" ]
