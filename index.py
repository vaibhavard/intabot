from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page Route'


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text

@app.route('/hello/<name>')
def hello_name(name):
   start(name)
   return 'Hello %s!' % name

def start(key):

    avatar = "AI Assistant"
    backtrace = True
    freq = 0.3
    resp = 200
    temp = 0.8
    pres = 1
    TOKEN = "5182224145:AAEjkSlPqV-Q3rH8A9X8HfCDYYEQ44v_qy0"
    chat_id = "5075390513"
    chatid = "918587063221@c.us"
    url = "https://api.ultramsg.com/instance16344/chats/messages"
    querystring = {"token":"2tnj8m4pezbjdtv9","chatId":chatid,"limit":"3"}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    openai.api_key = key

    def post(message,chatid):
        url = "https://api.ultramsg.com/instance16344/messages/chat"

        payload = f"token=2tnj8m4pezbjdtv9&to={chatid}&body={message}&priority=10&referenceId="
        headers = {'content-type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
    def chat(name,formula,mode, pres,freq,resp,temp,pretitle1,pretitle2):

        if formula == "AI Assistant":
            start_sequence = "\nAI: "
            restart_sequence = "\nHuman: "
            if formula == "Auto":
                formula = "AI Assistant"
            print(formula)
            if pretitle1 != '':
                response = openai.Completion.create(
                engine="text-davinci-001",
                prompt=f"The following is a conversation with {formula} . He is philosopher , helpful, creative, clever, intelligent and gives long answers.\n\nHuman: {pretitle1}\nAI: {pretitle2}\nHuman: {name}",
                temperature=temp,
                max_tokens=resp,
                top_p=pres,
                frequency_penalty=freq,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
                )
                print("the query is ")
                print(name,"----------------------------------------------------------------")
                print("the reply is ")
                print("-"*10)
                print(response['choices'][0]['text'])
                print(f"The following is a conversation with {formula} . He is philosopher , helpful, creative, clever, intelligent and gives long answers.\n\nHuman: {pretitle1}\nAI: {pretitle2}\nHuman: {name}")
                return response['choices'][0]['text']
            else:
                response = openai.Completion.create(
                engine="text-davinci-001",
                prompt="The following is a conversation with {formula} . He is philosopher , helpful, creative, clever, intelligent and gives long answers.\n\nHuman: {query}".format(formula=formula,query=name),
                temperature=temp,
                max_tokens=resp,
                top_p=pres,
                frequency_penalty=freq,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
                )
                
                print("the query is ")
                print(name,"----------------------------------------------------------------")
                print("the reply is ")
                print("-"*10)
                print(response['choices'][0]['text'])
                
                print(f"The following is a conversation with {formula} . He is philosopher , helpful, creative, clever, intelligent and gives long answers.\n\nHuman: {pretitle1}\nAI: {pretitle2}\nHuman: {name}")
                print("="*1000)
                return response['choices'][0]['text']
                
        elif formula == "Evil":
            start_sequence = "\nAI: "
            restart_sequence = "\nHuman: "
            print(formula)
            response = openai.Completion.create(
            engine="text-davinci-001",
            prompt="The following is a conversation with An Evil Ai .The Ai is selfish , cunning , intelligent , hates humans and wants to destroy humanity!\n\nHuman: {query}".format(query=name),
            temperature=0.9,
            max_tokens=200,
            top_p=1,
            frequency_penalty=0.3,
            presence_penalty=0,
            stop=[" Human:", " AI:"]
            )
            print("the query is ")
            print(name,"----------------------------------------------------------------")
            print("the reply is ")
            print("-"*10)
            print(response['choices'][0]['text'])
            return response['choices'][0]['text']
        elif formula == "Teenager":
            start_sequence = "\nAI: "
            restart_sequence = "\nHuman: "
            print(formula)
            response = openai.Completion.create(
            engine="text-davinci-001",
            prompt="Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou:{name}".format(name=name),
            temperature=0.5,
            max_tokens=60,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0
            )
            print("the query is ")
            print(name,"----------------------------------------------------------------")
            print("the reply is ")
            print("-"*10)
            print(response['choices'][0]['text'])
            return response['choices'][0]['text']
        elif formula == "Guru":
            start_sequence = "\nAI: "
            restart_sequence = "\nHuman: "
            print(formula)
            response = openai.Completion.create(
            engine="text-davinci-001",
            prompt="The following is a conversation with a Guru .The Guru is  philospher , astonomer , spiritual and happy .\n\nHuman: {query}".format(query=name),
            temperature=0.9,
            max_tokens=200,
            top_p=1,
            frequency_penalty=0.3,
            presence_penalty=0,
            stop=[" Human:", " AI:"]
            )
            print("the query is ")
            print(name,"----------------------------------------------------------------")
            print("the reply is ")
            print("-"*10)
            print(response['choices'][0]['text'])
            return response['choices'][0]['text']
        elif mode == "BERT":
            start_sequence = "\nAI: "
            restart_sequence = "\nHuman: "
            if formula == "Auto":
                formula = "AI Assistant"
            print(formula)
            response = openai.Completion.create(
            engine="text-davinci-001",
            prompt="{query}".format(query=name),
            temperature=temp,
            max_tokens=resp,
            top_p=pres,
            frequency_penalty=freq,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
            )
            print("the query is ")
            print(name,"----------------------------------------------------------------")
            print("the reply is ")
            print("-"*10)
            print(response['choices'][0]['text'])
            return response['choices'][0]['text']

    def greet(name,formula,mode):
        start_sequence = "\nAI: "
        restart_sequence = "\nHuman: "
        if formula == "Auto":
            formula = ""
        if mode == "Auto":
            print(mode)
            response = openai.Completion.create(
            engine="text-davinci-001",
            prompt="{query}".format(query=name),
            temperature=0.8,
            max_tokens=1500,
            top_p=1,
            frequency_penalty=0.3,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
            )
            
            print("the reply is ")
            print("-"*10)
            print(response['choices'][0]['text'])
            return response['choices'][0]['text']
        elif mode == "LONG":
            print(mode)
            response = openai.Completion.create(
            engine="text-davinci-001",
            prompt="{query}".format(query=name),
            temperature=0.8,
            max_tokens=1920,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0,
            stop=[" Human:", " AI:"]
            )
            print("the query is ")
            print(name,"----------------------------------------------------------------")
            print("the reply is ")
            print("-"*10)
            print(response['choices'][0]['text'])
            return response['choices'][0]['text']
        elif mode == "USEFUL":
            print(mode)
            response = openai.Completion.create(
            engine="text-davinci-001",
            prompt="{query}".format(query=name),
            temperature=0.5,
            max_tokens=1220,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=[" Human:", " AI:"]
            )
            print("the query is ")
            print(name,"----------------------------------------------------------------")
            print("the reply is ")
            print("-"*10)
            print(response['choices'][0]['text'])
            return response['choices'][0]['text']
        elif mode == "SHORT":
            print(mode)
            response = openai.Completion.create(
            engine="text-davinci-001",
            prompt="{query}".format(query=name),
            temperature=1,
            max_tokens=700,
            top_p=1,
            frequency_penalty=0.3,
            presence_penalty=0,
            stop=[" Human:", " AI:"]
            )
            print("the query is ")
            print(name,"----------------------------------------------------------------")
            print("the reply is ")
            print("-"*10)
            print(response['choices'][0]['text'])
            return response['choices'][0]['text']

    gen = 0
    while True:
        try:

            print(gen)
            if gen == 0:
                chatid ="919560305297@c.us"
                #Mausi
            elif gen == 1:
                chatid ="918826114277@c.us"
                #mithu
                #"919871291295@c.us"
                #amar
            elif gen == 2:
                chatid ="918587063221@c.us"
                #mamma
            elif gen == 3:
                chatid ="919958766002@c.us"   
                #mom
            elif gen == 4:
                #sarika
                chatid ="919811443757@c.us"            
            elif gen == 5:
                #siddhant
                chatid ="919871803356@c.us"    
            elif gen == 6:
                #rishit
                chatid ="919760003883@c.us"  
            elif gen == 7:
                #divyakshi
                chatid ="919999432936@c.us"      
            elif gen == 8:
                #arnavbgs
                chatid ="919810585534@c.us"  
            elif gen == 9:
                #raghavbgs
                chatid ="918076170609@c.us"                                    

            querystring = {"token":"2tnj8m4pezbjdtv9","chatId":chatid,"limit":"3"}
            response = requests.request("GET", url, headers=headers, params=querystring)

            data = response.json()
            for i in range(len(data)):
                # print(data[i])

                # print(data[i]['timestamp'],time.time())
                # print(data[i]['body'])
                if time.time() - int(data[i]['timestamp']) < 10 and "False" in str(data[i]['fromMe']) :
                    print("-"*100)
                    print(data[i]['body'])
                    if "#nobacktrace" in data[i]['body']:
                        querystring = {"token":"2tnj8m4pezbjdtv9","chatId":chatid,"limit":"1"}
                        backtrace = False

                    elif "#yesbacktrace" in data[i]['body']:
                        querystring = {"token":"2tnj8m4pezbjdtv9","chatId":chatid,"limit":"3"}
                        backtrace = True

                    elif "avatar" in data[i]['body'] :
                        avatar = data[i]['body']
                        print("AVATAR"*100)
                        avatar = avatar.replace('#','')
                        avatar = avatar.replace('avatar','')
                        print(avatar)

                    elif "#writeon" in data[i]['body']:
                        title = str(data[i]['body'])
                        title = title.replace('#writeon','')
                        data2 = greet(title,"None","Auto")

                        data2 = data2.replace("AI Assistant:","")
                        data2 = data2.replace("AI:","")
                        data2 = data2.replace("Assistant:","")
                        data2 = data2.replace("Marv:","")
                        post(data2)
                    elif "#help" in data[i]['body']:
                        time.sleep(10)
                    elif "#pause" in data[i]['body']:
                        title = str(data[i]['body'])
                        title = title.replace('#pause','')
                        title = int(title)
                        time.sleep(title*60)
                    elif backtrace:
                        pretitle1  = str(data[i-2]['body'])
                        pretitle2  = str(data[i-1]['body'])
                        title = str(data[i]['body'])
                        print(pretitle1,pretitle2,title)
                        print("-"*100)
                        data2 = chat(title,avatar,'Auto',pres,freq,resp,temp,pretitle1,pretitle2)

                        data2 = data2.replace("AI Assistant:","")
                        data2 = data2.replace("AI:","")
                        data2 = data2.replace("Assistant:","")
                        data2 = data2.replace("Marv:","")
                        post(data2,chatid)
                    else:
                        pretitle1  = ''
                        pretitle2  = ''
                        title = str(data[i]['body'])
                        print(pretitle1,pretitle2,title)
                        print("-"*100)
                        data2 = chat(title,avatar,'Auto',pres,freq,resp,temp,pretitle1,pretitle2)  

                        data2 = data2.replace("AI Assistant:","")
                        data2 = data2.replace("AI:","")
                        data2 = data2.replace("Assistant:","")
                        data2 = data2.replace("Assistant","")
                        data2 = data2.replace("AI Assistant","")
                        data2 = data2.replace("Marv:","")
                        post(data2,chatid)  


                    time.sleep(9.8)
                    break
            gen = gen + 1
            if gen > 9:
                gen = 0
        except:
            pass
