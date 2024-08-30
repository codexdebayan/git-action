class Hello:
    @staticmethod
    def hello_world():
        return "Hello world"

if __name__ == '__main__':
    greeting = Hello.hello_world()
    print(greeting)
