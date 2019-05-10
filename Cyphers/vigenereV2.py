'''
David Dodge & Rhodes White
Vigenere Encoder
5/6/19
Running Time: O(n) where n = len of cypherText
'''
import time
start = time.time()

key = 'blorpy'
cypherText = """Mary had a little lamb,
It's fleece was white as snow, yeah.
Everywhere the child went,
The little lamb was sure to go, yeah.
He followed her to school one day,
And broke the teachers rule.
What a time did they have,
That day at school.
Tisket, tasket,
A green and yellow basket.
Sent a letter to my baby,
On my way I passed it."""
#cypherText *= 1000
plainText = ''

n = len(key)
numPunctAndNums = 0

for i in range(len(cypherText)):
	char = cypherText[i]

	if ord(char) < 65 or (ord(char) < 97 and ord(char) > 90) or ord(char) > 122:
		plainText += char
		numPunctAndNums += 1
		continue

	pos = ord(key[(i - numPunctAndNums) % n]) - 97

	if char.islower():
		character = ord(char) - 97 - pos
		if character < 0:
			character += 26
		plainText += (chr(character + 97))

	else:
		character = ord(char) - 65 - pos
		if character < 0:
			character += 26
		plainText += (chr(character + 65))

print(plainText)
end = time.time()
print(end - start)