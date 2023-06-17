# Fortress for 2 player

<img alt="Pyhton" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=black"/> 

## pygame 으로 작성한 2인용 포트리스 게임입니다. 
### 해당 소스코드를 clone 한 후, vscode에서 폴더를 열어주세요.
### 터미널에서 pip install pygame 입력 하여 pygame 라이브러리 설치 후

### main.py에서 F5로 실행해서 사용해주세요<br><br>
[오류 발생시](#오류발생시)


#### 실행시 맵을 고르면 두명의 플레이어중 무작위로 한명의 턴이 시작됩니다.<br>턴 플레이어의 탱크 위에는 검은색 점이 떠있습니다<br> 해당 플레이어는 방향키로 이동하여 스페이스바를 길게 눌러 상대를 겨냥해서 탄환을 발사합니다.<br> 맞은 적은 상단에 있는 HP가 줄어들고 각 플레이어 사이드 상단의 HP바에서 확인할 수 있습니다.<br>먼저 상대의HP를 0으로 만든 플레이어가 승리하는 게임입니다.
![forgif](https://github.com/present0917/Fortress5/assets/49800800/9deba11f-b94a-463a-92f0-9413e94d8596)




<br>
프로젝트는 Github flow 방식으로 진행합니다
Pull Request 진행 및 커밋시<br> 수정한 모든 부분에 대해 잘 작성해주세요
rebase 하여 충돌을 최소화하며 진행

Pull Request 기준
제목 앞에 태그를 붙여주세요

| 태그    | 상황                    |
|---------|------------------------|
| Feat    | 새로운 기능을 추가할 경우   |
| Fix     | 버그를 고친 경우          |
| Design  | 디자인 변경        |
| Comment | 필요한 주석 추가 및 변경 |
| Docs    | 문서를 수정한 경우  |


# 오류발생시
pip install pygame --pre 명령어로 설치 시도 해주세요.
python을 3.10 버전으로 다운그레이드 해주세요.
python -m pip install -U pygame==2.4.0 명령어로 패키지 설치 시도 해주세요.

