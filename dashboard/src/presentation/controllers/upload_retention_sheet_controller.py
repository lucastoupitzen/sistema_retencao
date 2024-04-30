from typing import Dict
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse
from ..interfaces.controller_interface import ControllerInterface
from ...domain.use_cases.upload_retention_sheet import UploadRetentionSheetInterface


class UploadRetentionSheetController(ControllerInterface):

    def __init__(self, use_case: UploadRetentionSheetInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        year : int = int(http_request.query_params["year"])
        path : str = http_request.query_params["path"]

        response  = self.__use_case.upload_sheet(path = path, year = year)

        return HttpResponse (
            status_code= 200,
            body= {
                "data": response
            }
        )
    