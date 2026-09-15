import random

his = []
name = input("your name: ")
his.append(name)

print(f"Welcome {his[0]}! Database loaded.")

while True:
   v = input("You: ").strip()
   if not v:
       continue
       
   i2 = v.split()
   ll = [f"thats nice question {his[0]}", f"there is some many answers to this question {his[0]}"]
   li0 = ["hello ", "hi ", "welcome ", "yo "]
   li1 = ["193 country", "193 country", "193 country", "193 country", "192 country", "193 country", "200 country"]
   lu = [f"cake is a tasty food lets make it {his[0]}", f"ok {his[0]}", f"i will teach you {his[0]}", f"lets cook it {his[0]}", f"nice idea {his[0]}"]
   ll2 = [". 1 -first get a pan and some sugar and flour", " first get a sugar and flour -1", "  1- first get a sugar and some flour"]
   ll3 = ["  2 - Stay calm when handling uncooked eggs. and also we need 4 eggs", f". 2 -make sure handling 4 eggs very well {his[0]}", "  we need four eggs -2"]
   ll4 = [". -3 we need some hot milk 1 cup", "  -3 some milk 1 cup", "  -3 one cup of milk"]
   ll5 = [".  -4 we need a Vegetable oil", "   -4 we need some Vegetable oil"]
   ll6 = [".  -5 we need two big spoons of Baking powder", "   -5 two big spoons of Baking powder"]
   ll7 = ["   -6 we need a Vanilla. only one small spoon", "    -6 small spoon of Vanilla"]
   ll8 = [".   -7 and if you want some salt you can add it ", "some salt"]
   lm1 = [".  - you have to mix a liquid thing in a pot Or any dish with a deep opening. and you have to mix it with The electric blender", "     you have to mix a liquid with electric blender"]
   lm2 = [".   - but every thing on a pot", "you have to put every thing on a pot"]
   lm3 = [".    - place the mixture in a mold.", "   Place the mixture in a mold. to have a good cake"]
   lm4 = [".     - Bake the mixture in the pan. for about 40 - 45 then you have a tasty cake", "Bake the mixture in the pan. for about 40 - 45"]
   
   if len(i2) >= 1:

       if i2[0].lower() in ["hello", "hi", "welcome"]:
           print("Bot:", random.choice(li0) + his[0])
           

       elif len(i2) >= 2 and i2[0].lower() == "how" and i2[1].lower() == "many" and ("country" in v.lower() or "countries" in v.lower()):
           print("Bot:", random.choice(ll), random.choice(li1))

       elif len(i2) >= 5 and i2[0].lower() == "how" and i2[1].lower() == "can" and i2[2].lower() == "i" and i2[3].lower() == "make" and "cake" in v.lower():
           print("\nBot:", random.choice(lu))
           print("--- Ingredients ---")
           print(random.choice(ll2))
           print(random.choice(ll3))
           print(random.choice(ll4))
           print(random.choice(ll5))
           print(random.choice(ll6))
           print(random.choice(ll7))
           print(random.choice(ll8))
           print("--- Steps ---")
           print(random.choice(lm1))
           print(random.choice(lm2))
           print(random.choice(lm3))
           print(random.choice(lm4))
           print("--------------------\n")