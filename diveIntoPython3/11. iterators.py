import re


class Fib:
    """iterator that yields numbers in Fibonacci sequence"""

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


for n in Fib(1000):
    print(n, end=' ')


# ------------------------------------------------------------------

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return matches_rule, apply_rule


class LazyRules:
    rules_filename = '9. plural_rules'

    def __init__(self):
        self.pattern_file = open(self.rules_filename, encoding='utf-8')
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return selfz

    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 2)
        funcs = build_match_and_apply_functions(pattern, search, replace)
        self.cache.append(funcs)
        return funcs


rules = LazyRules()
r1 = LazyRules()
r2 = LazyRules()

print(r1.rules_filename)

# if you change the rules_filename attritube via __class__ it will affect all of the instances
r2.__class__.rules_filename = 'different_file.txt'

print(r1.rules_filename)

