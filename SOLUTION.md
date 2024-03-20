# Test results for GRPC and REST 

| Method | Local(ms) | Same-Zone(ms) | Different Region(ms) |
| :----	| ---- | ---- | ---- |
| REST add | 2.845 | 3.192 | 297.868 |
| gRPC add | 0.632 | 0.827 | 146.317 |
| REST rawimg | 5.374 | 7.776 | 1195.888 |
| gRPC rawimg | 7.641 | 11.733 | 205.438 |
| REST dotproduct | 3.553 | 4.209 | 299.414 |
| gRPC dotproduct | 0.746 | 0.901 | 146.331 |
| REST jsonimg | 40.993 | 41.104 | 1341.349 |
| gRPC jsonimg | 28.278 | 32.542 | 244.883 |
| PING | 0.043 | 0.421 | 142.364 |

## Observations
- Unary to Unary streaming was used for implementing gRPC and was observed to be faster than REST for most endpoints. It was found to be comparable with REST for rawImage endpoint while running on local and on different server in the same zone. 
- gRPC uses HTTP/2 as its underlying protocol, which provides features such as multiplexing, header compression, and the ability to send multiple requests in parallel over a single TCP connection. This allows for more efficient communication between clients and servers, reducing latency and overhead compared to REST, which typically uses HTTP 1.1
- gRPC uses Protocol Buffers by default for data serialization, which is a more efficient and faster serialization mechanism compared to JSON, used in REST. Protocol Buffers are binary, making them more efficient in terms of both CPU and bandwidth usage.
- gRPC was found to be faster than REST even while running the client and server in different regions. The latency seemed to increase very nominally from local to same zone to different region for gRPC, whereas for REST it was more prominent.
- The network latency or ping was the least on local and increased gradually for the same zone and different zone.