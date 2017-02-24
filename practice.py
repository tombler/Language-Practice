import json 
import subprocess
import random
import sys
reload(sys)  
import code
sys.setdefaultencoding('utf8')


class Vocab():

    def __init__(self,dict='spanish_english.json'):
        self.dict=dict
        self.langs = ['spanish','english']
        json_data=open(self.dict).read()
        self.vocab = json.loads(json_data)
        
    def add(self,spanish,english):
        # adds a word to JSON & saves
        self.vocab[spanish] = english
        json_data = json.dumps(self.vocab, indent=4, ensure_ascii=False).encode('utf8')
        with open(self.dict,'w') as f:
            f.write(json_data)
            f.close()

    def choose_random(self,vocab):
        spanish, english = random.choice(list(vocab.items()))
        return {'spanish':spanish,'english':english}

    def show_random(self):
        test = self.choose_random(self.vocab)
        print test['spanish']
        print test['english']

    def speak(self):
        ques_lang = random.sample(self.langs, 1)[0]
        ans_lang = list(set(self.langs) - set([ques_lang]))[0]
        item = self.choose_random(self.vocab)

        print "Speaking..."
        if ques_lang == 'english':
            subprocess.call(['say','-v','alex',item[ques_lang]])
        elif ques_lang == 'spanish':
            subprocess.call(['say','-v','carlos',item[ques_lang]])
        else:
            print "Something went wrong with the text-to-speech engine!"
        return (ques_lang,ans_lang,item)

    def write(self):
        ques_lang = random.sample(self.langs, 1)[0]
        ans_lang = list(set(self.langs) - set([ques_lang]))[0]
        item = self.choose_random(self.vocab)
        return (ques_lang,ans_lang,item)

if __name__ == "__main__":
    initial_text = "Press enter to play, type 'add' to add a word or phrase, or press q to quit anytime.\n"
    continue_text = "Press Enter to continue, type 'add' to add a word or phrase, or press 'q' to quit anytime...\n"

    v = Vocab()
    actual_ans = raw_input(initial_text)
    while actual_ans != 'q':
        # allow user to add a definition to the JSON
        if actual_ans == 'add':
            spanish = raw_input("Spanish word or phrase: ")
            if spanish == 'q': break
            english = raw_input("English translation: ")
            if english == 'q': break
            if len(spanish) == 0 or len(english) == 0:
                print "Please enter a word in both languages!"
                continue
            else:
                v.add(spanish,english)
                print "Saved!"
            actual_ans = ''
            actual_ans = raw_input(continue_text)
            continue

        # choose a random question type and execute
        functions = ['speak','write']
        func = random.sample(functions, 1)[0]
        if func == 'speak':
            ques_lang,ans_lang,item = v.speak()
            actual_ans = raw_input("Translate to %s: \n" % ans_lang)
            expected_ans = item[ans_lang]
        elif func == 'write':
            ques_lang,ans_lang,item = v.write()
            actual_ans = raw_input('Translate the following to %s: \t"%s"\n' % (ans_lang,item[ques_lang]))
            expected_ans = item[ans_lang]
        else:
            print 'Not a valid function!'
            exit()
        # check answer
        if actual_ans == 'q': break
        if expected_ans.lower() == actual_ans.lower():
            actual_ans = raw_input("Nice! %s" % continue_text)
        else:
            actual_ans = raw_input("Sorry, that's not right. "
                                'Correct translation: "%s"\n%s'
                                % (expected_ans, continue_text))

    # catch-all
    print 'Thanks for playing!'
    exit()


