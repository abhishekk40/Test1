FROM python:3
ADD myscript.py /
CMD [ "python", "./test1.py" ]
