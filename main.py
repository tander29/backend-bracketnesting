brackets = {'[': ']', '{': '}', '<': '>', '(*': '*)', '(': ')'}
# brackets = {'(*': '*)'}


def valid_parentheses(string, brackets):
    # f = open('filename', 'r')
    # f.read()
    # stack =[] only brackets
    # splitlist does logic for (*)
    for opener, closer in brackets.iteritems():
        if opener or closer in string:
            count_brackets = string.count(opener)
            if count_brackets == 0:
                count_brackets = string.count(closer)
            for i in range(count_brackets):
                open_index = find_nth(opener, string, i+1)
                close_index = find_nth(closer, string, i+1)
                if open_index > -1 and close_index == -1:
                    print('Open bracket has no closer', opener, open_index)
                    return
                if close_index > -1 and open_index == -1:
                    print('Close bracket has no opener', closer, len(string))
                    return


def find_nth(bracket, string, nth):
    start = string.find(bracket)
    bracket_len = len(bracket)
    while start >= 0 and nth > 1:
        start = string.find(bracket, start+bracket_len)
        nth -= 1
    return start


# valid_parentheses("(*a++(*)", brackets)
valid_parentheses("(*a{+}*)", brackets)
valid_parentheses("<(************)>", brackets)
valid_parentheses("<(************)>", brackets)
valid_parentheses("( [ aJKBCXSLBCD ( ) [[)", brackets)
