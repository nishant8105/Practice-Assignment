import socket
import threading
import tkinter as tk
from tkinter import messagebox


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

try:
    server_socket.bind((HOST_NAME, PORT))
    server_socket.listen(1)
    print("Waiting for client...")
    client, address = server_socket.accept()
    print("Client connected:", address)

except Exception as err:
    print("Server startup failed:", err)
    exit()

def send(listbox, entry):
    message = entry.get()
    if not message.strip():
        return
    try:
        client.send(message.encode("utf-8"))
        listbox.insert(tk.END, "Server: " + message)
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
            message = client.recv(1024)
            # If client disconnects
            if not message:
                listbox.insert(tk.END, "Client disconnected.")
                break
            decoded = message.decode("utf-8")
            listbox.insert(
                tk.END,
                "Client: " + decoded
            )

        except Exception as err:
            listbox.insert(
                tk.END,
                f"Receive error: {err}"
            )
            break

def on_closing():
    try:
        client.close()
        server_socket.close()
    except:
        pass
    root.destroy()

root = tk.Tk()
root.title("Server Chat")

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