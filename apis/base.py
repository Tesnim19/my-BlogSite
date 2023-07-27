from fastapi import APIRouter
from apis.v1 import router_user, router_blog, authentication

api_router = APIRouter()

api_router.include_router(authentication.router, prefix="", tags=["Authentication"])
api_router.include_router(router_user.router, prefix="", tags=["Authors"])
api_router.include_router(router_blog.router, prefix="", tags=["Blogs"])