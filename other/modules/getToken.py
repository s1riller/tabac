import requests

url = "https://lbe.litebox.ru/api/v1/auth-token"

headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Cookie": "_ym_uid=1682300907290900215; _ym_d=1682300907; _ga=GA1.2.1494914864.1682300908; tmr_lvid=3baa7013a9f7bff999c20c43f481b679; tmr_lvidTS=1682300908392; _fbp=fb.1.1682300909464.1758820943; csrftoken=aUCgsmE7yvPtFEPfyCklkxGItmSrX3k36OYFcUHbagYt2ExvFvWNU0cn6jm62f5w; sessionid=o5362u6izqr1xoz5l1seq8fyw0rlzkcv; _ga_7JL0LZZSRW=GS1.2.1691231033.9.0.1691231033.60.0.0; refresh_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MTM3NzcxOSwiaWF0IjoxNjkxMjkxMzE5LCJqdGkiOiIxNjU0NzYxZjIzNGY0OWQ0OWE1NmU1ZWNlZGM5ZmUxOCIsInVzZXJfaWQiOjYyODE0OSwib3duZXJfaWQiOjYyODIyOSwic2FfdWlkIjo2MjgyMjksInJvbGUiOiJcdTA0MTRcdTA0MzhcdTA0M2JcdTA0MzVcdTA0NDAiLCJtc2lzZG4iOiI3OTE0OTEzMDIwNCJ9.Iz66Bsr1-blM02YuF63HmopCJlPiSqc9HeWOd5d0EFTmkmZLrpaToM-j5kyTERJYzY_Dy03Fn7RtPBqmy6n9unC2r-Y98sFphaMrFcUE0W3nuvgt2jbhTgn_pVBVG2oP-o2UJDwCtaK1pQecRGgGtw1fNHlz2reveopv27azdcmg_wgyUdQDUiXTsKjuEZDn8dpTZiS45OgVSQeqX6QqLBSmqtppXZVXBN4YzhemDMSwuQAsI0ERpsg5_sS3COSeuOK1zN8cFCLr-FZkYsq7o_7WSdAY2sVnWzrzmsDchlAm71ZI6diqKaFXl8g2YD46jzc6rXVtucgetsySm0cIoS3VFexUh4FIVoIuBzJm5ah93OZuZYgJifclgK536uxmWX7rMzxIrC5S5d98ivvgsoNMBBy_G_sWa7AIlRqg8MuLXmC_aJ-mt82Dk-zJRATeZT4er1iFb4myHRg9tmbYIgOkd4s1gy7xo_Ogh52gg-japd-MttPIA9XiqW-VYM3wtRiIC4b0lZlb9JDDLDVZ1bb1GhqhMm_vqHsNar_w4hRncB-N8ozgz57Yqh1i85HKmSEJEyAauLnUzL3NAWz1BUWJdwPQyWxsM0ee6Y8wPZFx9WDmsQ0jVwueKfM5bZzLgJInHqEoGvTiKKGhnH5s70HXGUYjGs8bFUrvbx5fnh4",
    "DNT": "1",
    "EMAIL": "tabacorda@gmail.com",
    "Host": "lbe.litebox.ru",
    "PASSWORD": "Swat2002",
    "Referer": "https://lbe.litebox.ru/api/swagger/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    auth_token = response.json().get("token")
    print("Полученный токен доступа:", auth_token)

    # Запись токена в файл
    with open("modules/token.txt", "w") as file:
        file.write(auth_token)

    print("Токен записан в файл token.txt")
else:
    print("Ошибка при выполнении запроса:", response.status_code)