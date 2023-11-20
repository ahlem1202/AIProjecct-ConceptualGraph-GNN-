# serializers.py
from rest_framework import serializers

class ProcessedResultSerializer(serializers.Serializer):
    concepts = serializers.CharField()
    text = serializers.CharField()
    references = serializers.CharField()
    definition = serializers.CharField()  # Rename 'def' to 'definition'
    Keywords = serializers.CharField()
    Synonyms_Predicate = serializers.CharField()
    Object_Topic = serializers.CharField()
