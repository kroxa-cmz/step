def application(environ, start_response):
	data = b"Hello, World!\n"
	start_response("200 OK", [
    ("Content-Type", "text/plain"),
    ("Content-Length", str(len(data)))
    ])
    resp = environ['QUERY_STRING'].split("&")
    resp = [item+"\r\n" for item in resp]
	return iter([resp])
