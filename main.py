# Needed Libraries
'''
segno

'''

# Import Libraries
import os
import segno

# start of program
website = input("Enter the website URL: ")
file_name = input("Enter the name you want to save the QR code as (without extension): ")
print(f"The QR Code will save into the current directory as a png file type.")

# Generate QR code
qr = segno.make(website)

# Save QR code
qr.save("qr.png")
