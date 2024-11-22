# import time
# import os
# from flask import Flask, request, send_file, render_template_string
# import yt_dlp
#
# app = Flask(__name__)
#
#
# # Download video function using yt_dlp
# def download_best_quality(url, output_dir):
#     ydl_opts = {
#         'format': 'bestvideo+bestaudio[ext=m4a]/best',
#         'merge_output_format': 'mp4',
#         'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
#         'ffmpeg_location': r'C:\Users\ankit.mandloi\Downloads\ffmpeg-2024-11-18-git-970d57988d-full_build\ffmpeg-2024-11-18-git-970d57988d-full_build\bin',
#         'paths': {'temp': 'downloads/temp'}
#     }
#
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=True)
#         video_title = info.get('title', 'unknown_title')
#         video_file_path = os.path.join(output_dir, f"{video_title}.mp4")
#         return video_file_path
#
#
# # Serve the HTML page
# @app.route('/')
# def home():
#     html_content = """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Youtube Video Downloader</title>
#         <style>
#             body {
#                 font-family: Arial, sans-serif;
#                 display: flex;
#                 justify-content: center;
#                 align-items: center;
#                 height: 100vh;
#                 margin: 0;
#                 background-color: #f5f5f5;
#             }
#             .container {
#                 text-align: center;
#                 background: #ffffff;
#                 padding: 30px;
#                 border-radius: 8px;
#                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#             }
#             input[type="text"] {
#                 width: 80%;
#                 padding: 10px;
#                 margin-right: 10px;
#                 margin-bottom: 10px;
#                 border: 1px solid #ddd;
#                 border-radius: 4px;
#                 font-size: 16px;
#             }
#             button {
#                 padding: 10px 15px;
#                 border: none;
#                 background-color: #4CAF50;
#                 color: white;
#                 font-size: 16px;
#                 border-radius: 4px;
#                 cursor: pointer;
#                 margin-top: 10px;
#             }
#             button:hover {
#                 background-color: #45a049;
#             }
#         </style>
#     </head>
#     <body>
#     <div class="container">
#         <h2>Youtube Video Downloader</h2>
#         <input type="text" id="urlInput" placeholder="Enter the video URL here" />
#         <button onclick="downloadFile()">Download</button>
#     </div>
#     <script>
#         function downloadFile() {
#             const urlInput = document.getElementById('urlInput').value.trim();
#             if (urlInput) {
#                 const apiUrl = `http://127.0.0.1:8090/download?url=${encodeURIComponent(urlInput)}`;
#                 window.location.href = apiUrl; // Redirects to the API
#             } else {
#                 alert('Please enter a valid URL!');
#             }
#         }
#     </script>
#     </body>
#     </html>
#     """
#     return render_template_string(html_content)
#
#
#
# @app.route('/download', methods=['GET'])
# def download_video():
#     video_url = request.args.get('url')
#     if not video_url:
#         return "Missing 'url' parameter", 400
#
#     try:
#         # Ensure the downloads directory exists
#         output_dir = os.path.abspath('downloads')  # Use absolute path to ensure correct reference
#         os.makedirs(output_dir, exist_ok=True)
#
#         # Download the video and get the correct file path
#         video_file_path = download_best_quality(video_url, output_dir)
#
#         # Debugging: Check if the file exists and if it's accessible
#         if os.path.exists(video_file_path):
#             print(f"File {video_file_path} exists and is ready to be served.")
#
#         # Wait until the file is no longer in use (retry a few times)
#         max_retries = 10
#         retry_delay = 1  # Start with a 1-second delay, can be increased for further retries
#         for _ in range(max_retries):
#             try:
#                 # Check if the file exists and if it's accessible
#                 if os.path.exists(video_file_path):
#                     print(f"File {video_file_path} is accessible.")
#                     # After download is complete, return the video file
#                     filename = os.path.basename(video_file_path)
#                     response = send_file(video_file_path, as_attachment=True, download_name=filename)
#                     #os.remove(video_file_path)  # Cleanup the file after serving it
#                     return response
#                 else:
#                     print(f"File {video_file_path} does not exist, retrying...")
#             except PermissionError:
#                 # If the file is still being used, retry after a short delay
#                 print(f"PermissionError: The file is still being used, retrying after {retry_delay} seconds...")
#                 time.sleep(retry_delay)
#                 retry_delay += 1  # Increase delay between retries to give the download process more time
#
#         return f"Error: The downloaded file is still in use or not available at {video_file_path}", 500
#
#     except Exception as e:
#         return f"Error downloading video: {str(e)}", 500
#
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8090, threaded=True)







