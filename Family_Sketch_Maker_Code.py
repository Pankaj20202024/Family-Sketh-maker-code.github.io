import time
import tkinter

import cv2
from turtle import Screen
import turtle
from pygame import mixer
from tkinter import *

global flag
flag = 0

global flag3
flag3=0

global flag1
flag1 = 0

global flag4
flag4 = 0


def family_images(flag3):
    if flag3 == 1:
            mixer.init()
            music = mixer.Sound("C:\\Users\\hplap\\Music\\Palat.mp3")
            music.play()
            img = cv2.imread("papa4.jpeg", 0)
            print(img.shape)
            print("width  : ", int(img.shape[1]))
            print("height  : ", int(img.shape[0]))

            scale_factor = 65

            width = int(img.shape[1] * (scale_factor / 100))
            height = int(img.shape[0] * (scale_factor / 100))
            dim = (width, height)
            print(dim)
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)
            my_screen = Screen()
            my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)
            my_pen = turtle.Turtle()
            my_pen.shape("turtle")
            my_pen.color("gray17")
            my_screen.tracer(0)
            my_screen.bgcolor("papayawhip")
            turtle.hideturtle()
            for i in range(int(height / 2), int(height / -2), -1):
                my_pen.penup()
                my_pen.goto(-(width / 2), i)

                for l in range(-int(width / 2), int(width/ 2), 1):
                    pix_width = int(l + (width / 2))
                    pix_height = int(height / 2 - i)
                    if bw_img[pix_height, pix_width] == 0:
                        turtle.speed(10)
                        my_pen.pendown()
                        my_pen.hideturtle()
                        my_pen.forward(1)
                    else:
                        turtle.speed(10)
                        my_pen.penup()
                        my_pen.forward(1)
                my_screen.update()
            music.stop()
            print("completed")
            turtle.clear()
            print("completed")
            my_screen.reset()
            print("completed")
            time.sleep(10)
            turtle.done()

    elif flag3==2:
            mixer.init()

            music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")
            music.play()

            img = cv2.imread("chandni1.jpeg", 0)
            print(img.shape)
            print("width  : ", int(img.shape[1]))
            print("height  : ", int(img.shape[0]))

            scale_factor = 40

            width = int(img.shape[1] * (scale_factor / 100))
            height = int(img.shape[0] * (scale_factor / 100))
            dim = (width, height)
            print(dim)

            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)
            print("check")

            my_screen = Screen()

            my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)
            my_pen = turtle.Turtle()
            my_pen.shape("turtle")
            my_pen.color("gray17")
            my_screen.tracer(0)
            my_screen.bgcolor("papayawhip")
            turtle.hideturtle()
            for i in range(int(height / 2), int(height / -2), -1):
                my_pen.penup()
                my_pen.goto(-(width / 2), i)

                for l in range(-int(width / 2), int(width / 2), 1):
                    pix_width = int(l + (width / 2))
                    pix_height = int(height / 2 - i)
                    if bw_img[pix_height, pix_width] == 0:
                        turtle.speed(10)
                        my_pen.hideturtle()
                        my_pen.pendown()
                        my_pen.forward(1)
                    else:
                        turtle.speed(10)
                        my_pen.penup()
                        my_pen.forward(1)
                my_screen.update()
            music.stop()
            print("completed")
            turtle.clear()
            print("completed")
            time.sleep(10)
            my_screen.reset()
            print("completed")
            turtle.done()

    elif flag3 == 3:

        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("prithvi.jpg", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 80

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()

    elif flag3 == 4:
        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("mamta4.jpeg", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 60

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()

    elif flag3 == 5:
        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("mummy2.jpeg", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 40

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()

    elif flag3==6:
        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("mamta4.jpeg", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 60

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()
    else:
        print("completed")


def Papa():
    global flag3
    flag3=1
    family_images(flag3)


def chandni():
    global flag3
    flag3=2
    family_images(flag3)

def for_prithvi_image():
    global flag3
    flag3=3
    family_images(flag3)


def Mamta():
    global flag3
    flag3=4
    family_images(flag3)


def Mummy():
    global flag3
    flag3=5
    family_images(flag3)

def family_member():
    global flag3
    flag3=6
    family_images(flag3)

def show_navbar():
    global btnstate, btnstate1
    if btnstate is False:
        for i in range(-333, 0):
            navbar_label.place(x=i, y=0)
            navbar_frame2.update()
        btnstate = True
        if btnstate1 is True:
            for j in range(348, 738):
                option_label.place(x=j, y=65)
                root.update()
                btnstate1 = False
    else:
        for i in range(333):
            navbar_label.place(x=-i, y=0)
            navbar_frame2.update()
        btnstate = False


def family_member_name_options():
    ############## creating button for image making functions caller #################
    Papa_button = Button(option_label, width=10, height=2, text="Papa", bg="aquamarine",
                         font=("arial", 14, "italic bold")
                         , fg="navy", activebackground="aquamarine3", activeforeground="navy", bd=8,
                         command=Papa)
    Papa_button.place(x=130, y=30)

    chandni_button = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                            text="Chandni\nRaikwal",
                            font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                            command=chandni)
    chandni_button.place(x=15, y=150)

    prithvi_button = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                            text="Prithvi\nRaikwal",
                            font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                            command=for_prithvi_image)
    prithvi_button.place(x=235, y=150)

    Mamta_button = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                          text="Mamta\nRaikwal",command=Mamta,
                          font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy")
    Mamta_button.place(x=15, y=280)

    Mummy_button = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                          text="Mummy",command=Mummy,
                          font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy")
    Mummy_button.place(x=235, y=280)

    Whole_family_button = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                                 text="Family\nPhoto",command=family_member,
                                 font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy")
    Whole_family_button.place(x=130, y=400)


def Family_images():
    family_member_name_options()
    global btnstate, btnstate1
    btnstate = True
    if btnstate is True:
        for i in range(333):
            navbar_label.place(x=-i, y=0)
            navbar_frame2.update()
        btnstate = False
    if btnstate1 is False:
        for i in range(-738, -348):
            option_label.place(x=-i, y=65)
            root.update()
            btnstate1 = True

def Show_Group_Images(flag1):
    if flag1 == 1:
            mixer.init()
            music = mixer.Sound("C:\\Users\\hplap\\Music\\Palat.mp3")
            music.play()
            img = cv2.imread("group1.jpg", 0)
            print(img.shape)
            print("width  : ", int(img.shape[1]))
            print("height  : ", int(img.shape[0]))

            scale_factor = 38

            width = int(img.shape[1] * (scale_factor / 100))
            height = int(img.shape[0] * (scale_factor / 100))
            dim = (width, height)
            print(dim)
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)
            my_screen = Screen()
            my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)
            my_pen = turtle.Turtle()
            my_pen.shape("turtle")
            my_pen.color("gray17")
            my_screen.tracer(0)
            my_screen.bgcolor("papayawhip")
            turtle.hideturtle()
            for i in range(int(height / 2), int(height / -2), -1):
                my_pen.penup()
                my_pen.goto(-(width / 2), i)

                for l in range(-int(width / 2), int(width/ 2), 1):
                    pix_width = int(l + (width / 2))
                    pix_height = int(height / 2 - i)
                    if bw_img[pix_height, pix_width] == 0:
                        turtle.speed(10)
                        my_pen.pendown()
                        my_pen.hideturtle()
                        my_pen.forward(1)
                    else:
                        turtle.speed(10)
                        my_pen.penup()
                        my_pen.forward(1)
                my_screen.update()
            music.stop()
            print("completed")
            turtle.clear()
            print("completed")
            my_screen.reset()
            print("completed")
            time.sleep(10)
            turtle.done()

    elif flag1==2:
            mixer.init()

            music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")
            music.play()

            img = cv2.imread("group1.jpg", 0)
            print(img.shape)
            print("width  : ", int(img.shape[1]))
            print("height  : ", int(img.shape[0]))

            scale_factor = 38

            width = int(img.shape[1] * (scale_factor / 100))
            height = int(img.shape[0] * (scale_factor / 100))
            dim = (width, height)
            print(dim)

            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)
            print("check")

            my_screen = Screen()

            my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)
            my_pen = turtle.Turtle()
            my_pen.shape("turtle")
            my_pen.color("gray17")
            my_screen.tracer(0)
            my_screen.bgcolor("papayawhip")
            turtle.hideturtle()
            for i in range(int(height / 2), int(height / -2), -1):
                my_pen.penup()
                my_pen.goto(-(width / 2), i)

                for l in range(-int(width / 2), int(width / 2), 1):
                    pix_width = int(l + (width / 2))
                    pix_height = int(height / 2 - i)
                    if bw_img[pix_height, pix_width] == 0:
                        turtle.speed(10)
                        my_pen.hideturtle()
                        my_pen.pendown()
                        my_pen.forward(1)
                    else:
                        turtle.speed(10)
                        my_pen.penup()
                        my_pen.forward(1)
                my_screen.update()
            music.stop()
            print("completed")
            turtle.clear()
            print("completed")
            time.sleep(10)
            my_screen.reset()
            print("completed")
            turtle.done()

    elif flag1 == 3:

        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("group2.jpg", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 38

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()

    elif flag1 == 4:
        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("mamta4.jpeg", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 60

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()

    elif flag1 == 5:
        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("mummy2.jpeg", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 40

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()

    elif flag1==6:
        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("mamta4.jpeg", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 60

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()
    else:
        print("completed")

def show_group_imges1():
    global flag1
    flag1=1;
    Show_Group_Images(flag1)

def show_group_imges2():
    global flag1
    flag1 = 2;
    Show_Group_Images(flag1)

def show_group_imges3():
    global flag1
    flag1 = 3;
    Show_Group_Images(flag1)

def show_group_imges4():
    global flag1
    flag1 = 4;
    Show_Group_Images(flag1)

def show_group_imges5():
    global flag1
    flag1 = 5;
    Show_Group_Images(flag1)

def show_group_imges6():
    global flag1
    flag1 = 6;
    Show_Group_Images(flag1)

def group_images_options():
    ############## creating button for image making functions caller #################

    image1 = Button(option_label, width=10, height=2, text="Image1", bg="aquamarine",
                    font=("arial", 14, "italic bold")
                    , fg="navy", activebackground="aquamarine3", activeforeground="navy", bd=8,
                    command=show_group_imges1)
    image1.place(x=130, y=30)

    image2 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                    text="Image2", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                    command=show_group_imges2)
    image2.place(x=15, y=150)

    image3 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                    text="Image3", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                    command=show_group_imges3)
    image3.place(x=235, y=150)

    image4 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                    text="Image4", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                    command=show_group_imges4)
    image4.place(x=15, y=280)

    image5 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                    text="Image5", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                    command=show_group_imges5)
    image5.place(x=235, y=280)

    image6 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                    text="Image6", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                    command=show_group_imges6)
    image6.place(x=130, y=400)


