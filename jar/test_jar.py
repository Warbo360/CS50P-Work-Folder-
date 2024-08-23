from jar import Jar
import pytest

def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    jar2 = Jar(8)
    assert jar2.capacity == 8
    with pytest.raises(ValueError):
        jar3 = Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar4 = Jar()
    jar4.deposit(2)
    assert jar4.size == 2
    jar5 = Jar()
    with pytest.raises(ValueError):
        jar5.deposit(20)

def test_withdraw():
    jar6 = Jar()
    jar6.deposit(8)
    jar6.withdraw(4)
    assert jar6.size == 4
    with pytest.raises(ValueError):
        jar6.withdraw(7)
