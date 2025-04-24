class DomainRoutingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()

        if "xyz.com" in host:
            request.site_name = "xyz"
        elif "abcc.com" in host:
            request.site_name = "abcc"
        else:
            request.site_name = "default"

        response = self.get_response(request)
        return response
