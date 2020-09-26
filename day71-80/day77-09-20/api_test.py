from flask import Flask
from flask_restful import Resource, Api
import pymysql
import json

app = Flask(__name__)
api = Api(app)


class HelloPython(Resource):
    def get(self):
        return {'info': 'hello python'}


def get_connection():
    connection = pymysql.connect(host='39.97.253.19', port=3306, db='user_center', user='root', password='xxqroot')
    return connection


@app.route('/user/<u_id>', methods=['GET'])
def get_user_by_id(u_id):
    conn = get_connection()
    sql = 'SELECT u_name, class_name FROM t_user WHERE id =' + u_id
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    user_dto = {
        'uName': result[0],
        'className': result[1]
    }
    return json.dumps(user_dto, ensure_ascii=False)


# api.add_resource(HelloPython, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
    # print(get_user_by_id('3'))
