# i have created this file - ujjwal upadhyay....
from django.http import HttpResponse
from django.shortcuts import render


def index (request):

    return render(request,'index.html')
    # return HttpResponse ('''hello ujjwal
    # <a href = '/about/'>about</a>"
    # <a href = '/removepuck/'>removepuck</a>"
    # <a href = '/capfirst/'>capfirst</a>"
    # <a href = '/newlineremove/'>newlineremove</a>"
    # <a href = '/charcount/'>charcount</a>"
    # <a href = '/spaceremove/'>spaceremove</a>"
    # ''')
    
def analiyses (request):
    djtext = request.GET.get('text' , 'default')
    removepunc = request.GET.get('removepunc' , 'off')

    caps = request.GET.get('caps' , 'off')
    print (removepunc)
    if (removepunc == 'on'):
        a_text = " "
        punc = '''*{}:;!()-[]'"\,<>?@#^$%_~'''
        for char in djtext:
            if char not in punc:
                a_text += char
        params = {'purpose':'remove punchuation' , 'analised_text':a_text}
    
    elif (caps == 'on'):
        a_text = ""
        for char in djtext:
            a_text = a_text + char.upper()
        params = {'purpose':'CONVERT SENTENCES INTO UPPERCASE' , 'analised_text':a_text}

    else:
        return HttpResponse("error 404")


    return render(request , 'anlises.html' , params)
    # return HttpResponse ("")
    




# home work done ....
# def navigator(request):
#     return HttpResponse(
#         '''<a href = "www.youtube.com">youtube<br></a>
#         <a href = "www.google.com">google<br></a>
#         <a href = "www.linkdin.com">linkdin<br></a>
#         <a href = "www.instagram.com">instagram<br></a>
#         <a href = "www.facebook.com">facebook<br></a>'''
#     )


# def removepuck (request):
#     djtext = request.GET.get('text' , 'defalut')
#     print(djtext)
#     return HttpResponse ("<h1>removepuck</h1><a href = '/about/'>back</>")

# # def capfirst (request):
#     return HttpResponse ("<h1>capfirst</h1><a href = '/removepuck/'>back</>")

# def newlineremove (request):
#     return HttpResponse ("<h1>newlineremove</h1><a href = '/capfirst/'>back</>")

# def spaceremove (request):
#     return HttpResponse ("<h1>spaceremove</h1><a href = '/newlineremove/'>back</>")

# def charcount (request):
#     return HttpResponse ("<h1>charcoutn</h1><a href = '/spaceremove/'>back</>")
        