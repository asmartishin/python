def cakes(recipe, available):
    num = []
    for k, v in recipe.items():
        if k in available:
            num.append(available[k] // recipe[k])
        else:
            return 0
    return min(num)

print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))