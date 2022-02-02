import cv2
from pyzbar.pyzbar import decode
from time import sleep
import threading


class IsbnScanner:
    isbns = {}

    def scan(self):
        RTSP_URL = 'rtsp://192.168.1.142:8080/h264_pcm.sdp'
        # cap = cv2.VideoCapture(0) #default camera
        cap = cv2.VideoCapture(RTSP_URL)  # IP Camera
        th = None
        while cap.isOpened():
            ret, frame = cap.read()
            # frame = cv2.resize(frame, (2304, 1728))
            cv2.imshow('Capturing', frame)
            if th is None or not th.is_alive():
                th = threading.Thread(target=self.thread_scanner, args=[1, frame])
                th.start()
            # th.join()

            if cv2.waitKey(1) & 0xFF == ord('q'):  # click q to stop capturing
                break
            #    break

        cap.release()
        cv2.destroyAllWindows()
        return 0

    def thread_scanner(self, seconds, img):
        sleep(seconds)
        barcode = self.BarcodeReader(img)
        if barcode is not None and barcode['type'] == 'EAN13':
            try:
                self.isbns[barcode['data']] += 1
            except KeyError:
                self.isbns[barcode['data']] = 1
            print(barcode['data'])

    def BarcodeReader(self, img):
        # read the image in numpy array using cv2
        # img = cv2.imread(image)

        # Decode the barcode image
        detectedBarcodes = decode(img)

        # If not detected then print the message
        if detectedBarcodes:
            # Traverse through all the detected barcodes in image
            for barcode in detectedBarcodes:

                if barcode.data != "":
                    return {'type': barcode.type, 'data': barcode.data}
                # Display the image
                # cv2.imshow("Image", img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()


if __name__ == '__main__':
    while True:
        scanner = IsbnScanner()
        try:
            scanner.scan()
        except cv2.error:
            print(scanner.isbns)
        sleep(2)