# Assignment 13: Real-Time Socket Chat Application

## Overview

This project implements a simple **real-time client-server chat application** using Python sockets and the `tkinter` GUI library.

The application demonstrates how two systems can communicate over a TCP connection using socket programming. Both the server and client provide graphical chat windows where users can exchange messages instantly.

Unlike the earlier manual version, this implementation now supports:

- Real-time message receiving using threads
- Better error handling for socket operations
- Automatic disconnect detection
- Proper socket cleanup on exit
- Larger message buffer support

---

# Project Structure

```text
Assignment13/
│
├── server.py
├── client.py
└── README.md