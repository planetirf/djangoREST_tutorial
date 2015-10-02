## serializersX.py ##
#API- provide a way to serailize and de-serialize snippet instances into representations such as JSON
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


### DEFINES FIELDS WHICH GET SERIALIZED/DE-SERIALIZED ###
### SnippetSerializer is replicating a lot of information thats also contained in the Snippet model - Refactored in serializers.py##
class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template':'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    ### create/update methods define how instances are created or modified when calling serializer.save()
    def create(self,validated_data):
        """
        Create and return a new 'Snippet' instance, given the validated data
        """
        return Snippet.objects.create(**validated_data)


    def update(self,instance, validated_data):
        """
        Update and return an existing 'Snippet' instance, given the validated data
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
