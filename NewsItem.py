from tkinter import *
from PIL import ImageTk, Image
import requests, webbrowser
from io import BytesIO

def getImage(urlToImage="https://img.jagranjosh.com/images/2022/April/442022/Axiom_Mission_1_crew_members.jpg"):
    response = requests.get(urlToImage)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    fixed_width = 480
    height_percent = (float(fixed_width) / float(img.size[0]))
    w_size = int((float(img.size[1]) * float(height_percent)))
    img = img.resize((fixed_width,w_size))
    return img

class NewsItem(Frame):

    def __init__(self,master,news):
        super().__init__(master)
        self.news = news
        self.addImage()
        self.addTitle()
        self.addDescription()
        self.addVisitButton()

    def open_browser(self):
        webbrowser.open(self.news.url)

    def addImage(self):
        if self.news.urlToImage != None:
            try:
                image_file = getImage(self.news.urlToImage)
                self.image_file = ImageTk.PhotoImage(image_file)

                news_image = Label(self,image=self.image_file)
                news_image.pack(side=TOP,anchor=NW,padx=10,pady=10)
            except:
                pass

    def addTitle(self):
        title = Label(self, text="Title: " + self.news.title, justify=LEFT, wraplengt=480, bg="#FFFFFF",font="nunito 10 bold")
        title.pack(side=TOP, anchor=NW, padx=10, pady=5)


    def addDescription(self):
        description = Label(self, text=("Description: " + str(self.news.description)),justify=LEFT,wraplengt=480,bg="#FFFFFF",font="nunito 10 bold")
        description.pack(side=TOP, anchor=NW, padx=10, pady=5)

    def addVisitButton(self):
        view = Button(self,text="Read More",command=self.open_browser,bd=1,relief=FLAT,font="nunito 10 bold")
        view.pack(side=TOP, anchor=NW,fill=X, padx=10, pady=10)




