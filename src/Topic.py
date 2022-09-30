import json
import random

import os

class   Topic():
    topic_count = 0

    def __init__(self, filename = None):
        self.filename = filename
        self.good_answer = 0
        self.bad_answer = 0
        self.number_of_questions = 0
        self.load_configuration()
        Topic.topic_count += 1

    def load_configuration(self):
        with open("../topics/" + self.filename) as configuration_file:
            self.configuration = json.load(configuration_file)
            self.questions_answers = self.configuration["questions"]
            self.questions_pool = list(self.configuration["questions"])
            self.number_of_questions = len(self.questions_pool)
    
    def pick_questions(self):
            pick = random.choice(self.questions_pool)
            print(pick)
            user_answer = input(pick + "?")
            print(user_answer)
            if (user_answer != self.questions_answers[pick]):
                print("Wrong, Answer was:" + self.questions_answers[pick])
                self.bad_answer += 1
            else:
                print("Good")
                self.questions_pool.remove(pick)
                self.good_answer += 1
            self.score = 1 - len(self.questions_pool) / self.number_of_questions
            print(self.questions_answers[pick])
            print(self.questions_pool)

    def get_score(self):
        score = 1 - len(self.questions_pool) / self.number_of_questions
        return(score)
    def get_info(self):
        print("Filename: " + self.filename)
        print("Score: " + str(self.get_score() * 100) + "%")