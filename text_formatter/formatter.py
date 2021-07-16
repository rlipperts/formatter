import shutil
import textwrap
import pprintpp as pprint
import colored

indent_size = 4


def _terminal_width():
    return shutil.get_terminal_size(fallback=(80, 50)).columns


def box(text):
    filled = '#' * _terminal_width()
    blank = '#' + ' ' * (_terminal_width() - 2) + '#'
    prefix = "# ====> "
    suffix = " #"
    lines = split(text, " ", _terminal_width() - len(prefix) - len(suffix))

    output = ['', filled, blank]
    for line in lines:
        output.append(prefix + line + ' ' * (_terminal_width() - len(prefix) - len(line) - len(suffix)) + suffix)
    output.append(blank)
    output.append(filled)
    output.append('')
    output = '\n'.join(output)
    return output


def split(text, sep, length):
    separated = []
    words = text.split(sep)
    counter = 0
    iterator = 0

    while len(words) > 0:
        while counter + len(words[iterator]) + 1 < length:
            counter += len(words[iterator]) + 1
            iterator += 1
            if iterator == len(words):
                break
        separated.append(sep.join(words[:iterator]))
        words = words[iterator:]
        iterator = 0
        counter = 0

    return separated


def vsep():
    return '\n' + '=' * int(_terminal_width() / 2) + '\n\n'


def pretty(obj):
    return '\n' + pprint.pformat(obj, indent=indent_size)


def indent(text, amount=1, ch=' '):
    return textwrap.indent(text, amount*indent_size*ch)


def colorize(text, color : str):
    return colored.stylize(text, colored.fg(color))

def colorize_bg(text, color : str):
    return colored.stylize(text, colored.bg(color))
