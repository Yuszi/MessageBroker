import uvicorn

"""
    Benutzung von Uvicorn als Webserver Implementation für Python.
    Wird hier dazu verwendet, damit der Client benutzerfreundlich seine Nachricht versenden kann.
"""
if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.23.1", port=4200, log_level="info")