class HeaderMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response      

    def __call__(self, request):
        request.META['HTTP_MY_HEADER'] = 'Hello'
        response = self.get_response(request)
        return response