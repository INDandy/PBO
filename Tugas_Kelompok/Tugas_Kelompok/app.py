from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

def calculate_download_time(file_size, download_speed, unit):
    # Konversi ukuran file ke megabyte (1 GB = 1024 MB)
    file_size_mb = file_size * 1024

    # Konversi kecepatan download ke megabyte per detik jika satuan dalam MB/s
    if unit == 'MB':
        download_speed_mb = download_speed
    elif unit == 'KB':
        download_speed_mb = download_speed / 1024
    elif unit == 'GB':
        download_speed_mb = download_speed * 1024
    elif unit == 'TB':
        download_speed_mb = download_speed * 1024 * 1024

    # Hitung waktu download (dalam detik)
    download_time_seconds = file_size_mb / download_speed_mb

    # Konversi waktu ke jam, menit, dan detik
    download_time_hours = int(download_time_seconds // 3600)
    download_time_minutes = int((download_time_seconds % 3600) // 60)
    download_time_seconds = int(download_time_seconds % 60)

    return download_time_hours, download_time_minutes, download_time_seconds

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_size = float(request.form['file_size'])
        download_speed = float(request.form['download_speed'])
        unit = request.form['unit']

        download_time_hours, download_time_minutes, download_time_seconds = calculate_download_time(file_size, download_speed, unit)

        return render_template('index.html', file_size=file_size, download_speed=download_speed,
                               unit=unit, hours=download_time_hours, minutes=download_time_minutes, seconds=download_time_seconds)

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
