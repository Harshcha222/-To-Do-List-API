from rest_framework import serializers

class TodoSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=200)
    description = serializers.CharField(required=True)
    completed = serializers.BooleanField(required=True)


    def to_internal_value(self, data):
        
        validated_data = super().to_internal_value(data)

       
        if not isinstance(data.get('title', ''), str):
            raise serializers.ValidationError({"title": "This field must be a string."})

        
        if not isinstance(data.get('description', ''), str):
            raise serializers.ValidationError({"description": "This field must be a string."})

        
        return validated_data    
        