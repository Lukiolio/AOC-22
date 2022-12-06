LEN_OF_BUFFER = 4
# Teil 1 & 2
with open("6.in") as file:
    signal = file.readline()
    buffer = list(signal[0:LEN_OF_BUFFER])
    if len(set(buffer)) == LEN_OF_BUFFER:
        print("Was unique from beginning!")
    else:
        position = LEN_OF_BUFFER
        for new_char in signal[LEN_OF_BUFFER:]:
            position += 1
            for i in range(0, LEN_OF_BUFFER - 1):
                buffer[i] = buffer[i+1]
            buffer[LEN_OF_BUFFER - 1] = new_char
            if len(set(buffer)) == LEN_OF_BUFFER:
                print(position)
                break