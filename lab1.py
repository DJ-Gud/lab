
from functools import reduce 

def min_word(data: str) -> str:
	return reduce(lambda x,y: x if len(x) < len(y) else y, data.split()) if data else ""
	



def test_empty():
	assert min_word("") == ""

def test_normal():
	assert min_word("jgklfsjgk gfldkgl slfksd fsldkf gf") == "gf"

def qwetest_same():
	assert min_word("hhhhhhhhh hhhhhhhhh hhhhhhhhh") == "hhhhhhhhh"




if __name__ == '__main__':
	print(min_word(input()))


