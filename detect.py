import cv2
import numpy as np
import time

from mtcnn import mtcnn

if __name__ == "__main__":

    def display(img, threshold):
        # -------------------------------------#
        #   将图片传入并检测
        # -------------------------------------#
        temp_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        rectangles = model.detectFace(temp_img, threshold)

        draw = img.copy()
        for rectangle in rectangles:
            W = int(rectangle[2]) - int(rectangle[0])
            H = int(rectangle[3]) - int(rectangle[1])

            cv2.rectangle(draw, (int(rectangle[0]), int(rectangle[1])), (int(rectangle[2]), int(rectangle[3])),
                          (0, 0, 255),
                          2)

            for i in range(5, 15, 2):
                cv2.circle(draw, (int(rectangle[i + 0]), int(rectangle[i + 1])), 1, (255, 0, 0), 4)

        # cv2.imwrite(out_path, draw)
        cv2.imshow("test", draw)


    model = mtcnn()
    # -------------------------------------#
    #   设置检测门限
    # -------------------------------------#
    threshold = [0.5, 0.6, 0.7]
    # -------------------------------------#
    #   读取图片
    # -------------------------------------#
    NUM = int(input('输入数字,1代表检测图片，其他代表检测视频：'))
    if NUM==1:
        num = 3
        in_path = 'img/f'+str(num)+'.jpeg'
        out_path = "img/out"+str(num)+".jpg"
        img = cv2.imread(in_path)
        s = time.time()
        display(img, threshold)
        print('单张图片耗时：{}s'.format(round(time.time() - s, 2)))
        c = cv2.waitKey(0)

    else:
        cap = cv2.VideoCapture('img/zhou.mp4')
        while (cap.isOpened()):
            s = time.time()
            ret, frame = cap.read()
            display(frame, threshold)
            print('一帧耗时：{}s'.format(round(time.time()-s,2)))
            if cv2.waitKey(1) == ord('q'):
                break
        # 完成所有操作后，释放捕获器
        cap.release()
        cv2.destroyAllWindows()



