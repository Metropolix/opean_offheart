from importlib.util import LazyLoader
from Topic import Topic
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: Please Specify Topic configuration (main.py:ligne7) ")
        exit(-1)
    subject = Topic(sys.argv[1])
    subject.pick_questions()
    subject.pick_questions()
    subject.get_info()
