FROM tensorflow/tensorflow:latest

RUN pip install --upgrade pip \
                pandas

ADD ./input.txt /home/
ADD ./evaluation.sh /home/
ADD ML1/best_model.h5 /home/
ADD ML1/NeuralNet1.py /home/
ADD ML1/tokenizer.pickle /home/

WORKDIR /home/
# CMD ["python", "/home/NeuralNet1.py", "/home/input.txt"]