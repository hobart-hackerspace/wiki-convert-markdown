import re # for regular expressions
# import urllib # for URL encoding

def one_file(title:str) -> int:
    f = open(title,"r")
    lines = f.readlines(100)
    count = len(lines)
    print(f"""Found {count} lines""")
    for line in lines:
        print(line)
        return count

def make_re(expr:str) -> str:
    return re.compile(expr, re.IGNORECASE)

def main():
    print("Hello from wiki-temp!")
    print(one_file("sample.md"))


if __name__ == "__main__":
    main()
