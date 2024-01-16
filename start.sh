# Set variables
HOST=0.0.0.0
PORT=8000

# Start server
echo "Starting server..."
python -m uvicorn app.main:app --host $HOST --port $PORT
