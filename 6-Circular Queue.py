#Unnecessary step
import time
import sys

def enqueue(item):
    global queueLength, rear
    if queueLength < queueFull:
        if rear < len(myQueue) - 1:
            rear = rear + 1
        else:
            rear = 0
        queueLength = queueLength + 1
        myQueue[rear] = item
        
    else:
        print("⚠Queue is full⚠")

def dequeue():
    global queueLength, front, item
    if queueLength == 0:
        print("⚠Queue is empty⚠")
    else:
        myQueue[front] = item
        if front == len(myQueue) - 1:
            front = 0
        else:
            front = front + 1
    queueLength = queueLength - 1


queueFull = int(input("Input maximum size of the queue\n"))
myQueue = [None for i in range(queueFull)]
front = 0
rear = -1
queueLength = 0

print("================\nCurrent Queue\n"+str(myQueue)+"\n================\n")
while front <= queueFull:
    time.sleep(0.5)#Unnecessary step
    option = int(input("Choose an action to perform on the queue 1/2/3/4 :\n1. Enqueue(Add element)\n2. Dequeue(Remove an element)\n3. Peek(Display Queue)\n4. Exit\n"))

    if option == 1:
        item = int(input("Input the item to enqueue\n"))
        enqueue(item)
        time.sleep(1)#Unnecessary step
        print("================\nCurrent Queue\n"+str(myQueue)+"\n================\n")
    elif option == 2:
        item = None
        dequeue()
        time.sleep(1)#Unnecessary step
        print("================\nCurrent Queue\n"+str(myQueue)+"\n================\n")
    elif option == 3:
        time.sleep(1)#Unnecessary step
        print("================\nCurrent Queue\n"+str(myQueue)+"\n================\n")
    elif option == 4:
        sys.exit()
    else:
        print("Invalid Option, Please input 1, 2, 3 or 4\n")