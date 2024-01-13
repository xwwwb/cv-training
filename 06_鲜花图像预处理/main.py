# 对上一个实验爬取的图片进行处理
import cv2
import numpy as np

OUTPUT_DIR = 'output'


# 缩放
def resize_image(width, height, image):
    return cv2.resize(image, (width, height))


# 灰度图
def rgb2gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# 将图片的值标准化 (x-x_mean)/x_std
def normalize_image(image):
    return cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)


# 图片增强 gamma变换
def gamma_transform(image, gamma):
    invGamma = 1.0 / gamma
    table = []
    for i in range(256):
        table.append(((i / 255.0) ** invGamma) * 255)
    table = np.array(table).astype("uint8")
    return cv2.LUT(image, table)


# 变换图片的对比度和亮度
def contrast_brightness_image(image, alpha, beta):
    blank = np.zeros(image.shape, image.dtype)
    return cv2.addWeighted(image, alpha, blank, 1 - alpha, beta)


# 图片转向量
def image2vector(image):
    # 拿到形状
    shape = image.shape
    # 转换成一维向量
    return image.reshape(shape[0] * shape[1] * shape[2])



if __name__ == '__main__':
    # 读取图片
    image = cv2.imread('../05_鲜花图像爬取/鲜花/1.jpg')
    # 合成一个print
    print("选择需要测试的功能：\n1. 图片缩放\n2. 灰度图\n3. 图片标准化\n4. gamma变换\n5. 对比度和亮度变换\n6. 图片转向量\n7. 退出")

    while True:
        choice = input("请输入你的选择：")
        if choice == '1':
            width = int(input("请输入缩放后的宽度："))
            height = int(input("请输入缩放后的高度："))
            image = resize_image(width, height, image)
            cv2.imshow("image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif choice == '2':
            image = rgb2gray(image)
            cv2.imshow("image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif choice == '3':
            image = normalize_image(image)
            cv2.imshow("image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif choice == '4':
            gamma = float(input("请输入gamma值："))
            image = gamma_transform(image, gamma)
            cv2.imshow("image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif choice == '5':
            alpha = float(input("请输入alpha值："))
            beta = float(input("请输入beta值："))
            image = contrast_brightness_image(image, alpha, beta)
            cv2.imshow("image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif choice == '6':
            image = image2vector(image)
            print(image)
        elif choice == '7':
            break
        else:
            print("输入有误，请重新输入！")
