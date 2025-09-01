import requests

def buscar_clima(cidade):
    try:
        # chave da API do OpenWeatherMap
        api_key = "0b308693a0b592cf30cf063a0a82452d"
        
        # URL da API (pegando temperatura em Celsius)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"
        
        # Fazendo requisição
        resposta = requests.get(url)
        resposta.raise_for_status()  # se der erro HTTP, ele levanta exceção
        
        # Converte resposta para JSON
        dados = resposta.json()
        
        # Pega dados principais
        temperatura = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        cidade_nome = dados["name"]
        
        print(f"Clima em {cidade_nome}:")
        print(f"🌡️ Temperatura: {temperatura}°C")
        print(f"☁️ Condições: {descricao}")
    
    except requests.exceptions.RequestException as erro:
        print("❌ Erro de conexão com a API:", erro)
    except KeyError:
        print("❌ Erro ao processar os dados recebidos.")
    except Exception as e:
        print("❌ Ocorreu um erro inesperado:", e)

# Testando com uma cidade
buscar_clima("São Paulo")
