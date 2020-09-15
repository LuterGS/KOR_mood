import os
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

filepath = os.path.dirname(os.path.abspath(__file__))

class Network2:
    tokenizer = Tokenizer()

    def __init__(self):
        """/
        # init model 0번째 모델
        layer1 = tf.keras.layers.Embedding(19417, 200),
        layer2 = tf.keras.layers.GRU(units=128),
        layer3 = tf.keras.layers.Dropout(rate=0.2),
        layer4 = tf.keras.layers.GRU(units=64),
        layer5 = tf.keras.layers.Flatten(),
        layer6 = tf.keras.layers.BatchNormalization(axis=1, epsilon=1.001e-5),
        layer7 = tf.keras.layers.Dropout(rate=0.2),
            # tf.keras.layers.LSTM(units=64, return_sequences=False),

        layer_plus = tf.keras.layers.Add()([layer1, layer2])
        
        layer8 = tf.keras.layers.Dense(units=2, activation='softmax')[layer_plus]
        """

        """ 1번째 모델
        input1 = tf.keras.layers.Input(shape=(30, ))
        x1 = tf.keras.layers.Embedding(19417, 200)(input1)
        x2 = tf.keras.layers.GRU(units=128, return_sequences=True)(x1)
        x2 = tf.keras.layers.GRU(units=64)(x2)
        x2 = tf.keras.layers.Dropout(rate=0.3)(x2)
        x1 = tf.keras.layers.Flatten()(x1)
        x1 = tf.keras.layers.Dense(units=64)(x1)
        added = tf.keras.layers.Add()([x1, x2])
        # x3 = tf.keras.layers.BatchNormalization(axis=1, epsilon=1.001e-5)(added)
        out = tf.keras.layers.Dense(units=2, activation='softmax')(added)
        """

        """ 2번째 모델
        input1 = tf.keras.layers.Input(shape=(30, ))
        x1 = tf.keras.layers.Embedding(19417, 200)(input1)
        x1 = tf.keras.layers.GRU(units=200, return_sequences=True)(x1)
        x1 = tf.keras.layers.GRU(units=100, return_sequences=False)(x1)
        x1 = tf.keras.layers.Dropout(rate=0.3)(x1)
        out = tf.keras.layers.Dense(units=2, activation='softmax')(x1)
        """

        """ 3번째 코드
        input1 = tf.keras.layers.Input(shape=(30, ))
        x1 = tf.keras.layers.Embedding(19417, 200)(input1)
        x2 = tf.keras.layers.LSTM(units=200, return_sequences=True)(x1)
        x1 = tf.keras.layers.Add()([x1, x2])
        x1 = tf.keras.layers.Flatten()(x1)
        out = tf.keras.layers.Dense(units=2, activation='softmax')(x1)
        """
    
        """    # 4번째 코드 (basic)
        input1 = tf.keras.layers.Input(shape=(30, ))
        x1 = tf.keras.layers.Embedding(19417, 200)(input1)
        x1 = tf.keras.layers.LSTM(128)(x1)
        out = tf.keras.layers.Dense(2, activation='softmax')(x1)
        """
        """# 5번째 코드
        input1 = tf.keras.layers.Input(shape=(30,))
        x = tf.keras.layers.Embedding(19417, 200)(input1)
        x = tf.keras.layers.Dropout(rate=0.5)(x)
        
        x1 = tf.keras.layers.Conv1D(filters=128, kernel_size=3, padding="valid", activation="relu", strides=1)(x)
        x1 = tf.keras.layers.GlobalMaxPooling1D()(x1)
        x1 = tf.keras.layers.Flatten()(x1)

        x2 = tf.keras.layers.Conv1D(filters=128, kernel_size=3, padding="valid", activation="relu", strides=1)(x)
        x2 = tf.keras.layers.GlobalMaxPooling1D()(x2)
        x2 = tf.keras.layers.Flatten()(x2)

        x3 = tf.keras.layers.Conv1D(filters=128, kernel_size=3, padding="valid", activation="relu", strides=1)(x)
        x3 = tf.keras.layers.GlobalMaxPooling1D()(x3)
        x3 = tf.keras.layers.Flatten()(x3)

        x = tf.keras.layers.Concatenate()([x1, x2, x3])
        x = tf.keras.layers.Dropout(rate=0.8)(x)
        x = tf.keras.layers.Dense(128)(x)
        out = tf.keras.layers.Dense(2, activation="softmax")(x)"""

        # 6번째 코드
        input1 = tf.keras.layers.Input(shape=(30,))
        x = tf.keras.layers.Embedding(2980, 200)(input1)
        x = tf.keras.layers.Dropout(rate=0.5)(x)

        x = tf.keras.layers.Conv1D(filters=200, kernel_size=3, padding="valid", activation="relu", strides=1)(x)
        x1 = tf.keras.layers.BatchNormalization(epsilon=1.001e-5)(x)
        x1 = tf.keras.layers.Activation('relu')(x1)

        x = tf.keras.layers.Add()([x, x1])
        x = tf.keras.layers.Activation('relu')(x)

        x = tf.keras.layers.Conv1D(filters=100, kernel_size=3, padding="valid", activation="relu", strides=1)(x)
        x2 = tf.keras.layers.BatchNormalization(epsilon=1.001e-5)(x)
        x2 = tf.keras.layers.Activation('relu')(x2)

        x = tf.keras.layers.Add()([x, x2])
        x = tf.keras.layers.Activation('relu')(x)

        x = tf.keras.layers.Conv1D(filters=50, kernel_size=3, padding="valid", activation="relu", strides=1)(x)
        x3 = tf.keras.layers.BatchNormalization(epsilon=1.001e-5)(x)
        x3 = tf.keras.layers.Activation('relu')(x3)

        x = tf.keras.layers.Add()([x, x3])
        x = tf.keras.layers.Activation('relu')(x)

        x = tf.keras.layers.Dropout(rate=0.5)(x)
        x = tf.keras.layers.Flatten()(x)
        # x = tf.keras.layers.Dense(300, 'relu')(x)
        out = tf.keras.layers.Dense(1, activation='sigmoid')(x)

        self.model = tf.keras.models.Model(inputs=[input1], outputs=out)
        self.earlyStop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=4, restore_best_weights=True)
        self.model_checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath="checkpoint", monitor='val_accuracy', mode='max', verbose=1, save_best_only=True)
        self.model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
        self.model.summary()

    def test_ready(self):
        self.model.load_weights(filepath + '/variables')
        with open(filepath + '/tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)

    def get_tokenized_sentence(self, sentence):
        word_list = []
        sentence = sentence.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "")
        for word in sentence:
            word_list.append(word)
        encoded = self.tokenizer.texts_to_sequences([word_list])
        padding_sentence = pad_sequences(encoded, maxlen=30)
        score = float(self.model.predict(padding_sentence))
        # 1이 긍정, 0이 부정
        return score


if __name__ == "__main__":
    test = Network2()
    test.test_ready()
    print(test.get_tokenized_sentence("오늘은 날씨가 나쁘"))

