class Hello_world(object)
    hello = "public Hallo!"
    _hello = "protected Hallo!"
    __hello = "private Hallo!"

    def __init__(self):
        self.world = "public Hello!"
        self._world = "protected Hello World!"
        self.__world = "private Hello World!"

    def print_hello(self):
        print(self.hello)
        print(self._hello)
        print(self.__world)
        print(self.world)
        print(self._world)
        print(self.__world)


    class Hi(Hello_world):

        def print_hello(self):
                print(self.hello)
                print(self.world)
                print(self._hello)
                print(self._world)
                print(self.__hello)
                print(self.__world)

hello = Hello_world()
hello.print_hello()
print(hello.hello)
print("================")
hi = Hi()
hi.print_hello()