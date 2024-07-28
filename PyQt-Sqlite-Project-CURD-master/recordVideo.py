import sys

import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QWidget, QApplication

#仅录制视频
class CameraWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.is_recording=True
        # 创建摄像头对象
        self.cap = cv2.VideoCapture(0)

        # 设置视频编解码器和帧率
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # 设置视频输出文件名和路径
        self.video_file = 'output.mp4'
        # 创建一个VideoWriter对象，用于将帧写入视频文件
        self.video_writer = cv2.VideoWriter(self.video_file, self.fourcc, self.fps, (self.width, self.height))

        # 创建QTimer对象，以便每隔一段时间捕获帧
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cap_frame)
        self.timer.start(1000/self.fps)

        # 创建QPushButton对象，用于开始和停止录制视频
        self.start_button = QPushButton('开始录制')
        self.start_button.clicked.connect(self.start_recording)
        self.stop_button = QPushButton('停止录制')
        self.stop_button.clicked.connect(self.stop_recording)

        # 创建QLabel对象，用于显示摄像头捕获的视频
        self.label = QLabel()

        # 创建一个垂直布局管理器，并将QPushButton和QLabel添加到其中
        layout = QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.label)

        # 设置QWidget的布局管理器为垂直布局管理器
        self.setLayout(layout)

        # 设置QWidget的大小
        self.resize(640, 480)

    def cap_frame(self):
        try:
            # 从摄像头中捕获一帧
            ret, frame = self.cap.read()

            if ret:
                # 如果捕获到了帧，则将其显示在QLabel中
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                qimg = QImage(frame_rgb.data, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qimg)
                self.label.setPixmap(pixmap)

                # 如果正在录制视频，则将帧写入视频文件中
                if self.is_recording:
                    self.video_writer.write(frame)  # Note: we're writing the original frame (BGR)
        except Exception as e:
            print(f'Error: {e}')

    def start_recording(self):
        # 开始录制视频
        self.is_recording = True
        self.video_writer = cv2.VideoWriter(self.video_file, self.fourcc, self.fps, (640, 480))

    def stop_recording(self):
        # 停止录制视频，并释放资源
        self.is_recording = False
        self.video_writer.release()

    def closeEvent(self, event):
        # 在关闭窗口时释放摄像头资源
        self.cap.release()
        event.accept()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    recorder = CameraWindow()
    recorder.show()
    sys.exit(app.exec_())