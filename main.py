
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from supabase_client import supabase

app = FastAPI(
    title="Auth Login & Protect API",
    description="Secure authentication API using FastAPI and Supabase",
    version="1.0.0"
)

# JWT Bearer authentication
security = HTTPBearer(auto_error=False)


# Request model for signup and login
class AuthRequest(BaseModel):
    email: str | None = None
    password: str | None = None

class RefreshRequest(BaseModel):
    refresh_token: str


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Auth Login & Protect API",
        "status": "running"
    }


# Health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "supabase": "initialized"
    }


# Stage 1: User Signup
@app.post("/auth/signup", status_code=status.HTTP_201_CREATED)
def signup(data: AuthRequest):

    if not data.email or not data.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required"
        )

    try:
        response = supabase.auth.sign_up({
            "email": data.email,
            "password": data.password
        })

        user = response.user

        if user is None:
            raise HTTPException(
                status_code=400,
                detail="User registration failed"
            )

        return {
            "message": "User registered successfully",
            "user": {
                "id": user.id,
                "email": user.email,
                "created_at": user.created_at
            }
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# Stage 1: User Login
@app.post("/auth/login", status_code=status.HTTP_200_OK)
def login(data: AuthRequest):

    if not data.email or not data.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required"
        )

    try:
        response = supabase.auth.sign_in_with_password({
            "email": data.email,
            "password": data.password
        })

        session = response.session

        if session is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid login credentials"
            )

        return {
            "message": "Login successful",
            "access_token": session.access_token,
            "refresh_token": session.refresh_token,
            "token_type": "bearer",
            "user": {
                "id": response.user.id,
                "email": response.user.email
            }
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid login credentials"
        )


# Stage 2: Verify JWT access token
def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(security)
):

    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Authentication token is required",
            headers={"WWW-Authenticate": "Bearer"}
        )

    try:
        token = credentials.credentials

        response = supabase.auth.get_user(token)

        user = response.user

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired token"
            )

        return user

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"}
        )


# Stage 2: Public endpoint
@app.get("/public/info")
def public_info():

    return {
        "message": "This is a public endpoint",
        "access": "Anyone can access this endpoint"
    }


# Stage 2: Protected Profile
@app.get("/protected/profile")
def protected_profile(
    current_user=Depends(get_current_user)
):

    return {
        "message": "Protected profile accessed successfully",
        "user": {
            "id": current_user.id,
            "email": current_user.email
        }
    }


# Stage 2: Protected Dashboard
@app.get("/protected/dashboard")
def protected_dashboard(
    current_user=Depends(get_current_user)
):

    return {
        "message": "Welcome to your protected dashboard",
        "user_email": current_user.email,
        "authentication": "Verified"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

# Stage 3: Refresh Access Token
@app.post("/auth/refresh")
def refresh_token(data: RefreshRequest):

    try:
        response = supabase.auth.refresh_session(
            data.refresh_token
        )

        session = response.session

        if session is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired refresh token"
            )

        return {
            "message": "Token refreshed successfully",
            "access_token": session.access_token,
            "refresh_token": session.refresh_token,
            "token_type": "bearer"
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired refresh token"
        )