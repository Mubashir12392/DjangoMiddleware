from django.shortcuts import HttpResponse
import logging


class MyMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        
        # code logic executed before the view

        response = HttpResponse('The site you are looking for, is not ready')
        
        # code logic executed after the view

        return response
    

# Another Custom Middleware

# This middleware will log the request URL when a request is received and 
# the response status code before it's returned to the client. 

logger = logging.getLogger(__name__)

class RequestResponseLoggerMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        
        logger.info(f'Request URL: {request.path}')

        response = self.get_response(request)

        logger.info(f'Response status code: {response.status_code}')


        return response