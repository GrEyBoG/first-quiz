################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!
# def make_oven():
#   None

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()



# Actualizaremos la clase Oven para asegurarnos de que no haya impresiones en los métodos
class Oven:
    def __init__(self):
        self.ingredients = []
        self.temperature = None

    def add(self, item):
        self.ingredients.append(item)

    def freeze(self):
        # Asegúrate de que no haya ningún print aquí
        self.temperature = 'frozen'

    def boil(self):
        # Asegúrate de que no haya ningún print aquí
        self.temperature = 'boiling'

    def wait(self):
        # Asegúrate de que no haya ningún print aquí
        self.temperature = 'waiting'

    def get_output(self):
        # Aquí tampoco debería haber prints
        if self.temperature == 'boiling' and "lead" in self.ingredients and "mercury" in self.ingredients:
            return "gold"
        elif self.temperature == 'frozen' and "water" in self.ingredients and "air" in self.ingredients:
            return "snow"
        elif self.temperature == 'boiling' and all(ingredient in self.ingredients for ingredient in ["cheese", "dough", "tomato"]):
            return "pizza"
        else:
            return "unknown combination"

# La función make_oven no debería cambiar
def make_oven():
    return Oven()

# La función alchemy_combine tampoco debería cambiar
def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()

    return oven.get_output()

# Redefinimos la función de prueba test_alchemy_combine para asegurarnos de que no haya prints
# def test_alchemy_combine():
#     assert alchemy_combine(make_oven(), ["lead", "mercury"], 5000) == "gold", "Failed to create gold"
#     assert alchemy_combine(make_oven(), ["water", "air"], -100) == "snow", "Failed to create snow"
#     assert alchemy_combine(make_oven(), ["cheese", "dough", "tomato"], 150) == "pizza", "Failed to create pizza"
#     print("All tests passed successfully.")

# Ejecutamos la función de prueba
# test_alchemy_combine()

