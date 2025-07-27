# there are 3 threads - i dont know which one will run first
from threading import Condition
class Foo:
    def __init__(self):
        self.cond = Condition()
        self.done = 1

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        with self.cond:
            printFirst()
            self.done = 2
            self.cond.notify_all()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.cond:
            while self.done != 2:
                self.cond.wait()
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.done = 3
            self.cond.notify_all()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.cond:
            while self.done != 3:
                self.cond.wait()
            # printThird() outputs "third". Do not change or remove this line.
            printThird()