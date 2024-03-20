#!/usr/bin/env python3
from __future__ import print_function

import base64
import random
import sys
import time

import grpc

import labsix_pb2
import labsix_pb2_grpc


def doRawImage(channel, debug=False):
    stub = labsix_pb2_grpc.labSixStub(channel)
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    response = stub.GetRawImageDimensons(labsix_pb2.rawImageMsg(img=img))

    if debug:
        # decode response
        print("Response : \n", response)


def doAdd(channel, debug=False):
    stub = labsix_pb2_grpc.labSixStub(channel)
    response = stub.AddTwoNumbers(labsix_pb2.addMsg(a=5, b=10))

    if debug:
        # decode response
        print("Response : \n", response)


def doDotProduct(channel, debug=False):
    stub = labsix_pb2_grpc.labSixStub(channel)

    a = [random.random()] * 100
    b = [random.random()] * 100
    response = stub.GetDotProduct(labsix_pb2.dotProductMsg(a=a, b=b))

    if debug:
        # decode response
        print("Response : \n", response)


def doJsonImage(channel, debug=False):
    stub = labsix_pb2_grpc.labSixStub(channel)

    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    base_64_encoded = base64.b64encode(img)
    base_64_string_form = base_64_encoded.decode("ascii")

    response = stub.GetJsonImageDimensons(labsix_pb2.jsonImageMsg(img=base_64_string_form))

    if debug:
        # decode response
        print("Response : \n", response)

def run():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <server ip> <cmd> <reps>")
        print(f"where <cmd> is one of add, rawImage, sum or jsonImage")
        print(f"and <reps> is the integer number of repititions for measurement")

    host = sys.argv[1]
    cmd = sys.argv[2]
    reps = int(sys.argv[3])

    addr = f"{host}:8080"
    print(f"Running {reps} reps against {addr}")

    channel = grpc.insecure_channel(addr)

    with channel:
        if cmd == 'rawImage':
            start = time.perf_counter()
            for x in range(reps):
                doRawImage(channel, debug=False)
            delta = ((time.perf_counter() - start) / reps) * 1000
            print("Took", delta, "ms per operation")
        elif cmd == 'add':
            start = time.perf_counter()
            for x in range(reps):
                doAdd(channel, debug=False)
            delta = ((time.perf_counter() - start) / reps) * 1000
            print("Took", delta, "ms per operation")
        elif cmd == 'jsonImage':
            start = time.perf_counter()
            for x in range(reps):
                doJsonImage(channel, debug=False)
            delta = ((time.perf_counter() - start) / reps) * 1000
            print("Took", delta, "ms per operation")
        elif cmd == 'dotProduct':
            start = time.perf_counter()
            for x in range(reps):
                doDotProduct(channel, debug=False)
            delta = ((time.perf_counter() - start) / reps) * 1000
            print("Took", delta, "ms per operation")
        else:
            print("Unknown option", cmd)

if __name__ == '__main__':
    run()