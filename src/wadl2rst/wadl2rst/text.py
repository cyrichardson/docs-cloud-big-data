

def indent(text, count=4):
    """ Indent a block of text by the defined number of spaces. """

    spaces = u" " * count
    indented_output = [spaces + line + u"\n" for line in text.split("\n")]
    return u"".join(indented_output) + u"\n"
