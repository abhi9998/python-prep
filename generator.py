def generator():
    yield 1;
    yield 2;
    yield 4;

g =generator();

# for i in g:
#     print(i)

val = next(g)
print(val)

print(sorted(g,reverse=True))