################################################################################
#     ____                          __     _                          ___ 
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/ 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/ 
#                                                                         
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function 
# should change (x, y) into (y, x). 
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in 
# `question2_test.py.`

# Definimos la función swapper que intercambiará los elementos de una tupla
def swapper(tup):
    return (tup[1], tup[0])

swapper_function = swapper

def run_swapper(list_of_tuples):
    return list(map(swapper_function, list_of_tuples))

# Pruebas
def test_run_swapper():
    result1 = run_swapper([("a", "b"), ("c", "d"), ("e", "f")])

    assert result1 == [("b", "a"), ("d", "c"), ("f", "e")], "Test 1 failed."

    print("Test 1 passed. Result:", result1)



    result2 = run_swapper([(1, 1), ("foo", "bar"), (13, "cows"), (None, "Some")])

    assert result2 == [(1, 1), ("bar", "foo"), ("cows", 13), ("Some", None)], "Test 2 failed."

    print("Test 2 passed. Result:", result2)


# test_run_swapper()
