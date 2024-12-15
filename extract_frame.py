import cv2
import os

def extract_frame(video_path, output_dir, seconds):
    # 動画ファイルを開く
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Unable to open video.")
        return

    # 動画のフレームレートを取得
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 指定秒数をフレーム番号に変換
    frame_numbers = [int(fps * sec) for sec in seconds]

    # 出力フォルダが存在しない場合は作成
    os.makedirs(output_dir, exist_ok=True)

    current_frame = 0
    extracted_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break  # 動画の終わりに到達

        if current_frame in frame_numbers:
            # 指定したフレーム番号の場合は保存
            output_path = os.path.join(output_dir, f"frame_{current_frame}.jpg")
            cv2.imwrite(output_path, frame)
            print(f"Saved: {output_path}")
            extracted_count += 1

            # すべての指定フレームを保存した場合は終了
            if extracted_count == len(frame_numbers):
                break

        current_frame += 1

    cap.release()
    print("Extraction completed.")

# 使用例
video_path = "video/diverse_env.mov"  # 入力動画ファイルのパス
output_dir = "output"  # 出力フォルダのパス
seconds = [0, 3, 6, 9]  # 画像を切り取りたい秒数

extract_frame(video_path, output_dir, seconds)
