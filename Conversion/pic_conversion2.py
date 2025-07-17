import skimage as ski


def convert_to_grayscale(img_file):
    img = ski.io.imread(img_file)
    grayed_img = ski.color.rgb2gray(img)
    grayed_img = ski.img_as_ubyte(grayed_img)
    ski.io.imsave("grayed2_" + img_file, grayed_img)


if __name__ == "__main__":
    img_file = input("変換するファイル: ")
    convert_to_grayscale(img_file)
    print("変換が完了したはずです")
