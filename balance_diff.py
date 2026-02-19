def balance_diff(old,new):
	p={}
	for i in old:
		p[i["name"]]= i["balance"]
	c={}
	for i in new:
		c[i["name"]] = i["balance"]

    #balance amount
	for name in p:
		if name in c:
			print (name +":",  c[name]-p[name])
	#if any new accounts added
	for name in c:
		if name not in p:
			print(name +  " added")
	#if name is deleted
	for name in p:
		if name not in c:
			print (name +  " deleted ")


previous = [
    {"name": "Chase Freedom", "balance": 2000.0},
    {"name": "Citibank", "balance": 100.0}
]

current = [
    {"name": "Chase Freedom", "balance": 1000.0},
    {"name": "American Express", "balance": 500.0}
]

balance_diff(previous, current)



