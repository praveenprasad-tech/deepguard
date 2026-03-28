import cv2

# image load test
img = cv2.imread("test.jpg")

if img is None:
    print("Image not found ❌")
else:
    print("Image loaded successfully ✅")