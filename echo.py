import sys

def echo():
    """
    获取用户输入并打印出来，支持-s标志以大写形式输出
    """
    shout = "-s" in sys.argv
    message = input("Type anything: ")
    print(message.upper() if shout else message)

if __name__ == "__main__":
    echo()