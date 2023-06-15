from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class CustomLocaleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            if request.user.is_authenticated:
                print(f"1: {request.LANGUAGE_CODE}")
                translation.activate(request.user.UserProfile.language)
                request.LANGUAGE_CODE = request.user.UserProfile.language
                print(f"2: {request.LANGUAGE_CODE}")
        except:
            request.LANGUAGE_CODE = "en"
            print("iamma here")