import cv2

def preprocess(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found")
        return None

    img = cv2.resize(img, (224, 224))
    img = img / 255.0

    return img 