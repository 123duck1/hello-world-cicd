from main import hello

def test_hello():
    assert hello() == "Hello World"
    print("测试通过！")

if __name__ == "__main__":
    test_hello()