def group():
    group_images_options()
    global btnstate, btnstate1
    btnstate = True
    if btnstate is True:
        for i in range(333):
            navbar_label.place(x=-i, y=0)
            navbar_frame2.update()
        btnstate = False
    if btnstate1 is False:
        for i in range(-738, -348):
            option_label.place(x=-i, y=65)
            root.update()
            btnstate1 = True

# code for displaying the images for friends

def friend_images(flag):
    if flag == 1:
            mixer.init()
            music = mixer.Sound("C:\\Users\\hplap\\Music\\Palat.mp3")
            music.play()
            img = cv2.imread("shradha.jpg", 0)
            print(img.shape)
            print("width  : ", int(img.shape[1]))
            print("height  : ", int(img.shape[0]))

            scale_factor = 50

            width = int(img.shape[1] * (scale_factor / 100))
            height = int(img.shape[0] * (scale_factor / 100))
            dim = (width, height)
            print(dim)
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)
            my_screen = Screen()
            my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)
            my_pen = turtle.Turtle()
            my_pen.shape("turtle")
            my_pen.color("gray17")
            my_screen.tracer(0)
            my_screen.bgcolor("papayawhip")
            turtle.hideturtle()
            for i in range(int(height / 2), int(height / -2), -1):
                my_pen.penup()
                my_pen.goto(-(width / 2), i)

                for l in range(-int(width / 2), int(width/ 2), 1):
                    pix_width = int(l + (width / 2))
                    pix_height = int(height / 2 - i)
                    if bw_img[pix_height, pix_width] == 0:
                        turtle.speed(10)
                        my_pen.pendown()
                        my_pen.hideturtle()
                        my_pen.forward(1)
                    else:
                        turtle.speed(10)
                        my_pen.penup()
                        my_pen.forward(1)
                my_screen.update()
            music.stop()
            print("completed")
            turtle.clear()
            print("completed")
            my_screen.reset()
            print("completed")
            time.sleep(10)
            turtle.done()

    elif flag==2:
            mixer.init()

            music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")
            music.play()

            img = cv2.imread("bibhas.png", 0)
            print(img.shape)
            print("width  : ", int(img.shape[1]))
            print("height  : ", int(img.shape[0]))

            scale_factor = 68

            width = int(img.shape[1] * (scale_factor / 100))
            height = int(img.shape[0] * (scale_factor / 100))
            dim = (width, height)
            print(dim)

            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)
            print("check")

            my_screen = Screen()

            my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)
            my_pen = turtle.Turtle()
            my_pen.shape("turtle")
            my_pen.color("gray17")
            my_screen.tracer(0)
            my_screen.bgcolor("papayawhip")
            turtle.hideturtle()
            for i in range(int(height / 2), int(height / -2), -1):
                my_pen.penup()
                my_pen.goto(-(width / 2), i)

                for l in range(-int(width / 2), int(width / 2), 1):
                    pix_width = int(l + (width / 2))
                    pix_height = int(height / 2 - i)
                    if bw_img[pix_height, pix_width] == 0:
                        turtle.speed(10)
                        my_pen.hideturtle()
                        my_pen.pendown()
                        my_pen.forward(1)
                    else:
                        turtle.speed(10)
                        my_pen.penup()
                        my_pen.forward(1)
                my_screen.update()
            music.stop()
            print("completed")
            turtle.clear()
            print("completed")
            time.sleep(10)
            my_screen.reset()
            print("completed")
            turtle.done()

    elif flag == 3:

        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("abdullah.png", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 80

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()

    elif flag == 4:
        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("pradeep.png", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 60

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()

    elif flag == 5:
        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("satwik.png", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 60

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()

    elif flag==6:
        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("rahul.png", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 65

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()
    else:
        print("completed")

def show_shraddha():
    global flag
    flag = 1
    friend_images(flag)

def Bibhas_saho():
    global flag
    flag = 2
    friend_images(flag)

def Abdullah():
    global flag
    flag = 3
    friend_images(flag)

def pradeep_bora():
    global flag
    flag = 4
    friend_images(flag)



def Satwik_bhist():
    global flag
    flag = 5
    friend_images(flag)

def Rahul_sharma():
    global flag
    flag = 6
    friend_images(flag)
    
def friends_images_options():
    ############## creating button for image making functions caller #################

    image1 = Button(option_label, width=10, height=2, text="Shraddha\nSingh", bg="aquamarine",
                    font=("arial", 14, "italic bold"), fg="navy",activebackground="aquamarine3",
                    activeforeground="navy", bd=8,justify=tkinter.LEFT,
                    command=show_shraddha)
    image1.place(x=130, y=30)

    image2 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",justify=tkinter.LEFT,
                    text="Bibhas\n Saho", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                    command=Bibhas_saho)
    image2.place(x=15, y=150)

    image3 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",justify=tkinter.LEFT,
                    text="Abdullah", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                    command=Abdullah)
    image3.place(x=235, y=150)

    image4 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",justify=tkinter.LEFT,
                    text="Pradeep\nBora", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy"
                    ,command=pradeep_bora)
    image4.place(x=15, y=280)

    image5 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",justify=tkinter.LEFT,
                    text="Satwik\nBhist", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy"
                    ,command=Satwik_bhist)
    image5.place(x=235, y=280)

    image6 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",justify=tkinter.LEFT,
                    text="Rahul\nSharma", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy"
                    ,command=Rahul_sharma)
    image6.place(x=130, y=400)


