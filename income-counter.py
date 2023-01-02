import tkinter as tk

window = tk.Tk()
window.title('Income Counter')

label = tk.Label(
  text=0,
  fg='black',
  bg='#34A2FE',
  width=10,
  height=10
)
label.pack()

entry = tk.Entry(
  bg='red',
  fg='yellow',
  width=5,
)
entry.pack()
entry.insert(0, 0)


total_amount = 0
hourly_rate = 0

def update_amount():
  global total_amount, hourly_rate, button_pressed
  hourly_rate = float(entry.get())

  window.after(1000, update_amount)

  if hourly_rate > 0 and button_pressed == True:
    total_amount += hourly_rate / 60 / 60
    label['text'] = round(total_amount, 2)


button = tk.Button(
  text = 'Start',
  width=25,
  height=5,
  bg='red',
  fg='yellow',
  command=lambda: [update_amount(), update_button_status()]
)
button.pack()


button_pressed = False

def update_button_status():
  global button_pressed
  button_pressed = not button_pressed

  if button_pressed == False:
    button['text'] = 'Start'
    entry['state'] = 'normal'
  else:
    button['text'] = 'Stop'
    entry['state'] = 'readonly'


window.after(1000, update_amount)
window.mainloop()
