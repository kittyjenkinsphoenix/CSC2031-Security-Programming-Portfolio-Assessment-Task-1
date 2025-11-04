from app import create_app

# Instance
app = create_app()

# Run The Application
if __name__ == '__main__':
    app.run(debug=True)
