import json
import time
import websocket
from typing import Callable
import QQdealer


class WebApp:
    def __init__(self, group_list=None, user_list=None, ip: str = "127.0.0.1", port: int = 8080,
                 callback: Callable[[str], None] = lambda x: print(x)):

        if user_list is None:
            user_list = [int]
        if group_list is None:
            group_list = [int]
        self.url = "ws://{}:{}/".format(ip, port)
        self.ws = websocket.WebSocketApp(
            url=self.url,
            on_message=self.when_message,
            on_open=self.when_open,
            on_close=self.when_close
        )
        self.group_list = group_list
        self.user_list = user_list
        self.callback = callback

    def deal_message(self, message):
        message = json.loads(message)
        res_message = None
        if message['post_type'] == 'message':
            if message['message_type'] == 'group':
                if message['group_id'] in self.group_list:
                    res_message = QQdealer.deal_message(message['message'])

        self.callback(res_message)

    def send(self, message: dict):
        if type(message) is not dict:
            raise TypeError
        self.ws.send(json.dumps(message))

    def when_message(self, ws, message):
        self.deal_message(message)

    def when_open(self, ws):
        print("opened")
        pass

    def when_close(self, ws):
        print("closed")
        pass

    def run(self):
        self.ws.run_forever()


if __name__ == "__main__":
    webapp = WebApp(ip="127.0.0.1", port=8080, group_list=[1067245310])
    webapp.run()
    time.sleep(10)
