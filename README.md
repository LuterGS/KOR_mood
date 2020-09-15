# 2020 국어 정보 처리 시스템 경진대회

## 목차

1. [프로그램 실행방법](#프로그램-실행방법)
1. [Dockerfile로 실행하는법](#dockerfile로-실행하는법)
1. [Docker image로 실행하는법](#docker-image로-실행하는법)

### 프로그램 실행방법

테스트할 파일셋은 `input.txt`이어야 하며, 다음과 같은 형식을 따라야 합니다.

#### input.txt 예시

```
document label
문장1
오늘은 기분이 좋다
오늘은 기분이 나쁘다
...
```

`result.txt`은 모델이 평가한 결과값이며 label에 긍정일 경우 1, 부정일 경우 0이 출력됩니다.

#### result.txt 예시

```
document label
문장1 1
오늘은 기분이 좋다 1
오늘은 기분이 나쁘다 0
```

### Dockerfile로 실행하는법

Docker file로 실행하려면 먼저 해당 repository 를 clone하거나 코드를 저장합니다.

해당경로로 이동한 후 평가 데이터를 위 형식에 맞게 `input.txt`로 저장해줍니다.

이후 아래의 명령어를 통해 Dockerfile로 Docker image를 생성해줍니다.

```sh
docker build -t kormood:1.0 .
```

그러면 `docker images`로 아래와 같이 이미지가 생성된 것을 확인할 수 있습니다.

```sh
REPOSITORY                TAG                                  IMAGE ID            CREATED             SIZE
kormood            1.0                                  7daff282105c        5 hours ago         1.67GB
```

이제 만들어진 docker image를 바탕으로 아래의 코드를 입력해 container를 만들어 실행해줍니다.

```sh
docker run -it kormood:1.0
```

그러면 `/home/` 경로에 위치한 docker container가 실행될텐데 `./evaluation.sh` 명령어를 통해 프로그램을 실행시켜줍니다.

그러면 `result.txt`로 label이 붙어있는 결과값이 나오게 됩니다.

### Docker image로 실행하는법

먼저 `docker login`을 통해 docker를 로그인해줍니다.

이후 아래 명령어를 통해 docker image를 pull 해옵니다.

```sh
docker pull azzyjk/kormood:1.0
```

그러면 `docker images`로 아래와 같이 이미지가 생성된 것을 확인할 수 있습니다.

```sh
REPOSITORY                TAG                                  IMAGE ID            CREATED             SIZE
azzyjk/kormood            1.0                                  7daff282105c        5 hours ago         1.67GB
```

이제 pull해온 docker image를 바탕으로 아래의 코드를 입력해 container를 만들어 실행해줍니다.

```sh
docker run -it kormood:1.0
```

container가 실행된 후 `/home/` 경로를 보면 `input.txt` 파일이 있습니다.

해당 파일과 같이 양식에 맞춰서 평가 데이터를 입력해줍니다.

이후 `./evaluation.sh` 명령어를 통해 프로그램을 실행시켜줍니다.

그러면 `result.txt`로 label이 붙어있는 결과값이 나오게 됩니다.
