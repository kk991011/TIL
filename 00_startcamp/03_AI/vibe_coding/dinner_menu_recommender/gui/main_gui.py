"""
main_gui.py - PyQt5 기반 저녁 메뉴 추천 GUI

# 필요한 패키지 설치 명령어 (터미널에서 실행)
# pip install pyqt5 pandas requests
"""
import sys
import os
# 상위 폴더를 모듈 경로에 추가하여 recommender 임포트 오류 방지
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QTextEdit, QSpinBox
)
from recommender.loader import (
    load_menu, load_recipe, get_weather_status, filter_menu_by_avoid, filter_menu_by_nutrition
)
import os

class DinnerMenuGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("저녁 메뉴 추천기")
        self.setGeometry(100, 100, 500, 600)
        layout = QVBoxLayout()

        layout.addWidget(QLabel("매운맛 선호도 (1~5):"))
        self.spicy_pref = QSpinBox()
        self.spicy_pref.setRange(1, 5)
        layout.addWidget(self.spicy_pref)

        layout.addWidget(QLabel("알레르기 정보 (쉼표로 구분):"))
        self.allergy_input = QLineEdit()
        layout.addWidget(self.allergy_input)

        layout.addWidget(QLabel("피해야 할 재료 (쉼표로 구분, 예: 날생선, 회, 초밥):"))
        self.avoid_input = QLineEdit()
        layout.addWidget(self.avoid_input)

        layout.addWidget(QLabel("영양성분 조건 (숫자값 입력, 예: calorie(kcal)<=300, protein(g)>=15):"))
        self.nutrition_input = QLineEdit()
        layout.addWidget(self.nutrition_input)

        layout.addWidget(QLabel("최근 일주일 식단 (쉼표로 구분):"))
        self.meal_list_input = QLineEdit()
        layout.addWidget(self.meal_list_input)

        layout.addWidget(QLabel("오늘 날씨를 입력하세요 (예: 맑음, 비, 눈, 흐림):"))
        self.weather_input = QLineEdit()
        layout.addWidget(self.weather_input)

        self.recommend_btn = QPushButton("추천 메뉴 보기")
        self.recommend_btn.clicked.connect(self.safe_recommend_menu)
        layout.addWidget(self.recommend_btn)

        layout.addWidget(QLabel("추천 결과 (3개):"))
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        layout.addWidget(self.result_area)

        # 데이터 로딩 (인스턴스 변수로 선언)
        menu_path = os.path.join(os.path.dirname(__file__), '../data/menu.csv')
        recipe_path = os.path.join(os.path.dirname(__file__), '../data/recipe.csv')
        self.menu_df = load_menu(menu_path)
        self.recipe_df = load_recipe(recipe_path)
        # menu_df가 None이거나 필수 컬럼이 없으면 안내 메시지 출력
        if self.menu_df is None or not all(col in self.menu_df.columns for col in ['name','ingredients','spicy','carbohydrate(g)','protein(g)','fat(g)','calorie(kcal)']):
            self.result_area.setText("menu.csv 파일의 첫 줄에 반드시 헤더가 있어야 합니다.\n헤더: name,ingredients,spicy,carbohydrate(g),protein(g),fat(g),calorie(kcal)\n데이터를 올바르게 입력해 주세요.")

        self.setLayout(layout)
    def safe_recommend_menu(self):
        try:
            self.recommend_menu()
        except Exception as e:
            self.result_area.setText(f"추천 메뉴 처리 중 오류 발생: {str(e)}")



    def recommend_menu(self):
        try:
            if self.menu_df is None or self.recipe_df is None:
                self.result_area.setText("menu.csv 또는 recipe.csv를 불러올 수 없습니다. 파일 경로와 형식을 확인하세요.")
                return
            df = self.menu_df.copy()
            # 알레르기, 피해야 할 재료
            allergy = [x.strip() for x in self.allergy_input.text().split(',') if x.strip()]
            avoid = [x.strip() for x in self.avoid_input.text().split(',') if x.strip()]
            avoid += allergy
            if avoid:
                df = filter_menu_by_avoid(df, avoid)
            # 최근 식단 제외
            recent_meals = [x.strip() for x in self.meal_list_input.text().split(',') if x.strip()]
            if recent_meals:
                df = df[~df['name'].isin(recent_meals)]
            # 매운맛 선호도
            spicy_pref = self.spicy_pref.value()
            df = df[df['spicy'] == (spicy_pref >= 3)]
            # 영양성분 조건
            nutrition_filter = {}
            nut_text = self.nutrition_input.text().strip()
            if nut_text:
                for cond in nut_text.split(','):
                    cond = cond.strip()
                    if not cond:
                        continue
                    # 예: calorie(kcal) <= 300
                    for op in ['<=', '>=', '<', '>', '==']:
                        if op in cond:
                            col, val = cond.split(op)
                            col = col.strip()
                            try:
                                val = float(val.strip())
                            except:
                                continue
                            nutrition_filter[col] = (op, val)
                            break
            if nutrition_filter:
                df = filter_menu_by_nutrition(df, nutrition_filter)
            # 날씨 입력값 활용(예시: 맑음일 때만 추천, 실제 필터링은 필요에 따라 구현)
            weather = self.weather_input.text().strip()
            # 날씨별 추천 메뉴 필터링
            if weather:
                if weather == '맑음':
                    df = df[df['name'].str.contains('샐러드|파스타|스테이크|샤브샤브|비빔밥|샌드위치|스시롤|오코노미야키|카프레제샐러드|연어스테이크|오므라이스|피자|잡채|치즈돈까스|토마토리조또|불닭볶음면')]
                elif weather in ['비', '흐림', '눈']:
                    df = df[df['name'].str.contains('찌개|탕|국|국밥|라면')]
            # 추천 결과 3개 (데이터가 비어 있거나 3개 미만일 때 예외 처리)
            if df is None or len(df) == 0:
                self.result_area.setText("추천 가능한 메뉴가 없습니다.")
                return
            try:
                result = df.sample(n=min(3, len(df)))
            except Exception:
                result = df.head(3)
            text = f"오늘 날씨: {weather}\n\n"
            for _, row in result.iterrows():
                recipe_row = self.recipe_df[self.recipe_df['name'] == row['name']]
                recipe = recipe_row.iloc[0]['recipe'] if not recipe_row.empty else "레시피 정보 없음"
                text += f"메뉴: {row['name']}\n레시피: {recipe}\n칼로리: {row['calorie(kcal)']}kcal, 단백질: {row['protein(g)']}g, 지방: {row['fat(g)']}g, 난이도: {recipe_row.iloc[0]['difficulty'] if not recipe_row.empty else '-'}, 소요시간: {recipe_row.iloc[0]['time(min)'] if not recipe_row.empty else '-'}분\n---\n"
            self.result_area.setText(text)
        except Exception as e:
            self.result_area.setText(f"오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DinnerMenuGUI()
    window.show()
    sys.exit(app.exec_())

