import grpc
import texttoimg_pb2
import texttoimg_pb2_grpc
import base64
import time
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt

# Function to send one gRPC request and return the time it takes
def make_request(prompt):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = texttoimg_pb2_grpc.Text2ImageServiceStub(channel)
        start = time.time()
        response = stub.GenerateImage(texttoimg_pb2.ImageRequest(prompt=prompt))
        end = time.time()
        return end - start  # response time

# Function to run concurrent requests and return the average time
def run_concurrent_test(prompt, num_requests):
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(make_request, prompt) for _ in range(num_requests)]
        times = [f.result() for f in futures]
    avg_time = sum(times) / len(times)
    print(f"{num_requests} concurrent requests -> Avg response time: {avg_time:.2f} sec")
    return avg_time

# Main function to test different levels of concurrency
def main():
    prompt = "A majestic dragon soaring through the skies above a golden kingdom"
    concurrent_levels = [1, 5, 10, 20, 30, 40, 50]
    results = []

    for level in concurrent_levels:
        avg_time = run_concurrent_test(prompt, level)
        results.append(avg_time)

    # Plotting the performance graph
    plt.figure(figsize=(10, 6))
    plt.plot(concurrent_levels, results, marker='o', linestyle='-', color='purple')
    plt.title("Performance Evaluation: Concurrent Requests vs. Response Time")
    plt.xlabel("Number of Concurrent Requests")
    plt.ylabel("Average Response Time (seconds)")
    plt.grid(True)
    plt.savefig("performance_graph.png")
    plt.show()

if __name__ == "__main__":
    main()