import cv2

# Load the image
img = cv2.imread('newstron-mid.png')

# Define the desired size
width = 142
height = 142
dim = (width, height)

# Resize the image
resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# Save the resized image
cv2.imwrite('on1-mid.png', resized_img)

# Display the original and resized images
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()