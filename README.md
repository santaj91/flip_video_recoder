## 📌 IP Camera Recording Program

이 프로그램은 OpenCV를 이용하여 IP 카메라의 영상을 스트리밍하고,
미리보기(Preview) 모드와 녹화(Record) 모드를 지원합니다.

추가로, 사용자가 f 키를 누르면 영상 좌우 반전(Flip) 기능도 제공됩니다.

# 🚀 주요 기능

1. IP 카메라 스트리밍

  * cv2.VideoCapture를 이용하여 IP 카메라 주소(RTSP 등)에서 영상을 받아옴.

  * 예: rtsp://username:password@192.168.0.10:554/stream

2. Preview / Record 모드

  초기 상태는 미리보기 모드.

  Space 키를 누르면 녹화 모드로 전환/해제.

  녹화 모드일 때 화면 왼쪽 상단에 빨간 점(REC) 표시.

  실제 저장되는 파일에는 빨간 점이 들어가지 않음.

3. 영상 저장

  cv2.VideoWriter를 이용해 AVI (XVID 코덱) 형식으로 저장.

  저장 파일 이름: output.avi

  fps: 20.0, 해상도: 640×480 (필요 시 카메라 해상도에 맞게 변경 가능)

4. Flip 기능

  f 키를 누르면 좌우 반전 토글 (거울 모드).

  반전 상태에서는 화면 표시 + 저장되는 영상 모두 flip 적용됨.

5. 종료

ESC 키를 누르면 프로그램 종료.
