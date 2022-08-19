import platform
from pathlib import Path

import httpx
from IPython.display import Markdown, display
from streamlit import cache, markdown


def read_markdown_file(markdown_file):
    try:
        return Path(markdown_file).read_text()
    except Exception as IOError:
        sys_list.append(f"Error with markdown file: {markdown_file}")
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


def get_file_header(file_name, n_char=100, n_row=1):
    if file_name[:len("http")] == "http":
        sys_list.append(file_name)
        with httpx.Client() as client:
            r = client.get(file_name)
        return r.text[:min(n_char, len(r.text))]
    else:
        with open(file_name, "r") as f:
            return f.readlines()[:n_row]


def get_system_info():
    my_sys = platform.uname()
 
    sys_list = [f"System: {my_sys.system}"]
    sys_list.append(f"Node Name: {my_sys.node}")
    sys_list.append(f"Release: {my_sys.release}")
    sys_list.append(f"Version: {my_sys.version}")
    sys_list.append(f"Machine: {my_sys.machine}")
    sys_list.append(f"Processor: {my_sys.processor}")
    sys_list.append(f"Architecture: {platform.architecture()}")
    sys_list.append(f"Python version: {platform.python_version()}")

    return sys_list
