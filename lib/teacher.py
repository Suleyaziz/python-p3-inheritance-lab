#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "The Earth revolves around the Sun.",
            "Water boils at 100 degrees Celsius.",
            "The capital of France is Paris.",
            "Python is a programming language.",
            "The Great Wall of China is visible from space."
        ]

    def teach(self):
        return random.choice(self.knowledge)