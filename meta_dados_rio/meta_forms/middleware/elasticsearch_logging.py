# -*- coding: utf-8 -*-
from datetime import datetime
from time import time
import traceback

from django.http import HttpRequest, HttpResponse

from meta_dados_rio.utils import index_document


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        start_time = time()
        log_document = {
            "request_method": request.method,
            "request_path": request.get_full_path(),
            "request_body": request.body.decode(),
            "request_headers": dict(request.headers),
            "request_time": datetime.now(),
            "response_body": None,
            "response_time": None,
            "response_status": None,
            "error_traceback": None,
        }
        response: HttpResponse = self.get_response(request)
        if response:
            log_document["response_body"] = response.content.decode()
            log_document["response_status"] = response.status_code
        log_document["response_time"] = time() - start_time
        index_document(log_document)
        return response

    def process_exception(self, request: HttpRequest, exception: BaseException):
        try:
            raise exception
        except Exception as e:
            log_document = {
                "request_method": request.method,
                "request_path": request.get_full_path(),
                "request_body": request.body,
                "request_headers": request.headers,
                "request_time": datetime.now(),
                "response_body": str(e),
                "response_time": None,
                "response_status": 500,
                "error_traceback": traceback.format_exc(),
            }
            index_document(log_document)
        return exception
