FROM tensorflow/tensorflow:latest

RUN pip install --upgrade pip \
                pandas

ADD ./input.txt /home/
ADD ./evaluation.sh /home/
ADD ./main.py /home/
ADD ./ML1 /home/ML1
ADD ./ML2 /home/ML2

WORKDIR /home/