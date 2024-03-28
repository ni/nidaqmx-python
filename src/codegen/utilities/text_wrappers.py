"""This contains the helpers methods for wrapping texts."""

import textwrap

"""
 Use global text wrapper objects and reassign properties each time instead
 of instantiating a new text wrapper object each time, as it is about 2 orders
 of magnitude faster.

 An extra character is subtracted from the line width of the code text wrapper
 to allow for closing brackets, since the Mako template will be prettier
 without lines like [${variable + ']' | wrap(4. 8)}
"""
wrapper = textwrap.TextWrapper(width=78, break_long_words=False)
docstring_wrapper = textwrap.TextWrapper(width=72, break_long_words=False)


def wrap(initial_indent, subsequent_indent=None):
    """Returns custom Mako filter function that wraps code text.

    Returning another function from within this function is a trick used to
    enable Mako filter functions to accept arguments.
    """

    def text_wrap(text):
        wrapper.initial_indent = " " * initial_indent
        if subsequent_indent is None:
            wrapper.subsequent_indent = " " * initial_indent
        else:
            wrapper.subsequent_indent = " " * subsequent_indent
        return wrapper.fill(text).lstrip()

    return text_wrap


def docstring_wrap(initial_indent, subsequent_indent=None):
    """Returns custom Mako filter function that wraps docstring text.

    Returning another function from within this function is a trick used to
    enable Mako filter functions to accept arguments.
    """

    def doc_string_wrap(text):
        docstring_wrapper.initial_indent = " " * initial_indent
        if subsequent_indent is None:
            docstring_wrapper.subsequent_indent = " " * initial_indent
        else:
            docstring_wrapper.subsequent_indent = " " * subsequent_indent
        return docstring_wrapper.fill(text).lstrip()

    return doc_string_wrap
