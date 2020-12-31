import re


def make_counter(x):
    print('entering make_counter')
    while True:
        yield x
        print('incrementing x')
        x += 1


counter = make_counter(2)
print(next(counter))
print(next(counter))
print(next(counter))


def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return matches_rule, apply_rule


def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 2)
            yield build_match_and_apply_functions(pattern_file, search, replace)


def plural(noun, rules_filename='9. plural_rules'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))

