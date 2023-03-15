#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, string):
        if (type(string) == str):
            self._value = string
        else:
            print('The value must be a string.')

    value = property(get_value, set_value)

    def is_sentence(self):
        return self._value.endswith(".")

    def is_exclamation(self):
        return self._value.endswith("!")

    def is_question(self):
        return self._value.endswith("?")

    def count_sentences(self):
        number = self.value
        for end in ['?', '!']:
            number = number.replace(end, '.')
        sentences = [sent for sent in number.split('.') if sent]

        return len(sentences)
