from flask import Flask, render_template, redirect, make_response, request, session, abort

from flask_login import LoginManager, login_user, login_required, logout_user, current_user


from data.news import News
from data.users import User
import datetime

from forms.news import NewsForm
from forms.user import RegisterForm, LoginForm
from flask_restful import reqparse, abort, Api, Resource

from data import db_session
from news_resources import NewsResource, NewsListResource

app = Flask(__name__)
api = Api(app)






# для списка объектов
api.add_resource(NewsListResource, '/api/v2/news')

# для одного объекта
api.add_resource(NewsResource, '/api/v2/news/<int:news_id>')

api.init_app(app)


def main():
    db_session.global_init("db/blogs.db")


    app.run(host="127.0.0.1", port=8080)









if __name__ == '__main__':
    main()