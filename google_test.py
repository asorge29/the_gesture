import mediapipe as mp
import cv2

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

cap = cv2.VideoCapture(0)

# Create a gesture recognizer instance with the live stream mode:
def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    out = ''
    if len(result.handedness) > 0:
        out += f'Hand: {result.handedness[0][0].category_name} '
        out += f'Gesture: {result.gestures[0][0].category_name}'
    else:
        out = 'No Gesture'

    print(out)

    image_np = output_image.numpy_view()

    if output_image.image_format == mp.ImageFormat.SRGB:
        image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    elif output_image.image_format == mp.ImageFormat.SRGBA:
        image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGBA2BGR)
    else:
        raise ValueError("Unsupported image format")

    file_path = f'output/{timestamp_ms}.png'
    cv2.imwrite(file_path, image_cv)
    print(file_path)

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path='gesture_recognizer.task'),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)
with GestureRecognizer.create_from_options(options) as recognizer:
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

        recognizer.recognize_async(mp_image, int(cap.get(cv2.CAP_PROP_POS_MSEC)))