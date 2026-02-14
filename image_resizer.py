import cv2
image_src = "ChatGPT Image Mar 30, 2025, 10_35_52 PM.png"
image = cv2.imread(f"{image_src}", cv2.IMREAD_UNCHANGED)
cv2.imshow("title",image)
cv2.waitKey(0)
scale_per = int(input("Enter the percentage u wnat to resize to -> "))
scale_factor = scale_per/100
# height, width = image.shape[:2]
height = int(image.shape[0])
width = int(image.shape[1])
resized_image = cv2.resize(image,(int(width*scale_factor),int(height*scale_factor)))
cv2.imshow("Resized Image", resized_image)
cv2.imwrite(f"resized_{image_src}",resized_image)
cv2.waitKey(0)