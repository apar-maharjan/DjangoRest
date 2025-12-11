from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class ReviewThrottle(UserRateThrottle):
    scope = 'review'

class AnonymousReviewThrottle(AnonRateThrottle):
    scope = 'review'