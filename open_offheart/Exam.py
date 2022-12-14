from Topic import Topic
import os

class   Exam():
    def __init__(self) -> None:
        self.topics = []
        self.number_of_topics = 0
        self.load_configuration
        self.load_topics()
    def load_configuration(self):
        pass

    def load_topics(self):
        topics_repository = os.listdir("../topics")
        for topic_filename in topics_repository:
            self.topics.append(Topic(topic_filename))
        self.number_of_topics = Topic.topic_count
    
    def run(self):
        for topic in self.topics:
            while topic.get_score() < 1:
                topic.pick_questions()
            print("Congrats you finished: x" + topic.filename)
                