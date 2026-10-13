import random
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# 用來記錄每個連線 (sid) 對應的隨機顏色
user_colors = {}


def get_random_color():
    """隨機生成一個漂亮的 HSL 顏色，避免太淡或太深"""
    hue = random.randint(0, 360)
    # 使用 HSL 格式：飽和度 70%，亮度 45%，在網頁上看起來比較像有質感的標籤
    return f"hsl({hue}, 70%, 45%)"


@app.route('/')
def index():
    return render_template('index.html')


# 監聽客戶端連線
@socketio.on('connect')
def handle_connect():
    # 1. 為剛進來的這條連線生成一個專屬顏色並存起來
    user_colors[request.sid] = get_random_color()
    print(f"User connected! ID: {request.sid}, Color: {user_colors[request.sid]}")

    # 2. 一對一發送（只發給剛剛連線進來的這個人）
    # 我們打包成字典，順便把分配給他的顏色告訴他自己
    welcome_packet = {
        'msg': '【系統通知】歡迎來到專屬客服/個人通道！這是只有你才看得到的一對一訊息。',
        'your_color': user_colors[request.sid]
    }
    emit('one_on_one_response', welcome_packet)


# 監聽前端發送過來的自訂事件 'client_message'
@socketio.on('client_message')
def handle_message(data):
    # 找出是誰發的，並拿到他的專屬顏色
    my_color = user_colors.get(request.sid, '#000000')

    # 打包訊息與顏色
    message_packet = {
        'text': data,
        'user_id': request.sid[:6],  # 只取 ID 前六碼當作臨時暱稱
        'color': my_color
    }

    # 廣播給所有人（包含顏色資訊）
    emit('server_response', message_packet, broadcast=True)


# 監聽斷開連線
@socketio.on('disconnect')
def handle_disconnect():
    print(f"User disconnected: {request.sid}")
    # 玩家離開後，把記憶體中的顏色刪除，釋放資源
    if request.sid in user_colors:
        del user_colors[request.sid]


if __name__ == '__main__':
    socketio.run(app, debug=True, port=8080)