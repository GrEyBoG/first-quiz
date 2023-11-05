################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.
# Aquí está el código corregido para question1.py

def get_city_temperature(city):
   if city == "Quito":
      return 22
   if city == "Sao Paulo":
      return 17
   if city == "San Francisco":
      return 16
   if city == "New York":
      return 14  # Se añade la temperatura para New York

def get_city_weather(city):
   sky_condition = None

   if city == "Sao Paulo":
      sky_condition = "cloudy"
   elif city == "New York":
      sky_condition = "rainy"
   elif city == "Quito":
      sky_condition = "sunny"  # Se añade la condición del cielo para Quito

   temperature = get_city_temperature(city)
   if temperature is None or sky_condition is None:
      return "No data available"  # Manejo en caso de que no haya datos disponibles
   return str(temperature) + " degrees and " + sky_condition


#################### Pruebas ####################
def test_get_city_weather():
   assert get_city_weather("Quito") == "22 degrees and sunny"
   print("Test 1 passed")
   assert get_city_weather("New York") == "14 degrees and rainy"
   print("Test 2 passed")

# test_get_city_weather()
