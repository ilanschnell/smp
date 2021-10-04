NOT_FOUND = 404


def http_resp(status):
    match status:
        case 200:
            print("OK")
        case 400:
            print("Bad request")
        case NOT_FOUND:
            print("Not found: %r" % NOT_FOUND)


http_resp(200)
http_resp(403)
