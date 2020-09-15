FROM tensorflow/tensorflow:latest

RUN pip install --upgrade pip \
                pandas

ADD ./input.txt /home/
ADD ./evaluation.sh /home/
ADD ./main.py /home/
ADD ./ML1 /home/
ADD ./ML2 /home/

WORKDIR /home/