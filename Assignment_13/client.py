import socket
import threading
import tkinter as tk
from tkinter import messagebox


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

try:

    s.connect((HOST_NAME, PORT))
    print("Connected to server")

except Exception as err:
    print("Connection failed:", err)
    messagebox.showerror(
        "Connection Error",
        "Could not connect to server.\n"
        "Make sure server.py is running first."
    )
    exit()

def send(listbox, entry):
    message = entry.get()
    if not message.strip():
        return
    try:
        s.send(message.encode("utf-8"))
        listbox.insert(tk.END, "Client: " + message)
        entry.delete(0, tk.END)
    except Exception as err:
        messagebox.showerror(
            "Send Error",
            f"Could not send message:\n{err}"
        )

def receive_messages(listbox):
    while True:
        try:
            # Increased buffer size
            message = s.recv(1024)
            # Detect disconnect
            if not message:
                listbox.insert(tk.END, "Server disconnected.")
                break

            decoded = message.decode("utf-8")
            listbox.insert(
                tk.END,
                "Server: " + decoded
            )
        except Exception as err:
            listbox.insert(
                tk.END,
                f"Receive error: {err}"
            )
            break

def on_closing():
    try:
        s.close()
    except:
        pass
    root.destroy()

root = tk.Tk()
root.title("Client Chat")

listbox = tk.Listbox(root, width=50, height=20)
listbox.pack()

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT)

button = tk.Button(
    root,
    text="Send",
    command=lambda: send(listbox, entry)
)
button.pack(side=tk.LEFT)

receive_thread = threading.Thread(
    target=receive_messages,
    args=(listbox,),
    daemon=True
)

receive_thread.start()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()