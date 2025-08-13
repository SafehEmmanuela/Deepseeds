# def read_simple_file():
#     """demonstrate basic file reading......"""

#     file= open("sample.txt", "r")
#     # print(f"here is the file i want to read.......:{file}")
#     content=file.read()
#     print(f"here is the file i want to read: {content}")
#     file.close()

# read_simple_file()    


# # read_simpe_file()
# def read_simple_text():
#     """Read simple files"""
#     with open("sample.txt", "r") as file:
#         content=file.read()
#         print(f"Content is: {content}")
#         return content
# read_simple_text()


def read_simple_text():
    filename="sample.txt"
    try:
        with open(filename, "r") as file:
            print("\n\nreading line by line")
            for i, line in enumerate (file, 1):
                print(f"\n\nLine {i}: {line.strip()}")
            # content= file.read()
            # return content
    except FileNotFoundError:
        pass