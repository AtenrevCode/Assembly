from rest_framework import serializers
from django.contrib.auth.models import User

from citizens.models import Profile
from .models import Proposal, Comment, UserProposalPhaseVote, UserCommentVote


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "first_name", "last_name")


class CitizenSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=True)

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)

        Profile.objects.create(user=user)
        user.refresh_from_db()

        user.profile.profile_image = validated_data.pop("profile_image", None)
        user.profile.national_id = validated_data.pop("national_id")

        user.save()
        user.profile.save()
        return user.profile

    class Meta:
        model = Profile
        fields = ("profile_image", "national_id", "user")


class ProposalSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    review_votes_count = serializers.SerializerMethodField()
    vote_votes_count = serializers.SerializerMethodField()

    class Meta:
        model = Proposal
        fields = (
            "id",
            "title",
            "image",
            "description",
            "phase",
            "close_date",
            "user",
            "comment_count",
            "review_votes_count",
            "vote_votes_count",
        )

        read_only_fields = ("id", "phase", "close_date")

    def get_comment_count(self, proposal):
        return Comment.objects.filter(proposal=proposal).count()

    def get_review_votes_count(self, proposal):
        return UserProposalPhaseVote.objects.filter(
            proposal=proposal, phase="review"
        ).count()

    def get_vote_votes_count(self, proposal):
        return UserProposalPhaseVote.objects.filter(
            proposal=proposal, phase="vote"
        ).count()


class ProposalReviewVoteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserProposalPhaseVote
        fields = ("id", "phase", "proposal", "user")


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    votes_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ("id", "message", "proposal", "user", "nest_comment", "votes_count")

    def get_votes_count(self, comment):
        return UserCommentVote.objects.filter(comment=comment).count()


class UserCommentVoteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserCommentVote
        fields = ("id", "user", "comment")
