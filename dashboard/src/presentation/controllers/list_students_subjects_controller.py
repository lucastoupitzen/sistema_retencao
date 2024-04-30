from typing import Dict
from ....src.presentation.http_types.http_request import HttpRequest
from ....src.presentation.http_types.http_response import HttpResponse
from ....src.presentation.interfaces.controller_interface import ControllerInterface
from ....src.domain.use_cases.list_students_subjects import ListStudentsSubjectsInterface


class ListStudentsSubjectsController(ControllerInterface):

    def __init__(self, use_case: ListStudentsSubjectsInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        response : Dict = self.__use_case.list_students_most_subjects_to_do()

        return HttpResponse (
            status_code= 200,
            body= {
                "data": response
            }
        )
    