from eve import Eve
app = Eve()
app.HATEOAS = False

if __name__ == '__main__':
    app.run()