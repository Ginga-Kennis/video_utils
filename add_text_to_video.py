import cv2

def add_text_to_image(image, text, position, font_scale, color, thickness):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, position, font, font_scale, color, thickness)

if __name__ == '__main__':
    # 動画の読み込み
    video_path = 'mixed_5/mixed_5.mp4'
    video = cv2.VideoCapture(video_path)

    # 動画のプロパティを取得
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 動画の保存設定
    output_path = 'mixed_5/mixed_5_with_text.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        # フレームを読み込む
        ret, frame = video.read()

        if not ret:
            break

        # テキストを追加
        text = 'Environment'
        position = (30, 40)
        font_scale = 1.25
        color = (0, 0, 0)  # (B, G, R)
        thickness = 3
        add_text_to_image(frame, text, position, font_scale, color, thickness)

        # テキストを追加
        text = 'RGB image'
        position = (970, 40)
        font_scale = 1.25
        color = (0, 0, 0)  # (B, G, R)
        thickness = 3
        add_text_to_image(frame, text, position, font_scale, color, thickness)

        # テキストを追加
        text = 'Segmented image'
        position = (970, 485)
        font_scale = 1.25
        color = (255, 255, 255)  # (B, G, R)
        thickness = 3
        add_text_to_image(frame, text, position, font_scale, color, thickness)

        # テキストを追加
        text = '3D measurement result & Grasp poses'
        position = (1560, 40)
        font_scale = 1.25
        color = (255, 255, 255)  # (B, G, R)
        thickness = 3
        add_text_to_image(frame, text, position, font_scale, color, thickness)

        # フレームを保存
        writer.write(frame)

        # 画面に表示
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # リソースを解放
    video.release()
    writer.release()
    cv2.destroyAllWindows()
