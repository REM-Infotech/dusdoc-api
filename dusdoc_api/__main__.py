import uvicorn
from quart_cors import cors
from socketio import ASGIApp
from dusdoc_api.socket_dusdoc import sio
from dusdoc_api.app import app

if __name__ == "__main__":
    app = ASGIApp(sio, cors(app, allow_origin="*"))
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
