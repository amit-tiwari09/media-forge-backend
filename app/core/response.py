from typing import Any

from app.schemas.response.ApiResponse import ApiResponse


def successResponse(
    message: str,
    data: Any = None,
) -> ApiResponse:

    return ApiResponse(
        success=True,
        message=message,
        data=data,
        errors=None,
    )
