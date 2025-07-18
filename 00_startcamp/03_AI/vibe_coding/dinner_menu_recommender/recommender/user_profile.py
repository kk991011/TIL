"""
user_profile.py - 사용자 정보 관리 및 맞춤형 추천
"""
import json

def load_user_profile(profile_path):
    with open(profile_path, 'r', encoding='utf-8') as f:
        return json.load(f)
