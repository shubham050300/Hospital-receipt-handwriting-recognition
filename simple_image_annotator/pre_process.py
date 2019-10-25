import cv2
import os


folder = 'final_images'
out_folder = 'preprocessed_images'

files = os.listdir(os.path.join(os.getcwd(), folder))

# print(files)

for file in files:
	file1 = os.path.join(folder, file)
	grayImage = cv2.imread(file1,0)
	# grayImage = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
	invert_img = cv2.bitwise_not(grayImage)
	resized_img = cv2.resize(invert_img,(300,150))
	# cv2.imshow("Image",resized_img)
	# print(os.path.join(out_folder,file))
	cv2.imwrite(os.path.join(out_folder,file),resized_img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
