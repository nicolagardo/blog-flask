from flask import Blueprint, request, jsonify


#db
from db import get_connection_mysql


blog = Blueprint('blog', __name__, url_prefix='/blog')


@blog.post('/new')
def new_blog():
    name = request.json('blog')
    text = request.json('text')

    return jsonify()

query = 'SELECT * FROM post'
@blog.get('/all')
def get_blogs():

    conexion = get_connection_mysql()
    # posts = None
    with conexion.cursor() as cursor:
        cursor.execute(query)

        posts = cursor.fetchall()
    conexion.close()
    return jsonify(posts) 

    
    



# def to_json(self):
#     json_post = {
#         'post_id': self.id
#     }
