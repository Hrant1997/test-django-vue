# test-django-vue

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Hrant1997/test-django-vue.git
$ cd test-django-vue
```

Back end installation

```sh
$ cd back-end/test_app
$ sudo pip install -r requirements.txt
$ python3 ./manage.py migrate
$ python3 ./manage.py runserver
```

Front end installation

```sh
$ cd front-end
$ npm install
$ npm run serve
```

And navigate to `http://127.0.0.1:8080/`.
