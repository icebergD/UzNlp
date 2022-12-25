import config
import openai
from translator import en2uz, uz2en
openai.api_key = config.api_key

def simplifier(input_text, chars_count):
    print(chars_count)
    translated_input = uz2en(input_text)
    response = openai.Completion.create(
        model="davinci",
        prompt=f"Make it short:\n\n{translated_input}",
        temperature=0.7,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )


    return en2uz(response.choices[0].text)


# my_str="\
# Platformada ko'rsatilgan barcha narxlar AQSh dollarida ko'rsatilgan standart hisoblanadi. Synthesia sizning mahalliy valyutangiz bo'lishini belgilaydigan valyutadagi narxlarni ko'rsatishga qaror qilishimiz mumkin. Iste'molchilarga ko'rsatilgan barcha narxlar vaqti-vaqti bilan amalda bo'lgan stavka bo'yicha amaldagi savdo soliqlarini o'z ichiga oladi."
# result = simplifier(my_str)
#
# print(result)