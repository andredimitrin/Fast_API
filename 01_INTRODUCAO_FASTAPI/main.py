from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def index():
    html_content = """
    <html>    
        <head>
            <title>FastAPI</title>
        </head>  
        <body>
            <center>      
                <h1>FastAPI</h1>
                <p>FastAPI is a modern, high performance, open source web framework for building APIs with Python 3.6+.</p>
            </center>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
