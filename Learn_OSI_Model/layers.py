import uuid
def physical_layer(frame):
    bits = ''.join(format(ord(c), '08b') for c in frame)
    print("[Physical] Sending bits:",bits)
    return bits
def data_link_Layer(data):
    mac_src = "F4:4D:30:4B:BA:8C"
    mac_dst = "10:3C:59:f9:6b:cb"

    frame = f"{mac_src}|{mac_dst}|{data}"
    print("[Data Link] Frame:", frame)
    return physical_layer(frame)

def network_layer(data):
    ip_src = "192.168.8.100"
    ip_dst = "192.168.8.104"

    packet = f"{ip_src}|{ip_dst}|{data}"
    print("[Network] Packet:", packet)

    return data_link_Layer(packet)

def transport_layer(data):
    src_port = 5000
    dst_port = 5000

    segment = f"{src_port}|{dst_port}|{data}"
    print("[Transport] Segment:", segment)

    return network_layer(segment)

def session_layer(data):
    session_id = str(uuid.uuid4())[:8]
    session = f"SESSION-{session_id}|{data}"
    print("[Session] Session:", session)

    return transport_layer(session)

def presentation_layer(data):
    encoded = data.encode("utf-8").hex()
    print("[Presentation] Encoded:", encoded)
    return session_layer(encoded)
def application_layer():
    message = input("Enter message:")
    print("[Application] Message:", message)
    return presentation_layer(message)

if __name__ == "__main__":
    application_layer()
