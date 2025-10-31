import cv2
import numpy as np

# Load image
img_path = "image_file/night_photo.jpg"
image = cv2.imread(img_path)

# Check if image loaded
if image is None:
    print("❌ Image not found! Check file path.")
    exit()

# Convert image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range for black color in HSV
# Adjust values if your lighting is different
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 50])

# Create mask
mask = cv2.inRange(hsv, lower_black, upper_black)

# Apply mask to extract black regions
result = cv2.bitwise_and(image, image, mask=mask)

# Save and show results
cv2.imshow("Original Night Photo", image)
cv2.imshow("Black Object Mask", mask)
cv2.imshow("Segmented Black Objects", result)

cv2.imwrite("black_mask.jpg", mask)
cv2.imwrite("segmented_black_objects.jpg", result)

print("✅ Segmentation complete! Saved as 'black_mask.jpg' and 'segmented_black_objects.jpg'.")

cv2.waitKey(0)
cv2.destroyAllWindows()
