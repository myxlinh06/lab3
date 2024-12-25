from django.utils.deprecation import MiddlewareMixin

class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Xử lý yêu cầu trước khi vào view
        pass

    def process_response(self, request, response):
        # Xử lý phản hồi trước khi trả về cho người dùng
        return response