def friends():
    friends_images_options()
    global btnstate, btnstate1
    btnstate = True
    if btnstate is True:
        for i in range(333):
            navbar_label.place(x=-i, y=0)
            navbar_frame2.update()
        btnstate = False
    if btnstate1 is False:
        for i in range(-738, -348):
            option_label.place(x=-i, y=65)
            root.update()
            btnstate1 = True

# code for showing the childhood_images

def show_childhood_images(flag4):
    if flag4 == 1:
            mixer.init()
            music = mixer.Sound("C:\\Users\\hplap\\Music\\Palat.mp3")
            music.play()
            img = cv2.imread("papa4.jpeg", 0)
            print(img.shape)
            print("width  : ", int(img.shape[1]))
            print("height  : ", int(img.shape[0]))

            scale_factor = 65

            width = int(img.shape[1] * (scale_factor / 100))
            height = int(img.shape[0] * (scale_factor / 100))
            dim = (width, height)
            print(dim)
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)
            my_screen = Screen()
            my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)
            my_pen = turtle.Turtle()
            my_pen.shape("turtle")
            my_pen.color("gray17")
            my_screen.tracer(0)
            my_screen.bgcolor("papayawhip")
            turtle.hideturtle()
            for i in range(int(height / 2), int(height / -2), -1):
                my_pen.penup()
                my_pen.goto(-(width / 2), i)

                for l in range(-int(width / 2), int(width/ 2), 1):
                    pix_width = int(l + (width / 2))
                    pix_height = int(height / 2 - i)
                    if bw_img[pix_height, pix_width] == 0:
                        turtle.speed(10)
                        my_pen.pendown()
                        my_pen.hideturtle()
                        my_pen.forward(1)
                    else:
                        turtle.speed(10)
                        my_pen.penup()
                        my_pen.forward(1)
                my_screen.update()
            music.stop()
            print("completed")
            turtle.clear()
            print("completed")
            my_screen.reset()
            print("completed")
            time.sleep(10)
            turtle.done()

    elif flag4==2:
            mixer.init()

            music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")
            music.play()

            img = cv2.imread("chandni1.jpeg", 0)
            print(img.shape)
            print("width  : ", int(img.shape[1]))
            print("height  : ", int(img.shape[0]))

            scale_factor = 40

            width = int(img.shape[1] * (scale_factor / 100))
            height = int(img.shape[0] * (scale_factor / 100))
            dim = (width, height)
            print(dim)

            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)
            print("check")

            my_screen = Screen()

            my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)
            my_pen = turtle.Turtle()
            my_pen.shape("turtle")
            my_pen.color("gray17")
            my_screen.tracer(0)
            my_screen.bgcolor("papayawhip")
            turtle.hideturtle()
            for i in range(int(height / 2), int(height / -2), -1):
                my_pen.penup()
                my_pen.goto(-(width / 2), i)

                for l in range(-int(width / 2), int(width / 2), 1):
                    pix_width = int(l + (width / 2))
                    pix_height = int(height / 2 - i)
                    if bw_img[pix_height, pix_width] == 0:
                        turtle.speed(10)
                        my_pen.hideturtle()
                        my_pen.pendown()
                        my_pen.forward(1)
                    else:
                        turtle.speed(10)
                        my_pen.penup()
                        my_pen.forward(1)
                my_screen.update()
            music.stop()
            print("completed")
            turtle.clear()
            print("completed")
            time.sleep(10)
            my_screen.reset()
            print("completed")
            turtle.done()

    elif flag4 == 3:

        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("prithvi.jpg", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 80

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()

    elif flag4 == 4:
        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("mamta4.jpeg", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 60

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()

    elif flag4 == 5:
        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("mummy2.jpeg", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 40

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()

    elif flag4==6:
        mixer.init()

        music = mixer.Sound("C:\\Users\\hplap\\Music\\palat.mp3")

        music.play()

        img = cv2.imread("mamta4.jpeg", 0)

        print(img.shape)

        print("width  : ", int(img.shape[1]))

        print("height  : ", int(img.shape[0]))

        scale_factor = 60

        width = int(img.shape[1] * (scale_factor / 100))

        height = int(img.shape[0] * (scale_factor / 100))

        dim = (width, height)

        print(dim)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        ret, bw_img = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

        print("check")

        my_screen = Screen()

        my_screen.screensize(canvwidth=width + 60, canvheight=height + 150)

        my_pen = turtle.Turtle()

        my_pen.shape("turtle")

        my_pen.color("gray17")

        my_screen.tracer(0)

        my_screen.bgcolor("papayawhip")

        turtle.hideturtle()

        for i in range(int(height / 2), int(height / -2), -1):

            my_pen.penup()

            my_pen.goto(-(width / 2), i)

            for l in range(-int(width / 2), int(width / 2), 1):

                pix_width = int(l + (width / 2))

                pix_height = int(height / 2 - i)

                if bw_img[pix_height, pix_width] == 0:

                    turtle.speed(10)

                    my_pen.hideturtle()

                    my_pen.pendown()

                    my_pen.forward(1)

                else:

                    turtle.speed(10)

                    my_pen.penup()

                    my_pen.forward(1)

            my_screen.update()

        music.stop()

        print("completed")

        turtle.clear()

        print("completed")

        time.sleep(10)

        my_screen.reset()

        print("completed")

        turtle.done()
    else:
        print("completed")

def childhood_image1():
    global flag4
    flag4=1
    show_childhood_images(flag4)

def childhood_image2():
    global flag4
    flag4=2
    show_childhood_images(flag4)

def childhood_image3():
    global flag4
    flag4=3
    show_childhood_images(flag4)

def childhood_image4():
    global flag4
    flag4=4
    show_childhood_images(flag4)

def childhood_image5():
    global flag4
    flag4=5
    show_childhood_images(flag4)

def childhood_image6():
    global flag4
    flag4=6
    show_childhood_images(flag4)

def childhood_images_options():
    ############## creating button for image making functions caller #################

    image1 = Button(option_label, width=10, height=2, text="Image1", bg="aquamarine",
                    font=("arial", 14, "italic bold"),command=childhood_image1
                    , fg="navy", activebackground="aquamarine3", activeforeground="navy", bd=8)
    image1.place(x=130, y=30)

    image2 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                    text="Image2", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                    command = childhood_image2
                    )
    image2.place(x=15, y=150)

    image3 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                    text="Image3", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                    command=childhood_image3
                    )
    image3.place(x=235, y=150)

    image4 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                    text="Image4", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                    command = childhood_image4)
    image4.place(x=15, y=280)

    image5 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                    text="Image5", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                    command = childhood_image5)
    image5.place(x=235, y=280)

    image6 = Button(option_label, width=10, height=2, bg="aquamarine", activebackground="aquamarine3",
                    text="Image6", font=("arial ", 14, "italic bold"), fg="navy", bd=8, activeforeground="navy",
                    command = childhood_image6)
    image6.place(x=130, y=400)


