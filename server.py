import grpc
from concurrent import futures
import texttoimg_pb2
import texttoimg_pb2_grpc
from image_generator import StoryImageGenerator

class TextToImageService(texttoimg_pb2_grpc.Text2ImageServiceServicer):
    def __init__(self):
        self.generator =StoryImageGenerator()

    def GenerateImage(self, request, context):
        try:
            image_b64 = self.generator.generate_image(request.prompt)
            return texttoimg_pb2.ImageResponse(
                status="200",
                message="Image generated successfully",
                image_base64=image_b64
            )
        except Exception as e:
            return texttoimg_pb2.ImageResponse(
                status="500",
                message=str(e),
                image_base64=""
            )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    texttoimg_pb2_grpc.add_Text2ImageServiceServicer_to_server(TextToImageService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print(" gRPC server is running on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
