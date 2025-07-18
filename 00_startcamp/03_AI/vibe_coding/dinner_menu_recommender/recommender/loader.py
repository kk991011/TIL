import requests
import os
"""
loader.py - 메뉴 및 레시피 데이터 로딩 모듈
"""
import pandas as pd

def load_menu(menu_path):
    """
    메뉴 데이터 로딩 및 필수 컬럼 검증
    """
    try:
        df = pd.read_csv(menu_path)
    except Exception as e:
        print(f"[오류] 메뉴 데이터 로딩 실패: {e}")
        return None
    required_cols = [
        'name', 'ingredients', 'spicy', 'carbohydrate(g)', 'protein(g)', 'fat(g)', 'calorie(kcal)'
    ]
    for col in required_cols:
        if col not in df.columns:
            print(f"[오류] 메뉴 데이터에 '{col}' 컬럼이 없습니다.")
            return None
    return df

def load_recipe(recipe_path):
    """
    레시피 데이터 로딩 및 필수 컬럼 검증
    """
    try:
        df = pd.read_csv(recipe_path)
    except Exception as e:
        print(f"[오류] 레시피 데이터 로딩 실패: {e}")
        return None
    required_cols = ['name', 'recipe', 'difficulty', 'time(min)']
    for col in required_cols:
        if col not in df.columns:
            print(f"[오류] 레시피 데이터에 '{col}' 컬럼이 없습니다.")
            return None
    return df

def load_user_meal_list(meal_list):
    """
    최근 일주일 식단(메뉴명 리스트) 입력값 검증 및 반환
    """
    if not isinstance(meal_list, list):
        print("[오류] 식단 정보는 리스트 형식이어야 합니다.")
        return []
    return [str(menu).strip() for menu in meal_list if menu]

def get_weather_status(city="Daejeon", api_key=None):
    """
    대전 지역 날씨 상태(맑음, 비, 눈, 흐림 등) 자동 조회 (OpenWeatherMap API 예시)
    """
    if api_key is None:
        api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("[오류] 날씨 API 키가 필요합니다.")
        return None
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=kr&units=metric"
    try:
        resp = requests.get(url)
        data = resp.json()
        weather = data['weather'][0]['main']
        # 한글 변환 및 상태 매핑
        mapping = {
            'Clear': '맑음',
            'Clouds': '흐림',
            'Rain': '비',
            'Snow': '눈',
            'Drizzle': '비',
            'Thunderstorm': '비',
            'Mist': '흐림',
            'Fog': '흐림',
        }
        return mapping.get(weather, weather)
    except Exception as e:
        print(f"[오류] 날씨 정보 조회 실패: {e}")
        return None

def filter_menu_by_avoid(menu_df, avoid_ingredients=None):
    """
    피해야 할 재료(예: 날 생선 등) 포함 메뉴 제외
    """
    if not avoid_ingredients:
        return menu_df
    avoid_ingredients = [str(x).strip() for x in avoid_ingredients]
    def contains_avoid(row):
        for ing in avoid_ingredients:
            if ing in row['ingredients']:
                return True
        return False
    return menu_df[~menu_df.apply(contains_avoid, axis=1)]

def filter_menu_by_nutrition(menu_df, nutrition_filter=None):
    """
    영양성분 조건(예: 저칼로리, 고단백 등) 필터링
    nutrition_filter: dict, 예시 {'calorie(kcal)': ('<=', 300), 'protein(g)': ('>=', 15)}
    """
    if not nutrition_filter:
        return menu_df
    df = menu_df.copy()
    for col, (op, val) in nutrition_filter.items():
        if col not in df.columns:
            continue
        if op == '>=':
            df = df[df[col] >= val]
        elif op == '<=':
            df = df[df[col] <= val]
        elif op == '>':
            df = df[df[col] > val]
        elif op == '<':
            df = df[df[col] < val]
        elif op == '==':
            df = df[df[col] == val]
    return df
