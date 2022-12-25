from yandexfreetranslate import YandexFreeTranslate
yt = YandexFreeTranslate()
# yt = YandexFreeTranslate(api = "web")
# yt = YandexFreeTranslate(api = "ios")

# yt.set_proxy("socks5", "localhost", 9050, "username", "password")
def en2uz(input_string):
    output_string = yt.translate("en", "uz", input_string)
    return output_string

def uz2en(input_string):
    output_string = yt.translate("uz", "en", input_string)
    return output_string

