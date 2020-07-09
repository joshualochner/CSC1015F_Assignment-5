def to_pig_latin(sentence):
    spl = sentence.split(' ')
    for i in range(len(spl)):
        if(spl[i].lower()[0] in ['a','e','i','o','u']):
            spl[i]+='way'
        else:
            firstXConsanants = 0
            for x in spl[i]:
                if(x.lower() not in ['a','e','i','o','u']):
                    firstXConsanants+=1
                else:
                    break
            spl[i] = spl[i][firstXConsanants:]+'a' + spl[i][0:firstXConsanants] + 'ay'
    return ' '.join(spl)

def to_english(sentence):
    spl = sentence.split(' ')
    for i in range(len(spl)):
        if(spl[i][-3:]=='way'):
            spl[i] = spl[i][:-3]
        else:
            spl[i] = spl[i][0:-2]
            lastAIndex = spl[i].rfind('a')
            spl[i] = spl[i][lastAIndex+1:] + spl[i][0:lastAIndex]
    return ' '.join(spl)