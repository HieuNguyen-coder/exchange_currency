import requests as rq
from bs4 import BeautifulSoup
from tkinter import ttk 
from tkinter import *
from tkinter import messagebox as mb

url="https://www.agribank.com.vn/vn/ty-gia"
response = rq.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

cur_dict = {}

currency = soup.find_all('tr')
for cur in currency:
    c_type = cur.find_all('td')
    if len(c_type)>0:
        country, cash, transfer, price = c_type[0].text.replace(",", ""), c_type[1].text.replace(",", ""), c_type[2].text.replace(",", ""), c_type[3].text.replace(",", "")
        if len(country)==3:
            cur_dict[country] = [float(cash), float(transfer), float(price)]
cur_dict["VND"] = [1, 1, 1]

def curr_exchange():
    try:
        choice1 = input_choice.get()
        choice2 = output_choice.get()
        choice1_value = float(input_value.get())
        denomination1 = cur_dict[choice1][1]
        denomination2 = cur_dict[choice2][1]
        output_result.configure(text=str(round(denomination1*choice1_value/denomination2, 2)))
    except:
        if len(choice1)==0 or len(choice2)==0:
            mb.showerror("Error", "Choose currency unit !!!")
        else:
            mb.showerror("Error", "Unable to exchange !!!")

root = Tk()
root.title("NguyenNDH")
root.geometry("500x300")
label = Label(root, text="Currency exchange rate", font=("digital-7", 30, "bold"), foreground="green")
label.pack(pady=10)

choices = list(cur_dict.keys())

input_frame = Frame(root)
input_label = Label(input_frame, text="Input currency", font=("tahoma", 15, "bold"), foreground="green")
input_label.pack()

input_choice = ttk.Combobox(input_frame, values=choices, width=5)
input_choice.pack(side=RIGHT)

input_value = StringVar()
input_entry = Entry(input_frame, width = 15, textvariable=input_value, font=("tahoma", 12))
input_entry.pack(side=LEFT)
input_frame.place(x=20, y=100)

output_frame = Frame(root)
output_label = Label(output_frame, text="Output currency", font=("tahoma", 15, "bold"), foreground="green")
output_label.pack()

output_choice = ttk.Combobox(output_frame, values=choices, width=5)
output_choice.pack(side=RIGHT)

output_result = Label(output_frame, font=("tahoma"))
output_result.pack(side=LEFT)
output_frame.place(x=300, y=100)

exchange = Button(root, text="Exchange", font=("tahoma"), activebackground="green", command=curr_exchange)
exchange.pack(pady=100)

root.mainloop()