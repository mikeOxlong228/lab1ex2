#FROM ubuntu:latest
FROM python:3

WORKDIR /usr/src/app

RUN git init
RUN git config --global user.name "Ion"
RUN git config --global user.email "ion.matei@student.tuiasi.ro"
#RUN git remote remove origin
#RUN git remote add origin "https://github.com/mikeOxlong228/lab1ex2"
RUN git clone "https://github.com/mikeOxlong228/lab1ex2"


WORKDIR /usr/src/app/lab1ex2

CMD ["/bin/bash"]
#CMD [ "python3", "./application.py" ]