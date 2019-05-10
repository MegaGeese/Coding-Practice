'''
Rhodes White & David Dodge
5/6/19
Vigenere Encoder/Decoder
Encoded txt: Mary had a little lamb lyrics
Running Time: O(n + m) where n = len of cypher_text m = len of key
Version 1
'''

#Main funtion call
def vigenere(cypher_text, key):
	m = len(key)
	n = len(cypher_text)

	key_order = []

	for i in key: #generates a list of numbers used to alter the cypher_text in accordance with the key
		key_order.append(ord(i) - 97)

	plain_text_forward, plain_text_backward = character_calculation(cypher_text, key_order, 0, m, n)

	print(f"Forward Decoding:\n{plain_text_forward}\n")
	print(f"Backward Decoding:\n{plain_text_backward}\n")



def character_calculation(cypher_text, key_order, position_counter, key_len, cypher_len):
	plain_text_forward, plain_text_backward = '', '' #running tab of the plain_text
	pointer = 0 #points to a position in the key to move the char

	for char in range(cypher_len):
		cypher_character = cypher_text[char]
		order = ord(cypher_character)

		#this if checks for special characters and adds tehm to the cypher_text without altering them.
		if order < 65 or (order < 97 and order > 90) or order > 122:
			plain_text_forward += cypher_character
			plain_text_backward += cypher_character
			continue

		pos = key_order[pointer % key_len]


		if order > 97: 
			'''
			Checks lower-first and alters the cypher_text accordingly.
			Cypher_character in number form converted from ascii to a number. 
			Modded 26 to correct the cypher alteraion. 
			Then converted back to ascii for appending into the plain_text
			'''
			character = (order - 97 - pos) % 26 + 97 
			plain_text_backward  += chr(character)

			character = (order - 97 + pos) % 26 + 97
			plain_text_forward  += chr(character)
		else:
			character = (order - 65 - pos) % 26 + 65
			plain_text_backward += chr(character)

			character = (order - 65 + pos) % 26 + 65
			plain_text_forward += chr(character)

		pointer += 1

	return plain_text_forward, plain_text_backward




#cypher_text = input("Enter cypher_text: ")
#key = input("Enter key: ")

key = 'blorpy'

cypher_text = """Lpdh scc p xrevkt xjxd,
Hi'e owgdrq flu vwucp cr hzxh, adpt.
Nggqniqptd itn njhap fpps,
Itn wksixn wclq ijd utgq cz in, nqjs.
Jd uauwqvtp qpt sd elsqna awp fzn,
Mwo dqdwn ejd iqjnjdge afnd.
Ltje c sxyn okc itnj jzkq,
Cscs smh lv rrtxzn.
Sxetpv, spetpv,
Z vdnpp zcp hpnkdi klujtf.
Bpps p xnevdg fx xa apnh,
Zp ln ijj K opebpf hi."""

#cypher_text *= 10000
vigenere(cypher_text, key)
