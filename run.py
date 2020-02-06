from application import app

# Ei toimi??? Pitäisi:

# app.logger.addHandler(logging.StreamHandler(sys.stdout))
# app.logger.setLevel(logging.ERROR)

if __name__ == '__main__':
    app.run(debug=True)
