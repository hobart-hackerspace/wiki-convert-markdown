import re # for regular expressions
# import urllib # for URL encoding
def make_re(expr:str) -> str:
    return re.compile(expr, re.IGNORECASE + re.VERBOSE)

md_link = make_re(r'''
\[.*\]\(.*\)
''')
ext_link = make_re(r'''
^.+\:.+
''')
anchor_link = make_re(r'''
^\#.+
''')
link_sep = make_re(r'''
\]\(
''')
wk_link = make_re(r'''
\[\[.*\]\]
''')

result = []

def process_md(line:str) -> str:
    '''
    Amend all MarkDown links in `line` and return updated line text
    '''
    rl = md_link.finditer(line)
    for r in rl:
        group = r.group()
        s = r.start()
        e = r.end()
        front = line[:s]
        mid = line[s:e]
        back = line[e:]
        print(f"Front: |{front}|  Mid: |{mid}|  Back: |{back}|")
        breakpt = link_sep.search(mid)
        text = mid[:breakpt.start()+1]
        url = mid[breakpt.end()-1:]
        print(f"Text: |{text}| URL: |{url}|")
        result.append(f"Markdown: {group} at {r.span()} ")

    return line

def one_file(title:str) -> int:
    f = open(title,"r")
    lines = f.readlines()
    count = len(lines)
    print(f"""Found {count} lines""")
    for line in lines:
        result = []
        print(line, end="")
        if md_link.search(line) is not None:
            line = process_md(line)
        rl = md_link.finditer(line)
        for r in rl:
            result.append(f"Markdown: {r.group()} at {r.span()} ")
        rl = wk_link.finditer(line)
        for r in rl:
            result.append(f"Wiki: {r.group()} at {r.span()} ")
        if len(result)>0:
            print("".join(result))
    return count

def main():
    print("Hello from wiki-temp!")
    print(one_file("links.md"))


if __name__ == "__main__":
    main()
