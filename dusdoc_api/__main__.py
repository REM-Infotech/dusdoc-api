import uvicorn
from socketio import ASGIApp
from dusdoc_api.socketio import sio
from dusdoc_api.app import app

if __name__ == "__main__":
    
    app = ASGIApp(sio, app)
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")