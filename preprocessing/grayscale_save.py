import cv2
image=cv2.imread("indra.jpeg")
if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    choice=int(input("Enter Your Choice \n 1. show \n 2. save \n"))
    if choice==1:
        cv2.imshow("image showing",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice==2:
        success=cv2.imwrite("gray_image.jpg", gray)
        if success:
            print("Image saved successfully!")
        else:
            print("Failed to save image")
    else:
        print("Invalid Choice")
else:
    print("Could not find the image")