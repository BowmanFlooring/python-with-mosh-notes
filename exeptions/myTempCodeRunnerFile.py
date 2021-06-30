from timeit import timeit

code3 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age



xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("third code =", timeit(code3, number=10000))
# Now, let's compare the speed of 'code2' vs. 'code3':
'''
RESULT:
first code = 0.003558457000000001
'''