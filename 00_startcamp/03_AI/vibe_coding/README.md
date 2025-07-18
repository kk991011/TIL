# 저녁 메뉴 추천 프로젝트 (Dinner Menu Recommender)

## 프로젝트 개요
- 목적: 사용자의 취향과 상황에 맞는 저녁 메뉴를 추천하는 파이썬 기반 응용 프로그램 개발
- 대상: 누구나 쉽게 사용할 수 있는 데스크탑/웹/CLI 형태의 추천 시스템
- 주요 기능:
 1. 메뉴 데이터 관리(추가/수정/삭제)
 2. 메뉴별 레시피 제공 기능
 3. 사용자 입력(취향, 상황, 재료, 어제 먹은 음식, 알레르기 정보, 매운맛 선호, 오늘 날씨 등) 기반 맞춤형 추천
 4. 추천 결과 시각화 및 저장
 5. 향후 확장: GUI(PYQT5), 웹(Flask), AI 추천 알고리즘 등

## 개발 워크플로우
1. **기획 및 요구사항 정의**
   - 추천 방식(랜덤, 조건 기반, AI)
   - 사용자 입력 방식(텍스트, 체크박스 등)
   - 데이터 저장 방식(CSV, DB 등)
   - 메뉴별 레시피 데이터 관리
   - 사용자 정보(어제 먹은 음식, 알레르기, 매운맛 선호, 날씨 등) 기반 추천 로직
2. **폴더 및 파일 구조 설계**
   - main.py: 진입점
   - recommender/: 핵심 모듈
     - __init__.py
     - loader.py: 메뉴 데이터 로딩
     - recommender.py: 추천 로직
     - visualizer.py: 결과 출력
     - recipe.py: 메뉴별 레시피 제공 모듈
     - user_profile.py: 사용자 정보 관리 및 맞춤형 추천 모듈
   - data/: 메뉴 데이터 파일(menu.csv)
   - tests/: 테스트 코드(test_recommender.py)
   - gui/: GUI 코드(main_gui.py)
3. **기본 기능 구현**
   - 메뉴 데이터 로딩 및 관리
   - 추천 알고리즘(랜덤/조건 기반)
   - CLI 인터페이스
   - 메뉴별 레시피 출력 기능
   - 사용자 정보 기반 맞춤형 추천 기능
4. **테스트 코드 작성 및 검증**
   - 단위 테스트, 통합 테스트
5. **GUI/웹 확장**
   - PyQt5 기반 GUI
   - Flask 기반 웹앱(선택)
6. **고도화 및 배포**
   - AI 추천(사용자 피드백 반영)
   - 패키징 및 배포

## 개발 환경 및 권장 사항
- Python 3.8 이상
- 필수 패키지: pandas, PyQt5(선택), Flask(선택)
- 코드 스타일: PEP8, 주석 및 문서화 철저

---

### 예시 폴더 구조
```
dinner_menu_recommender/
├── main.py
├── recommender/
│   ├── __init__.py
│   ├── loader.py
│   ├── recommender.py
│   └── visualizer.py
│   ├── recipe.py
│   └── user_profile.py
├── data/
│   └── menu.csv
│   └── recipe.csv
│   └── user_profile_example.json
├── tests/
│   └── test_recommender.py
│   └── test_user_profile.py
├── gui/
│   └── main_gui.py
└── README.md
```

---

### 추가 안내
- 모든 코드는 10년차 파이썬 개발자의 관점에서 작성
- 확장성과 유지보수성을 고려한 구조 설계
- 추가 기능 요청 시 언제든 문의 가능
