from rest_framework import serializers
from userProfile.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ('user',)

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user:
            validated_data['user'] = request.user
        return super().create(validated_data)