from pathlib import Path

from IPython.display import Markdown, display
from streamlit import cache, markdown, code


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


# Acknowledgement: https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
class DisplayablePath(object):
    display_filename_prefix_middle = '├──'
    display_filename_prefix_last = '└──'
    display_parent_prefix_middle = '    '
    display_parent_prefix_last = '│   '

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        self.depth = self.parent.depth + 1 if self.parent else 0

    @property
    def displayname(self):
        return f'{self.path.name}/' if self.path.is_dir() else self.path.name


    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria
        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted([path for path in root.iterdir() if criteria(path)], key=lambda s: str(s).lower())

        for count, path in enumerate(children, start=1):
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(path,
                                         parent=displayable_root,
                                         is_last=is_last,
                                         criteria=criteria)
            else:
                yield cls(path, displayable_root, is_last)


    @classmethod
    def _default_criteria(cls, path):
        return True


    @property
    def displayname(self):
        return f'{self.path.name}/' if self.path.is_dir() else self.path.name


    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))


# With a criteria (skip hidden files)

def is_not_hidden(path):
    return not path.name.startswith(".")


def show_dir_tree(my_path=Path.cwd(), not_hidden=True):
    if not_hidden:
        paths = DisplayablePath.make_tree(my_path, criteria=is_not_hidden)
    else:
        paths = DisplayablePath.make_tree(my_path)
    tree = "".join(f"{path.displayable()}\n" for path in paths)
    code(tree)
    return tree