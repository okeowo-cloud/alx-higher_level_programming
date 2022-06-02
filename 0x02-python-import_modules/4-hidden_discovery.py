#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lines = dir(hidden_4)
    for line in lines:
        if line[:2] != "__":
            print(line)
