import os
import cv2
import time
import random

def imagechecker(pathfo):
    image_paths = []
    for root, dirs, files in os.walk(pathfo):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                image_path = os.path.join(root, file)
                image_paths.append(image_path)
    return image_paths

def showimage(pathfi, interval):
    time.sleep(interval)
    image = cv2.imread(str(pathfi))
    if image is not None:
        cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Image', image)
        cv2.waitKey(0)  
        cv2.destroyAllWindows()
    else:
        print("Error reading image:", pathfi)

def main():
    while True:
        try:
            pathfo = str(input("Path to folder with images: "))
            random_interval = str(input("Random interval?(10-60 second) y/n "))
            random_info = str(input("Random images? y/n "))
            infinty_info = str(input("Infinity images? y/n "))
            if random_interval not in ['y', 'n'] or random_info not in ['y', 'n'] or infinty_info not in ['y', 'n']:
                raise ValueError
            if random_interval == 'n':
                interval = int(input("Opening interval (in seconds): "))
            break
        except ValueError:
            print("Input correct data")

    while not os.path.exists(pathfo):
        print("Incorrect path folder")
        pathfo = str(input("Path to folder with images: "))

    image_paths = imagechecker(pathfo)
    if len(image_paths) == 0:
        print("No images found in the specified folder.")
    else:
        if infinty_info == "y":
            image_paths = image_paths*1488
        if random_info == 'y':
            random.shuffle(image_paths)
        for i in image_paths:
            if random_interval == 'y':
                interval = random.randint(1, 60)
            showimage(i, interval)

if __name__ == "__main__":
    main()