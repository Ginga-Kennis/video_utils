import cv2
import numpy as np

def merge_videos(input_video1_path, input_video2_path, output_video_path):
    # 動画の読み込み
    video1 = cv2.VideoCapture(input_video1_path)
    video2 = cv2.VideoCapture(input_video2_path)

    # 動画の高さを取得
    height1 = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    height2 = int(video2.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 動画の幅を取得
    width1 = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
    width2 = int(video2.get(cv2.CAP_PROP_FRAME_WIDTH))

    # 高さを揃えるためにリサイズ
    if height1 > height2:
        ret, frame = video1.read()
        if ret:
            frame = cv2.resize(frame, (int(width1 * height2 / height1), height2))
            height1, width1 = frame.shape[:2]
        video1.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset to the first frame
    else:
        ret, frame = video2.read()
        if ret:
            frame = cv2.resize(frame, (int(width2 * height1 / height2), height1))
            height2, width2 = frame.shape[:2]
        video2.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset to the first frame

    # 出力動画のサイズを計算
    output_width = width1 + width2
    output_height = min(height1, height2)

    # 出力動画の設定
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_video_path, fourcc, 30.0, (output_width, output_height))

    # 動画のフレームを結合して出力
    while True:
        ret1, frame1 = video1.read()
        ret2, frame2 = video2.read()

        if not ret1 or not ret2:
            break

        # フレームの高さを揃えるためにリサイズ
        frame1 = cv2.resize(frame1, (width1, output_height))
        frame2 = cv2.resize(frame2, (width2, output_height))

        # フレームを結合
        merged_frame = np.hstack((frame1, frame2))

        # 出力動画にフレームを書き込み
        output_video.write(merged_frame)

    # リソースの解放
    video1.release()
    video2.release()
    output_video.release()

if __name__ == "__main__":
    input_video1_path = "transparent_bag_3/time_size_trim/transparent_bag_3_robot.mp4"
    input_video2_path = "transparent_bag_3/time_size_trim/transparent_bag_3_rviz.mp4"
    output_video_path = "transparent_bag_3/transparent_bag_3.mp4"

    merge_videos(input_video1_path, input_video2_path, output_video_path)
