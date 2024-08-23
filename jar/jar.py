class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f'{self.size*"🍪"}'

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('Invalid capacity')
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError('Too many cookies')
        if size < 0:
            raise ValueError('Too few cookies')
        self._size = size

def main():
    jar1 = Jar(8)
    print(jar1)
    jar1.deposit(3)
    print(jar1.size)
    print(jar1.capacity)
    print(jar1)
    jar1.withdraw(2)
    print(jar1)

if __name__ == '__main__':
    main()
