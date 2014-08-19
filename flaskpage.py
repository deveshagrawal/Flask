import flask, flask.views

app =  flask.Flask(__name__)

class View (flask.views.MethodView):
	def get (self):
		return flask.render_template('index.html')

	def post(self):
		return str(flask.request.form['fullname'])
		

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.debug = True
app.run()