## 로컬에서 사용하기
`git init` 
- 내가 git 관리할 폴더 위치한 상태에서 입력
- 가장 상위 폴더라고 생각하면 편함 

`git add 하고싶은 파일` 
- 내가 올리고 싶은 파일 레파지 토리에 임시 저장 
- `git add .` : 현재 파일 올리기

`git commit -m "버전명"` 
- 버전 커밋 


`git status` 
- git 현재 상태 확인 

`git config --global user.email "내 이메일"` 
- 사용자 계정 저장하기 

`git config --global user.name "내 이름"` 
- 사용자 이름 저장하기 

`git config --global --list`
- 사용자 계정 확인하기  

`code ~/.gitconfig` 
- 현재 계정 확인하기  & 계정 수정하기 


----
## 원격 저장소랑 연결하기 
`git remote add origin [ 원격 저장소 경로]` 
- 원격 저장소 연결하기 

`git remote -v` 
- 원격 저장소 확인하기 

`git log` 
- 버전 확인하기

### add -> commit -> push 
`git push origin master` : 원격 저장소에 업로드 

`git clone url` : 원격 저장소 전체를 복제 

`git pull origin master` : 원격 저장소에서 변경 사항만 받아옴 



### 중요 사항
- init 파일 안에 또 다른 git 관리 파일이 
있으면 안된다. 

- `:q` : `vim` 환경에서 오류 발생 시 해당 창 나가기 
  - 주로, commit 시 버전 이름을 적지 않았을 때 발생한다. 

- 강사님 파일은 `복사 & 붙여넣기` 로 내 파일에 가져오기 

- git pull 하면, 원격 저장소에 있는 내용을 가져오게 된다. 
- push는 원격 저장소로 밀어 넣는 것이고, pull은 내 로컬 컴퓨터로 받는 것이다. 

  - 원격 저장소는 여러명이 같이 받는 공간이므로, 최신 버전을 받기 위해서는 pull을 하고 수정하는 방식 

# Git Branch 
- 또 다른 가지를 생성하는 것으로 하나의 원격 저장소에서 여러 명이 작업할 수 있는 환경 
- 여러 명이서 프로젝트를 동시에 관리하는 방법 
- `독립된 개발 환경`을 형성하기 때문에 원본에 대한 안전 
- 하나의 작업은 하나의 브랜치로  나누어 진행되므로 체계적인 협업과 개발이 가능 
- 손쉽게 브랜치를 생성하고 브랜치 사이를 이동할 수 있음 
- git add를 하지 않았던 파일은 브랜치가 바뀌더라고 계속 유지됨 

##  명령어 
- `git branch` : 브랜치 목록 확인 
- `git branch -r` : 원격 저장소의 브랜치 목록 확인
- `git branch 브랜치 이름` : 새로운 브랜치 생성 
- `git branch -d 브랜치 이름` :  브랜치 삭제  
- `git branch -D 브랜치 이름` :  브랜치 삭제(강제 삭제)  
- `git log --oneline --graph` : 병합 그래프 확인하기 
- `git switch 다른 브랜치 이름` : 브랜치 목록 확인
- `git switch -c 브랜치 이름` : 원격 저장소의 브랜치 목록 확인 
- `git switch -c 브랜치 이름 커밋 id` : 새로운 브랜치 생성 
- `git log --oneline` : 현재 브랜치와 commit 상태 확인 
- `git log --oneline --all` : 모든 브랜치 로그 확인 