def childhood_images():
    childhood_images_options()
    global btnstate, btnstate1
    btnstate = True
    if btnstate is True:
        for i in range(333):
            navbar_label.place(x=-i, y=0)
            navbar_frame2.update()
        btnstate = False
    if btnstate1 is False:
        for i in range(-738, -348):
            option_label.place(x=-i, y=65)
            root.update()
            btnstate1 = True


def create():
    #####################making the global variable #################
    global nav_button_image, close_button, navbar_frame2, navbar_label, btnstate, option_label, btnstate1

    #################### putton image on python project #########################
    nav_button_image = PhotoImage(file="menu.png")
    close_button = PhotoImage(file="cancel.png")

    ################### resizing the images ######################################

    nav_button_image = nav_button_image.subsample(11, 11)
    close_button = close_button.subsample(12, 12)

    ################################# creating the project heading #############################
    Project_heading = Label(root, width=35, height=2, text="Automatic Family Member Sketch Maker",
                            font=("arial", 21, "bold "), fg="aquamarine", bg="gray17")
    Project_heading.place(x=80, y=0)

    ######################### creating nav bar  ########################

    navbar_frame = LabelFrame(root, width=305, height=580, bg='gray17', bd=0)
    navbar_frame.place(x=1, y=65)

    navbar_frame2 = LabelFrame(navbar_frame, width=300, height=575, bg="gray17", bd=0)
    navbar_frame2.place(x=1, y=1)

    btnstate = False
    btnstate1 = False

    nav_button = Button(navbar_frame2, width=50, height=40, bg="gray17", image=nav_button_image,
                        activebackground="gray17", bd=0,
                        command=show_navbar)
    nav_button.place(x=1, y=1)

    navbar_label = LabelFrame(navbar_frame2, width=300, height=530, bg="aquamarine", bd=5)
    navbar_label.place(x=-333, y=0)

    navbar_topframe_label = Label(navbar_label, width=41, height=3, bg="aquamarine4", bd=1)
    navbar_topframe_label.place(x=0, y=0)

    close_bar_button = Button(navbar_label, width=45, height=43, bg="aquamarine4", image=close_button, bd=0
                              , activebackground="aquamarine4", command=show_navbar)
    close_bar_button.place(x=242, y=1)

    ########### options inside the nav bar ##################
    option1 = Button(navbar_label, width=20, height=2, bg="aquamarine", text="Family Members Images", bd=0,
                     font=("arial", 14, "italic bold "), activebackground="aquamarine", fg="navy",
                     activeforeground="purple",
                     command=Family_images)
    option1.place(x=1, y=67)
    option2 = Button(navbar_label, width=16, height=2, bg="aquamarine", text="Childhood Images", bd=0,
                     font=("arial", 14, "italic bold "), activebackground="aquamarine", fg="navy",
                     activeforeground="purple",
                     command=childhood_images)
    option2.place(x=1, y=140)

    option3 = Button(navbar_label, width=16, height=2, bg="aquamarine", text="Group Images ", bd=0,
                     font=("arial", 14, "italic bold "), activebackground="aquamarine", fg="navy",
                     activeforeground="purple"
                     , command=group)
    option3.place(x=1, y=210)

    option4 = Button(navbar_label, width=16, height=2, bg="aquamarine", text="Friends Images ", bd=0,
                     font=("arial", 14, "italic bold "), activebackground="aquamarine", fg="navy",
                     activeforeground="purple"
                     , command=friends)
    option4.place(x=1, y=260)

    ##################### creating the label for putting options #####################
    option_label = LabelFrame(root, width=400, height=580, bg="gray17", bd=0)
    option_label.place(x=738, y=65)


root = Tk()

root.title("Creating the family sketch")
root.resizable(False, False)
root.geometry("750x600+350+20")
root.config(bg="gray17")
root.iconbitmap("family.ico")
create()
root.mainloop()
