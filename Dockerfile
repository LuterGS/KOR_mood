FROM tensorflow/tensorflow:latest

RUN pip install --upgrade pip \
                pandas

ADD ./input.txt /home/
ADD ./evaluation.sh /home/
ADD ./best_model.h5 /home/
ADD ./NeuralNet.py /home/
ADD ./tokenizer.pickle /home/

WORKDIR /home/