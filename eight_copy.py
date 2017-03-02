def function (the_text, pattern):
    count = 0
    for x in xrange(len(the_text)):
        new_string = the_text[x:x + len(pattern)]
        if (new_string == pattern):
            count = count + 1
    return count