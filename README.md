Flask Setup

* Make dir projects
```
mkdir ~/projects
cd ~/projects
```
* git clone this repo
```
git clone git@github.com:abhi1kush/web_development_python.git
cd web_development_python
```

Installation
* Upgrade the package manager pip.
```
pip install --upgrade pip
```
* Create virtual environment
```
python3 -m venv ~/.virtualenvs/web_development_python
```
* Activate virtual environment
```
source ~/.virtualenvs/web_development_python/bin/activate
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
alias flask_setup="cd ~/projects/web_development_python; source ~/.virtualenvs/web_development_python/bin/activate"
```
* To runserver
```
python manage.py runserver
```
* Docker commands
```
sudo docker build -t web_development_python .
sudo docker run -p5005:80 -d -v /home/abhishek/projects/web_development_python:/web_development_python web_development_python
```
