def read_simple_file():
    """demonstrate basic file reading......"""

    file= open("sample.txt", "r")
    # print(f"here is the file i want to read.......:{file}")
    content=file.read()
    print(f"here is the file i want to read: {content}")
    file.close()

read_simple_file()    