from PIL import Image # Read image contents

pi_file = open("./pi.txt", "r", encoding="utf-8-sig") # Open file with decimal points of pi, You need enough decimal points to fill every non-transparent pixel in the image
img_file = Image.open("./image.png").convert("RGBA") # Open the image file to be converted, and convert to RGBA

# One pixel gets converted to one digit, you need to scale down your image previously
# Since one digit is not square, the image should be streched previously
# Every pixel that is not fully transparent (alpha = 0) will be converted to a digit of pi

pi = tuple(pi_file.read()) # Create a tuple with one digit per element
img_width, img_height = img_file.size # Get the size of the image in width and height
img_data = img_file.load() # Load the image data
img = [] # Initialize List
for y in range(img_height): # Loop through every row
	for x in range(img_width): # Loop through every column
		n, n, n, a = img_data[x, y] # Ignoring everything except Alpha
		
		if a == 0: # Transparent Pixel > No Digit
			img.append(False)
		else: # Otherwise > Digit
			img.append(True)
	img.append("\n") # Go to a new line

output = open("./output.txt", "w") # Open for appending each new character
n = 0 # Digit of Pi counter
for i in range(len(img)): # Loop through img list
	if img[i] == True: # True > Digit
		print(pi[n], end="") # Print next digit of pi, end="" to prevent new line
		output.write(pi[n]) # Write next digit of pi to output file
		n += 1 # Increade pi digit counter for next digit
	elif img[i] == False: # False > No Digit
		print(" ", end="") # Print space, end="" to prevent new line
		output.write(" ") # Write space to output file
	elif img[i] == "\n": # If new line
		print("") # Print nothing to enter new line
		output.write("\n") # Write new line to output file

pi_file.close()
img_file.close()
output.close()