from PIL import Image
import csv
import os
from datetime import datetime

def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    saved_loc=os.path.join('final_images', saved_location)
    cropped_image.save(saved_loc)
    # cropped_image.show()



def main():

	image_folder='IMAGES/'
	with open('test.csv', 'r') as csvFile:
	    reader = csv.reader(csvFile)
	    for row in reader:
	    	image=image_folder+row[0]
	    	cropped_img_name=row[2]+'-'+row[0]+'.jpeg'
	    	# print(cropped_img_name)
	    	# print(row[3],row[4])
	    	crop(image, (int(row[3]),int(row[5]),int(row[4]),int(row[6])), cropped_img_name)
	        
	csvFile.close()

if __name__ == '__main__':
	main()
