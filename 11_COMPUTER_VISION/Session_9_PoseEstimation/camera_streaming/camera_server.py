import cv2
import socket
import pickle
import struct
import threading
import time

class CameraServer:
    def __init__(self, host='0.0.0.0', port=8485):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Server listening on {host}:{port}")
        
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")
        
        self.running = True
        self.clients = []
        
        # Start accepting connections in a separate thread
        self.accept_thread = threading.Thread(target=self.accept_connections)
        self.accept_thread.start()
        
        # Start sending frames
        self.send_frames()
    
    def accept_connections(self):
        while self.running:
            try:
                client_socket, addr = self.server_socket.accept()
                print(f"New connection from {addr}")
                self.clients.append(client_socket)
            except:
                break
    
    def send_frames(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            # Flip the frame horizontally
            frame = cv2.flip(frame, 1)
            
            # Encode frame
            _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            data = pickle.dumps(buffer)
            
            # Send to all connected clients
            dead_clients = []
            for client in self.clients:
                try:
                    message_size = struct.pack("L", len(data))
                    client.sendall(message_size + data)
                except:
                    dead_clients.append(client)
            
            # Remove dead clients
            for client in dead_clients:
                self.clients.remove(client)
                client.close()
            
            time.sleep(0.033)  # ~30 FPS
    
    def stop(self):
        self.running = False
        self.server_socket.close()
        self.cap.release()
        for client in self.clients:
            client.close()

if __name__ == "__main__":
    server = CameraServer()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down server...")
        server.stop() 