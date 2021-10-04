def http_resp(status):
    match status:
        case 200:
            print("OK")
        case 400:
            print("Bad request")
        case 404:
            print("Not found")
        case unknown:
            print("Unknown request: %r" % unknown)


http_resp(404)
http_resp(403)
