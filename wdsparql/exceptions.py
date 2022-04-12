from requests.exceptions import HTTPError


class MalformedQueryException(HTTPError):
    """Wrapper form malformed queries"""

    def __init__(self, httperr: HTTPError):
        super().__init__(request=httperr.request, response=httperr.response)

    def __str__(self) -> str:
        if self.response.status_code == 400:
            return f"400 Bad Request: {self.response.text}"

        return super().__str__()
