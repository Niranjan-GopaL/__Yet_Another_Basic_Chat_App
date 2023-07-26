FILENAME = "./chat_area.txt"

while 1:
    msg = input()
    if msg == "exit":
        break
    with open(FILENAME,'a') as f:
        f.write(f"MSG --> {msg}\n")