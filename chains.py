import bisect

def create_alphagrams():
	wordset = set(open('wordlist.txt').read().split())
	wordlist = sorted(list(wordset))
	
	l = len(wordlist)
	print(l)
	
	for i in range(0, len(wordlist)-1):
		temp_alph = wordlist[i]
		alph = "".join(sorted(temp_alph))
		wordlist[i] = alph
	

	wordset = set(wordlist)
	wordlist = sorted(list(wordset))
	
	alphabet = 	['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	length = len(wordlist)
	
	for i in range(0, length-1):
		next_node = wordlist[i]
		for j in range(0, 25):
			next_node = next_node + alphabet[j]
			index = bisect.bisect(wordlist, next_node)-1
			if index != -1:	
				a = 1 #random assignment so code doesn't break
				#add the node to the list
		#needed to sort the linked lists by length and return one of the longest
		#assuming with a sample of about 178k words, the longest string would be
		#above 10.. 
			

	
create_alphagrams()