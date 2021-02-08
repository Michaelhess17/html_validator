#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation
    by checking whether every opening tag has a corresponding
    closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate
    # a list of html tags without any extra text;
    # # # then process these html tags using the balanced parentheses
    # # algorithm from the book
    # # the main difference between your code and the book's
    # # code will be that you will have to keep track of not
    # # just the 3 types of parentheses,
    # # but arbitrary text located between the html tags
    balanced = True
    results = []
    tags = _extract_tags(html)
    for k, tag in enumerate(tags):
        if '/' not in tag:
            results.append(tag)
        else:
            if results == []:
                balanced = False
            else:
                last_tag = results.pop()
                if tag[2:] != last_tag[1:]:
                    print('tag', tag)
                    print('last_tag', last_tag)
                    balanced = False
    if (results == []) & balanced:
        return True
    else:
        return False


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not
    meant to be used directly by the user are prefixed with
    an underscore.

    This function returns a list of all the html tags contained
    in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    if html == '':
        return []
    results = []
    lefts = 0
    rights = 0
    if ('<' in html) & ('>' in html):
        for k in range(len(html)):
            if html[k] == '<':
                lefts += 1
                if '>' in html[k + 1:]:
                    for i in range(len(html) - k):
                        if html[k + i] == '>':
                            rights += 1
                            results.append(html[k:k + i + 1])
                            break
                else:
                    raise ValueError('found < without matching >')
        if lefts == rights:
            return results
        else:
            raise ValueError('found < without matching >')
    else:
        return []
