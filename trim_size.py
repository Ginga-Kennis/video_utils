import cv2

def trim_video(input_file, output_file, x, y, width, height):
    # 動画を読み込む
    video = cv2.VideoCapture(input_file)
    
    # 動画のフレームサイズを取得
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # トリミングする領域の座標を計算
    x1 = int(frame_width * x)
    y1 = int(frame_height * y)
    x2 = int(frame_width * (x + width))
    y2 = int(frame_height * (y + height))
    
    # 出力用の動画ファイルを作成
    output_video = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), 30, (x2 - x1, y2 - y1))
    
    while True:
        # フレームを読み込む
        ret, frame = video.read()
        
        if not ret:
            break
        
        # トリミングする領域を切り出す
        trimmed_frame = frame[y1:y2, x1:x2]
        
        # トリミングしたフレームを出力用の動画に書き込む
        output_video.write(trimmed_frame)
    
    # メモリを解放する
    video.release()
    output_video.release()

# 使用例
input_file = 'mixed_5/time_trim/mixed_5_rviz.mp4'
output_file = 'mixed_5/time_size_trim/mixed_5_rviz.mp4'
x = 0.0  # トリミングする領域の左上のx座標の割合
y = 0.09  # トリミングする領域の左上のy座標の割合
width = 0.9  # トリミングする領域の幅の割合
height = 0.84  # トリミングする領域の高さの割合

trim_video(input_file, output_file, x, y, width, height)
