import json 
from .models import Logger

class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):
        response = self.get_response(request) 
        request_ip = self.get_ip(request)
        print(request, 'request')
        try:
            request_data = request.POST.get('formula')
            response_body=response.content.decode('utf-8')
            response_body = json.loads(response_body).get('formula')
            request_log= Logger(request_ip=request_ip, request_data=request_data,
            is_valid = response_body)
            request_log.save()
        except:
            pass
        return response

    def get_ip(self, request):
        req_headers = request.META
        x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for_value:
            ip_addr = x_forwarded_for_value.split(',')[-1].strip()
        else:
            ip_addr = req_headers.get('REMOTE_ADDR')
        return ip_addr