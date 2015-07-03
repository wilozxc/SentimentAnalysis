def sentimentAnalysis(phrase):
    state = 0
    sentiment = 0
    phrase = phrase.split()
    positiveWords = ['good','great','like','love','amazing','fabulo11us','extraordinary','awesome','liked','love','loved','fun']
    negativeWords = ['bad','horrible','not','no','hate','dont','didnt','wasent','worst']

    for i in range(len(phrase)):

        #check for positive
        for q in range (len(positiveWords)):
            if phrase[i] == positiveWords[q]:
                state+=1

            if ((phrase[i] == 'very') or (phrase[i] == 'really') ) and (phrase[i+1] == positiveWords[q]):
                state+=1

        #check for negative               
        for z in range (len(negativeWords)):
            if phrase[i] == negativeWords[z]: 
                state-=1

            if ((phrase[i] == 'very') or (phrase[i] == 'really') ) and (phrase[i+1] == negativeWords[z]):
                state-=1

        #sentiment positive
        for q in range (len(positiveWords)):
            if phrase[i] == positiveWords[q]:
                sentiment = 1 
                   
        
    print state
        

for i in range(5):
    phrase = raw_input('Give me a phrase')
    sentimentAnalysis(phrase)
