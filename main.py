from newsapi import NewsApiClient
import json
import os
import re
from nltk.corpus import stopwords
from math import log
from tkinter import *
import webbrowser
from PIL import Image, ImageTk, ImageSequence

prepositions_path = os.getcwd() + '\\prepositions.txt'
prepositions_file = open(prepositions_path, 'r', encoding='UTF8')
prepositions = prepositions_file.read().split()


def replacement_file(path):

    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    f = open(path, 'r', encoding='UTF8')
    doc = f.read()
    f.close()
    for sym in doc:
        if symbols.find(sym) == -1:
            doc = doc.replace(sym, ' ')
    doc = re.sub(' +', ' ', doc)
    if doc[len(doc) - 1] == ' ':
        doc = doc[:len(doc) - 1]
    doc = doc.split(' ')
    for word in doc:
        if len(word) == 1 or word in prepositions or word in stopwords.words("english") or word == '':
            doc.remove(word)
    #doc = list(set(doc))
    doc = ' '.join(doc)
    #print(doc)
    f = open(path, 'w')
    f.write(doc.lower())
    f.close()


def replacement_text(text):
    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for sym in text:
        if symbols.find(sym) == -1:
            text = text.replace(sym, ' ')
    text = text.lower()
    text = re.sub(' +', ' ', text)
    if text[len(text) - 1] == ' ':
        text = text[:len(text) - 1]
    text = text.split(' ')
    for word in text:
        if len(word) == 1 or word in prepositions or word in stopwords.words("english") or word == '':
            text.remove(word)
    # doc = list(set(text))
    #doc = ' '.join(text)
    return text



newsapi = NewsApiClient(api_key='52857ad900a945aba893edfca853c052')

categories = ['sports', 'business', 'health', 'science']
countries = ['us', 'gb']

#print(json.dumps((newsapi.get_top_headlines(category='sports', country='us')), sort_keys=True, indent=4))


'''
for cat in categories:
    i = 0
    dir = os.getcwd() + '\\' + cat + '\\'
    print('----------------------------------------------------------------------' + '\n@@@' + cat + '@@@\n')
    for cntr in countries:
        top_headlines = newsapi.get_top_headlines(category=cat, country=cntr)
        for a in range(0, len(top_headlines['articles'])):
            if (top_headlines['articles'][a]['content'] != None) and (top_headlines['articles'][a]['source']['name'].find('Youtube') == -1):
                print('###' + str(i) + '###' + '\n' + json.dumps(top_headlines['articles'][a], sort_keys=True, indent=4))
                
                f = open(dir + str(i) + '.txt', 'w')
                #f.write(top_headlines['articles'][a]['content'])
                f.close()
                
                i += 1
'''


'''
for cat in categories:
    dir = os.getcwd() + '\\' + cat + '\\'
    files = os.listdir(dir)
    for f in files:
        path = dir + f
        replacement_file(path)
'''

words_in_dict = {'sports': {}, 'business': {}, 'health': {}, 'science': {}}
num_of_docs = {'sports': 0, 'business': 0, 'health': 0, 'science': 0}
num_of_words_in_cat = {'sports': 0, 'business': 0, 'health': 0, 'science': 0}
'''##############################
for cat in categories:
    #print('----------------------------------------------------------------------' + '\n@@@' + cat + '@@@\n')
    dir = os.getcwd() + '\\' + cat + '\\'
    files = os.listdir(dir)
    num_of_docs[cat] += len(files)
    for i in files:
        words = open(dir + i, 'r', encoding='UTF8').read().split(' ')
        for word in words:
            if words_in_dict[cat].get(word) == None:
                words_in_dict[cat][word] = 1
            else:
                words_in_dict[cat][word] += 1
            num_of_words_in_cat[cat] += 1
    #print(json.dumps(words_in_dict[cat], sort_keys=True, indent=4))
    #print(str(num_of_docs[cat]))
'''


articles = {}
for cat in categories:
    #for country in countries:
    articles[cat] = newsapi.get_top_headlines(category=cat, language='en', country='us')['articles']

