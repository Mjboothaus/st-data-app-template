from pathlib import Path

from IPython.display import Markdown, display
from streamlit import cache, markdown


def read_markdown_file(markdown_file):
    try:
        return Path(markdown_file).read_text()
    except Exception as IOError:
        print(f"Error with markdown file: {markdown_file}")
        raise(IOError)


@cache
def st_read_markdown_file(markdown_file):
    return read_markdown_file(markdown_file)


def render_markdown_file(markdown_file, output="streamlit"):
    if output == "jupyter":
        md_text = read_markdown_file(markdown_file)
        display(Markdown(md_text))
    else:
        md_text = st_read_markdown_file(markdown_file)
        markdown(md_text, unsafe_allow_html=True)
    return