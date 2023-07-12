import os

def Ammar_youtube_downloader():
    url = input('>> what is the url? ')
    res_ch = input("""
    >> choose resultion?
    1-144p
    2-240p
    3-360p
    4-480p
    5-720p
    6-1080p

    >> type the number of resultion from 1 to 6 >> 
    """)
    res_list = [
        144,
        240,
        360,
        480,
        720,
        1080
    ]

    while True:
        try:
            print(f'res_ch = {res_ch}')
            index = int(res_ch)
            if index > 0 and index <= 6:
                res = res_list[index - 1] 
                print(res)
                os.system(f"yt-dlp -f 'best[height={res}]' {url}")
                break
            else:
                print('please type number from 1 to 6')
        except Exception as e:
            print(f'please type number , {e}')

    print('finished downloading !!!!')

    

Ammar_youtube_downloader()