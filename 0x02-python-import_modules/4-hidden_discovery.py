#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as hidden

    for str in dir(hidden):
        if not str.startswith("__"):
            print(str)
