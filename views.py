__author__ = 'Yash'

from flask import Flask, request, render_template
import subprocess
import platform
from app import app

@app.route('/', methods=['GET','POST'])
def index():
    """[The default path that takes the IP address and tries to ping the provided IP address]
    
    Returns:
        [String] -- [The result of the pingcommand]
    """
    if 'ip' in request.form:
        try:
            ip = request.form.get('ip')
            param = '-c'
            if platform.system() == "Windows":
                param ='-n'
            return subprocess.check_output(
                'ping {0} 1 "{1}"'.format(param,ip),
                shell=True
            ).decode()
        except Exception as e:
            return str(e)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
