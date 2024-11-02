import random
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.transtions = defaultdict(list)

    def add_sentence(self, sentence):
        words = sentence.split()
        for i in range(len(words) - 1):
            self.transitions[words[i]].append(words[i + 1])

    def generate_sentence(self, start_word, max_length=10):
        current_word = start_word
        output = [current_word]

        for _ in range(max_length - 1):
            next_words = self.transitions.get(current_word)
            if not next_words:
                break
            current_word = random.choice(next_words)
            output.append(current_word)

        return ' '.join(output)

# Example usage
if __name__ == "__main__":
    # Create a Markov chain instance
    markov_chain = MarkovChain()

    # Add some sentences to the Markov chain
    sentences = [
        "the cat sat on the mat",
        "the dog sat on the log",
        "the cat chased the dog",
        "the dog barked at the cat",
        "the mat was on the floor",
        "the chair was on the table"
    ]

    for sentence in sentences:
        markov_chain.add_sentence(sentence)

    # Generate a sentence starting with "the"
    start_word = "the"
    generated_sentence = markov_chain.generate_sentence(start_word)
    print("Generated Sentence:", generated_sentence)
