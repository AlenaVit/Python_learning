fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": " a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in brunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)

nice = fruit.copy()
nice.update(veg)
print(nice)