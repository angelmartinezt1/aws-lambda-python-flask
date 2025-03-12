from app import app
from mangum import Mangum

handler = Mangum(app)  # Adaptador para API Gateway en AWS Lambda
