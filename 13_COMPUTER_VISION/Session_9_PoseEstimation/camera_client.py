import cv2
import socket
import pickle
import struct
import numpy as np

class CameraClient:
    def __init__(self, host='localhost', port=8485):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        
        self.data = b""
        self.payload_size = struct.calcsize("L")
    
    def get_frame(self):
        while len(self.data) < self.payload_size:
            self.data += self.client_socket.recv(4096)
        
        packed_msg_size = self.data[:self.payload_size]
        self.data = self.data[self.payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]
        
        while len(self.data) < msg_size:
            self.data += self.client_socket.recv(4096)
        
        frame_data = self.data[:msg_size]
        self.data = self.data[msg_size:]
        
        frame = pickle.loads(frame_data)
        return cv2.imdecode(frame, cv2.IMREAD_COLOR)
    
    def close(self):
        self.client_socket.close()

if __name__ == "__main__":
    # Example usage
    client = CameraClient()
    try:
        while True:
            frame = client.get_frame()
            cv2.imshow('Remote Camera', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        client.close()
        cv2.destroyAllWindows() 