import time
import os
from flask import Flask, request, send_file, render_template_string
import yt_dlp

app = Flask(__name__)

# Download video function using yt_dlp
def download_best_quality(url, output_dir):
    ydl_opts = {
        'format': 'bestvideo+bestaudio[ext=m4a]/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'ffmpeg_location': r'C:\Users\ankit.mandloi\Downloads\ffmpeg-2024-11-18-git-970d57988d-full_build\ffmpeg-2024-11-18-git-970d57988d-full_build\bin',
        'paths': {'temp': 'downloads/temp'}
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_title = info.get('title', 'unknown_title')
        video_file_path = os.path.join(output_dir, f"{video_title}.mp4")
        return video_file_path


# Serve the HTML page
@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Youtube Video Downloader</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f5f5f5;
            }
            .container {
                text-align: center;
                background: #ffffff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            input[type="text"] {
                width: 80%;
                padding: 10px;
                margin-right: 10px;
                margin-bottom: 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 16px;
            }
            button {
                padding: 10px 15px;
                border: none;
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                border-radius: 4px;
                cursor: pointer;
                margin-top: 10px;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
    <div class="container">
        <h2>Youtube Video Downloader</h2>
        <input type="text" id="urlInput" placeholder="Enter the video URL here" />
        <button onclick="downloadFile()">Download</button>
    </div>
    <script>
        function downloadFile() {
            const urlInput = document.getElementById('urlInput').value.trim();
            if (urlInput) {
                const apiUrl = `https://127.0.0.1:8099/download?url=${encodeURIComponent(urlInput)}`;  // Use HTTPS
                window.location.href = apiUrl; // Redirects to the API
            } else {
                alert('Please enter a valid URL!');
            }
        }
    </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/download', methods=['GET'])
def download_video():
    video_url = request.args.get('url')
    if not video_url:
        return "Missing 'url' parameter", 400

    try:
        # Ensure the downloads directory exists
        output_dir = os.path.abspath('downloads')  # Use absolute path to ensure correct reference
        os.makedirs(output_dir, exist_ok=True)

        # Download the video and get the correct file path
        video_file_path = download_best_quality(video_url, output_dir)

        # Debugging: Check if the file exists and if it's accessible
        if os.path.exists(video_file_path):
            print(f"File {video_file_path} exists and is ready to be served.")

        # Wait until the file is no longer in use (retry a few times)
        max_retries = 10
        retry_delay = 1  # Start with a 1-second delay, can be increased for further retries
        for _ in range(max_retries):
            try:
                # Check if the file exists and if it's accessible
                if os.path.exists(video_file_path):
                    print(f"File {video_file_path} is accessible.")
                    # After download is complete, return the video file
                    filename = os.path.basename(video_file_path)
                    response = send_file(video_file_path, as_attachment=True, download_name=filename)
                    return response
                else:
                    print(f"File {video_file_path} does not exist, retrying...")
            except PermissionError:
                # If the file is still being used, retry after a short delay
                print(f"PermissionError: The file is still being used, retrying after {retry_delay} seconds...")
                time.sleep(retry_delay)
                retry_delay += 1  # Increase delay between retries to give the download process more time

        return f"Error: The downloaded file is still in use or not available at {video_file_path}", 500

    except Exception as e:
        return f"Error downloading video: {str(e)}", 500


if __name__ == "__main__":
    # Specify the paths to your certificate and key files
    ssl_context = ('server.crt', 'server.key')  # Replace with your certificate and key paths
    app.run(host="0.0.0.0", port=8091, threaded=True, ssl_context=ssl_context)
