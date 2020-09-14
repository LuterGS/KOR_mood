테스트할 파일셋은 input.txt이어야 하며, 다음과 같은 형식을 따라야 합니다.

document	label
문장1	
오늘은 기분이 좋다	
오늘은 기분이 나쁘다
...

파일이 도커 내부에 있다면, 도커 내부에 쉘로 접속 후

python NeuralNet.py input.txt 혹은
./evaluate.sh 를 입력해 실행합니다.

이후, result.txt로 출력값이 나오게 되며, label에 긍정일 경우 1, 부정일 경우 0이 출력됩니다.


result.txt 예시
document	label
문장1	1
오늘은 기분이 좋다	1
오늘은 기분이 나쁘다	0