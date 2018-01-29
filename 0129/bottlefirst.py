from bottle import route, run


@route('/test')
def test():
    return "test site"

if __name__ == '__main__':
    run(host='127.0.0.1', port=8090, debug=True)
