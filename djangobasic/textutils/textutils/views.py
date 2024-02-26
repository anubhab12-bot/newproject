from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyzingTexts(request):
    textareaWords = request.POST.get('text', 'default')
    removePunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    newlineremover =  request.POST.get('newlineremover', 'off')
    if (removePunc == 'on'):
        textAnalyzed = ''
        punctuationList = '''~@!$%^&*:"?()'{}[]|\></*-+`,_-.=;'''
        if not textareaWords:
            print("true")
            return HttpResponse("please enter your text here")
        for chars in textareaWords:
            if chars not in punctuationList:
                textAnalyzed = textAnalyzed + chars
            print(textAnalyzed)      
        params = {'purpose' : 'Remove punctuations', 'textAnalyzed' : textAnalyzed}
        textareaWords = textAnalyzed # update the textAreaword with textanalyzed
        # return render(request, 'analyzedText.html', params)
    
    if (fullcaps == 'on'):
        textAnalyzed = ''
        if not textareaWords:
            return HttpResponse("Please enter your text here")
        textareaWords = textareaWords[0].upper() + textareaWords[1:].lower()
        textAnalyzed = textAnalyzed + textareaWords
        params = {'purpose': 'Capitalized First one', 'textAnalyzed': textAnalyzed}
        textareaWords = textAnalyzed        
        # return render(request, 'analyzedText.html', params)
    
    if (extraspaceremover == 'on'):
        textAnalyzed = ''
        if not textareaWords:
            return HttpResponse("Please enter your text here")
        for index, chars in enumerate(textareaWords):
            if not (textareaWords[index] == " " and textareaWords[index+1] == " "):
                textAnalyzed = textAnalyzed + ''.join(chars)
        params = {'purpose': 'Extra space remover', 'textAnalyzed': textAnalyzed}
        textareaWords = textAnalyzed
    
    if (newlineremover == 'on'):
        textAnalyzed = ''
        if not textareaWords:
            return HttpResponse("Please enter your text here")
        for chars in textareaWords:
            if chars != '\n'and chars!="\r":
               textAnalyzed = textAnalyzed + chars 
        params = {'purpose': 'New Line remover', 'textAnalyzed': textAnalyzed}
        textareaWords = textAnalyzed
    return render(request, 'analyzedText.html', params)
    

# def capitalizeFirstLetter(request):
#     return HttpResponse("space remover")

# def spaceRemover(request):
#     return HttpResponse("space remover")

# def newLineRemover(Request):
#     return HttpResponse("new line remover")

# def charecterCount(request):
#     return HttpResponse("charecter counts")