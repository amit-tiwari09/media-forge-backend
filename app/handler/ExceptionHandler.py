from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.exceptions.AppException import AppException
from app.schemas.response.ApiResponse import ApiResponse


async def appExceptionHandler(
    request: Request,
    exc: AppException,
):
    response = ApiResponse(
        success=False,
        message=exc.message,
        data=None,
        errors=exc.errors,
    )

    return JSONResponse(
        status_code=exc.statusCode,
        content=response.model_dump(),
    )


async def validationExceptionHandler(
    request: Request,
    exc: RequestValidationError,
):
    errors = {}

    for error in exc.errors():

        field = error["loc"][-1]

        errors.setdefault(field, []).append(error["msg"])

    response = ApiResponse(
        success=False,
        message="Validation failed",
        data=None,
        errors=errors,
    )

    return JSONResponse(
        status_code=422,
        content=response.model_dump(),
    )


async def unexpectedExceptionHandler(
    request: Request,
    exc: Exception,
):
    response = ApiResponse(
        success=False,
        message="Something went wrong",
        data=None,
        errors=None,
    )

    return JSONResponse(
        status_code=500,
        content=response.model_dump(),
    )
