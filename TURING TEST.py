"""
Simple Turing Test Program
The judge asks questions to a human and a machine.
Based on the answers, the judge guesses who is the bot.
"""

import random


# ----------- BOT CLASS -----------

class Machine:

    replies = {
        "name": [
            "I am known as Robo-X.",
            "My identifier is Machine-21.",
            "You may call me CyberUnit."
        ],

        "how": [
            "I am operating normally.",
            "Performance level is optimal.",
            "All functions are working."
        ],

        "feel": [
            "Emotions are not part of my system.",
            "I analyze emotions but do not feel them.",
            "Feelings are human attributes."
        ],

        "today": [
            "I analyzed several datasets.",
            "I completed many processing tasks.",
            "I performed scheduled computations."
        ],

        "joke": [
            "Why do robots like numbers? Because they compute everything.",
            "Beep beep... that was a robotic laugh.",
            "Humor module activated."
        ]
    }

    def answer(self, question):
        q = question.lower()

        if "name" in q:
            return random.choice(self.replies["name"])
        elif "how" in q:
            return random.choice(self.replies["how"])
        elif "feel" in q:
            return random.choice(self.replies["feel"])
        elif "today" in q:
            return random.choice(self.replies["today"])
        elif "joke" in q:
            return random.choice(self.replies["joke"])
        else:
            return "I cannot generate a response."


# ----------- JUDGE CLASS -----------

class Evaluator:

    machine_keywords = [
        "system", "process", "compute", "robot",
        "analyze", "identifier", "module"
    ]

    def calculate_score(self, text):
        score = 0
        lower = text.lower()

        for word in self.machine_keywords:
            if word in lower:
                score += 15

        if len(text.split()) <= 3:
            score += 10

        return score

    def guess(self, text):
        s = self.calculate_score(text)

        if s >= 30:
            return "BOT", s
        else:
            return "HUMAN", s


# ----------- MAIN PROGRAM -----------

def start_test():

    questions = [
        "What is your name?",
        "How are you today?",
        "Do you feel emotions?",
        "What did you do today?",
        "Tell me a joke."
    ]

    human_answers = [
        "My name is Sam.",
        "I'm doing well, thanks for asking.",
        "Yes, I feel emotions like happiness and sadness.",
        "I attended classes and finished my assignments.",
        "Why did the computer go to school? To improve its memory!"
    ]

    bot = Machine()
    judge = Evaluator()

    print("\n--- TURING TEST DEMO ---\n")

    for i in range(len(questions)):

        q = questions[i]

        human = human_answers[i]
        bot_reply = bot.answer(q)

        human_guess, human_score = judge.guess(human)
        bot_guess, bot_score = judge.guess(bot_reply)

        print("Question:", q)

        print("Human Response:", human)
        print("Judge Decision:", human_guess, "| Suspicion:", human_score)

        print("Bot Response:", bot_reply)
        print("Judge Decision:", bot_guess, "| Suspicion:", bot_score)

        print("-----------------------------------")


if __name__ == "__main__":
    start_test()
