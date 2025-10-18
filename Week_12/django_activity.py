from django.http import HttpResponse
 
def welcome(request, name):
    """
    A simple Django view that takes a name from the URL
    and returns a personalized welcome message.
    """
    return HttpResponse(f"<h1>Welcome {name} to Django!</h1>")

if __name__ == "__main__":
    print("This module is intended to be used as a Django view and cannot be run standalone.")