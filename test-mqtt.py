import paho.mqtt.client as mqtt
import time
import socket

def test_connectivity():
    """Testa conectividade TCP básica"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex(('mosquitto-production.up.railway.app', 1883))
        sock.close()
        
        if result == 0:
            print("✅ Porta 1883 está acessível")
            return True
        else:
            print("❌ Porta 1883 não está acessível")
            return False
    except Exception as e:
        print(f"❌ Erro no teste de conectividade: {e}")
        return False

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"🔗 Callback conectar: rc={rc}")
    if rc == 0:
        print("✅ Conectado com sucesso!")
        client.subscribe("test/railway")
        # Publicar mensagem de teste
        client.publish("test/railway", "Hello from Railway Client!")
    else:
        print(f"❌ Falha na conexão. Código: {rc}")
        print("Códigos de erro:")
        print("0: Sucesso")
        print("1: Protocolo incorreto")
        print("2: ID cliente inválido") 
        print("3: Servidor indisponível")
        print("4: Usuário/senha inválidos")
        print("5: Não autorizado")

def on_message(client, userdata, msg):
    print(f"📨 Mensagem: {msg.topic} -> {msg.payload.decode()}")

def on_disconnect(client, userdata, rc, properties=None):
    print(f"🔌 Desconectado. Código: {rc}")

def on_log(client, userdata, level, buf):
    print(f"🐛 Log: {buf}")

# Teste básico de conectividade primeiro
print("🔍 Testando conectividade básica...")
if not test_connectivity():
    print("❌ Falha no teste de conectividade. Verifique se o serviço está rodando.")
    exit(1)

# Configurar cliente MQTT
client = mqtt.Client(
    client_id="railway_test_v2",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    clean_session=True
)

# Configurar callbacks
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_log = on_log  # Para debug detalhado

print("🎯 Conectando ao Mosquitto Railway...")
print("📡 Host: mosquitto-production.up.railway.app:1883")

try:
    # Configurar timeouts mais longos
    client.connect_async("mosquitto-production.up.railway.app", 1883, 60)
    client.loop_start()
    
    # Aguardar conexão
    print("⏳ Aguardando conexão...")
    time.sleep(10)
    
    # Manter vivo
    print("🔄 Mantendo conexão ativa...")
    time.sleep(15)
    
except Exception as e:
    print(f"❌ ERRO na conexão: {e}")
    
finally:
    print("🔌 Finalizando...")
    client.loop_stop()
    client.disconnect()