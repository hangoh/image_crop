from PIL import Image
import os


def imgcrop(input, box):
    files = os.listdir(input)
    print(input)
    print(files)
    for file in files:
        if file == ".DS_Store":
            pass
        else:
            filename, file_extension = os.path.splitext(file)
            im = Image.open(str(input+file))

            a = im.crop(box)
            try:
                a.save('/Users/gohyuhan/Downloads/test_image/' +
                       filename + "-" + "1" + file_extension)
                print('save')
            except:
                print('pass')
                pass


print("start")
box1 = (166, 166, 2614, 2614)
box2 = (2186, 166, 4634, 2614)
imgcrop("/Users/gohyuhan/Downloads/crop_image/", box1)
