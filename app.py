from flask import Flask, render_template

app = Flask(__name__)

# 模擬一些部落格文章資料
posts = [
    {
        'id': 1,
        'title': '我的第一篇部落格文章',
        'author': '小明',
        'content': '這是我的第一篇文章，來分享一些 Python Flask 的基本知識！'
    },
    {
        'id': 2,
        'title': 'Flask 與模板引擎',
        'author': '小華',
        'content': 'Flask 使用 Jinja2 作為模板引擎，可以讓你很輕鬆地在前端呈現資料。'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    # 根據 post_id 查找文章
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return "文章未找到", 404
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
