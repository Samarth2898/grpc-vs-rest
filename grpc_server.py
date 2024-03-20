from __future__ import print_function

import base64
import io
from concurrent import futures
import grpc
from PIL import Image

import labsix_pb2_grpc
import labsix_pb2


class LabsixServicer(labsix_pb2_grpc.labSixServicer):
    def AddTwoNumbers(self, request, context):
        sum = request.a + request.b
        return labsix_pb2.addReply(sum=sum)
    
    def GetRawImageDimensons(self, request, context):
        ioBuffer = io.BytesIO(request.img)
        img = Image.open(ioBuffer)
        response = {
            'width': img.size[0],
            'height': img.size[1]
        }
        return labsix_pb2.imageReply(height=response['height'], width=response['width'])

    def GetDotProduct(self, request, context):
        dotproduct = 0
        try:
            a = request.a
            b = request.b

            if not (len(a) == len(b)):
                raise Exception
            for i in range(len(a)):
                dotproduct += a[i] * b[i]

            return labsix_pb2.dotProductReply(dotproduct=dotproduct)

        except:
            return labsix_pb2.dotProductReply(dotproduct=0)
    
    def GetJsonImageDimensons(self, request, context):
        image_string = request.img
        image_ascii = image_string.encode("ascii")
        img_byte = base64.b64decode(image_ascii)
        ioBuffer = io.BytesIO(img_byte)
        img = Image.open(ioBuffer)
        response = {
            'width': img.size[0],
            'height': img.size[1]
        }
        return labsix_pb2.imageReply(height=response['height'], width=response['width'])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    labsix_pb2_grpc.add_labSixServicer_to_server(LabsixServicer(), server)

    server.add_insecure_port('[::]:8080')
    server.start()
    print('Server is running')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
