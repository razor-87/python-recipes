# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2020-01-15 11:40:42
# @Last Modified by:   razor87
# @Last Modified time: 2020-01-26 17:57:27


# Coroutines and Microthreading (tasklets, green threads, greenlets)
def foo():
    for n in range(5):
        print(f"I'm foo {n}")
        yield


def bar():
    for n in range(10):
        print(f"I'm bar {n}")
        yield


def spam():
    for n in range(7):
        print(f"I'm spam {n}")
        yield


# Create and populate a task queue
from collections import deque
taskqueue: deque = deque()
taskqueue.extend((foo(), bar(), spam()))  # Add some tasks (generators)
# Run all of the tasks
while taskqueue:
    # Get the next task
    task = taskqueue.pop()
    try:
        # Run it to the next yield and enqueue
        next(task)
        taskqueue.appendleft(task)
    except StopIteration:
        # Task is done
        pass

# -----------------------------------------------------------------------------

# Network Programming Basics
from socket import socket, AF_INET, SOCK_STREAM
# Time server program
import time
s = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket
s.bind(('', 8888))  # Bind to port 8888
s.listen(5)  # Listen, but allow no more than
# 5 pending connections.
while True:
    client, addr = s.accept()  # Get a connection
    print(f"Got a connection from {addr}")
    timestr = time.ctime(time.time()) + "\r\n"
    client.send(timestr.encode('ascii'))
    client.close()

# Time client program
s = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket
s.connect(('localhost', 8888))  # Connect to the server
tm = s.recv(1024)  # Receive no more than 1024 bytes
s.close()
print(f"The time is {tm.decode('ascii')}")

# -----------------------------------------------------------------------------

# Advanced Asynchronous I/O Example
import select
import types
import collections


# Object that represents a running task
class Task():
    def __init__(self, target):
        self.target = target  # A coroutine
        self.sendval = None  # Value to send when resuming
        self.stack = []  # Call stack

    def run(self):
        try:
            result = self.target.send(self.sendval)
            if isinstance(result, SystemCall):
                return result
            if isinstance(result, types.GeneratorType):
                self.stack.append(self.target)
                self.sendval = None
                self.target = result
            else:
                if not self.stack:
                    return
                self.sendval = result
                self.target = self.stack.pop()
        except StopIteration:
            if not self.stack:
                raise
            self.sendval = None
            self.target = self.stack.pop()


# Object that represents a "system call"
class SystemCall():
    def handle(self, sched, task):
        pass


# Scheduler object
class Scheduler():
    def __init__(self):
        self.task_queue = collections.deque()
        self.read_waiting = {}
        self.write_waiting = {}
        self.numtasks = 0

    # Create a new task out of a coroutine
    def new(self, target):
        newtask = Task(target)
        self.schedule(newtask)
        self.numtasks += 1

    # Put a task on the task queue
    def schedule(self, task):
        self.task_queue.append(task)

    # Have a task wait for data on a file descriptor
    def readwait(self, task, fd):
        self.read_waiting[fd] = task

    # Have a task wait for writing on a file descriptor
    def writewait(self, task, fd):
        self.write_waiting[fd] = task


# Main scheduler loop
def mainloop(self, count=-1, timeout=None):
    while self.numtasks:
        # Check for I/O events to handle
        if self.read_waiting or self.write_waiting:
            wait = 0 if self.task_queue else timeout
            r, w, e = select.select(self.read_waiting, self.write_waiting, [],
                                    wait)
            for fileno in r:
                self.schedule(self.read_waiting.pop(fileno))
            for fileno in w:
                self.schedule(self.write_waiting.pop(fileno))
        # Run all of the tasks on the queue that are ready to run
        while self.task_queue:
            task = self.task_queue.popleft()
            try:
                result = task.run()
                if isinstance(result, SystemCall):
                    result.handle(self, task)
                else:
                    self.schedule(task)
            except StopIteration:
                self.numtasks -= 1
        # If no tasks can run, we decide if we wait or return
        else:
            if count > 0:
                count -= 1
            if count == 0:
                return


# Implementation of different system calls
class ReadWait(SystemCall):
    def __init__(self, f):
        self.f = f

    def handle(self, sched, task):
        fileno = self.f.fileno()
        sched.readwait(task, fileno)


class WriteWait(SystemCall):
    def __init__(self, f):
        self.f = f

    def handle(self, sched, task):
        fileno = self.f.fileno()
        sched.writewait(task, fileno)


class NewTask(SystemCall):
    def __init__(self, target):
        self.target = target

    def handle(self, sched, task):
        sched.new(self.target)
        sched.schedule(task)


class CoSocket():
    def __init__(self, sock):
        self.sock = sock

    def close(self):
        yield self.sock.close()

    def bind(self, addr):
        yield self.sock.bind(addr)

    def listen(self, backlog):
        yield self.sock.listen(backlog)

    def connect(self, addr):
        yield WriteWait(self.sock)
        yield self.sock.connect(addr)

    def accept(self):
        yield ReadWait(self.sock)
        conn, addr = self.sock.accept()
        yield CoSocket(conn), addr

    def send(self, bytes_):
        while bytes_:
            evt = yield WriteWait(self.sock)
            nsent = self.sock.send(bytes_)
            bytes_ = bytes_[nsent:]

    def recv(self, maxsize):
        yield ReadWait(self.sock)
        yield self.sock.recv(maxsize)


def drink_beer():
    remaining = 12.0
    while remaining > 0.0:
        remaining -= 0.1


bottles = 10000000


def drink_bottles():
    global bottles
    while bottles > 0:
        drink_beer()
        bottles -= 1
        scheduler.mainloop(count=1, timeout=0)  # Poll for connections


# An asynchronous server based on coroutines.
def server(port):
    s = CoSocket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    yield s.bind(('', port))
    yield s.listen(5)
    while True:
        client, addr = yield s.accept()
        yield client.send(("%d bottles\r\n" % bottles).encode('latin-1'))
        yield client.close()


scheduler = Scheduler()
scheduler.new(server(10000))
drink_bottles()
