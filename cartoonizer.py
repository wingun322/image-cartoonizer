import cv2

# Load the original image
image = cv2.imread('butterfly-8414148_640.jpg')

# Convert the original image to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a median blur to the grayscale image to reduce noise
blurred_gray_image = cv2.medianBlur(grayscale_image, 5)

# Apply Canny edge detection
canny_edges = cv2.Canny(blurred_gray_image, 100, 200)

# Use adaptive thresholding on the blurred grayscale image to detect edges
edges = cv2.adaptiveThreshold(blurred_gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Combine Canny edges with adaptive thresholding edges
combined_edges = cv2.bitwise_or(canny_edges, edges)

# Apply a bilateral filter to the original image to smooth it while retaining edges
smoothed_color_image = cv2.bilateralFilter(image, 9, 300, 300)

# Combine the smoothed color image with the combined edge mask to get a cartoon effect
cartoon_image = cv2.bitwise_and(smoothed_color_image, smoothed_color_image, mask=combined_edges)

# Display the resulting cartoon image
cv2.imshow("Cartoon Effect with Enhanced Edges", cartoon_image)

# Wait for a key press and then close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
