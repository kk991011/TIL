"""
loader.py - 메뉴 및 레시피 데이터 로딩 모듈
"""
import pandas as pd

def load_menu(menu_path):
    return pd.read_csv(menu_path)

def load_recipe(recipe_path):
    return pd.read_csv(recipe_path)
