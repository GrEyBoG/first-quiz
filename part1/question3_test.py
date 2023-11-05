from question3 import make_oven, alchemy_combine

def test_alchemy_combine():
    result = alchemy_combine(make_oven(), ["lead", "mercury"], 5000)
    print(f"Result for lead + mercury at 5000: {result}")
    assert result == "gold", f"Expected 'gold', got '{result}'"

    result = alchemy_combine(make_oven(), ["water", "air"], -100)
    print(f"Result for water + air at -100: {result}")
    assert result == "snow", f"Expected 'snow', got '{result}'"

    result = alchemy_combine(make_oven(), ["cheese", "dough", "tomato"], 150)
    print(f"Result for cheese + dough + tomato at 150: {result}")
    assert result == "pizza", f"Expected 'pizza', got '{result}'"

    print("All tests passed successfully.")

test_alchemy_combine()