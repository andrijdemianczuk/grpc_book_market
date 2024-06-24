import grpc
from recommendations.recommendations_pb2_grpc import RecommendationsStub
from recommendations.recommendations_pb2 import BookCategory, RecommendationRequest


if __name__=='__main__':
    channel = grpc.insecure_channel("localhost:50051")
    client = RecommendationsStub(channel)

    request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
    client.Recommend(request)