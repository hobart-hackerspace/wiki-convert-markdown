import re # for regular expressions
import urllib.parse # for URL encoding
import os.path
import pathlib

def make_re(expr:str) -> str:
    return re.compile(expr, re.IGNORECASE + re.VERBOSE)

# Set up our compiled regular expressions
md_link = make_re(r'\[.*\]\(.*\)') # [<text>](<link>)
ext_link = make_re(r'^.+\:.+') # URL including schema
url_schema = make_re(r'^\(((http:)|(https:)|(mailto:)|(file:))')
anchor_link = make_re(r'^\#.+') # #<text>
anchor_schema = make_re(r'^\(\#.+')
link_sep = make_re(r'\]\(') # just the "](" bit
link_body = make_re(r'^\(.+\)$') # full "(<text>)"
wiki_link = make_re(r'\[\[.*\]\]') # [[<text>]]
file_suffix = make_re(r'\.[a-zA-Z]{1,6}$') # .<text>)<EOL>

result = []

def process_url(url:str) -> str:
    '''
    Processing intra-vault links for Obsidian - it never links to a 
    directory, so all links should be to files and should be URL-encoded
   
    Amend a URL if necessary by 
    1. URL-encoding the body and 
    2. adding a '.md' suffix to file title if it has no other suffix
    
    Returns the updated link.
    '''
    # print(f"Got a live one: {url}")
    # first verify the basic format
    if (b:=link_body.search(url)) is None:
        print(f"URL body doesn't look right: |{url}|")
        return(url)
    body = url[b.start()+1:b.end()-1]
    # print(f"Body: |{body}|")
    if file_suffix.search(body) is None: 
        # Not a file - need to add the ".md" bit
        body = body + ".md"
    # Now we URL-encode it. 
    # but first we un-quote it, it screws up if we try to do it twice
    body = urllib.parse.unquote(body)
    body = urllib.parse.quote(body)
    url = "("+body+")"
    # print(f"Amended URL: |{url}|")
    return( url)

def process_md(line:str) -> str:
    '''
    Amend all MarkDown links in `line`
    return updated line text
    '''
    rl = md_link.finditer(line)
    for r in rl:
        # in truth this will only work for a single link per line.
        # Multiple links may cause the start/end offsets to be wrong
        # really need to re-parse in some way...
        # group = r.group()
        s = r.start()
        e = r.end()
        front = line[:s]
        mid = line[s:e]
        back = line[e:]
        # `mid` is now the bit to process "[...](..)"
        # print(f"Front: |{front}|  Mid: |{mid}|  Back: |{back}|")
        breakpt = link_sep.search(mid)
        text = mid[:breakpt.start()+1]
        url = mid[breakpt.end()-1:]
        new_url = url
        # print(f"Text: |{text}| URL: |{url}|")
        # Filter out the ones that don't need adjusting
        if url_schema.search(url) is not None:
            # print(f"External link: |{url}|")
            pass
        elif anchor_schema.search(url) is not None:
            # print(f"Anchor link: |{url}|")
            pass
        else:
            new_url = process_url(url)
        # result.append(f"Markdown: {group} at {r.span()} ")
        full_link = text + new_url
        line = front + full_link + back
        # print(f"New line: |{line}|")
    return line

def process_wikilink(line:str) -> str:
    return(line)


def one_file(title:str) -> int:
    f_in = open(title,"r")
    lines = f_in.readlines()
    f_name, f_ext = os.path.splitext(title)
    f_new = f_name+"_new"+f_ext
    lines_out = ""
    changed = False
    # f_out = open(f_new, "w")
    count = len(lines)
    print(f"Found {count} lines in {title}")
    for line in lines:
        # result = []
        # print("-------------")
        # print(line, end="")
        saved_line = line
        if md_link.search(line) is not None:
            line = process_md(line)
        if wiki_link.search(line) is not None:
            line = process_wikilink(line)
        # rl = wiki_link.finditer(line)
        # for r in rl:
        #     result.append(f"Wiki: {r.group()} at {r.span()} ")
        # if len(result)>0:
        #     print("".join(result))
        lines_out += line
        if saved_line != line:
            changed = True
    if changed:
        f_name, f_ext = os.path.splitext(title)
        f_new = f_name+"_new"+f_ext
        f_out = pathlib.Path(f_new)
        f_out.write_text(lines_out)

    return count

def main():
    print(one_file("links.md"))

if __name__ == "__main__":
    main()
