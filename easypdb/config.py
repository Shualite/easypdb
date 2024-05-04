import pdb
from fancycompleter import Color
from pygments.formatters import Terminal256Formatter

class Config(pdb.DefaultConfig):
    prompt = '(EasyPDB) '
    sticky_by_default = True
    highlight = True

    # Pygments.
    use_pygments = True  # Tries to use it if available.
    pygments_formatter_class = Terminal256Formatter  # Defaults to autodetect, based on $TERM.
    pygments_formatter_kwargs = {
        "style": "monokai",
        "bg": 'dark',
        "colorscheme": None,
    }

    editor = None  # Autodetected if unset.
    stdin_paste = None       # for emacs, you can use my bin/epaste script
    truncate_long_lines = True
    exec_if_unfocused = None
    disable_pytest_capturing = False
    encodings = ('utf-8', 'latin-1')

    enable_hidden_frames = True
    show_hidden_frames_count = True

    line_number_color = Color.turquoise
    filename_color = Color.yellow
    current_line_color = "39;49;7"  # default fg, bg, inversed

    show_traceback_on_error = True
    show_traceback_on_error_limit = None

    # Default keyword arguments passed to ``Pdb`` constructor.
    default_pdb_kwargs = {
    }

    def setup(self, pdb):
        pass

    def before_interaction_hook(self, pdb):
        pass