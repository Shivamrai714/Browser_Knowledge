#  CODE BY Shivam Rai

from flask import Flask, render_template, request
import os

app = Flask(__name__)
browserLastVisitedURLS = dict()


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


############# START BROWSER ##############


@app.route('/start', methods=['GET'])
def start():
    if 'browser' in request.args and 'url' in request.args:
        browserName = str(request.args['browser'])
        url = str(request.args['url'])

        if browserName == 'chrome':
            command = "start chrome {}".format(url)
            os.system(command)
            browserLastVisitedURLS.update({browserName: url})
            return "Chrome fired up with specified url."

        elif browserName == 'firefox':
            command = "start firefox {}".format(url)
            os.system(command)
            browserLastVisitedURLS.update({browserName: url})
            return "Firefox fired up with specified url."

        else:
            return "This browser is not available"

    elif 'browser' in request.args:
        return "Please specify a url"

    elif 'url' in request.args:
        return "Please provide a browser name"


############### STOP BROWSER ####################


@app.route('/stop', methods=['GET'])
def stop():
    if 'browser' in request.args:
        browserName = str(request.args['browser'])
        if browserName == 'chrome':
            os.system("taskkill /f /im chrome.exe")
            return "Chrome closed"

        elif browserName == 'firefox':
            os.system("taskkill /f /im firefox.exe")
            return "Firefox closed"

        else:
            return "Browser not available."

    else:
        return "Browser not provided."


############# GETURL #################


@app.route('/geturl', methods=['GET'])
def geturl():
    if 'browser' in request.args:
        browserName = str(request.args['browser'])

        if browserName == 'chrome' or browserName == 'firefox':

            if browserName in browserLastVisitedURLS:
                return browserLastVisitedURLS[browserName]
            else:
                return "No url found"
        else:
            return "Browser not available."
    else:
        return "Browser not provided."


############ DELETE HISTORY ###############

@app.route('/cleanup', methods=['GET'])
def cleanup():
    if 'browser' in request.args:
        browserName = str(request.args['browser'])
        if browserName == 'chrome':
            # Clean up Chrome browsing session , but its dangerous so putting wrong path here
            chrome_data_dir = os.path.expandvars(r'C:\Users\ASUS\AppData\Roaming\Mozilla\Firefox\Profiles\f6de4m2w.default')
            os.system(f"del /F /Q {chrome_data_dir}\\History")
            os.system(f"del /F /Q {chrome_data_dir}\\Cookies")
            os.system(f"del /F /Q {chrome_data_dir}\\DownloadMetadata")
            os.system(f"del /F /Q {chrome_data_dir}\\Favicons")
            return "Chrome browser session information deleted"

        elif browserName == 'firefox':
            # Clean up Firefox browsing session         
            firefox_profile_dir = r'C:\Users\ASUS\AppData\Roaming\Mozilla\Firefox\Profiles\cory1763.default-release'
            os.system(f"del /F /Q {firefox_profile_dir}\\cookies.sqlite")
            os.system(f"del /F /Q {firefox_profile_dir}\\favicons.sqlite")
            os.system(f"del /F /Q {firefox_profile_dir}\\places.sqlite")
            os.system(f"del /F /Q {firefox_profile_dir}\\storage.sqlite")
            return "Firefox browser session information deleted"

        else:
            return "Browser not available"
    else:
        return "Browser not provided"












if __name__ == '__main__':
    app.run()
