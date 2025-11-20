from parser import parse
from pprint import pp


def test1():
    input = """Oronris,Urakris,Oroneth,Uraketh

r > a,i,o
i > p,w
n > e,r
o > n,m
k > f,r
a > k
U > r
e > t
O > r
t > h"""

    parse(input)


def main():
    test1()


if __name__ == "__main__":
    main()
