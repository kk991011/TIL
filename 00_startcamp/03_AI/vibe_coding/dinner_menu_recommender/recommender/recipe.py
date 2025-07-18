"""
recipe.py - 메뉴별 레시피 제공 모듈
"""
def get_recipe(recipe_df, menu_name):
    recipe = recipe_df[recipe_df['name'] == menu_name]
    if not recipe.empty:
        return recipe.iloc[0]['recipe']
    return "레시피 정보가 없습니다."
