Flask Setup

* Make dir projects
```
mkdir ~/projects
cd ~/projects
```
* git clone this repo
```
git clone git@github.com:abhi1kush/flask_setup.git
cd flask_setup
```

Installation
* Upgrade the package manager pip.
```
pip install --upgrade pip
```
* Create virtual environment
```
python3 -m venv ~/.virtualenvs/flask_setup_env
```
* Activate virtual environment
```
source ~/.virtualenvs/flask_setup_env/bin/activate
```
* Install requirements in the environment.
```
pip install -r requirements.txt
```
* Install pre-commit
```
pre-commit install
or 
sudo snap install pre-commit --classic
```
* To create an alias, add this to your ~/.bash_aliases
```
alias flask_setup="cd ~/projects/flask_setup; source ~/.virtualenvs/flask_setup_env/bin/activate"
```
* To runserver
```
python manage.py runserver
```
* Docker commands
```
sudo docker build -t flask_setup .
sudo docker run -p5005:80 -d -v /home/abhishek/projects/flask_setup:/flask_setup flask_setup
```
