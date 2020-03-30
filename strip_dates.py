import sys
import os
import re


if __name__ == "__main__":
    path = sys.argv[1]

    def process(path):
        with open(path, "r", encoding="utf-8") as h:
            data = h.read()

        data = re.sub("<title>\[\d{4}-\d{2}\] ", "<title> ", data)
        data = re.sub("<h1>\[\d{4}-\d{2}\] ", "<h1> ", data)

        with open(path, "w", encoding="utf-8") as h:
            h.write(data)

    for root, dirs, files in os.walk(path):
        for name in files:
            file_ = os.path.join(root, name)
            if file_.endswith(".html"):
                process(file_)
