def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    # 返回一个元组tuple
    return damage1, damage2

"""
damages = damage(3, 6)
print(type(damages))

这样获取返回结果不合适
print(damages[0],damages[1])

"""

skill1_damage,skill2_damage = damage(3, 6)


print(skill1_damage, skill2_damage)
