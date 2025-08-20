import shutil
import random
import subprocess
import sys
import os
import time
import base64
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
width = shutil.get_terminal_size().columns
def auto_install(*packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f'>> Đang tải package còn thiếu: {package}')
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            __import__(package)

auto_install("requests", "rich")
from rich.console import Console
console = Console()
import requests
def format_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url + '/'
    return url
def linktot_bypass():
    randm = random.randint(100000, 999999)
    rad = str(randm)
    url = format_url(console.input('[bold bright_cyan]>> Nhập URL quest: [/bold bright_cyan]').strip())
    type = console.input('[bold bright_cyan]>> Nhập loại quest: (ví dụ backlink, normal, changecolor): [/bold bright_cyan]').strip()

    if type == 'normal':
        headers = {
            'origin': url,
            'referer': url,
            'rid': rad,
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15',
        }
        response = requests.options('https://linktot.net/ping.php', headers=headers)
    elif type == 'backlink':
        headers = {
            'origin': url,
            'referer': url,
            'rid': rad,
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15',
        }
        response = requests.options('https://linktot.net/ping_backlink.php', headers=headers)
    else:
        console.print("[bold red]>> Không thành công: Loại quest không hợp lệ[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    console.print("[bold yellow]>> Đang chờ xử lý...[/bold yellow]")
    if response.status_code != 200:
        console.print(f"[bold red]>> Không thành công: Mã trạng thái phản hồi {response.status_code}[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    time.sleep(80)

    gheaders = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/json',
        'origin': url,
        'priority': 'u=1, i',
        'ref': url,
        'referer': url,
        'rid': rad,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15',
    }
    gjson_data = {
        'href': url,
        'hostname': url,
    }

    gresponse = requests.post('https://linktot.net/get-code.php', headers=gheaders, json=gjson_data)
    if gresponse.status_code != 200:
        console.print(f"[bold red]>> Không thành công: Lấy mã thất bại, mã trạng thái {gresponse.status_code}[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    gjson = gresponse.json()
    enstring = gjson.get('code')
    if not enstring:
        console.print("[bold red]>> Không thành công: Không có mã trong phản hồi[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    K_Dilink = "1ThDrStTr"
    try:
        decoded_base64 = base64.b64decode(enstring).decode('utf-8')
    except Exception:
        console.print("[bold red]>> Không thành công: Giải mã base64 thất bại[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    decrypted_string = ""
    for i in range(len(decoded_base64)):
        decrypted_string += chr(ord(decoded_base64[i]) ^ ord(K_Dilink[i % len(K_Dilink)]))

    console.print(f"[bold green]>> Giải mã thành công:[/bold green] {decrypted_string}")
    input("Nhấn Enter để quay lại...")

def xlink_bypass():
    url = format_url(console.input('[bold bright_cyan]>> Nhập URL quest: [/bold bright_cyan]').strip())

    if 'vinhomesgreencity.org' in url:
        hurl = 'https://vinhomesgreencity.org/'
        code = 'wNpeq5Sror'
    elif 'thamtututhanglong.vn' in url:
        hurl = 'https://thamtututhanglong.vn/dich-vu-tham-tu-ha-noi/'
        code = 'Tz9l0jtEga'
    elif 'duhocbluesea.edu.vn' in url:
        hurl = 'https://duhocbluesea.edu.vn/'
        code = 'FO2h370lxh'
    elif 'viettinexpress.com' in url:
        hurl = 'https://viettinexpress.com/dich-vu/gui-hang-di-my/'
        code = 'QoFDwuMBx3'
    elif 'nhatthuc.com.vn' in url:
        hurl = 'https://www.nhatthuc.com.vn/'
        code = '8lBryd9IWJ'
    elif 'noithatbenthanh.vn' in url:
        hurl = 'https://noithatbenthanh.vn/'
        code = 'UlF13VHgwa'
    elif 'hunganhgroups.vn' in url:
        hurl = 'https://hunganhgroups.vn/'
        code = 'khuOkdGbVh'
    else:
        console.print("[bold red]>> Lỗi: URL không hợp lệ hoặc chưa hỗ trợ[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    fheaders = {
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': hurl,
        'priority': 'u=1, i',
        'referer': hurl,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    }
    fdata = {
        'code': code,
        'token': '',
    }

    try:
        fresponse = requests.post('https://xlink.co/step', headers=fheaders, data=fdata)
    except Exception as e:
        console.print(f"[bold red]>> Lỗi kết nối bước 1: {e}[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    if fresponse.status_code != 200:
        console.print(f"[bold red]>> Lỗi bước 1: Mã trạng thái {fresponse.status_code}[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    fjson = fresponse.json()
    token = fjson.get('token')
    if not token:
        console.print("[bold red]>> Lỗi: Không nhận được token ở bước 1, có thể là do bạn chưa nhận được nhiệm vụ Xlink chính xác hoặc chưa nhận nhiệm vụ từ Xlink[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    sheaders = {
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': hurl,
        'priority': 'u=1, i',
        'referer': hurl,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    }
    sdata = {
        'code': code,
        'token': token,
    }

    try:
        sresponse = requests.post('https://xlink.co/countdown', headers=sheaders, data=sdata)
    except Exception as e:
        console.print(f"[bold red]>> Lỗi kết nối bước 2: {e}[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    if sresponse.status_code != 200:
        console.print(f"[bold red]>> Lỗi bước 2: Mã trạng thái {sresponse.status_code}[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    sjson = sresponse.json()
    stime = sjson.get('timer')
    if stime is None:
        console.print("[bold red]>> Lỗi: Không nhận được thời gian đếm ngược[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    stime = int(stime) + 5
    console.print(f"[bold yellow]>> Vui lòng chờ {stime} giây...[/bold yellow]")
    time.sleep(stime)

    theaders = {
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': hurl,
        'referer': hurl,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    }
    tdata = {
        'code': code,
        'token': token,
    }

    try:
        tresponse = requests.post('https://xlink.co/continue', headers=theaders, data=tdata)
    except Exception as e:
        console.print(f"[bold red]>> Lỗi kết nối bước cuối: {e}[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    if tresponse.status_code != 200:
        console.print(f"[bold red]>> Lỗi bước cuối: Mã trạng thái {tresponse.status_code}[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    tjson = tresponse.json()
    fcode = tjson.get('code')
    if not fcode:
        console.print("[bold red]>> Lỗi: Không nhận được mã ở bước cuối[/bold red]")
        input("Nhấn Enter để quay lại...")
        return

    console.print(f"[bold green]>> Giải mã thành công: {fcode}[/bold green]")
    input("Nhấn Enter để quay lại...")
title = "Tool Bypass Link Rút Gọn"
credit = 'Made by withstock'
discord = 'Discord Server: https://discord.gg/HFakPJpQJ7'
choice = '[1] Bypass Xlink   [2] Bypass Linktot'
while True:
    clear_screen()
    console.print(title.center(width), style="#ff32b4")
    print('')
    console.print(credit.center(width), style="#FFF05A")
    console.print(discord.center(width), style="#5865F2")
    print('')
    console.print(choice.center(width), style="#16c58e")
    print('')
    choice_input = console.input("[bold bright_cyan]>> Nhập lựa chọn của bạn: [/bold bright_cyan]").strip()

    if choice_input == '1' or choice_input == 'xlink' or choice_input == 'Xlink':
        xlink_bypass()
    elif choice_input == '2' or choice_input == 'linktot' or choice_input == 'Linktot':
        linktot_bypass()
    else:
        console.print("[bold red]>> Lựa chọn không hợp lệ, vui lòng thử lại [/bold red]")
        sys.exit()
