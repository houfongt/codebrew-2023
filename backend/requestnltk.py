from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import subprocess

class ExampleJSONHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        len = int(self.headers.get('Content-Length'))
        data = json.loads(self.rfile.read(len).decode('utf-8'))
        self.send_response(200)
        self.send_header(b'Content-type', b'text/plain')
        self.end_headers()
        f = open('input.json', 'w', encoding="utf-8")
        datapy=json.dumps(data, separators=(',', ':'))
        f.write(datapy)
        f.close()
       # subprocess.Popen(["bash",  "/home/codebrew/convert.sh"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        task=subprocess.call(["python3",  "nltkscript.py"],  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        g = open('array_output.json', 'r', encoding="utf-8")
        out=g.read()
        self.wfile.write(" {} ".format(out).encode('utf-8'))
        task=subprocess.call(["nohup /home/codebrew/kill.sh &"], shell=True)
server = HTTPServer(('0.0.0.0', 81), ExampleJSONHandler)
server.serve_forever()

