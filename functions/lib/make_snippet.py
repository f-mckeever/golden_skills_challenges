#Returns string or first 5 words of string followed by an ellipsis
def make_snippet(string):
    #If string longer shorter than 5 words, return string
    if len(string.split(" ")) > 5:
        return " ".join(string.split(" ")[0:5]) + "..."
    return string