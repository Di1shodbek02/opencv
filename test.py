import cv2


class MobileCamera:
    def get_video(self, camera_url):
        # Initialize video capture with the URL.
        cap = cv2.VideoCapture(camera_url)

        # Check if the camera has been successfully opened.
        if not cap.isOpened():
            print("Error: Camera could not be opened.")
            return

        while True:
            # Capture frame-by-frame.
            ret, frame = cap.read()

            # If frame is read correctly, ret is True.
            if not ret:
                print("Error: Can't receive frame (stream end?). Exiting ...")
                break

            # Display the resulting frame.
            cv2.imshow('Mobile Cam', frame)

            # Wait for 'q' key to stop the program.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture and destroy all windows.
        cap.release()
        cv2.destroyAllWindows()


# Example usage:
cam = MobileCamera()
cam.get_video("http://172.20.10.3:4747/video")
