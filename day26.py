def add(a, b):
    return a + b

# assert add(2, 3) == 6

# Why this matters (real world)
# Prevents breaking working code
# Useful in automation scripts
# Critical in production systems

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 5
    assert add(0, 0) == 0

test_add()
