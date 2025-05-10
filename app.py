from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

# CSSとJSのバンドル設定
css = Bundle(
    'css/style.css',
    filters='cssmin',
    output='gen/packed.css'
)

js = Bundle(
    'js/main.js',
    filters='jsmin',
    output='gen/packed.js'
)

assets.register('css_all', css)
assets.register('js_all', js)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 