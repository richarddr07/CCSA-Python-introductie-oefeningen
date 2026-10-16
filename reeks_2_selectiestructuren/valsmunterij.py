standEerst = input()
standTweede = input()

if standEerst == "evenwicht":
  valseGroep = [7,8,9]
elif standEerst == "links":
  valseGroep = [4,5,6]
else:
  valseGroep = [1,2,3]


if standTweede == "evenwicht":
  valseMunt = valseGroep[2]
elif standTweede == "links":
  valseMunt = valseGroep[1]
else:
  valseMunt = valseGroep[0]

print(f"muntstuk #{valseMunt} is vervalst")