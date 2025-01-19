from flask import Flask, render_template
from modules.files_handler import get_videos

app = Flask(__name__, static_folder="static", static_url_path="/")

@app.route("/")
def home():
    available_videos = get_videos("./static/videos")
    return render_template("index.html", available_videos=available_videos)

@app.route("/video/<video_id>")
def video_player(video_id):
    return render_template("video_player.html", video=video_id)



if __name__ == "__main__":
    app.run(debug=True)