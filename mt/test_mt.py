import mt

def test_both_true():
    assert mt.monkey_trouble(True, True) == True

def test_both_false():
    assert mt.monkey_trouble(False, False) == True

def test_mixed():
    assert mt.monkey_trouble(True, False) == False
    assert mt.monkey_trouble(False, True) == False
