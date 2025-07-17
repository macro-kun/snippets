import cv2


def convert_to_grayscale(img_file):
    img = cv2.imread(img_file)
    grayed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayed_" + img_file, grayed_img)


if __name__ == "__main__":
    img_file = input("変換するファイル: ")
    convert_to_grayscale(img_file)
    print("変換が完了したはずです")
