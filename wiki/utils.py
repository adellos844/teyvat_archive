import requests
import time

def obtener_datos_enka(uid):
    """Obtiene datos del perfil de Genshin Impact usando la API de Enka"""
    url = f"https://enka.network/api/uid/{uid}/"
    headers = {'User-Agent': 'MiWikiGenshin/1.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            return {"error": "Demasiadas peticiones a Enka. Por favor, espera unos minutos antes de intentar de nuevo."}
        elif response.status_code == 404:
            return {"error": "UID no encontrado o perfil privado. Asegúrate de que tu UID es correcto y tu perfil está público en Genshin Impact."}
        else:
            return {"error": f"Error al conectar con Enka (código {response.status_code}). Intenta más tarde."}
    except requests.exceptions.Timeout:
        return {"error": "Timeout: La conexión tardó demasiado. Intenta más tarde."}
    except requests.exceptions.RequestException as e:
        return {"error": "Error de conexión. Verifica tu conexión a internet."}