#print(json.dumps(text, sort_keys=True, indent=4))
#print(text[4])
#i = 5
#article = replacement_text(text[i]['content'])
#print(article)
'''############################
acc = 0
length = len(text)
for i in text:
    if i['content'] != None:
        article = replacement_text(i['content'])
        max = 0
        max_cat = ''
        for cat in categories:
            sum = 0
            #_log = log(len(words_in_dict[cat]))
            #_log = log(num_of_words_in_cat[cat])
            for word in article:
                if words_in_dict[cat].get(word) != None:
                    sum += log(words_in_dict[cat][word]/num_of_words_in_cat[cat])
            if abs(sum) > max:
                max = abs(sum)
                max_cat = cat
        if max_cat == 'health':
            acc += 1
            #print(cat + ' = ' + str(abs(sum)))
    else:
        length -= 1
print(acc)
print(length)

#print(text[i])

prepositions_file.close()
'''




window = Tk()
lbl = []


def open_url(url):
    webbrowser.open(url)




def changeText(str):
    label.config(text=str + ' news:')
    if str == 'Sport':
        str = 'sports'
    txt.config(state='normal')
    txt.delete(1.0, END)

    lbl.clear()
    link = lambda x: (lambda p: open_url(x))
    y = 0
    i = 0
    '''
    if (str != 'All'):
        for a in articles[str.lower()]:
            lbl.append(Label(txt, text=a['title'], fg='blue', cursor='hand2'))
            lbl[i].place(relx=0, y=y)
            lbl[i].bind('<Button-1>', link(a['url']))
            y += 30
            i += 1
    else:
        for cat in categories:
            for a in articles[cat]:
                lbl.append(Label(txt, text=a['title'], fg='blue', cursor='hand2'))
                lbl[i].place(relx=0, y=y)
                lbl[i].bind('<Button-1>', link(a['url']))
                y += 30
                i += 1
    '''

    if (str != 'All'):
        for a in articles[str.lower()]:
            pos = txt.index(INSERT)
            txt.insert(END, a['title'])
            txt.tag_add(a['url'], pos, END)
            txt.insert(END, '\n\n')
            txt.tag_config(a['url'], foreground='blue', underline=1)
            txt.tag_bind(a['url'], '<Button-1>', link(a['url']))
    else:
        for cat in categories:
            for a in articles[cat]:
                pos = txt.index(INSERT)
                txt.insert(END, a['title'])
                txt.tag_add(a['url'], pos, END)
                txt.insert(END, '\n\n')
                txt.tag_config(a['url'], foreground='blue', underline=1)
                txt.tag_bind(a['url'], '<Button-1>', link(a['url']))

    txt.config(state='disabled')


window.title('News classification')
window.geometry("1000x600+150+50")
#window.configure(bg='#292826')

#frame2 = PhotoImage(file='circle.gif')

frame = Frame(window, bg='#292826')
frame.place(relwidth=1, relheight=1, relx=0, rely=0)


def animate(counter):
    canvas.itemconfig(image, image=sequence[counter])
    frame.after(25, lambda: animate((counter+1) % len(sequence)))

canvas = Canvas(frame, width=100, height=100, bg='#292826', highlightthickness=0)
canvas.place(relx=0.07, rely=0.055)
sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(r'circle2.gif'))]
image = canvas.create_image(50, 50, image=sequence[0])
animate(1)

txt = Text(frame, width=93, height=32)
txt.place(x=240, y=70)
txt.config(state='disabled', cursor='hand2')

label = Label(frame, text='All news:', font="TimesNewRoman 20 bold", bg='#292826', fg='white')
label.place(x=240, y=20)

all_but = Button(frame, width=10, text="All", font="TimesNewRoman 20 bold", command=lambda: changeText("All"))
all_but.place(x=30, y=170)

sport_but = Button(frame, width=10, text="Sport", font="TimesNewRoman 20 bold", command=lambda: changeText("Sport"))
sport_but.place(x=30, y=250)

science_but = Button(frame, width=10, text="Science", font="TimesNewRoman 20 bold", command=lambda: changeText("Science"))
science_but.place(x=30, y=330)

health_but = Button(frame, width=10, text="Health", font="TimesNewRoman 20 bold", command=lambda: changeText("Health"))
health_but.place(x=30, y=410)

business_but = Button(frame, width=10, text="Business", font="TimesNewRoman 20 bold", command=lambda: changeText("Business"))
business_but.place(x=30, y=490)


window.mainloop()
