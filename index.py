from flask import render_template
from app import app

@app.route('/')
def index():
    import subproces
    cmd = subprocess.Popen(['ps_mem'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = cmd.communicate()
    memory = out.splitlines()
    return render_template('index.html', memory=memory)

