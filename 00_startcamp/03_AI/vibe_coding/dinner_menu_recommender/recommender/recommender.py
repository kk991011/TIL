"""
recommender.py - 저녁 메뉴 추천 알고리즘
"""
import random

def recommend_menu(menu_df, user_profile=None):
    # TODO: 조건 기반/맞춤형 추천 구현
    return random.choice(menu_df['name'].tolist())
