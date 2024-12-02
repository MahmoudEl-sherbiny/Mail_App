import random
import smtplib
import tkinter as tk


window = tk.Tk()
window.title("Send Mail")
window.config(pady=50, padx=50)


def random_quote():
    with open(file="quotes.txt", mode="r") as quotesFile:
        list_of_quotes = quotesFile.readlines()
        r_quote = random.choice(list_of_quotes)
    message_textbox.insert(1.0, r_quote)


def send_mail():
    sender_email = sender_email_entry.get()
    sender_email_password = password_entry.get()
    receiver_email = receiver_email_entry.get()
    message = message_textbox.get("1.0", tk.END)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_email_password)
        connection.sendmail(
                    from_addr=sender_email,
                    to_addrs=receiver_email,
                    msg=f"Subject:Special Quote"
                        f"\n\n{message}"
                )


board = tk.Canvas(width=256, height=256)
logo = tk.PhotoImage(file="logo.png")
board.create_image(130, 100, image=logo)
board.grid(row=0, column=1)

# create labels --> SenderEmail: , Password: , ReceiverEmail, Message
email_label = tk.Label(text="Sender Email:")
email_label.grid(row=1, column=0)

password_label = tk.Label(text="Password:")
password_label.grid(row=2, column=0)

receiver_email_label = tk.Label(text="Receiver Email:")
receiver_email_label.grid(row=3, column=0)

message_Label = tk.Label(text="Message:")
message_Label.grid(row=4, column=0)

# Create Entries
sender_email_entry = tk.Entry(width=55)
sender_email_entry.grid(row=1, column=1, columnspan=2)
sender_email_entry.focus()

password_entry = tk.Entry(width=55, show="*")
password_entry.grid(row=2, column=1, columnspan=2)

receiver_email_entry = tk.Entry(width=55)
receiver_email_entry.grid(row=3, column=1, columnspan=2)

# Create textbox
message_textbox = tk.Text(width=31, height=5)
message_textbox.grid(row=4, column=1, pady=2)

# Buttons
random_quote = tk.Button(text="Quote", width=10, height=5, command=random_quote)
random_quote.grid(row=4, column=2)

send = tk.Button(text="Send", width=47, command=send_mail)
send.grid(row=5, column=1, columnspan=2, pady=4)


window.mainloop()
