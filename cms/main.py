from flask import Flask, render_template, request
from cms.forms.publish import new_story

app = Flask(__name__, template_folder="templates")
app.secret_key = '7tioyugf£%&%£&hvj2dghcxgbn  !$$'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/publish", methods=["GET", "POST"])
def publish():
    form = new_story()
    if form.validate_on_submit():
        story_title = request.form.get('title')
        story_body = request.form.get('body')
        story_image = request.form.get('image')
        return render_template('new_story.html', story_title=story_title, story_body=story_body, story_image=story_image)
    return render_template("publish_story.html", form=form)


if __name__ == "__main__":
    app.run(port=9001, debug=True)
