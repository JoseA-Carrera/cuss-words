from better_profanity import profanity

if __name__ == '__main__':
    text = input('enter the sentence: ')
    censored = profanity.censor(text)
    print(censored)
