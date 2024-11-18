import cv2
import pytesseract
from pytesseract import Output
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

class TableDetector:
    
    @staticmethod
    def load_and_preprocess_image(image_path):
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        return image, thresh

    @staticmethod
    def extract_text_positions(thresh):
        d = pytesseract.image_to_data(thresh, output_type=Output.DICT)
        positions = []
        n_boxes = len(d['text'])
        for i in range(n_boxes):
            if int(d['conf'][i]) > 40:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                positions.append((x, y, w, h))
        return positions

    @staticmethod
    def cluster_positions(positions):
        positions = np.array(positions)
        if len(positions) > 0:
            dbscan_y = DBSCAN(eps=10, min_samples=2).fit(positions[:, 1].reshape(-1, 1))
            unique_rows = len(set(dbscan_y.labels_)) - (1 if -1 in dbscan_y.labels_ else 0)

            dbscan_x = DBSCAN(eps=10, min_samples=2).fit(positions[:, 0].reshape(-1, 1))
            unique_columns = len(set(dbscan_x.labels_)) - (1 if -1 in dbscan_x.labels_ else 0)

            is_tabular = unique_rows > 1 and unique_columns > 1
        else:
            is_tabular = False
        return is_tabular

    @staticmethod
    def display_image_with_text(image, positions):
        for (x, y, w, h) in positions:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title('Detected Text')
        plt.axis('off')
        plt.show()

    @staticmethod
    def detect_tabular_data(image_path):
        image, thresh = TableDetector.load_and_preprocess_image(image_path)
        positions = TableDetector.extract_text_positions(thresh)
        is_tabular = TableDetector.cluster_positions(positions)
        TableDetector.display_image_with_text(image, positions)
        return is_tabular
