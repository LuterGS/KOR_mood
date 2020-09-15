import pandas as pd
import ML1.NeuralNet1 as nn1
import ML2.NeuralNet2 as nn2
import sys

NeuralNet1 = nn1.NeuralNet1(None)
NeuralNet2 = nn2.Network2()
NeuralNet2.test_ready()
print("two model all ready")


def get_output():
    filename = sys.argv[1]
    filedata = pd.read_table(filename)

    for i in range(len(filedata)):
        n1_result = NeuralNet1.sentiment_predict(filedata['document'][i], True)
        n2_result = NeuralNet2.get_tokenized_sentence(filedata['document'][i])
        if (n1_result + n2_result) / 2 > 0.5:
            filedata.loc[i, ['label']] = 1
        else:
            filedata.loc[i, ['label']] = 0

    filedata.to_csv("result.txt", sep='	', float_format='%.0f')





if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("아무 값도 인자로 주지 않았습니다. 프로그램을 종료합니다.")
    elif len(sys.argv) == 2:
        get_output()
        print("result.txt로 저장되었습니다.")
    else:
        print("비정상적인 입력입니다. 프로그램을 종료합니다.")