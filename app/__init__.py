from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.exceptions import EntityNotFoundException
from app.routers import branch, student

app = FastAPI(
    title='Students API',
    description='Simple python students API',
    version='1.0.0',
    contact={
        'name': 'SuRu',
        'url': 'https://github.com/suru33/students-api-python',
        'email': '33urus@gmail.com'
    },
    license_info={
        'name': 'GNU General Public License v2.0',
        'url': 'https://github.com/suru33/students-api-python/blob/master/LICENSE'
    }
)

app.include_router(branch.router)
app.include_router(student.router)


@app.exception_handler(EntityNotFoundException)
async def entity_not_found_exception_handler(request: Request, ex: EntityNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "path": request.url.path,
            "message": f"{ex.name}: {ex.value} does not exist"
        },
    )
