class Solution:
    def sortSentence(self, s: str) -> str:
        sent = []
        s=s.split()
        for i in s:
            the_word = i[:-1]
            #print(the_word)
            num = int(i[-1:])
            sent.append((the_word, num))
            #print(sent)

        sent.sort(key=lambda x: x[1])
        print(sent)
        sorted_words = []
        for the_word,nums in sent:
             sorted_words.append(the_word)

        return " ".join(sorted_words)
                
        
               
