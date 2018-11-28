from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import LoginForm, IPForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = LoginForm()
	if form.validate_on_submit():
		session['username'] = form.username.data
		return redirect(url_for('home'))
	return render_template('login.html', form=form)

@app.route('/home')
def home():
	user = session.get('username')
	return render_template('home.html', user=user)

@app.route('/ssh', methods=['GET', 'POST'])
def ssh():
	form = IPForm()
	if form.validate_on_submit():
		with open("/home/rahadian/AutoJoRa/app/hosts","w") as fo:
			fo.write('{}{}\n{}{}{}{}\n'.format("[ios]\n", form.ip1.data, "\n", "[junos]\n", form.ip2.data, "\n"))
		with open("/home/rahadian/AutoJoRa/app/hosts","a") as fo:
			fo.write('{}{}{}\n{}{}\n{}{}\n'.format("[ios:vars]\n","ansible_user=", form.user1.data, "ansible_ssh_pass=", form.pw1.data, "dev_os=ios","\n"))
		with open("/home/rahadian/AutoJoRa/app/hosts","a") as fo:
			fo.write('{}{}{}\n{}{}\n{}'.format("[junos:vars]\n","ansible_user=", form.user2.data, "ansible_ssh_pass=", form.pw2.data, "dev_os=junos"))
			flash('Berhasil memasukkan IP Address target!')
		return redirect(url_for('config'))
	return render_template('hosts.html', form=form)

@app.route('/config')
def config():
	return render_template('config.html')